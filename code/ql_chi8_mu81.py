#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""χ₈ Neumann at μ=8, 8.1 (2³), 9.1 (3²). Last living take.

Identified Q_pk, cap √2. T infinite. Not Galerkin. Not RH.

    python code/ql_chi8_mu81.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_neumann_pk import clear_cache, row_at  # noqa: E402

MUS = (8.0, 8.1, 9.1)
HEADS = (2, 4, 8, 16, 24)


def step_is_taken() -> bool:
    return False


def run() -> dict:
    clear_cache()
    rows = [row_at("chi8", mu, h) for mu in MUS for h in HEADS]
    by = {(r["mu"], r["h"]): r for r in rows}
    old_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-chi817-mu8.json",
    )
    old = json.load(open(old_path, encoding="utf-8"))
    old24 = [
        r["s_lo"]
        for r in old["rows"]
        if r["name"] == "chi8" and r["mu"] == 8.0 and r["h"] == 24
    ][0]
    taken = {
        mu: [h for h in HEADS if by[(mu, h)]["s_lo_pos"]] for mu in MUS
    }
    pred_ok = (
        by[(8.0, 24)]["ns"] == [2, 3, 4, 5, 7]
        and by[(8.1, 24)]["ns"] == [2, 3, 4, 5, 7, 8]
        and by[(9.1, 24)]["ns"] == [2, 3, 4, 5, 7, 8, 9]
        and by[(8.0, 24)]["s_lo_pos"]
        and abs(by[(8.0, 24)]["s_lo"] - old24) < 1e-12
    )
    return {
        "name": "chi8",
        "mus": list(MUS),
        "heads": list(HEADS),
        "taken": taken,
        "alive_after_8": bool(taken[8.1] or taken[9.1]),
        "weil_positive": False,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print("χ₈ Neumann μ=8, 8.1, 9.1; not RH", flush=True)
    data = run()
    for r in data["rows"]:
        slo = f"{r['s_lo']:+.4e}" if r["s_lo"] is not None else "—"
        print(
            f"  μ={r['mu']:.1f} h={r['h']:2d}  ns={r['ns']}  "
            f"ρ={r['rho']:.3f}  Slo={slo}",
            flush=True,
        )
    print(
        f"taken={data['taken']}  alive_after_8={data['alive_after_8']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-chi8-mu81.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
