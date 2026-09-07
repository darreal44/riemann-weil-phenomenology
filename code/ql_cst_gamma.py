#!/usr/bin/env python3
"""CST+Gauss of D₂ vs C_A_lo vs log(q/π)+ψ(s₀). Constant mode.

Named in Qnm-is-not-Weil.md. Not RH.

    python code/ql_cst_gamma.py
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import (  # noqa: E402
    C_A_lo,
    PI,
    psi_s0,
    s0_of,
)
from ql_schur_tail import Q_nm  # noqa: E402

MUS = (3.0, 3.5, 5.0)
CHARS = (
    ("chi3", 3, s0_of(1)),
    ("chi5", 5, s0_of(0)),
)


def gamma_inf(q: int, s0: float) -> float:
    return math.log(q / PI) + psi_s0(s0)


def row_at(name: str, q: int, s0: float, mu: float) -> dict:
    L = math.log(mu)
    arch = Q_nm(0, 0, q, s0, 0.0, L)
    clo, _ = C_A_lo(q, s0, L)
    ginf = gamma_inf(q, s0)
    return {
        "name": name,
        "mu": mu,
        "L": L,
        "arch00": arch,
        "C_A_lo": clo,
        "gamma_inf": ginf,
        "gap_arch_CA": arch - clo,
        "gap_CA_inf": clo - ginf,
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    rows = [row_at(n, q, s0, mu) for n, q, s0 in CHARS for mu in MUS]
    chi3_3 = [r for r in rows if r["name"] == "chi3" and r["mu"] == 3.0][0]
    pred_ok = (
        abs(chi3_3["gap_arch_CA"]) > 0.5
        and all(abs(r["gap_arch_CA"]) > 0.5 for r in rows)
        and all(r["C_A_lo"] > r["gamma_inf"] for r in rows)
    )
    return {
        "step_taken": step_is_taken(),
        "identified": False,
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        "CST+Gauss vs C_A_lo vs ψ(s₀); constant mode; not RH",
        flush=True,
    )
    data = run()
    for r in data["rows"]:
        print(
            f"  {r['name']:4s} μ={r['mu']:.1f}  arch={r['arch00']:+.4f}  "
            f"C_A={r['C_A_lo']:+.4f}  gap={r['gap_arch_CA']:+.4f}  "
            f"Γ∞={r['gamma_inf']:+.4f}",
            flush=True,
        )
    print(
        f"identified={data['identified']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-cst-gamma.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
