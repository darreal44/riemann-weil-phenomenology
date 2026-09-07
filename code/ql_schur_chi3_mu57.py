#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Neumann Q_pk χ₃ on (5, 7], h=16 and 24. When does the take die?

Identified form, cap √2. T infinite. Not Galerkin. Not RH.

    python code/ql_schur_chi3_mu57.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_neumann_pk import clear_cache, row_at  # noqa: E402

MUS = (5.0, 5.5, 6.0, 6.5, 7.0)
HEADS = (16, 24)


def step_is_taken() -> bool:
    return False


def run() -> dict:
    clear_cache()
    rows = [row_at("chi3", mu, h) for mu in MUS for h in HEADS]
    by = {(r["mu"], r["h"]): r for r in rows}
    old_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-H16-mu.json",
    )
    old = json.load(open(old_path, encoding="utf-8"))
    old_by = {r["mu"]: r for r in old["rows"]}
    take_mu = sorted(
        {r["mu"] for r in rows if r["h"] == 16 and r["s_lo_pos"]}
    )
    pred_ok = (
        by[(5.0, 16)]["ns"] == [2, 3, 4]
        and by[(7.0, 16)]["ns"] == [2, 3, 4, 5]
        and by[(5.0, 16)]["s_lo_pos"]
        and (not by[(7.0, 16)]["s_lo_pos"])
        and by[(5.0, 16)]["log2_in_band"]
        and by[(7.0, 16)]["log2_in_band"]
        and abs(by[(5.0, 16)]["lamH"] - old_by[5.0]["lamH"]) < 1e-12
        and abs(by[(7.0, 16)]["lamH"] - old_by[7.0]["lamH"]) < 1e-12
    )
    return {
        "name": "chi3",
        "mus": list(MUS),
        "heads": list(HEADS),
        "take_mu_h16": take_mu,
        "take_dies": 5.0 in take_mu and 7.0 not in take_mu,
        "weil_positive": False,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        "Neumann Q_pk χ₃ (5,7] h=16,24; take die?; not RH",
        flush=True,
    )
    data = run()
    for r in data["rows"]:
        slo = f"{r['s_lo']:+.6e}" if r["s_lo"] is not None else "  —"
        print(
            f"  μ={r['mu']:.1f} h={r['h']:2d}  lamH={r['lamH']:+.6e}  "
            f"ρ={r['rho']:.3f}  Slo={slo}",
            flush=True,
        )
    print(
        f"take_mu_h16={data['take_mu_h16']}  dies={data['take_dies']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-chi3-mu57.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
