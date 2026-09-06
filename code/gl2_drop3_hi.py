#!/usr/bin/env python3
"""37a1 drop-3 on μ=100..250. 32 jobs on 32 cores.

    python code/gl2_drop3_hi.py
    python code/gl2_drop3_hi.py --control   # μ=74 and 80, ppts with 71+
"""
from __future__ import annotations

import concurrent.futures
import json
import multiprocessing
import os
import sys
import time

os.environ.setdefault("GL2_FIX", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan_q_gl2 import an_points, assemble  # noqa: E402

# --control: recompute μ=74 and 80 with primes 71+ in ppts (the old
# small-list cap at 67 made drop-71 = full at μ=74).
MUS = [74, 80] if "--control" in sys.argv else list(range(100, 260, 10))
NB, DPS, DEG = 80, 50, 12
OUT_NAME = (
    "gl2-37a1-drop3-control.json"
    if "--control" in sys.argv
    else "gl2-37a1-drop3-hi.json"
)


def _job(payload):
    mu, drop, an = payload
    os.environ["GL2_FIX"] = "1"
    lam, ell = assemble("37a1", float(mu), NB, DPS, DEG=DEG, drop=drop, an=an)
    return int(mu), drop, float(lam), float(ell[0])


def main() -> None:
    an_all = an_points("37a1", max(MUS))
    jobs = []
    for mu in MUS:
        an = {n: a for n, a in an_all.items() if n <= mu}
        jobs.append((mu, None, an))
        jobs.append((mu, 3, an))
    workers = min(len(jobs), os.cpu_count() or 32)
    # One assemble at NB=80 dps=50 was 216–222 s (μ=62/74/80 quorum,
    # 18–22 workers). fill() is Θ(NB²·K), almost independent of μ.
    # 32 jobs on 32 cores → wall ≈ one assemble.
    est_s = 240
    print(f"jobs={len(jobs)} workers={workers} mus={MUS}", flush=True)
    print(
        f"estimate wall ~{est_s}s (~{est_s // 60} min); "
        "previous assemble 216-222s at mu=62-80 NB=80",
        flush=True,
    )
    t0 = time.time()
    out = {}
    ctx = multiprocessing.get_context("spawn")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=ctx
    ) as pool:
        futs = [pool.submit(_job, job) for job in jobs]
        for fut in concurrent.futures.as_completed(futs):
            mu, drop, lam, ell0 = fut.result()
            out[(mu, drop)] = (lam, ell0)
            tag = "full" if drop is None else "drop3"
            print(
                f"  {mu:3d} {tag:5s}  lam0={lam: .4e}  ell={ell0:7.2f}  "
                f"{time.time()-t0:.0f}s",
                flush=True,
            )
    rows = []
    for mu in MUS:
        lf, ef = out[(mu, None)]
        ld, ed = out[(mu, 3)]
        rows.append(
            {
                "mu": mu,
                "full_lam0": lf,
                "full_ell": ef,
                "drop3_lam0": ld,
                "drop3_ell": ed,
                "necessary": bool(ld < 0),
            }
        )
        print(
            f"mu={mu:3d}  full={lf:.4e} ell={ef:.2f}  "
            f"drop3={ld:.4e}  {'NEG' if ld < 0 else 'pos'}",
            flush=True,
        )
    dest = os.path.join(os.path.dirname(__file__), "..", "report", OUT_NAME)
    payload = {
        "label": "37a1",
        "NB": NB,
        "dps": DPS,
        "seconds": round(time.time() - t0, 1),
        "rows": rows,
    }
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    nneg = sum(1 for r in rows if r["necessary"])
    print(f"wrote {dest}  drop3_neg={nneg}/{len(rows)}", flush=True)
    print("SURVIVE" if nneg == 0 else "KILL-joined", flush=True)


class _Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, data):
        for s in self.streams:
            s.write(data)
            s.flush()

    def flush(self):
        for s in self.streams:
            s.flush()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    _log_name = (
        "gl2-37a1-drop3-control.log"
        if "--control" in sys.argv
        else "gl2-37a1-drop3-hi.log"
    )
    _log_path = os.path.join(os.path.dirname(__file__), "..", "report", _log_name)
    _logf = open(_log_path, "w", encoding="utf-8")
    sys.stdout = _Tee(sys.__stdout__, _logf)
    sys.stderr = _Tee(sys.__stderr__, _logf)
    try:
        main()
    finally:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        _logf.close()
