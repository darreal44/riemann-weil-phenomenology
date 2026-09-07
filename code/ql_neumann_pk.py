#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Neumann of identified Q_pk. Shared by the μ-grid, quorum, and ρ_far drivers.

T infinite. Cap √2 on [L/4, L/2). Not Galerkin of W_L. Not RH.
"""
from __future__ import annotations

import math

import numpy as np

from ql_operator_bound import LOG2, PI, s0_of
from ql_q_pk import Q_pk, interior_ns, wn
from ql_schur_neumann import block_norm
from ql_schur_tail import HILBERT_HANKEL, r_frob_bound
from ql_theta_sqrt2 import in_sqrt2_band, theta_op_cap

CHARS = {
    "chi5": dict(q=5, d=5, a=0),
    "chi8": dict(q=8, d=8, a=0),
    "chi4": dict(q=4, d=-4, a=1),
    "chi3": dict(q=3, d=-3, a=1),
    "chi7": dict(q=7, d=-7, a=1),
    "chi17": dict(q=17, d=17, a=0),
}

_cache: dict[tuple[str, float, int, int], float] = {}


def clear_cache() -> None:
    _cache.clear()


def Q(name: str, n: int, m: int, mu: float) -> float:
    cf = CHARS[name]
    L = math.log(mu)
    key = (name, mu, min(n, m), max(n, m))
    if key not in _cache:
        _cache[key] = Q_pk(
            n, m, cf["q"], s0_of(cf["a"]), cf["d"], L, mu
        )
    return _cache[key]


def t_atoms(name: str, mu: float) -> float:
    d = CHARS[name]["d"]
    L = math.log(mu)
    s = 0.0
    for k in interior_ns(mu):
        s += abs(wn(d, k)) * theta_op_cap(math.log(k), L)
    return s


def far_pieces(name: str, mu: float, n_near: int = 32) -> dict:
    """t_atoms, qmin_far, off_far, ρ_far. Diagonals only on the far block."""
    m_c = n_near + 8
    tat = t_atoms(name, mu)
    qmin_far = min(Q(name, n, n, mu) for n in range(n_near, m_c))
    hilbert = 0.5 * HILBERT_HANKEL
    rem = 1.0 / (4.0 * n_near) + r_frob_bound(n_near)
    off_far = hilbert + rem + tat
    return {
        "n_near": n_near,
        "t_atoms": tat,
        "qmin_far": qmin_far,
        "hilbert": hilbert,
        "rem": rem,
        "off_far": off_far,
        "rho_far": off_far / qmin_far,
    }


def row_at(name: str, mu: float, h: int) -> dict:
    L = math.log(mu)
    d = CHARS[name]["d"]
    tat = t_atoms(name, mu)
    n_near = max(32, h + 16)
    m_c = n_near + 8
    H = np.zeros((h, h))
    for i in range(h):
        for j in range(i, h):
            v = Q(name, i, j, mu)
            H[i, j] = v
            H[j, i] = v
    lam_h = float(np.linalg.eigvalsh(H)[0])
    dim = n_near - h
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(h, n_near)):
        for j, m in enumerate(range(h, n_near)):
            T[i, j] = Q(name, n, m, mu)
    dd = np.diag(T)
    A = (T - np.diag(dd)) * np.outer(1.0 / np.sqrt(dd), 1.0 / np.sqrt(dd))
    rho_n = float(np.linalg.norm(A, 2))
    far = far_pieces(name, mu, n_near)
    qmin_far = far["qmin_far"]
    weights = [wn(d, k) for k in interior_ns(mu)]
    b2 = 0.0
    for n in range(h, n_near):
        qnn = Q(name, n, n, mu)
        for m in range(n_near, m_c):
            b2 += Q(name, n, m, mu) ** 2 / (qnn * Q(name, m, m, mu))
        b2 += 0.25 / max(n + m_c - 1, 1) / (qnn * qmin_far)
        for w in weights:
            if abs(w) > 0.0:
                b2 += (2.0 * abs(w) / PI) ** 2 / max(m_c - n - 1, 1) / (
                    qnn * qmin_far
                )
    rho = block_norm(rho_n, math.sqrt(b2), far["rho_far"])
    C = np.array(
        [[Q(name, i, m, mu) for m in range(h, n_near)] for i in range(h)],
        float,
    )
    cdc = C @ np.diag(1.0 / dd) @ C.T
    cfar = np.zeros((h, h))
    for k in range(n_near, m_c):
        ck = np.array([Q(name, i, k, mu) for i in range(h)])
        cfar += np.outer(ck, ck) / Q(name, k, k, mu)
    s_lo = (
        float(np.linalg.eigvalsh(H - (cdc + cfar) / (1.0 - rho))[0])
        if rho < 1.0
        else None
    )
    return {
        "name": name,
        "mu": mu,
        "h": h,
        "L": L,
        "ns": interior_ns(mu),
        "lamH": lam_h,
        "rho": rho,
        "rho_n": rho_n,
        "rho_far": far["rho_far"],
        "t_atoms": tat,
        "qmin_far": qmin_far,
        "s_lo": s_lo,
        "s_lo_pos": bool(s_lo is not None and s_lo > 0.0),
        "log2_in_band": in_sqrt2_band(LOG2, L),
    }
