#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Schur tail of Q̂_L on W_{log 3}, split h=2 in the cosine ONB.

H is a finite 2×2. T and C are infinite: Off_T is the Hankel
1/(2(n+m)) plus an HS remainder (and T₂ when χ(2)≠0). Not a
Galerkin of W_L. Not RH.

    python code/ql_schur_tail.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kronecker import kronecker  # noqa: E402
from ql_operator_bound import (  # noqa: E402
    CHARS,
    D2,
    EC,
    EULER,
    LOG2,
    LOG3,
    N_GAUSS,
    N_PANELS,
    PI,
    SCAN_S00,
    SCAN_S11,
    _gauss_nodes,
    s0_of,
    w2_of,
)

HEAD = 2
N_DIAG = 40
M_C = 40
# |n (π/2 − I_sin(ω_n))| ≤ SI + IBP. Si tail n/(ω L)=1/(2π);
# IBP (|g(0)|+|g(L)|+TV(g)) L/(2π) ≤ 0.18 (g=D₂−1/y).
DELTA_N_MAX = 0.40
# ‖[1/(i+j+1)]‖₂ = π (Hilbert 1894). Hence ‖[1/(n+m)]‖ ≤ π.
HILBERT_HANKEL = PI
# Discrete Hilbert transform ‖[1/(n−m)]_{n≠m}‖ ≤ π;
# |θ_nm| ≤ 2/(π |n−m|) ⇒ ‖Θ‖ ≤ 2.
THETA_OP = 2.0


def theta_hat(n: int, m: int, y: float, L: float = LOG3) -> float:
    om = lambda k: 2.0 * PI * k / L
    if n == 0 and m == 0:
        return 2.0 * (L - y) / L
    if n == 0 or m == 0:
        j = max(n, m)
        return -2.0 * math.sin(om(j) * y) / (math.sqrt(2.0) * PI * j)
    if n == m:
        return 2.0 * (
            (L - y) * math.cos(om(n) * y) / L - math.sin(om(n) * y) / (2.0 * PI * n)
        )
    return 2.0 * (n * math.sin(om(n) * y) - m * math.sin(om(m) * y)) / (
        PI * (m * m - n * n)
    )


def Q_nm(n: int, m: int, q: int, s0: float, w2: float, L: float = LOG3) -> float:
    """Arch − w₂ θ(log 2). F0=2 on the diagonal, 0 off. Gauss of the regular integrand."""
    if n > m:
        n, m = m, n
    F0 = 2.0 if n == m else 0.0
    cst = math.log(q / PI) - EULER - math.log(1.0 - math.exp(-2.0 * L))
    acc = 0.0
    h = L / N_PANELS
    for p in range(N_PANELS):
        ys, ws = _gauss_nodes(p * h, (p + 1) * h)
        for y, w in zip(ys, ws):
            th = theta_hat(n, m, y, L)
            acc += w * D2(y, s0) * (F0 * EC(y, s0) - th)
    A = 0.5 * F0 * cst + 0.5 * acc
    return A - w2 * theta_hat(n, m, LOG2, L)


def r_frob_bound(head: int = HEAD) -> float:
    """‖R‖_F for R_nm = (n δ_n − m δ_m)/(π(m−n)(m+n)), |n δ_n|≤DELTA_N_MAX."""
    coeff = 2.0 * DELTA_N_MAX / PI
    # ∑_{n≥h} ∑_{k≥1} 2 / (k² (2n+k)²) ≤ (π²/12) ∑_{n≥h} 1/n² ≤ π²/(12(h-1))
    s = (PI * PI) / (12.0 * (head - 1))
    return coeff * math.sqrt(s)


def c_tail_sq(i: int, m0: int, w2: float) -> float:
    """∑_{j≥m0} |Q_ij|² majorant. i < HEAD, m0 ≥ HEAD."""
    # |Q_0j| ≤ (π/2 + 0.2) / (√2 π j) ≤ 1.8 / (√2 π j)
    # |Q_1j| ≤ 1/(2(1+j)) + 2 Δ / (π (j-1)(j+1)) + |w2| * 2/(π (j-1))
    acc = 0.0
    if i == 0:
        a = 1.8 / (math.sqrt(2.0) * PI)
        # ∑_{j≥m0} a²/j² ≤ a² ∫_{m0-1}^∞ dx/x² = a²/(m0-1)
        acc = (a * a) / (m0 - 1)
    else:
        # 1/(2(i+j))² + T2 2|w2|/(π(j-i))² + R
        a1 = 0.5
        a2 = 2.0 * abs(w2) / PI
        a3 = 2.0 * DELTA_N_MAX / PI
        # ∑_{j≥m0} 1/(j+i)² ≤ 1/(m0+i-1); ∑ 1/(j-i)² ≤ 1/(m0-i-1)
        acc += (a1 * a1) / (m0 + i - 1)
        if m0 > i + 1:
            acc += (a2 * a2 + a3 * a3) / (m0 - i - 1)
        else:
            acc += (a2 * a2 + a3 * a3) * 2.0
    return acc


def row_of(name: str) -> dict:
    cf = CHARS[name]
    q, d, a = cf["q"], cf["d"], cf["a"]
    s0 = s0_of(a)
    w2 = w2_of(d)
    chi2 = kronecker(d, 2)
    H = np.zeros((HEAD, HEAD))
    for i in range(HEAD):
        for j in range(i, HEAD):
            v = Q_nm(i, j, q, s0, w2)
            H[i, j] = v
            H[j, i] = v
    lamH = float(np.linalg.eigvalsh(H)[0])
    diags = [Q_nm(n, n, q, s0, w2) for n in range(HEAD, N_DIAG)]
    qmin = min(diags)
    qmin_at = HEAD + int(np.argmin(diags))
    cfrob_sq = 0.0
    for i in range(HEAD):
        for j in range(HEAD, M_C):
            cfrob_sq += Q_nm(i, j, q, s0, w2) ** 2
        cfrob_sq += c_tail_sq(i, M_C, w2)
    c_frob = math.sqrt(cfrob_sq)
    r_f = r_frob_bound(HEAD)
    # Hilbert Hankel includes a diagonal 1/(2n) we do not put in Off.
    hankel = 0.5 * HILBERT_HANKEL + 1.0 / (4.0 * HEAD)
    t2 = abs(w2) * THETA_OP
    off_op = hankel + r_f + t2
    delta = qmin - off_op
    beta = lamH - (c_frob * c_frob) / delta if delta > 0.0 else None
    return {
        "name": name,
        "q": q,
        "s0": s0,
        "chi2": chi2,
        "w2": w2,
        "lamH": lamH,
        "H00": float(H[0, 0]),
        "H11": float(H[1, 1]),
        "H01": float(H[0, 1]),
        "qmin": qmin,
        "qmin_at": qmin_at,
        "Q_nn_last": diags[-1],
        "c_frob": c_frob,
        "r_frob": r_f,
        "hankel_op": hankel,
        "t2_op": t2,
        "off_op": off_op,
        "delta": delta,
        "beta": beta,
        "beta_pos": bool(beta is not None and beta > 0.0),
        "S00_match": abs(float(H[0, 0]) - SCAN_S00[name]) < 1e-8,
        "S11_match": abs(float(H[1, 1]) - SCAN_S11[name]) < 1e-8,
    }


def step_is_taken() -> bool:
    """The (log 2, log 3] class for every character is open. Not RH."""
    return False


def run() -> dict:
    rows = [row_of(name) for name in ("chi5", "chi8", "chi4", "chi3")]
    by = {r["name"]: r for r in rows}
    chi8_ok = by["chi8"]["beta_pos"]
    chi5_fail = not by["chi5"]["beta_pos"]
    chi3_fail = not by["chi3"]["beta_pos"]
    pred_ok = chi8_ok and chi5_fail and chi3_fail
    return {
        "L": LOG3,
        "mu": 3.0,
        "head": HEAD,
        "step_taken": step_is_taken(),
        "chi8_taken": chi8_ok,
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        f"L=log 3; Schur h={HEAD}; Hilbert–Hankel π/2 + HS rem + T₂; not Galerkin",
        flush=True,
    )
    data = run()
    for r in data["rows"]:
        b = f"{r['beta']:+.4f}" if r["beta"] is not None else "−∞"
        print(
            f"  {r['name']:4s} χ(2)={r['chi2']:+d}  lamH={r['lamH']:+.5f}  "
            f"qmin={r['qmin']:.4f}@n={r['qmin_at']}  δ={r['delta']:+.4f}  "
            f"‖C‖F={r['c_frob']:.4f}  β={b}  S00_match={r['S00_match']}",
            flush=True,
        )
    print(
        f"chi8_taken={data['chi8_taken']}  step_taken={data['step_taken']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-tail.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
