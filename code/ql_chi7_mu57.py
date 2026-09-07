#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""χ₇ Neumann on (5.1, 7], h=16 and 24. Where the sliver dies.

Identified Q_pk. T infinite. Not RH.

    python code/ql_chi7_mu57.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_neumann_pk import clear_cache, row_at  # noqa: E402

MUS = (5.1, 5.5, 6.0, 6.5, 7.0)
HEADS = (16, 24)


def step_is_taken() -> bool:
    return False


def run() -> dict:
    clear_cache()
    rows = [row_at("chi7", mu, h) for mu in MUS for h in HEADS]
    by = {(r["mu"], r["h"]): r for r in rows}
    taken = {mu: [h for h in HEADS if by[(mu, h)]["s_lo_pos"]] for mu in MUS}
    dead = [mu for mu in MUS if not taken[mu]]
    pred_ok = (
        by[(5.1, 24)]["s_lo_pos"]
        and (not taken[7.0])
        and by[(5.1, 24)]["ns"] == [2, 3, 4, 5]
        and by[(7.0, 24)]["ns"] == [2, 3, 4, 5]
    )
    return {
        "name": "chi7",
        "mus": list(MUS),
        "heads": list(HEADS),
        "taken": {str(mu): taken[mu] for mu in MUS},
        "first_dead": dead[0] if dead else None,
        "weil_positive": False,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print("χ₇ Neumann (5.1, 7] h=16,24; not RH", flush=True)
    data = run()
    for r in data["rows"]:
        slo = f"{r['s_lo']:+.4e}" if r["s_lo"] is not None else "—"
        print(
            f"  μ={r['mu']:.1f} h={r['h']:2d}  ρ={r['rho']:.3f}  Slo={slo}",
            flush=True,
        )
    print(
        f"taken={data['taken']}  first_dead={data['first_dead']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-chi7-mu57.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
