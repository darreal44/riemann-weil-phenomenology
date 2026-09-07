#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Schur tail for χ₃ at larger h. Combine #60 raise-h with #61 Neumann.

Grid h=2,4,8,16,20,24. β is the #60 machine plus T₂ (does not take).
S_lo is Neumann T^{-1}≤D^{-1}/(1−ρ) with head=h (the certificate).
T infinite. Not Galerkin of W_L. Not RH.

    python code/ql_schur_chi3_h.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import CHARS, PI, w2_of  # noqa: E402
from ql_schur_neumann import Q, block_norm  # noqa: E402
from ql_schur_tail import (  # noqa: E402
    HILBERT_HANKEL,
    c_tail_sq,
    r_frob_bound,
)
from ql_theta_tail import theta_op_bound  # noqa: E402

NAME = "chi3"
HEADS = (2, 4, 8, 16, 20, 24)
M_C_BETA = 40
N_DIAG = 40


def n_near_of(h: int) -> int:
    return max(32, h + 16)


def m_c_of(h: int) -> int:
    return n_near_of(h) + 8


def row_at_h(h: int) -> dict:
    w2 = w2_of(CHARS[NAME]["d"])
    t2 = abs(w2) * theta_op_bound()
    H = np.zeros((h, h))
    for i in range(h):
        for j in range(i, h):
            v = Q(NAME, i, j)
            H[i, j] = v
            H[j, i] = v
    lam_h = float(np.linalg.eigvalsh(H)[0])

    diags = [Q(NAME, n, n) for n in range(h, N_DIAG)]
    qmin = min(diags)
    c_ex = 0.0
    for i in range(h):
        for j in range(h, M_C_BETA):
            c_ex += Q(NAME, i, j) ** 2
    c_tail = sum(c_tail_sq(i, M_C_BETA, w2) for i in range(h))
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
            T[i, j] = Q(NAME, n, m)
    d = np.diag(T)
    A = (T - np.diag(d)) * np.outer(1.0 / np.sqrt(d), 1.0 / np.sqrt(d))
    rho_n = float(np.linalg.norm(A, 2))
    qmin_far = min(Q(NAME, n, n) for n in range(n_near, m_c))
    off_far = (
        0.5 * HILBERT_HANKEL
        + 1.0 / (4.0 * n_near)
        + r_frob_bound(n_near)
        + t2
    )
    rho_far = off_far / qmin_far
    b2 = 0.0
    for n in range(h, n_near):
        qnn = Q(NAME, n, n)
        for m in range(n_near, m_c):
            b2 += Q(NAME, n, m) ** 2 / (qnn * Q(NAME, m, m))
        b2 += 0.25 / max(n + m_c - 1, 1) / (qnn * qmin_far)
        if abs(w2) > 0.0:
            b2 += (2.0 * abs(w2) / PI) ** 2 / max(m_c - n - 1, 1) / (
                qnn * qmin_far
            )
    rho_b = math.sqrt(b2)
    rho = block_norm(rho_n, rho_b, rho_far)
    C = np.array(
        [[Q(NAME, i, m) for m in range(h, n_near)] for i in range(h)], float
    )
    cdc = C @ np.diag(1.0 / d) @ C.T
    cfar = np.zeros((h, h))
    for k in range(n_near, m_c):
        ck = np.array([Q(NAME, i, k) for i in range(h)])
        cfar += np.outer(ck, ck) / Q(NAME, k, k)
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
    rows = [row_at_h(h) for h in HEADS]
    by = {r["h"]: r for r in rows}
    pos = [r["h"] for r in rows if r["s_lo_pos"]]
    h_star = [2, 4] if (not by[2]["s_lo_pos"] and by[4]["s_lo_pos"]) else None
    pred_ok = (
        (not by[2]["s_lo_pos"])
        and by[4]["s_lo_pos"]
        and by[24]["s_lo_pos"]
        and all(not r["beta_pos"] for r in rows)
        and by[2]["lamH"] > by[24]["lamH"]
        and by[2]["s_lo"] is not None
        and by[2]["s_lo"] < 0.0
    )
    return {
        "name": NAME,
        "heads": list(HEADS),
        "M_C_beta": M_C_BETA,
        "step_taken": step_is_taken(),
        "chi3_taken": bool(pos),
        "h_star": h_star,
        "first_positive_h": pos[0] if pos else None,
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        "χ₃ Schur; h=2,4,8,16,20,24; β=#60+T₂; S_lo=#61 Neumann; "
        "T infinite; not Galerkin",
        flush=True,
    )
    data = run()
    print(
        " h   lamH     δ      β      ρ     Sexact    Slo",
        flush=True,
    )
    for r in data["rows"]:
        b = f"{r['beta']:+.4f}" if r["beta"] is not None else "  —  "
        d = f"{r['delta']:+.3f}"
        slo = f"{r['s_lo']:+.4f}" if r["s_lo"] is not None else "  —"
        print(
            f"{r['h']:2d}  {r['lamH']:.5f}  {d}  {b}  {r['rho']:.3f}  "
            f"{r['s_exact']:+.4f}  {slo}",
            flush=True,
        )
    print(
        f"chi3_taken={data['chi3_taken']}  h*={data['h_star']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-chi3-h.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
