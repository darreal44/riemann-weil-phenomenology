#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""True Schur of the computed near block: S_T = H − C T^{-1} C*.

S_diag uses D=diag(T), not T. S_lo inflates by 1/(1−ρ) and
the far envelope. S_T inverts the Gauss T on hats
HEAD…N_NEAR (30×30). It is still not S of the infinite
tail. Not Galerkin of W_L. Not RH.

    python code/ql_schur_Tnear.py
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ql_schur_neumann as neu


def row_ST(name: str) -> dict:
    r = neu.row_of(name)
    dim = neu.N_NEAR - neu.HEAD
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(neu.HEAD, neu.N_NEAR)):
        for j, m in enumerate(range(neu.HEAD, neu.N_NEAR)):
            T[i, j] = neu.Q(name, n, m)
    H = np.array(
        [[neu.Q(name, i, j) for j in range(neu.HEAD)] for i in range(neu.HEAD)],
        float,
    )
    C = np.array(
        [
            [neu.Q(name, i, m) for m in range(neu.HEAD, neu.N_NEAR)]
            for i in range(neu.HEAD)
        ],
        float,
    )
    evals_T = np.linalg.eigvalsh(T)
    tmin = float(evals_T[0])
    # T X = C*; S_T = H − C X
    X = np.linalg.solve(T, C.T)
    ST = H - C @ X
    s_T = float(np.linalg.eigvalsh(ST)[0])
    r["tmin"] = tmin
    r["s_T"] = s_T
    r["s_T_pos"] = bool(s_T > 0.0)
    r["cond_T"] = float(evals_T[-1] / evals_T[0]) if tmin > 0.0 else float("inf")
    return r


def main() -> int:
    neu._cache.clear()
    print(
        "S_T = H−C T_near^{-1} C*; not D^{-1}; not 1/(1−ρ); not infinite S",
        flush=True,
    )
    rows = [row_ST(name) for name in ("chi5", "chi8", "chi4", "chi3")]
    print(
        f"{'χ':4s}  {'λ_H':>9s}  {'S_diag':>9s}  {'S_T':>9s}  "
        f"{'S_lo':>9s}  tmin    ρ",
        flush=True,
    )
    for r in rows:
        slo = f"{r['s_lo']:+.4f}" if r["s_lo"] is not None else "−∞"
        print(
            f"{r['name']:4s}  {r['lamH']:+9.4f}  {r['s_diag']:+9.4f}  "
            f"{r['s_T']:+9.4f}  {slo:>9s}  {r['tmin']:.3f}  {r['rho']:.3f}",
            flush=True,
        )
    by = {r["name"]: r for r in rows}
    chi3_near_ok = by["chi3"]["s_T"] > 0.0 and by["chi3"]["tmin"] > 0.0
    data = {
        "step_taken": False,
        "verdict": "KILL",
        "why": (
            "S_T is the Schur of the computed T_near, not of the "
            "infinite tail; χ₃ S_lo still red"
        ),
        "chi3_s_T_pos": chi3_near_ok,
        "chi3_s_lo_pos": by["chi3"]["s_lo_pos"],
        "rows": rows,
    }
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-Tnear.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(
            {
                "step_taken": data["step_taken"],
                "verdict": data["verdict"],
                "why": data["why"],
                "chi3_s_T_pos": data["chi3_s_T_pos"],
                "chi3_s_lo_pos": data["chi3_s_lo_pos"],
                "rows": [
                    {
                        k: (float(v) if isinstance(v, (float, np.floating)) else v)
                        for k, v in r.items()
                    }
                    for r in rows
                ],
            },
            f,
            indent=2,
        )
        f.write("\n")
    print(f"wrote {out}", flush=True)
    print(
        f"chi3 S_T>0={chi3_near_ok}  S_lo>0={by['chi3']['s_lo_pos']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
