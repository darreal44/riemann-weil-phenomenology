#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Neumann Q_pk six-character quorum at μ=7. Is χ₃ alone?

Identified form, cap √2. T infinite. Not Galerkin. Not RH.

    python code/ql_schur_quorum_mu7.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_neumann_pk import clear_cache, row_at  # noqa: E402

MU = 7.0
HEADS = (2, 4, 8, 16, 24)
GRID = ("chi3", "chi5", "chi4", "chi8", "chi7", "chi17")


def step_is_taken() -> bool:
    return False


def run() -> dict:
    clear_cache()
    rows = [row_at(name, MU, h) for name in GRID for h in HEADS]
    by = {(r["name"], r["h"]): r for r in rows}
    taken = {
        name: [h for h in HEADS if by[(name, h)]["s_lo_pos"]]
        for name in GRID
    }
    pred_ok = (
        by[("chi3", 16)]["ns"] == [2, 3, 4, 5]
        and (not by[("chi3", 16)]["s_lo_pos"])
        and (not by[("chi3", 24)]["s_lo_pos"])
        and all(by[(n, 16)]["ns"] == [2, 3, 4, 5] for n in GRID)
    )
    return {
        "mu": MU,
        "heads": list(HEADS),
        "grid": list(GRID),
        "taken": taken,
        "chi3_taken": bool(taken["chi3"]),
        "n_taken": sum(1 for v in taken.values() if v),
        "weil_positive": False,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        "Neumann Q_pk quorum μ=7; six χ; not RH",
        flush=True,
    )
    data = run()
    for name in GRID:
        bits = []
        for r in data["rows"]:
            if r["name"] != name:
                continue
            slo = f"{r['s_lo']:+.3e}" if r["s_lo"] is not None else "—"
            bits.append(f"h={r['h']}:{slo}")
        print(f"  {name:5s}  taken={data['taken'][name]}  {bits}", flush=True)
    print(
        f"chi3_taken={data['chi3_taken']}  n_taken={data['n_taken']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-quorum-mu7.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
