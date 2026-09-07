#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Identified Q_pk, χ₃, λ_min(H₁₆) vs μ through 7 and 8=2³.

Head 16. CST+Gauss. No Neumann. A negative section is not
a disproof of RH. Not (∀ L). Not RH.

    python code/ql_H16_mu.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import s0_of  # noqa: E402
from ql_q_pk import D3, Q3, Q_pk, interior_ns  # noqa: E402

S0 = s0_of(1)
HEAD = 16
MUS = (5.0, 7.0, 7.1, 8.0, 8.1)


def row_at(mu: float) -> dict:
    L = math.log(mu)
    H = np.zeros((HEAD, HEAD))
    for i in range(HEAD):
        for j in range(i, HEAD):
            v = Q_pk(i, j, Q3, S0, D3, L, mu)
            H[i, j] = v
            H[j, i] = v
    lam = float(np.linalg.eigvalsh(H)[0])
    return {
        "mu": mu,
        "L": L,
        "h": HEAD,
        "ns": interior_ns(mu),
        "H00": float(H[0, 0]),
        "lamH": lam,
        "lamH_pos": bool(lam > 0.0),
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    rows = [row_at(mu) for mu in MUS]
    by = {r["mu"]: r for r in rows}
    old_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-pk-mu5.json",
    )
    old = json.load(open(old_path, encoding="utf-8"))
    old16 = [r for r in old["rows"] if r["h"] == 16][0]["lamH"]
    d71 = by[7.1]["lamH"] - by[7.0]["lamH"]
    d81 = by[8.1]["lamH"] - by[8.0]["lamH"]
    pred_ok = (
        by[5.0]["ns"] == [2, 3, 4]
        and by[7.0]["ns"] == [2, 3, 4, 5]
        and by[7.1]["ns"] == [2, 3, 4, 5, 7]
        and by[8.0]["ns"] == [2, 3, 4, 5, 7]
        and by[8.1]["ns"] == [2, 3, 4, 5, 7, 8]
        and abs(by[5.0]["lamH"] - old16) < 1e-12
        and abs(d71) < 1e-2
        and abs(d81) < 1e-2
    )
    return {
        "name": "chi3",
        "head": HEAD,
        "mus": list(MUS),
        "lamH16_mu5_ref": old16,
        "dlam_T7": d71,
        "dlam_8": d81,
        "any_negative": any(r["lamH"] <= 0.0 for r in rows),
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        "χ₃ H₁₆ vs μ, Q_pk; through 7 and 8=2³; not RH",
        flush=True,
    )
    data = run()
    print("mu    ns                 H00       lamH16", flush=True)
    for r in data["rows"]:
        print(
            f"{r['mu']:.1f}  {str(r['ns']):18s}  {r['H00']:+.5f}  "
            f"{r['lamH']:+.6e}",
            flush=True,
        )
    print(
        f"dT7={data['dlam_T7']:+.3e}  d8={data['dlam_8']:+.3e}  "
        f"any_neg={data['any_negative']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-H16-mu.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
