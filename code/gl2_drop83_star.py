#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""μ** of 37a1 drop-83 on a 2-unit grid in (84, 100].

    python code/gl2_drop83_star.py
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

MUS = [86, 88, 90, 92, 94, 96, 98]
NB, DPS, DEG = 80, 50, 12
ANCHOR = {
    84: 3.293819964120377e-09,
    100: -0.08033524704896937,
}


def _job(payload):
    mu, an = payload
    os.environ["GL2_FIX"] = "1"
    lam, ell = assemble("37a1", float(mu), NB, DPS, DEG=DEG, drop=83, an=an)
    return int(mu), float(lam), float(ell[0])


def main() -> None:
    an_all = an_points("37a1", 100)
    jobs = []
    for mu in MUS:
        an = {n: a for n, a in an_all.items() if n <= mu}
        jobs.append((mu, an))
    workers = min(len(jobs), os.cpu_count() or 32)
    est_s = 240
    print(f"jobs={len(jobs)} workers={workers} mus={MUS} drop=83", flush=True)
    print(
        f"estimate wall ~{est_s}s (~{est_s // 60} min); "
        "same assemble as gl2_drop3_star (215s)",
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
            mu, lam, ell0 = fut.result()
            out[mu] = (lam, ell0)
            print(
                f"  {mu:3d} drop83  lam0={lam: .4e}  ell={ell0:7.2f}  "
                f"{time.time()-t0:.0f}s",
                flush=True,
            )
    rows = []
    for mu in MUS:
        lam, ell0 = out[mu]
        rows.append(
            {
                "mu": mu,
                "drop83_lam0": lam,
                "drop83_ell": ell0,
                "necessary": bool(lam < 0),
            }
        )
        print(
            f"mu={mu:3d}  drop83={lam:.4e}  {'NEG' if lam < 0 else 'pos'}",
            flush=True,
        )
    chain = (
        [{"mu": 84, "necessary": ANCHOR[84] < 0}]
        + rows
        + [{"mu": 100, "necessary": ANCHOR[100] < 0}]
    )
    mu_lo, mu_hi = 84, 100
    for a, b in zip(chain, chain[1:]):
        if (not a["necessary"]) and b["necessary"]:
            mu_lo, mu_hi = a["mu"], b["mu"]
            break
    dest = os.path.join(
        os.path.dirname(__file__), "..", "report", "gl2-37a1-mu-star83.json"
    )
    payload = {
        "label": "37a1",
        "NB": NB,
        "dps": DPS,
        "seconds": round(time.time() - t0, 1),
        "mu_star83": [mu_lo, mu_hi],
        "rows": rows,
    }
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"wrote {dest}  mu** in ({mu_lo}, {mu_hi}]", flush=True)
    if mu_hi <= 86:
        print("KILL-early", f"drop83(86)={out[86][0]:.4e}", flush=True)
    else:
        print("SURVIVE", f"mu** in ({mu_lo}, {mu_hi}]", flush=True)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
