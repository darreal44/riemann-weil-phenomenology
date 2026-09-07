#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""χ₄ and χ₅ Neumann at μ=8. Slivers at μ=7; T₇ now interior.

Identified Q_pk, cap √2. T infinite. Not Galerkin. Not RH.

    python code/ql_chi45_mu8.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_neumann_pk import clear_cache, row_at  # noqa: E402

NAMES = ("chi4", "chi5")
MU = 8.0
HEADS = (2, 4, 8, 16, 24)


def step_is_taken() -> bool:
    return False


def run() -> dict:
    clear_cache()
    rows = [row_at(n, MU, h) for n in NAMES for h in HEADS]
    taken = {
        n: [h for h in HEADS if any(r["name"] == n and r["h"] == h and r["s_lo_pos"] for r in rows)]
        for n in NAMES
    }
    early = any(h in taken[n] for n in NAMES for h in (2, 4, 8))
    by = {(r["name"], r["h"]): r for r in rows}
    pred_ok = (
        by[("chi4", 16)]["ns"] == [2, 3, 4, 5, 7]
        and by[("chi5", 16)]["ns"] == [2, 3, 4, 5, 7]
        and (not early)
    )
    return {
        "mu": MU,
        "names": list(NAMES),
        "heads": list(HEADS),
        "taken": taken,
        "early_take": early,
        "any_take": any(taken[n] for n in NAMES),
        "weil_positive": False,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print("χ₄ χ₅ Neumann μ=8; not RH", flush=True)
    data = run()
    for r in data["rows"]:
        slo = f"{r['s_lo']:+.4e}" if r["s_lo"] is not None else "—"
        print(
            f"  {r['name']:4s} h={r['h']:2d}  ρ={r['rho']:.3f}  Slo={slo}",
            flush=True,
        )
    print(
        f"taken={data['taken']}  any={data['any_take']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-chi45-mu8.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
