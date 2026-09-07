#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""χ₈ and χ₁₇ Neumann at μ=8; μ=11 if χ₁₇ still takes.

Identified Q_pk, cap √2. T infinite. Not Galerkin. Not RH.

    python code/ql_chi817_mu8.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_neumann_pk import clear_cache, row_at  # noqa: E402

NAMES = ("chi8", "chi17")
HEADS = (2, 4, 8, 16, 24)
MU8 = 8.0
MU11 = 11.0


def step_is_taken() -> bool:
    return False


def run() -> dict:
    clear_cache()
    rows = [row_at(n, MU8, h) for n in NAMES for h in HEADS]
    taken8 = {
        n: [h for h in HEADS if any(r["name"] == n and r["h"] == h and r["s_lo_pos"] for r in rows)]
        for n in NAMES
    }
    chi17_takes_8 = bool(taken8["chi17"])
    mus_run = [MU8]
    if chi17_takes_8:
        mus_run.append(MU11)
        rows += [row_at(n, MU11, h) for n in NAMES for h in HEADS]
    taken11 = {
        n: [
            h
            for h in HEADS
            if any(
                r["name"] == n and r["mu"] == MU11 and r["h"] == h and r["s_lo_pos"]
                for r in rows
            )
        ]
        for n in NAMES
    }
    by = {(r["name"], r["mu"], r["h"]): r for r in rows}
    pred_ok = (
        by[("chi17", MU8, 16)]["ns"] == [2, 3, 4, 5, 7]
        and by[("chi8", MU8, 16)]["ns"] == [2, 3, 4, 5, 7]
        and chi17_takes_8
    )
    return {
        "names": list(NAMES),
        "heads": list(HEADS),
        "mus_run": mus_run,
        "taken8": taken8,
        "taken11": taken11 if chi17_takes_8 else None,
        "chi17_takes_8": chi17_takes_8,
        "weil_positive": False,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        "χ₈ χ₁₇ Neumann μ=8 then 11 if χ₁₇ takes; not RH",
        flush=True,
    )
    data = run()
    for r in data["rows"]:
        slo = f"{r['s_lo']:+.4e}" if r["s_lo"] is not None else "—"
        print(
            f"  {r['name']:5s} μ={r['mu']:.0f} h={r['h']:2d}  "
            f"ρ={r['rho']:.3f}  Slo={slo}",
            flush=True,
        )
    print(
        f"taken8={data['taken8']}  taken11={data['taken11']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-chi817-mu8.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
