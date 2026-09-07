#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""χ₃ Neumann at μ=5 vs 5.1: does T₅ arrival kill the take?

Identified Q_pk, cap √2. T infinite. Not Galerkin. Not RH.

    python code/ql_chi3_mu51.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_neumann_pk import clear_cache, far_pieces, row_at  # noqa: E402

MUS = (5.0, 5.1)
HEADS = (16, 24)
N_NEAR = 32


def step_is_taken() -> bool:
    return False


def run() -> dict:
    clear_cache()
    rows = [row_at("chi3", mu, h) for mu in MUS for h in HEADS]
    fars = []
    for mu in MUS:
        far = far_pieces("chi3", mu, N_NEAR)
        far["mu"] = mu
        fars.append(far)
    by = {(r["mu"], r["h"]): r for r in rows}
    byf = {f["mu"]: f for f in fars}
    pred_ok = (
        by[(5.1, 16)]["ns"] == [2, 3, 4, 5]
        and by[(5.0, 16)]["ns"] == [2, 3, 4]
        and by[(5.0, 16)]["s_lo_pos"]
        and byf[5.1]["t_atoms"] > byf[5.0]["t_atoms"]
    )
    return {
        "name": "chi3",
        "mus": list(MUS),
        "heads": list(HEADS),
        "take_at_51": bool(by[(5.1, 16)]["s_lo_pos"] or by[(5.1, 24)]["s_lo_pos"]),
        "dies_at_arrival": by[(5.0, 16)]["s_lo_pos"]
        and (not by[(5.1, 16)]["s_lo_pos"]),
        "weil_positive": False,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "far": fars,
        "rows": rows,
    }


def main() -> int:
    print(
        "χ₃ Neumann μ=5 vs 5.1; T₅ arrival; not RH",
        flush=True,
    )
    data = run()
    for f in data["far"]:
        print(
            f"  far μ={f['mu']:.1f}  t_atoms={f['t_atoms']:.4f}  "
            f"ρ_far={f['rho_far']:.3f}",
            flush=True,
        )
    for r in data["rows"]:
        slo = f"{r['s_lo']:+.6e}" if r["s_lo"] is not None else "  —"
        print(
            f"  μ={r['mu']:.1f} h={r['h']:2d}  ρ={r['rho']:.3f}  Slo={slo}",
            flush=True,
        )
    print(
        f"dies_at_arrival={data['dies_at_arrival']}  "
        f"take_at_51={data['take_at_51']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-chi3-mu51.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
