#!/usr/bin/env python3
"""μ* of 37a1 drop-3 on a 2-unit grid in (84, 100].

    python code/gl2_drop3_star.py
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
DROPS = [None, 3]
NB, DPS, DEG = 80, 50, 12
# judged anchors (gl2-37a1-drop83.json)
ANCHOR = {
    84: {"full_lam0": 3.58021759510591e-09, "drop3_lam0": 0.04814961259111051},
    100: {"full_lam0": 2.758697022422327e-10, "drop3_lam0": -0.4184825830427477},
}


def _job(payload):
    mu, drop, an = payload
    os.environ["GL2_FIX"] = "1"
    lam, ell = assemble("37a1", float(mu), NB, DPS, DEG=DEG, drop=drop, an=an)
    return int(mu), drop, float(lam), float(ell[0])


def main() -> None:
    an_all = an_points("37a1", 100)
    jobs = []
    for mu in MUS:
        an = {n: a for n, a in an_all.items() if n <= mu}
        for drop in DROPS:
            jobs.append((mu, drop, an))
    workers = min(len(jobs), os.cpu_count() or 32)
    est_s = 240
    print(f"jobs={len(jobs)} workers={workers} mus={MUS}", flush=True)
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
            f"mu={mu:3d}  full={lf:.4e}  drop3={ld:.4e}  "
            f"{'NEG' if ld < 0 else 'pos'}",
            flush=True,
        )
    chain = (
        [{"mu": 84, "drop3_lam0": ANCHOR[84]["drop3_lam0"], "necessary": False}]
        + rows
        + [{"mu": 100, "drop3_lam0": ANCHOR[100]["drop3_lam0"], "necessary": True}]
    )
    mu_star_lo, mu_star_hi = 84, 100
    for a, b in zip(chain, chain[1:]):
        if (not a["necessary"]) and b["necessary"]:
            mu_star_lo, mu_star_hi = a["mu"], b["mu"]
            break
    dest = os.path.join(
        os.path.dirname(__file__), "..", "report", "gl2-37a1-mu-star.json"
    )
    payload = {
        "label": "37a1",
        "NB": NB,
        "dps": DPS,
        "seconds": round(time.time() - t0, 1),
        "mu_star": [mu_star_lo, mu_star_hi],
        "rows": rows,
    }
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"wrote {dest}  mu* in ({mu_star_lo}, {mu_star_hi}]", flush=True)
    if mu_star_hi <= 86:
        print("KILL-early", f"drop3(86)={out[(86, 3)][0]:.4e}", flush=True)
    else:
        print("SURVIVE", f"mu* in ({mu_star_lo}, {mu_star_hi}]", flush=True)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
