#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""CST 4-plane vs 2 m_Q(ω_n) hybrid, χ₃ μ=5.

Diagonals Q_nn^{arch} vs 2 m_Q(ω_n). Hybrid = 2 m_Q
on diag, CST off-diag, plus p^k. Not RH.

    python code/ql_arch_4plane.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import C_A_lo, PI, k_of_t, s0_of  # noqa: E402
from ql_q_pk import D3, Q3, interior_ns, wn  # noqa: E402
from ql_schur_tail import Q_nm, theta_hat  # noqa: E402

S0 = s0_of(1)
MU = 5.0
L = math.log(MU)
H = 4


def m_arch(t: float) -> float:
    clo, _ = C_A_lo(Q3, S0, L)
    kt, _ = k_of_t(t, S0, L)
    return 0.5 * clo + kt


def omega(n: int) -> float:
    return 0.0 if n == 0 else 2.0 * PI * n / L


def mat_cst_arch() -> np.ndarray:
    M = np.zeros((H, H))
    for i in range(H):
        for j in range(i, H):
            v = Q_nm(i, j, Q3, S0, 0.0, L)
            M[i, j] = v
            M[j, i] = v
    return M


def mat_pk_side() -> np.ndarray:
    P = np.zeros((H, H))
    for k in interior_ns(MU):
        w = wn(D3, k)
        y = math.log(k)
        for i in range(H):
            for j in range(i, H):
                v = -w * theta_hat(i, j, y, L)
                P[i, j] += v
                if i != j:
                    P[j, i] += v
    return P


def step_is_taken() -> bool:
    return False


def run() -> dict:
    C = mat_cst_arch()
    P = mat_pk_side()
    diag_m = [2.0 * m_arch(omega(n)) for n in range(H)]
    D = np.diag(diag_m)
    Off = C - np.diag(np.diag(C))
    hybrid = D + Off + P
    cst_pk = C + P
    gaps = [diag_m[n] - float(C[n, n]) for n in range(H)]
    lam_cst = float(np.linalg.eigvalsh(cst_pk)[0])
    lam_hyb = float(np.linalg.eigvalsh(hybrid)[0])
    clo, _ = C_A_lo(Q3, S0, L)
    pred_ok = (
        lam_cst > 0.0
        and lam_hyb < 0.0
        and gaps[0] < -0.5
        and all(g < 0.0 for g in gaps)
    )
    return {
        "mu": MU,
        "L": L,
        "C_A_lo": clo,
        "diag_2mQ": diag_m,
        "diag_Qnn_arch": [float(C[n, n]) for n in range(H)],
        "gaps": gaps,
        "lam_CST_pk": lam_cst,
        "lam_hybrid_pk": lam_hyb,
        "signs_agree": (lam_cst > 0.0) == (lam_hyb > 0.0),
        "step_taken": step_is_taken(),
        "identified": False,
        "verdict": "SURVIVE" if pred_ok else "KILL",
    }


def main() -> int:
    print("CST 4-plane vs 2 m_Q(ω_n) hybrid; χ₃ μ=5; not RH", flush=True)
    data = run()
    print(
        f"  2mQ={['{:+.4f}'.format(x) for x in data['diag_2mQ']]}",
        flush=True,
    )
    print(
        f"  Qnn={['{:+.4f}'.format(x) for x in data['diag_Qnn_arch']]}",
        flush=True,
    )
    print(
        f"  lam CST+pk={data['lam_CST_pk']:+.6e}  "
        f"hybrid={data['lam_hybrid_pk']:+.6f}  "
        f"signs_agree={data['signs_agree']}",
        flush=True,
    )
    print(f"verdict={data['verdict']}", flush=True)
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-arch-4plane.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
