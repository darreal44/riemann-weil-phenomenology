#!/usr/bin/env python3
"""Schur tail for χ₁₇ on W_log3. Even χ(2)=+1 cell.

q=17, d=17, s₀=1/4, w₂=+log2/√2. Grid h=2,4,8,16,20,24.
β is the #60 machine plus T₂. S_lo is Neumann (#61), head=h.
T infinite. Not Galerkin of W_L. Not RH.

    python code/ql_schur_chi17_h.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kronecker import kronecker  # noqa: E402
from ql_operator_bound import PI, s0_of, w2_of  # noqa: E402
from ql_schur_neumann import block_norm  # noqa: E402
from ql_schur_tail import (  # noqa: E402
    HILBERT_HANKEL,
    Q_nm,
    c_tail_sq,
    r_frob_bound,
)
from ql_theta_tail import theta_op_bound  # noqa: E402

NAME = "chi17"
Q17, D17, A17 = 17, 17, 0
S0 = s0_of(A17)
W2 = w2_of(D17)
CHI2 = kronecker(D17, 2)
HEADS = (2, 4, 8, 16, 20, 24)
M_C_BETA = 40
N_DIAG = 40

_cache: dict[tuple[int, int], float] = {}


def Q(n: int, m: int) -> float:
    key = (min(n, m), max(n, m))
    if key not in _cache:
        _cache[key] = Q_nm(n, m, Q17, S0, W2)
    return _cache[key]


def n_near_of(h: int) -> int:
    return max(32, h + 16)


def m_c_of(h: int) -> int:
    return n_near_of(h) + 8


def row_at_h(h: int) -> dict:
    t2 = abs(W2) * theta_op_bound()
    H = np.zeros((h, h))
    for i in range(h):
        for j in range(i, h):
            v = Q(i, j)
            H[i, j] = v
            H[j, i] = v
    lam_h = float(np.linalg.eigvalsh(H)[0])
    diags = [Q(n, n) for n in range(h, N_DIAG)]
    qmin = min(diags)
    c_ex = 0.0
    for i in range(h):
        for j in range(h, M_C_BETA):
            c_ex += Q(i, j) ** 2
    c_tail = sum(c_tail_sq(i, M_C_BETA, W2) for i in range(h))
    c_frob = math.sqrt(c_ex + c_tail)
    off_beta = (
        0.5 * HILBERT_HANKEL + 1.0 / (4.0 * h) + r_frob_bound(h) + t2
    )
    delta = qmin - off_beta
    beta = lam_h - (c_frob * c_frob) / delta if delta > 0.0 else None
    n_near = n_near_of(h)
    m_c = m_c_of(h)
    dim = n_near - h
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(h, n_near)):
        for j, m in enumerate(range(h, n_near)):
            T[i, j] = Q(n, m)
    d = np.diag(T)
    A = (T - np.diag(d)) * np.outer(1.0 / np.sqrt(d), 1.0 / np.sqrt(d))
    rho_n = float(np.linalg.norm(A, 2))
    qmin_far = min(Q(n, n) for n in range(n_near, m_c))
    off_far = (
        0.5 * HILBERT_HANKEL
        + 1.0 / (4.0 * n_near)
        + r_frob_bound(n_near)
        + t2
    )
    rho_far = off_far / qmin_far
    b2 = 0.0
    for n in range(h, n_near):
        qnn = Q(n, n)
        for m in range(n_near, m_c):
            b2 += Q(n, m) ** 2 / (qnn * Q(m, m))
        b2 += 0.25 / max(n + m_c - 1, 1) / (qnn * qmin_far)
        b2 += (2.0 * abs(W2) / PI) ** 2 / max(m_c - n - 1, 1) / (
            qnn * qmin_far
        )
    rho_b = math.sqrt(b2)
    rho = block_norm(rho_n, rho_b, rho_far)
    C = np.array(
        [[Q(i, m) for m in range(h, n_near)] for i in range(h)], float
    )
    cdc = C @ np.diag(1.0 / d) @ C.T
    cfar = np.zeros((h, h))
    for k in range(n_near, m_c):
        ck = np.array([Q(i, k) for i in range(h)])
        cfar += np.outer(ck, ck) / Q(k, k)
    s_diag = float(np.linalg.eigvalsh(H - cdc)[0])
    s_exact = float(np.linalg.eigvalsh(H - C @ np.linalg.inv(T) @ C.T)[0])
    eat = cdc + cfar
    if rho < 1.0:
        s_lo = float(np.linalg.eigvalsh(H - eat / (1.0 - rho))[0])
    else:
        s_lo = None
    return {
        "h": h,
        "n_near": n_near,
        "M_C": m_c,
        "lamH": lam_h,
        "H00": float(H[0, 0]),
        "qmin": qmin,
        "c_frob": c_frob,
        "delta": delta,
        "beta": beta,
        "beta_pos": bool(beta is not None and beta > 0.0),
        "rho_near": rho_n,
        "rho_B": rho_b,
        "rho_far": rho_far,
        "rho": rho,
        "qmin_far": qmin_far,
        "s_diag": s_diag,
        "s_exact": s_exact,
        "s_lo": s_lo,
        "s_lo_pos": bool(s_lo is not None and s_lo > 0.0),
        "tr_CDC": float(np.trace(cdc)),
        "tr_Cfar": float(np.trace(cfar)),
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    _cache.clear()
    rows = [row_at_h(h) for h in HEADS]
    by = {r["h"]: r for r in rows}
    pos = [r["h"] for r in rows if r["s_lo_pos"]]
    pred_ok = (
        CHI2 == 1
        and W2 > 0.0
        and by[2]["s_lo_pos"]
        and by[24]["s_lo_pos"]
        and by[2]["beta_pos"]
        and by[2]["lamH"] > by[24]["lamH"]
        and by[2]["lamH"] > 0.6
        and abs(S0 - 0.25) < 1e-15
    )
    return {
        "name": NAME,
        "q": Q17,
        "d": D17,
        "s0": S0,
        "chi2": CHI2,
        "w2": W2,
        "heads": list(HEADS),
        "M_C_beta": M_C_BETA,
        "step_taken": step_is_taken(),
        "chi17_taken": bool(pos) and by[2]["s_lo_pos"],
        "first_positive_h": pos[0] if pos else None,
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
        "cache_size": len(_cache),
    }


def main() -> int:
    print(
        "χ₁₇ Schur; s0=1/4 χ(2)=+1; h=2,4,8,16,20,24; β=#60+T₂; S_lo=#61; "
        "T infinite; not Galerkin",
        flush=True,
    )
    data = run()
    print(
        f"  w2={data['w2']:+.4f}  chi2={data['chi2']}  s0={data['s0']}",
        flush=True,
    )
    print(" h   H00    lamH     ρ     Sexact    Slo      β", flush=True)
    for r in data["rows"]:
        b = f"{r['beta']:+.4f}" if r["beta"] is not None else "  —  "
        slo = f"{r['s_lo']:+.4f}" if r["s_lo"] is not None else "  —"
        print(
            f"{r['h']:2d}  {r['H00']:.4f}  {r['lamH']:.5f}  {r['rho']:.3f}  "
            f"{r['s_exact']:+.4f}  {slo}  {b}",
            flush=True,
        )
    print(
        f"chi17_taken={data['chi17_taken']}  first_h={data['first_positive_h']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-chi17-h.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
