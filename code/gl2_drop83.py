#!/usr/bin/env python3
"""Isolate 83 on 37a1: μ=82, 84, 100 × full, drop 3, drop 83.

    python code/gl2_drop83.py
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

MUS = [82, 84, 100]
DROPS = [None, 3, 83]
NB, DPS, DEG = 80, 50, 12


def _job(payload):
    mu, drop, an = payload
    os.environ["GL2_FIX"] = "1"
    lam, ell = assemble("37a1", float(mu), NB, DPS, DEG=DEG, drop=drop, an=an)
    return int(mu), drop, float(lam), float(ell[0])


def _tag(drop) -> str:
    return "full" if drop is None else f"drop{int(drop)}"


def main() -> None:
    an_all = an_points("37a1", max(MUS))
    jobs = []
    for mu in MUS:
        an = {n: a for n, a in an_all.items() if n <= mu}
        for drop in DROPS:
            jobs.append((mu, drop, an))
    workers = min(len(jobs), os.cpu_count() or 32)
    est_s = 240
    print(f"jobs={len(jobs)} workers={workers} mus={MUS} drops={DROPS}", flush=True)
    print(
        f"estimate wall ~{est_s}s (~{est_s // 60} min); "
        "same assemble as gl2_drop3_hi (216-265s)",
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
            print(
                f"  {mu:3d} {_tag(drop):6s}  lam0={lam: .4e}  ell={ell0:7.2f}  "
                f"{time.time()-t0:.0f}s",
                flush=True,
            )
    rows = []
    for mu in MUS:
        row = {"mu": mu}
        for drop in DROPS:
            lam, ell0 = out[(mu, drop)]
            key = "full" if drop is None else f"drop{int(drop)}"
            row[f"{key}_lam0"] = lam
            row[f"{key}_ell"] = ell0
            row[f"{key}_necessary"] = bool(drop is not None and lam < 0)
        rows.append(row)
        d3 = row["drop3_lam0"]
        d83 = row["drop83_lam0"]
        print(
            f"mu={mu:3d}  full={row['full_lam0']:.4e}  "
            f"drop3={d3:.4e} {'NEG' if d3 < 0 else 'pos'}  "
            f"drop83={d83:.4e} {'NEG' if d83 < 0 else 'pos'}",
            flush=True,
        )
    dest = os.path.join(
        os.path.dirname(__file__), "..", "report", "gl2-37a1-drop83.json"
    )
    payload = {
        "label": "37a1",
        "NB": NB,
        "dps": DPS,
        "seconds": round(time.time() - t0, 1),
        "rows": rows,
    }
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    by = {r["mu"]: r for r in rows}
    join_before = by[82]["drop3_lam0"] < 0
    voter100 = by[100]["drop83_lam0"] < 0
    mute82 = abs(by[82]["drop83_lam0"] - by[82]["full_lam0"]) / max(
        abs(by[82]["full_lam0"]), 1e-30
    ) < 0.05
    print(f"wrote {dest}", flush=True)
    if join_before:
        print("KILL-before-83", f"drop3(82)={by[82]['drop3_lam0']:.4e}", flush=True)
    elif not voter100:
        print("KILL-83-mute", f"drop83(100)={by[100]['drop83_lam0']:.4e}", flush=True)
    else:
        print(
            "SURVIVE-83",
            f"drop3(82)={by[82]['drop3_lam0']:.4e}",
            f"drop3(84)={by[84]['drop3_lam0']:.4e}",
            f"drop83(100)={by[100]['drop83_lam0']:.4e}",
            f"mute82={mute82}",
            flush=True,
        )


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
