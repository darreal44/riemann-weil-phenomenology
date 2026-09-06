#!/usr/bin/env python3
"""Linearised mass of block(2) on the archimedean compression.

    Fmat <- block(2) only
    A    <- P F_infty P
    tau  <- lambda^{-1/2} (cross terms)
    m    <- int_{window at 2} tau d*lambda

Preregistered: if m freezes, kappa = m * 2 * sqrt(2);
kappa=4 -> module 1/sqrt(2); kappa=8 -> inverse sqrt(2).
Not RH.

    python code/kappa_block2.py 4 32          # sandbox smoke
    python code/kappa_block2.py 16 80         # one server job
    python code/kappa_block2.py --ladder      # five locked jobs, 32 cores
"""
from __future__ import annotations

import concurrent.futures
import json
import math
import multiprocessing
import os
import sys
import time

import numpy as np
from scipy.special import sici

LADDER = [(8, 40), (16, 80), (16, 160), (16, 400), (24, 200)]


def Si(x):
    return sici(x)[0]


def _nthreads() -> int:
    return max(1, int(os.environ.get("KAPPA_THREADS", "1")))


def block(ein, eout, s):
    """Si kernel, row-chunked so xa/xb never span the full N_out at once.

    Same values as the one-shot (G(d)-G(c))/dc. Threads share one Fmat;
    do not spawn extra processes here (that would duplicate the matrix).
    """
    a = np.ascontiguousarray(ein[:-1])
    b = np.ascontiguousarray(ein[1:])
    c = np.ascontiguousarray(eout[:-1])
    d = np.ascontiguousarray(eout[1:])
    nout, nin = len(c), len(a)
    out = np.empty((nout, nin), dtype=np.float64)
    k = 2.0 * np.pi * s
    pis = np.pi * s
    nthr = _nthreads()
    nchunk = max(1, min(nthr, max(1, nout // 64)))
    bounds = np.linspace(0, nout, nchunk + 1, dtype=int)

    def work(i0: int, i1: int) -> None:
        cc = c[i0:i1]
        dd = d[i0:i1]
        dc = (dd - cc)[:, None]

        def G(x):
            xa = k * x[:, None] * a[None, :]
            xb = k * x[:, None] * b[None, :]
            return (Si(xb) - Si(xa)) / pis

        out[i0:i1] = (G(dd) - G(cc)) / dc

    if nchunk == 1:
        work(0, nout)
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=nchunk) as pool:
            futs = [
                pool.submit(work, int(bounds[i]), int(bounds[i + 1]))
                for i in range(nchunk)
            ]
            for fut in futs:
                fut.result()
    return out


def memory_gb(Lam: float, cpu: int) -> float:
    n_in = int(Lam * cpu)
    r = Lam * 2.60 * 1.02
    n_out = int(np.ceil(r / (Lam / n_in)))
    return 8 * n_out * n_in * 6 / 1e9


def probe(Lam: float, cpu: int, half: float = 0.12) -> dict:
    t0 = time.time()
    lams = np.concatenate(
        [
            np.linspace(1.50, 1.80, 31),
            np.linspace(1.81, 2.20, 81),
            np.linspace(2.21, 2.60, 31),
        ]
    )
    R = Lam * float(lams.max()) * 1.02
    N_in = int(Lam * cpu)
    hc = Lam / N_in
    ein = np.linspace(0.0, Lam, N_in + 1)
    N_out = int(np.ceil(R / hc))
    eout = np.linspace(0.0, N_out * hc, N_out + 1)
    Finf = block(ein, eout, 1.0)
    B2 = block(ein, eout, 2.0)
    A = 0.5 * (Finf[:N_in, :N_in] + Finf[:N_in, :N_in].T)
    PB2P = 0.5 * (B2[:N_in, :N_in] + B2[:N_in, :N_in].T)
    # Delta F carries +1/2 B2; cross terms with that factor.
    # Build W without keeping both GEMM products at once.
    W = B2.dot(A)
    del A
    W += Finf.dot(PB2P)
    W *= 0.5
    del Finf, B2, PB2P
    xin = 0.5 * (ein[:-1] + ein[1:])
    tau = np.empty(len(lams))
    cols = np.arange(N_in)
    for k, lam in enumerate(lams):
        idx = np.clip(np.floor(xin / lam / hc).astype(int), 0, N_out - 1)
        tau[k] = lam ** -0.5 * np.sum(W[idx, cols])
    m = np.abs(lams - 2.0) < half * 2.0
    mass = float(np.trapezoid(tau[m] / lams[m], lams[m]))
    kappa = mass * 2.0 * math.sqrt(2.0)
    return {
        "Lam": float(Lam),
        "cpu": int(cpu),
        "N_in": N_in,
        "N_out": N_out,
        "sec": round(time.time() - t0, 2),
        "mass": mass,
        "kappa": kappa,
        "target4": abs(kappa - 4.0),
        "target8": abs(kappa - 8.0),
        "mem_gb_est": round(memory_gb(Lam, cpu), 2),
    }


def _fmt(row: dict) -> str:
    return (
        f"Lam={row['Lam']} cpu={row['cpu']}  "
        f"N={row['N_in']}x{row['N_out']}  "
        f"m={row['mass']:+.4f}  kappa={row['kappa']:+.3f}  "
        f"|k-4|={row['target4']:.3f} |k-8|={row['target8']:.3f}  "
        f"{row['sec']}s"
    )


def _job(payload):
    Lam, cpu, nthr = payload
    os.environ["KAPPA_THREADS"] = str(int(nthr))
    os.environ["OMP_NUM_THREADS"] = str(int(nthr))
    os.environ["OPENBLAS_NUM_THREADS"] = str(int(nthr))
    os.environ["MKL_NUM_THREADS"] = str(int(nthr))
    return probe(float(Lam), int(cpu))


def _thread_split(ncpu: int) -> list[int]:
    costs = np.array([(L * c) ** 2 for L, c in LADDER], dtype=float)
    raw = ncpu * costs / costs.sum()
    nthr = np.maximum(1, np.floor(raw).astype(int))
    while int(nthr.sum()) < ncpu:
        nthr[int(np.argmax(raw - nthr))] += 1
    while int(nthr.sum()) > ncpu:
        j = int(np.argmax(nthr))
        if nthr[j] <= 1:
            break
        nthr[j] -= 1
    return [int(x) for x in nthr]


def ladder() -> list[dict]:
    ncpu = os.cpu_count() or 32
    nthr = _thread_split(ncpu)
    jobs = [(L, c, t) for (L, c), t in zip(LADDER, nthr)]
    mem = sum(memory_gb(L, c) for L, c in LADDER)
    # 2-adic tau_curve at Λ=16 cpu=400 was 1383 s for arch+S.
    # This probe is two blocks; wall is the 16/400 job.
    est_s = 480
    print(
        f"ladder jobs={len(jobs)} cores={ncpu} threads={nthr}  "
        f"RAM~{mem:.1f} GB / 64  estimate wall ~{est_s}s (~{est_s // 60} min)",
        flush=True,
    )
    t0 = time.time()
    rows = []
    ctx = multiprocessing.get_context("spawn")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=len(jobs), mp_context=ctx
    ) as pool:
        futs = [pool.submit(_job, job) for job in jobs]
        for fut in concurrent.futures.as_completed(futs):
            row = fut.result()
            rows.append(row)
            print(f"  {_fmt(row)}  wall={time.time()-t0:.0f}s", flush=True)
    rows.sort(key=lambda r: (r["Lam"], r["cpu"]))
    dest = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "report",
        "kappa-block2-ladder.json",
    )
    payload = {
        "seconds": round(time.time() - t0, 1),
        "threads": nthr,
        "rows": rows,
    }
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    by = {(int(r["Lam"]), int(r["cpu"])): r for r in rows}
    k160 = by[(16, 160)]["kappa"]
    k400 = by[(16, 400)]["kappa"]
    wander = abs(k400 - k160)
    near4 = abs(k400 - 4.0) <= 0.2
    near8 = abs(k400 - 8.0) <= 0.2
    if wander > 0.3:
        verdict = "KILL"
    elif near4 or near8:
        verdict = "SURVIVE"
    else:
        verdict = "KILL"
    print(f"wrote {dest}", flush=True)
    print(
        f"{verdict}  kappa16/160={k160:.3f}  kappa16/400={k400:.3f}  "
        f"wander={wander:.3f}",
        flush=True,
    )
    return rows


def main() -> None:
    if "--ladder" in sys.argv:
        ladder()
        return
    Lam = float(sys.argv[1]) if len(sys.argv) > 1 else 4.0
    cpu = int(sys.argv[2]) if len(sys.argv) > 2 else 32
    os.environ.setdefault("KAPPA_THREADS", str(os.cpu_count() or 8))
    os.environ.setdefault("OMP_NUM_THREADS", os.environ["KAPPA_THREADS"])
    os.environ.setdefault("OPENBLAS_NUM_THREADS", os.environ["KAPPA_THREADS"])
    os.environ.setdefault("MKL_NUM_THREADS", os.environ["KAPPA_THREADS"])
    row = probe(Lam, cpu)
    print(_fmt(row), flush=True)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
