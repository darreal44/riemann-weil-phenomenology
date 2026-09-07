#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""T₅ on H₄ at μ=5.1 with Q_pk. Six-character quorum. Not RH.

    python code/ql_T5_H4.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import s0_of  # noqa: E402
from ql_q_pk import Q_pk, interior_ns  # noqa: E402

MUS = (5.0, 5.1)
CHARS = (
    ("chi3", 3, -3, 1),
    ("chi5", 5, 5, 0),
    ("chi4", 4, -4, 1),
    ("chi8", 8, 8, 0),
    ("chi7", 7, -7, 1),
    ("chi17", 17, 17, 0),
)


def row_at(name: str, q: int, d: int, a: int, mu: float) -> dict:
    L = math.log(mu)
    s0 = s0_of(a)
    H = np.zeros((4, 4))
    for i in range(4):
        for j in range(i, 4):
            v = Q_pk(i, j, q, s0, d, L, mu)
            H[i, j] = v
            H[j, i] = v
    return {
        "name": name,
        "mu": mu,
        "ns": interior_ns(mu),
        "H00": float(H[0, 0]),
        "lamH4": float(np.linalg.eigvalsh(H)[0]),
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    rows = [row_at(n, q, d, a, mu) for n, q, d, a in CHARS for mu in MUS]
    by = {(r["name"], r["mu"]): r for r in rows}
    pred_ok = (
        by[("chi3", 5.1)]["ns"] == [2, 3, 4, 5]
        and by[("chi3", 5.0)]["ns"] == [2, 3, 4]
        and by[("chi3", 5.1)]["lamH4"] > 0.0
        and all(by[(n, 5.1)]["lamH4"] > 0.0 for n, _, _, _ in CHARS)
        and by[("chi3", 5.1)]["H00"] > by[("chi3", 5.0)]["H00"]
    )
    return {
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print("T₅ on H₄; Q_pk; μ=5 vs 5.1; six χ; not RH", flush=True)
    data = run()
    for r in data["rows"]:
        print(
            f"  {r['name']:5s} μ={r['mu']:.1f}  ns={r['ns']}  "
            f"H00={r['H00']:+.4f}  lamH4={r['lamH4']:+.6f}",
            flush=True,
        )
    print(f"verdict={data['verdict']}", flush=True)
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-T5-H4.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
