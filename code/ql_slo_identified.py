#!/usr/bin/env python3
"""Re-judge S_lo of identified Q_pk, χ₃ μ=5, cap ‖Θ‖=2.

The arch gap 0.6 is dead. Same Neumann as #70. T infinite.
A take of W_log5 in the certificates-Wlog3 sense is not
Weil-positive. Not RH.

    python code/ql_slo_identified.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_schur_pk_mu5 import run as run_pk  # noqa: E402


def step_is_taken() -> bool:
    return False


def run() -> dict:
    pk = run_pk()
    by = {r["h"]: r for r in pk["rows"]}
    take = (
        by[16]["s_lo"] is not None
        and by[16]["s_lo"] > 0.0
        and by[24]["s_lo"] is not None
        and by[24]["s_lo"] > 0.0
        and by[2]["s_lo"] < 0.0
        and by[4]["s_lo"] < 0.0
        and by[24]["lamH"] > 0.0
    )
    pred_ok = take and pk["verdict"] == "SURVIVE"
    return {
        "mu": pk["mu"],
        "name": pk["name"],
        "ns": pk["ns"],
        "rows": pk["rows"],
        "identified_arch": True,
        "w_log5_take": take,
        "weil_positive": False,
        "weil_negative": False,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
    }


def main() -> int:
    print(
        "S_lo identified Q_pk χ₃ μ=5 cap 2; take ≠ Weil+; not RH",
        flush=True,
    )
    data = run()
    by = {r["h"]: r for r in data["rows"]}
    for h in (2, 4, 8, 16, 20, 24):
        r = by[h]
        slo = f"{r['s_lo']:+.6e}" if r["s_lo"] is not None else "  —"
        print(
            f"  h={h:2d}  lamH={r['lamH']:+.6e}  Slo={slo}",
            flush=True,
        )
    print(
        f"w_log5_take={data['w_log5_take']}  Weil+={data['weil_positive']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-slo-identified.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
