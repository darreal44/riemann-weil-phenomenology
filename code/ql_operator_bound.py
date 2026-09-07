#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Bochner / Fourier multiplier of Q̂_L on W_{log 3}.

Not Galerkin. No N. No assemble. The class step is
α_line = 2 inf m_Q(t) ≥ 0, which is sufficient for
Q̂_L ≥ 0 on every even L² function with θ(0)=2, hence
on W_L. Young dropped g(0)=0; this keeps it.

    python code/ql_operator_bound.py

Not RH. One L.
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np
from numpy.polynomial.legendre import leggauss

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kronecker import kronecker  # noqa: E402

LOG2 = math.log(2.0)
LOG3 = math.log(3.0)
MU = 3.0
EULER = 0.5772156649015328606
PI = math.pi
N_SERIES = 120
N_GAUSS = 32
N_PANELS = 16

# ψ(1/4) = −γ − π/2 − 3 log 2;  ψ(3/4) = −γ + π/2 − 3 log 2.
PSI_14 = -EULER - 0.5 * PI - 3.0 * math.log(2.0)
PSI_34 = -EULER + 0.5 * PI - 3.0 * math.log(2.0)

CHARS = {
    "chi5": dict(q=5, d=5, a=0),
    "chi8": dict(q=8, d=8, a=0),
    "chi4": dict(q=4, d=-4, a=1),
    "chi3": dict(q=3, d=-3, a=1),
}

# scan_s μ=3 NB=2 diagonals (judge, not inputs).
SCAN_S00 = {
    "chi5": 0.20230279679679541,
    "chi8": 0.3105223114690086,
    "chi4": 0.15352125555184098,
    "chi3": 0.22762329767358241,
}
SCAN_S11 = {
    "chi5": 1.6304573266018838,
    "chi8": 2.232223868185052,
    "chi4": 1.5393625256952042,
    "chi3": 1.1199175409059907,
}


def s0_of(a: int) -> float:
    return 0.25 + 0.5 * a


def psi_s0(s0: float) -> float:
    if abs(s0 - 0.25) < 1e-15:
        return PSI_14
    if abs(s0 - 0.75) < 1e-15:
        return PSI_34
    raise ValueError(f"s0={s0} not a quarter")


def w2_of(d: int) -> float:
    return kronecker(d, 2) * LOG2 / math.sqrt(2.0)


def C_A_lo(q: int, s0: float, L: float = LOG3, n: int = N_SERIES) -> tuple[float, float]:
    """log(q/π)+ψ(s₀)+∑ μ^{-2(s₀+k)}/(s₀+k), plus a positive tail bound."""
    acc = math.log(q / PI) + psi_s0(s0)
    for k in range(n):
        acc += math.exp(-2.0 * (s0 + k) * L) / (s0 + k)
    eN = math.exp(-2.0 * (s0 + n) * L)
    den = (s0 + n) * (1.0 - math.exp(-2.0 * L))
    return acc, eN / den


def _laplace_1_minus_cos(alpha: float, t: float, L: float) -> float:
    """∫_0^L e^{-α y} (1 − cos(t y)) dy, α>0."""
    I1 = (1.0 - math.exp(-alpha * L)) / alpha
    if abs(t) < 1e-14:
        return 0.0
    d = alpha * alpha + t * t
    eL = math.exp(-alpha * L)
    icos = (alpha - eL * (alpha * math.cos(t * L) - t * math.sin(t * L))) / d
    return I1 - icos


def k_of_t(t: float, s0: float, L: float = LOG3, n: int = N_SERIES) -> tuple[float, float]:
    """k(t)=∑_m ∫ e^{-2(s₀+m)y}(1−cos(ty)) dy. Tail ≤ t²/(16 (s₀+n−1)²)."""
    acc = 0.0
    for m in range(n):
        acc += _laplace_1_minus_cos(2.0 * (s0 + m), t, L)
    sn = s0 + n - 1.0
    tail = (t * t) / (16.0 * sn * sn) if sn > 0 else float("inf")
    return acc, tail


def m_Q(t: float, q: int, s0: float, w2: float, L: float = LOG3) -> dict:
    clo, ctail = C_A_lo(q, s0, L)
    kt, ktail = k_of_t(t, s0, L)
    val = 0.5 * clo + kt - w2 * math.cos(t * LOG2)
    return {
        "mQ": val,
        "C_A_lo": clo,
        "k": kt,
        "tail": 0.5 * ctail + ktail,
        "C_A_lo_tail": ctail,
        "k_tail": ktail,
    }


def D2(y: float, s0: float) -> float:
    return 2.0 * math.exp(-2.0 * s0 * y) / (1.0 - math.exp(-2.0 * y))


def EC(y: float, s0: float) -> float:
    return math.exp(-(2.0 - 2.0 * s0) * y)


def theta_unnorm(y: float, omega: float, L: float) -> float:
    if abs(omega) < 1e-14:
        return L - y
    return ((L - y) / 2.0) * math.cos(omega * y) + math.sin(omega * (L - y)) / (
        2.0 * omega
    )


def theta_weil(y: float, omega: float, L: float) -> float:
    den = theta_unnorm(0.0, omega, L)
    return 2.0 * theta_unnorm(y, omega, L) / den


def _gauss_nodes(lo: float, hi: float, n: int = N_GAUSS):
    x, w = leggauss(n)
    h = (hi - lo) / 2.0
    m = (hi + lo) / 2.0
    return [m + h * float(xi) for xi in x], [h * float(wi) for wi in w]


def Q_cosine(omega: float, q: int, s0: float, w2: float, L: float = LOG3) -> dict:
    """Rayleigh of the even windowed cosine. Weil θ(0)=2."""
    cst = math.log(q / PI) - EULER - math.log(1.0 - math.exp(-2.0 * L))
    acc = 0.0
    h = L / N_PANELS
    for p in range(N_PANELS):
        ys, ws = _gauss_nodes(p * h, (p + 1) * h)
        for y, w in zip(ys, ws):
            th = theta_weil(y, omega, L)
            acc += w * D2(y, s0) * (2.0 * EC(y, s0) - th)
    A = cst + 0.5 * acc
    th2 = theta_weil(LOG2, omega, L)
    Q = A - w2 * th2
    return {"Q": Q, "A": A, "theta_log2": th2, "omega": omega}


def cosine_scan(q: int, s0: float, w2: float, L: float = LOG3) -> dict:
    omegas = [0.0, 2.0 * PI / L, 4.0 * PI / L]
    omegas += [0.05 * i for i in range(1, 301)]  # (0, 15]
    best_Q, best_om = float("inf"), 0.0
    q0 = Q_cosine(0.0, q, s0, w2, L)
    q1 = Q_cosine(2.0 * PI / L, q, s0, w2, L)
    for om in omegas:
        row = Q_cosine(om, q, s0, w2, L)
        if row["Q"] < best_Q:
            best_Q, best_om = row["Q"], om
    return {
        "Q_const": q0["Q"],
        "A_const": q0["A"],
        "theta_const_log2": q0["theta_log2"],
        "Q_hat1": q1["Q"],
        "A_hat1": q1["A"],
        "Q_cos_min": best_Q,
        "omega_cos_min": best_om,
    }


def mQ_scan(q: int, s0: float, w2: float, L: float = LOG3) -> dict:
    ts = [0.05 * i for i in range(0, 401)]  # [0, 20]
    t_star = PI / LOG2
    ts.append(t_star)
    best, t_inf = float("inf"), 0.0
    for t in ts:
        v = m_Q(t, q, s0, w2, L)["mQ"]
        if v < best:
            best, t_inf = v, t
    at0 = m_Q(0.0, q, s0, w2, L)
    atstar = m_Q(t_star, q, s0, w2, L)
    return {
        "inf_mQ": best,
        "t_inf": t_inf,
        "mQ_0": at0["mQ"],
        "mQ_pi_log2": atstar["mQ"],
        "C_A_lo": at0["C_A_lo"],
        "C_A_lo_tail": at0["C_A_lo_tail"],
        "tail_0": at0["tail"],
        "tail_pi_log2": atstar["tail"],
    }


def row_of(name: str) -> dict:
    cf = CHARS[name]
    q, d, a = cf["q"], cf["d"], cf["a"]
    s0 = s0_of(a)
    w2 = w2_of(d)
    chi2 = kronecker(d, 2)
    mq = mQ_scan(q, s0, w2)
    cos = cosine_scan(q, s0, w2)
    alpha = 2.0 * mq["inf_mQ"]
    return {
        "name": name,
        "q": q,
        "s0": s0,
        "chi2": chi2,
        "w2": w2,
        "C_A_lo": mq["C_A_lo"],
        "C_A_lo_tail": mq["C_A_lo_tail"],
        "mQ_0": mq["mQ_0"],
        "mQ_pi_log2": mq["mQ_pi_log2"],
        "inf_mQ": mq["inf_mQ"],
        "t_inf": mq["t_inf"],
        "alpha_line": alpha,
        "alpha_line_neg": alpha < 0.0,
        "Q_const": cos["Q_const"],
        "A_const": cos["A_const"],
        "Q_hat1": cos["Q_hat1"],
        "Q_cos_min": cos["Q_cos_min"],
        "omega_cos_min": cos["omega_cos_min"],
        "cosine_pos": cos["Q_cos_min"] > 0.0,
        "cstar_finite": cos["A_const"] > 0.0,
        "S00_ref": SCAN_S00[name],
        "S11_ref": SCAN_S11[name],
        "S00_match": abs(cos["Q_const"] - SCAN_S00[name]) < 1e-8,
        "S11_match": abs(cos["Q_hat1"] - SCAN_S11[name]) < 1e-8,
        "tail_0": mq["tail_0"],
        "tail_pi_log2": mq["tail_pi_log2"],
    }


def bochner_takes_the_class(rows: list[dict]) -> bool:
    return all(r["alpha_line"] >= 0.0 for r in rows)


def cosine_kills_the_class(rows: list[dict]) -> bool:
    return any(r["Q_cos_min"] <= 0.0 for r in rows)


def step_is_taken() -> bool:
    """c_L^* ≥ 0 on W_{log 3} is open. Not RH (one L)."""
    return False


def run() -> dict:
    rows = [row_of(name) for name in ("chi5", "chi8", "chi4", "chi3")]
    taken = bochner_takes_the_class(rows)
    killed = cosine_kills_the_class(rows)
    pred_ok = (not taken) and (not killed) and all(
        (r["name"] not in ("chi5", "chi3")) or (r["A_const"] < 0.0) for r in rows
    )
    return {
        "L": LOG3,
        "mu": MU,
        "step_taken": step_is_taken(),
        "bochner_takes_class": taken,
        "cosine_kills_class": killed,
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        f"L=log 3={LOG3:.6f}; Bochner α_line; cosine family; not Galerkin",
        flush=True,
    )
    data = run()
    for r in data["rows"]:
        print(
            f"  {r['name']:4s} χ(2)={r['chi2']:+d}  "
            f"α_line={r['alpha_line']:+.6f} (t={r['t_inf']:.3f})  "
            f"Qcos_min={r['Q_cos_min']:+.6f} @ω={r['omega_cos_min']:.3f}  "
            f"A(const)={r['A_const']:+.6f}  S00_match={r['S00_match']}",
            flush=True,
        )
    print(
        f"bochner_takes_class={data['bochner_takes_class']}  "
        f"cosine_kills_class={data['cosine_kills_class']}  "
        f"step_taken={data['step_taken']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-operator-bound.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
