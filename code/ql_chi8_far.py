#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""χ₈ ρ_far at μ=8 vs 8.1. 2³ in t_atoms. Not a take. Not RH.

    python code/ql_chi8_far.py
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_neumann_pk import CHARS, clear_cache, far_pieces  # noqa: E402
from ql_q_pk import interior_ns, wn  # noqa: E402
from ql_theta_sqrt2 import theta_op_cap  # noqa: E402

MUS = (8.0, 8.1)
N_NEAR = 32


def step_is_taken() -> bool:
    return False


def run() -> dict:
    clear_cache()
    rows = []
    d = CHARS["chi8"]["d"]
    for mu in MUS:
        far = far_pieces("chi8", mu, N_NEAR)
        far["mu"] = mu
        far["ns"] = interior_ns(mu)
        far["w8"] = wn(d, 8)
        far["cap8"] = theta_op_cap(math.log(8.0), math.log(mu))
        rows.append(far)
    by = {r["mu"]: r for r in rows}
    pred_ok = (
        by[8.0]["ns"] == [2, 3, 4, 5, 7]
        and by[8.1]["ns"] == [2, 3, 4, 5, 7, 8]
        and by[8.1]["t_atoms"] > by[8.0]["t_atoms"]
        and by[8.1]["cap8"] == 1.0
    )
    return {
        "name": "chi8",
        "n_near": N_NEAR,
        "dt_atoms": by[8.1]["t_atoms"] - by[8.0]["t_atoms"],
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print("χ₈ ρ_far μ=8 vs 8.1; 2³; not a take; not RH", flush=True)
    data = run()
    for r in data["rows"]:
        print(
            f"  μ={r['mu']:.1f} ns={r['ns']}  t_atoms={r['t_atoms']:.4f}  "
            f"qmin={r['qmin_far']:.4f}  ρ_far={r['rho_far']:.3f}",
            flush=True,
        )
    print(f"dt_atoms={data['dt_atoms']:+.4f}  verdict={data['verdict']}", flush=True)
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-chi8-far.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
