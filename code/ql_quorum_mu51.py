#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Quorum Neumann at μ=5.1, T₅ arrival, h=16 and 24.

Identified Q_pk. T infinite. Not RH.

    python code/ql_quorum_mu51.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_neumann_pk import clear_cache, row_at  # noqa: E402

MU = 5.1
HEADS = (16, 24)
GRID = ("chi3", "chi5", "chi4", "chi8", "chi7", "chi17")


def step_is_taken() -> bool:
    return False


def run() -> dict:
    clear_cache()
    rows = [row_at(n, MU, h) for n in GRID for h in HEADS]
    taken = {
        n: [h for h in HEADS if any(r["name"] == n and r["h"] == h and r["s_lo_pos"] for r in rows)]
        for n in GRID
    }
    by = {(r["name"], r["h"]): r for r in rows}
    pred_ok = (
        by[("chi3", 16)]["ns"] == [2, 3, 4, 5]
        and (not taken["chi3"])
        and 24 in taken["chi7"]
    )
    return {
        "mu": MU,
        "heads": list(HEADS),
        "grid": list(GRID),
        "taken": taken,
        "n_taken": sum(1 for v in taken.values() if v),
        "weil_positive": False,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print("quorum Neumann μ=5.1 T₅; not RH", flush=True)
    data = run()
    for n in GRID:
        print(f"  {n:5s}  taken={data['taken'][n]}", flush=True)
    print(
        f"n_taken={data['n_taken']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-quorum-mu51.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
