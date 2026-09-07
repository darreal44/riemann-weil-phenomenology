#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""χ₃ λ_min(H_n) vs n at μ=7 and μ=8. Identified Q_pk.

Heads 16, 24, 32, 48. No Neumann. A negative section is
not a disproof of RH. Not (∀ L). Not RH.

    python code/ql_Hn_mu78.py
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
HEADS = (16, 24, 32, 48)
MUS = (7.0, 8.0)
_cache: dict[tuple[float, int, int], float] = {}


def Q(mu: float, n: int, m: int) -> float:
    L = math.log(mu)
    key = (mu, min(n, m), max(n, m))
    if key not in _cache:
        _cache[key] = Q_pk(n, m, Q3, S0, D3, L, mu)
    return _cache[key]


def row_at(mu: float, h: int) -> dict:
    L = math.log(mu)
    H = np.zeros((h, h))
    for i in range(h):
        for j in range(i, h):
            v = Q(mu, i, j)
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
    _cache.clear()
    rows = [row_at(mu, h) for mu in MUS for h in HEADS]
    by = {(r["mu"], r["h"]): r for r in rows}
    old_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-H16-mu.json",
    )
    old = json.load(open(old_path, encoding="utf-8"))
    old_by = {r["mu"]: r for r in old["rows"]}
    courant = True
    for mu in MUS:
        lams = [by[(mu, h)]["lamH"] for h in HEADS]
        if any(lams[i] + 1e-15 < lams[i + 1] for i in range(len(lams) - 1)):
            courant = False
    pred_ok = (
        by[(7.0, 16)]["ns"] == [2, 3, 4, 5]
        and by[(8.0, 16)]["ns"] == [2, 3, 4, 5, 7]
        and abs(by[(7.0, 16)]["lamH"] - old_by[7.0]["lamH"]) < 1e-12
        and abs(by[(8.0, 16)]["lamH"] - old_by[8.0]["lamH"]) < 1e-12
        and courant
    )
    return {
        "name": "chi3",
        "mus": list(MUS),
        "heads": list(HEADS),
        "courant_ok": courant,
        "any_negative": any(r["lamH"] <= 0.0 for r in rows),
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        "χ₃ H_n vs n; μ=7,8; Q_pk; not Neumann; not RH",
        flush=True,
    )
    data = run()
    print("mu   h    ns                 lamH", flush=True)
    for r in data["rows"]:
        print(
            f"{r['mu']:.1f}  {r['h']:2d}  {str(r['ns']):18s}  "
            f"{r['lamH']:+.6e}",
            flush=True,
        )
    print(
        f"any_neg={data['any_negative']}  courant={data['courant_ok']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-Hn-mu78.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
