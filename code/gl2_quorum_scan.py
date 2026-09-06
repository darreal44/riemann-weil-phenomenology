#!/usr/bin/env python3
"""Parallel GL2 quorum scan: full Q and one drop per prime, one wall-clock assemble.

    python code/gl2_quorum_scan.py 37a1 62 80 50
    python code/gl2_quorum_scan.py 37a1 62 80 50 --drops 2,3,5,7

Writes report/gl2-<label>-mu<mu>-quorum.json. No RH.
"""
from __future__ import annotations

import json
import multiprocessing
import os
import sys
import time

os.environ.setdefault("GL2_FIX", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan_q_gl2 import an_points, assemble_drops  # noqa: E402


def primes_below(mu: float) -> list[int]:
    n = int(mu)
    sieve = [False, False] + [True] * (n - 1)
    p = 2
    while p * p <= n:
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = False
        p += 1
    return [i for i in range(2, n) if sieve[i]]


def main() -> None:
    name = sys.argv[1]
    mu, NB, dps = float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    if "--drops" in sys.argv:
        raw = sys.argv[sys.argv.index("--drops") + 1]
        drops = [int(x) for x in raw.split(",") if x.strip()]
    else:
        drops = primes_below(mu)
    an = an_points(name, int(mu))
    t0 = time.time()
    out = assemble_drops(name, mu, NB, dps, drops=drops, an=an, include_full=True)
    rows = []
    for drop in [None] + drops:
        lam, ell = out[drop]
        rows.append(
            {
                "drop": drop,
                "lam0": lam,
                "ell0": ell[0],
                "necessary": bool(lam < 0),
            }
        )
        tag = "full" if drop is None else f"p={drop}"
        sign = "NEG" if lam < 0 else "pos"
        print(f"  {tag:8s}  lam0={lam: .4e}  ell={ell[0]:7.2f}  {sign}", flush=True)
    payload = {
        "label": name,
        "mu": mu,
        "NB": NB,
        "dps": dps,
        "seconds": round(time.time() - t0, 1),
        "rows": rows,
    }
    here = os.path.dirname(os.path.abspath(__file__))
    dest = os.path.join(
        here, "..", "report", f"gl2-{name}-mu{int(mu)}-quorum.json"
    )
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"wrote {dest}", flush=True)
    full = next(r for r in rows if r["drop"] is None)
    d3 = next((r for r in rows if r["drop"] == 3), None)
    if name == "37a1" and d3 is not None and int(mu) in (62, 74, 80):
        # §116: drop 3 → negative at μ=62 (killed). Next: μ=74, linear
        # 0.38→0.093 crosses ~70.
        print(
            "KILL" if d3["lam0"] > 0 else "SURVIVE",
            f"mu={int(mu)}",
            f"full={full['lam0']:.4e}",
            f"drop3={d3['lam0']:.4e}",
            flush=True,
        )


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
