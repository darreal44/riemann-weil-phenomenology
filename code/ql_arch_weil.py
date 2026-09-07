#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Classical Γ pairing on W_L: CST+Gauss vs digamma vs mixed (ψ+γ)I.

On W_L, θ=0 for y>L. Frullani folds the EC tail into CST.
Weierstrass identifies the two writings. Mixing Γ∞ with EC
is not the classical term. The 10^{-5} of Q_pk H₄ is neither
Weil-positive nor Weil-negative. Not RH.

    python code/ql_arch_weil.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import (  # noqa: E402
    C_A_lo,
    D2,
    EC,
    EULER,
    N_PANELS,
    N_SERIES,
    PI,
    _gauss_nodes,
    psi_s0,
    s0_of,
)
from ql_q_pk import D3, Q3, Q_pk, interior_ns, wn  # noqa: E402
from ql_schur_tail import Q_nm, theta_hat  # noqa: E402

S0_ODD = s0_of(1)
S0_EVEN = s0_of(0)
MU = 5.0
L5 = math.log(MU)
H = 4
Y_WEIER = 8.0
N_PANELS_W = 64


def delta_psi_gamma(s0: float) -> float:
    """ψ(s₀)+γ. χ₃: π/2−3 log 2; χ₅: −π/2−3 log 2."""
    return psi_s0(s0) + EULER


def frullani_closed(L: float) -> float:
    return -math.log(1.0 - math.exp(-2.0 * L))


def frullani_series(L: float, n: int = N_SERIES) -> float:
    """∑_{k≥1} e^{-2 k L}/k = ∫_L^∞ D₂ EC."""
    acc = 0.0
    e = math.exp(-2.0 * L)
    pk = e
    for _k in range(1, n + 1):
        acc += pk / _k
        pk *= e
    return acc


def weierstrass_quad(s0: float, Y: float = Y_WEIER) -> float:
    """∫_0^∞ D₂(EC−1) dy: Gauss on (0,Y] plus exact series tail."""
    acc = 0.0
    h = Y / N_PANELS_W
    for p in range(N_PANELS_W):
        ys, ws = _gauss_nodes(p * h, (p + 1) * h)
        for y, w in zip(ys, ws):
            acc += w * D2(y, s0) * (EC(y, s0) - 1.0)
    tail = 0.0
    for k in range(N_SERIES):
        tail += math.exp(-2.0 * (k + 1) * Y) / (k + 1) - math.exp(
            -2.0 * (s0 + k) * Y
        ) / (s0 + k)
    return acc + tail


def arch_cst(n: int, m: int, q: int, s0: float, L: float) -> float:
    """Writing (1): Q_nm arch, w₂=0."""
    return Q_nm(n, m, q, s0, 0.0, L)


def arch_digamma(n: int, m: int, q: int, s0: float, L: float) -> float:
    """Writing (3): (F₀/2) C_A_lo + ½ ∫_0^L D₂(F₀−θ)."""
    if n > m:
        n, m = m, n
    F0 = 2.0 if n == m else 0.0
    clo, _ = C_A_lo(q, s0, L)
    acc = 0.0
    h = L / N_PANELS
    for p in range(N_PANELS):
        ys, ws = _gauss_nodes(p * h, (p + 1) * h)
        for y, w in zip(ys, ws):
            th = theta_hat(n, m, y, L)
            acc += w * D2(y, s0) * (F0 - th)
    return 0.5 * F0 * clo + 0.5 * acc


def mat_arch(fn, q: int, s0: float, L: float) -> np.ndarray:
    M = np.zeros((H, H))
    for i in range(H):
        for j in range(i, H):
            v = fn(i, j, q, s0, L)
            M[i, j] = v
            M[j, i] = v
    return M


def mat_pk_side(d: int, L: float, mu: float) -> np.ndarray:
    P = np.zeros((H, H))
    for k in interior_ns(mu):
        w = wn(d, k)
        y = math.log(k)
        for i in range(H):
            for j in range(i, H):
                v = -w * theta_hat(i, j, y, L)
                P[i, j] += v
                if i != j:
                    P[j, i] += v
    return P


def plane_of(name: str, q: int, d: int, s0: float) -> dict:
    C = mat_arch(arch_cst, q, s0, L5)
    D = mat_arch(arch_digamma, q, s0, L5)
    P = mat_pk_side(d, L5, MU)
    delta = delta_psi_gamma(s0)
    diff = C - D
    max_abs = float(np.max(np.abs(diff)))
    lam_cst = float(np.linalg.eigvalsh(C + P)[0])
    lam_dig = float(np.linalg.eigvalsh(D + P)[0])
    lam_mix = float(np.linalg.eigvalsh(C + P + delta * np.eye(H))[0])
    pk = Q_pk(0, 0, q, s0, d, L5, MU)
    clo, _ = C_A_lo(q, s0, L5)
    return {
        "name": name,
        "q": q,
        "s0": s0,
        "delta": delta,
        "max_abs_CST_digamma": max_abs,
        "diag_CST": [float(C[n, n]) for n in range(H)],
        "diag_digamma": [float(D[n, n]) for n in range(H)],
        "diag_gap": [float(C[n, n] - D[n, n]) for n in range(H)],
        "offdiag_max_abs": float(
            np.max(np.abs(C - np.diag(np.diag(C)) - (D - np.diag(np.diag(D)))))
        ),
        "arch00_CST": float(C[0, 0]),
        "C_A_lo": clo,
        "gap_arch_CA": float(C[0, 0] - clo),
        "lam_CST_pk": lam_cst,
        "lam_digamma_pk": lam_dig,
        "lam_mixed_pk": lam_mix,
        "Q_pk_00": pk,
        "ns": interior_ns(MU),
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    fr_closed = frullani_closed(L5)
    fr_series = frullani_series(L5)
    fr_err = abs(fr_closed - fr_series)
    w_rows = []
    for s0 in (S0_ODD, S0_EVEN):
        quad = weierstrass_quad(s0)
        target = delta_psi_gamma(s0)
        w_rows.append(
            {
                "s0": s0,
                "quad": quad,
                "psi_plus_gamma": target,
                "err": abs(quad - target),
            }
        )
    chi3 = plane_of("chi3", Q3, D3, S0_ODD)
    chi5 = plane_of("chi5", 5, 5, S0_EVEN)
    writings_agree = (
        chi3["max_abs_CST_digamma"] < 1e-6 and chi5["max_abs_CST_digamma"] < 1e-6
    )
    fr_ok = fr_err < 1e-12
    w_ok = all(r["err"] < 1e-6 for r in w_rows)
    mixed_neg = chi3["lam_mixed_pk"] < 0.0
    sliver_pos = chi3["lam_CST_pk"] > 0.0 and chi3["lam_digamma_pk"] > 0.0
    pred_ok = (
        fr_ok
        and w_ok
        and writings_agree
        and mixed_neg
        and sliver_pos
        and chi3["lam_CST_pk"] < 1e-3
        and abs(chi3["delta"] + 0.5) < 0.02
        and chi3["ns"] == [2, 3, 4]
    )
    return {
        "mu": MU,
        "L": L5,
        "frullani_closed": fr_closed,
        "frullani_series": fr_series,
        "frullani_err": fr_err,
        "weierstrass": w_rows,
        "planes": [chi3, chi5],
        "identified_arch": writings_agree and fr_ok and w_ok,
        "weil_positive": False,
        "weil_negative": False,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
    }


def main() -> int:
    print(
        "classical Γ on W_L: CST+Gauss vs digamma vs mixed; not RH",
        flush=True,
    )
    data = run()
    print(
        f"  Frullani err={data['frullani_err']:.3e}  "
        f"Weierstrass err={[r['err'] for r in data['weierstrass']]}",
        flush=True,
    )
    for p in data["planes"]:
        print(
            f"  {p['name']:4s} max|CST−dig|={p['max_abs_CST_digamma']:.3e}  "
            f"δ={p['delta']:+.4f}  "
            f"lam CST={p['lam_CST_pk']:+.6e}  "
            f"dig={p['lam_digamma_pk']:+.6e}  "
            f"mixed={p['lam_mixed_pk']:+.4f}",
            flush=True,
        )
        print(
            f"       arch00={p['arch00_CST']:+.4f}  "
            f"C_A_lo={p['C_A_lo']:+.4f}  "
            f"gap={p['gap_arch_CA']:+.4f}",
            flush=True,
        )
    print(
        f"identified_arch={data['identified_arch']}  "
        f"Weil+={data['weil_positive']}  Weil−={data['weil_negative']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-arch-weil.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
