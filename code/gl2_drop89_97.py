#!/usr/bin/env python3
"""drop-89 and drop-97 at 37a1 μ=100. Two jobs, same assemble as gl2_drop83.

    python code/gl2_drop89_97.py
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

MU, NB, DPS, DEG = 100, 80, 50, 12
DROPS = (89, 97)


def _job(payload):
    mu, drop, an = payload
    os.environ["GL2_FIX"] = "1"
    lam, ell = assemble("37a1", float(mu), NB, DPS, DEG=DEG, drop=drop, an=an)
    return int(drop), float(lam), float(ell[0])


def main() -> None:
    an = an_points("37a1", MU)
    jobs = [(MU, d, an) for d in DROPS]
    workers = min(len(jobs), os.cpu_count() or 32)
    est_s = 240
    print(f"jobs={len(jobs)} workers={workers} mu={MU} drops={list(DROPS)}", flush=True)
    print(
        f"estimate wall ~{est_s}s (~{est_s // 60} min); "
        "same assemble as gl2_drop83 (211s)",
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
            drop, lam, ell0 = fut.result()
            out[drop] = (lam, ell0)
            print(
                f"  drop={drop}  lam0={lam: .4e}  ell={ell0:7.2f}  "
                f"{time.time()-t0:.0f}s",
                flush=True,
            )
    rows = []
    nneg = 0
    for drop in DROPS:
        lam, ell0 = out[drop]
        neg = lam < 0
        nneg += int(neg)
        rows.append(
            {
                "mu": MU,
                "drop": drop,
                "lam0": lam,
                "ell0": ell0,
                "necessary": bool(neg),
            }
        )
        print(
            f"drop {drop}  lam0={lam:.4e}  {'NEG' if neg else 'pos'}",
            flush=True,
        )
    dest = os.path.join(
        os.path.dirname(__file__), "..", "report", "gl2-37a1-drop89-97.json"
    )
    payload = {
        "label": "37a1",
        "mu": MU,
        "NB": NB,
        "dps": DPS,
        "seconds": round(time.time() - t0, 1),
        "rows": rows,
    }
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"wrote {dest}  neg={nneg}/{len(rows)}", flush=True)
    print("KILL-piece" if nneg else "SURVIVE-no-piece", flush=True)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
