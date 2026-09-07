#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""χ₇ Neumann on (3, 7]: when does the log-3 take die?

Identified Q_pk, cap √2. T infinite. Not Galerkin. Not RH.

    python code/ql_chi7_mu.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_neumann_pk import clear_cache, row_at  # noqa: E402

MUS = (3.0, 3.5, 5.0, 5.1, 7.0)
HEADS = (2, 4, 8, 16, 24)


def step_is_taken() -> bool:
    return False


def run() -> dict:
    clear_cache()
    rows = [row_at("chi7", mu, h) for mu in MUS for h in HEADS]
    by = {(r["mu"], r["h"]): r for r in rows}
    taken = {
        mu: [h for h in HEADS if by[(mu, h)]["s_lo_pos"]] for mu in MUS
    }
    dead = [mu for mu in MUS if not taken[mu]]
    first_dead = dead[0] if dead else None
    pred_ok = (
        by[(3.0, 2)]["ns"] == [2]
        and by[(5.1, 2)]["ns"] == [2, 3, 4, 5]
        and by[(7.0, 2)]["ns"] == [2, 3, 4, 5]
        and by[(3.0, 2)]["s_lo"] is not None
        and by[(3.0, 2)]["s_lo"] > 0.2
        and (not taken[7.0])
    )
    return {
        "name": "chi7",
        "mus": list(MUS),
        "heads": list(HEADS),
        "taken": taken,
        "first_dead": first_dead,
        "weil_positive": False,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print("χ₇ Neumann μ=3..7; take death; not RH", flush=True)
    data = run()
    for mu in MUS:
        bits = []
        for r in data["rows"]:
            if r["mu"] != mu:
                continue
            slo = f"{r['s_lo']:+.3e}" if r["s_lo"] is not None else "—"
            bits.append(f"h={r['h']}:{slo}")
        print(
            f"  μ={mu:.1f}  taken={data['taken'][mu]}  {bits}",
            flush=True,
        )
    print(
        f"first_dead={data['first_dead']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-chi7-mu.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
