#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""χ₇ vs χ₁₇ far tail at μ=7. Same χ(2)=+1; one takes, one fails.

Identified Q_pk, cap √2. N_NEAR=32. Not a take. Not RH.

    python code/ql_chi7_vs_chi17.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kronecker import kronecker  # noqa: E402
from ql_neumann_pk import CHARS, clear_cache, far_pieces  # noqa: E402
from ql_q_pk import interior_ns, wn  # noqa: E402

MU = 7.0
N_NEAR = 32
NAMES = ("chi7", "chi17")


def step_is_taken() -> bool:
    return False


def weights(name: str) -> dict:
    d = CHARS[name]["d"]
    out = {}
    for k in interior_ns(MU) + [7]:
        out[str(k)] = wn(d, k)
    out["chi7_at_7"] = kronecker(d, 7)
    return out


def run() -> dict:
    clear_cache()
    rows = []
    for name in NAMES:
        far = far_pieces(name, MU, N_NEAR)
        far["name"] = name
        far["s0"] = 0.75 if CHARS[name]["a"] == 1 else 0.25
        far["chi2"] = kronecker(CHARS[name]["d"], 2)
        far["ns"] = interior_ns(MU)
        far["weights"] = weights(name)
        rows.append(far)
    by = {r["name"]: r for r in rows}
    tat_diff = abs(by["chi7"]["t_atoms"] - by["chi17"]["t_atoms"])
    qmin_diff = abs(by["chi7"]["qmin_far"] - by["chi17"]["qmin_far"])
    sides = (by["chi7"]["rho_far"] >= 1.0, by["chi17"]["rho_far"] >= 1.0)
    explained = (tat_diff > 1e-6) or (sides[0] != sides[1]) or (qmin_diff > 0.1)
    pred_ok = (
        by["chi7"]["ns"] == [2, 3, 4, 5]
        and by["chi17"]["ns"] == [2, 3, 4, 5]
        and by["chi7"]["weights"]["chi7_at_7"] == 0.0
        and by["chi7"]["chi2"] == 1
        and by["chi17"]["chi2"] == 1
        and explained
    )
    return {
        "mu": MU,
        "n_near": N_NEAR,
        "explained": explained,
        "tat_diff": tat_diff,
        "qmin_diff": qmin_diff,
        "rho_far_sides_differ": sides[0] != sides[1],
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print("χ₇ vs χ₁₇ far tail μ=7; not a take; not RH", flush=True)
    data = run()
    for r in data["rows"]:
        print(
            f"  {r['name']:5s} s0={r['s0']}  t_atoms={r['t_atoms']:.4f}  "
            f"qmin={r['qmin_far']:.4f}  ρ_far={r['rho_far']:.3f}  "
            f"χ(7)={r['weights']['chi7_at_7']}",
            flush=True,
        )
        print(f"         w={r['weights']}", flush=True)
    print(
        f"explained={data['explained']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-chi7-vs-chi17.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
