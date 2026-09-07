#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""χ₃ λ_min(H_2) and λ_min(H_4) vs μ on (3.5, 5].

Same Q_window as #66/#67. No Neumann. Negative H_4
is c_L^*<0 on that 4-plane. Not RH.

    python code/ql_chi3_H4_mu.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from log2_log3_step import interior_primes  # noqa: E402
from ql_operator_bound import LOG2, s0_of  # noqa: E402
from ql_schur_mu35 import Q_window  # noqa: E402
from ql_theta_tail import theta_op_bound  # noqa: E402

MUS = (3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0)
HEADS = (2, 4)
Q3, D3, A3 = 3, -3, 1
S0 = s0_of(A3)


def row_at(mu: float, h: int) -> dict:
    L = math.log(mu)
    H = np.zeros((h, h))
    for i in range(h):
        for j in range(i, h):
            v = Q_window(i, j, Q3, S0, D3, L, mu)
            H[i, j] = v
            H[j, i] = v
    lam = float(np.linalg.eigvalsh(H)[0])
    return {
        "mu": mu,
        "h": h,
        "L": L,
        "primes": interior_primes(mu),
        "log2_ge_half": bool(LOG2 >= 0.5 * L),
        "theta_op_log2": theta_op_bound(LOG2, L),
        "H00": float(H[0, 0]),
        "lamH": lam,
        "lamH_pos": bool(lam > 0.0),
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    rows = [row_at(mu, h) for mu in MUS for h in HEADS]
    by = {(r["mu"], r["h"]): r for r in rows}
    h4 = [by[(mu, 4)] for mu in MUS]
    pos = [r["mu"] for r in h4 if r["lamH_pos"]]
    neg = [r["mu"] for r in h4 if not r["lamH_pos"]]
    last_pos = pos[-1] if pos else None
    first_neg = neg[0] if neg else None
    mu_star = (
        [last_pos, first_neg]
        if last_pos is not None and first_neg is not None
        else None
    )
    pred_ok = (
        all(by[(mu, 2)]["lamH"] > 0.0 for mu in MUS)
        and by[(4.75, 4)]["lamH"] > 0.0
        and by[(5.0, 4)]["lamH"] < 0.0
        and by[(3.5, 4)]["lamH"] > 0.0
        and by[(4.0, 4)]["lamH"] > 0.0
        and mu_star == [4.75, 5.0]
        and all(r["primes"] == [2, 3] for r in rows)
    )
    return {
        "name": "chi3",
        "mus": list(MUS),
        "heads": list(HEADS),
        "step_taken": step_is_taken(),
        "mu_star": mu_star,
        "first_negative_mu": first_neg,
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        "χ₃ H₂/H₄ vs μ; Q_window; no Neumann; not Galerkin positivity; not RH",
        flush=True,
    )
    data = run()
    print("mu    lamH2      lamH4     th2", flush=True)
    by = {(r["mu"], r["h"]): r for r in data["rows"]}
    for mu in MUS:
        a = by[(mu, 2)]
        b = by[(mu, 4)]
        print(
            f"{mu:.2f}  {a['lamH']:+.6f}  {b['lamH']:+.6f}  "
            f"{a['theta_op_log2']:.0f}",
            flush=True,
        )
    print(
        f"mu*={data['mu_star']}  first_neg={data['first_negative_mu']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-chi3-H4-mu.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
