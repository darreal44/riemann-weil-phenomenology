#!/usr/bin/env python3
"""χ₃ λ_min(H_2) and λ_min(H_4) vs μ, with Q_pk (n=p^k).

Same grid as #68. Filling 2² at μ>4. No Neumann. Not RH.

    python code/ql_chi3_H4_pk.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_chi3_H4_mu import HEADS, MUS  # noqa: E402
from ql_operator_bound import s0_of  # noqa: E402
from ql_q_pk import D3, Q3, Q_pk, interior_ns  # noqa: E402

S0 = s0_of(1)


def row_at(mu: float, h: int) -> dict:
    L = math.log(mu)
    H = np.zeros((h, h))
    for i in range(h):
        for j in range(i, h):
            v = Q_pk(i, j, Q3, S0, D3, L, mu)
            H[i, j] = v
            H[j, i] = v
    lam = float(np.linalg.eigvalsh(H)[0])
    return {
        "mu": mu,
        "h": h,
        "L": L,
        "ns": interior_ns(mu),
        "H00": float(H[0, 0]),
        "lamH": lam,
        "lamH_pos": bool(lam > 0.0),
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    rows = [row_at(mu, h) for mu in MUS for h in HEADS]
    by = {(r["mu"], r["h"]): r for r in rows}
    pred_ok = (
        all(by[(mu, 2)]["lamH"] > 0.0 for mu in MUS)
        and all(by[(mu, 4)]["lamH"] > 0.0 for mu in MUS)
        and by[(3.5, 4)]["ns"] == [2, 3]
        and by[(4.0, 4)]["ns"] == [2, 3]
        and by[(4.25, 4)]["ns"] == [2, 3, 4]
        and by[(5.0, 4)]["ns"] == [2, 3, 4]
        and by[(5.0, 4)]["lamH"] > 0.0
        and abs(by[(3.5, 4)]["lamH"] - 0.002683744354559708) < 1e-12
    )
    return {
        "name": "chi3",
        "mus": list(MUS),
        "heads": list(HEADS),
        "step_taken": step_is_taken(),
        "mu_star": None,
        "h4_positive_on_grid": all(by[(mu, 4)]["lamH"] > 0.0 for mu in MUS),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        "χ₃ H₂/H₄ vs μ with Q_pk (p^k); no Neumann; not RH",
        flush=True,
    )
    data = run()
    print("mu    ns           H00      lamH2      lamH4", flush=True)
    by = {(r["mu"], r["h"]): r for r in data["rows"]}
    for mu in MUS:
        a, b = by[(mu, 2)], by[(mu, 4)]
        print(
            f"{mu:.2f}  {str(a['ns']):12s}  {a['H00']:+.5f}  "
            f"{a['lamH']:+.6f}  {b['lamH']:+.6f}",
            flush=True,
        )
    print(
        f"h4_all_pos={data['h4_positive_on_grid']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-chi3-H4-pk.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
