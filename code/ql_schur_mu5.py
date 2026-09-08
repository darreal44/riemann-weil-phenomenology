#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Schur Neumann at μ=5, L=log 5. log2 < L/2 so ‖Θ(log 2)‖≤2.

Q = A − ∑_{p<μ} χ(p)(log p)/√p Θ(log p). Six-character quorum.
T infinite. Not Galerkin of W_L. Not RH.

    python code/ql_schur_mu5.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kronecker import kronecker  # noqa: E402
from log2_log3_step import interior_primes  # noqa: E402
from ql_operator_bound import LOG2, LOG3, PI, s0_of, w2_of  # noqa: E402
from ql_schur_neumann import block_norm  # noqa: E402
from ql_schur_tail import (  # noqa: E402
    HILBERT_HANKEL,
    Q_nm,
    r_frob_bound,
    theta_hat,
)
from ql_theta_tail import theta_op_bound  # noqa: E402

MU = 5.0
L = math.log(MU)
HEADS = (2, 4, 8, 16, 20, 24)
GRID = ("chi3", "chi5", "chi4", "chi8", "chi7", "chi17")
SNAP: tuple = ()
CHARS = {
    "chi5": dict(q=5, d=5, a=0),
    "chi8": dict(q=8, d=8, a=0),
    "chi4": dict(q=4, d=-4, a=1),
    "chi3": dict(q=3, d=-3, a=1),
    "chi7": dict(q=7, d=-7, a=1),
    "chi17": dict(q=17, d=17, a=0),
}

_cache: dict[tuple[str, float, int, int], float] = {}


def wp(d: int, p: int) -> float:
    return kronecker(d, p) * math.log(p) / math.sqrt(p)


def interior_atoms(mu: float) -> list[tuple[int, int, int]]:
    """Pairs (n, p, k) with n = p^k and 1 < n < μ. Includes primes."""
    hi = int(math.floor(float(mu) - 1e-15))
    out: list[tuple[int, int, int]] = []
    for p in interior_primes(mu):
        n, k = p, 1
        while n <= hi:
            out.append((n, p, k))
            n *= p
            k += 1
    return out


def wn(d: int, p: int, k: int) -> float:
    """Λ(p^k) χ(p^k) / p^{k/2}."""
    return (kronecker(d, p) ** k) * math.log(p) / (p ** (0.5 * k))


def Q_window(
    n: int, m: int, q: int, s0: float, d: int, L: float, mu: float
) -> float:
    """Arch minus every interior prime power. μ=3 recovers Q_nm (only 2)."""
    arch = Q_nm(n, m, q, s0, 0.0, L)
    acc = arch
    for _n, p, k in interior_atoms(mu):
        acc -= wn(d, p, k) * theta_hat(n, m, k * math.log(p), L)
    return acc


def Q(name: str, n: int, m: int, mu: float = MU, L: float = L) -> float:
    cf = CHARS[name]
    q, d, a = cf["q"], cf["d"], cf["a"]
    key = (name, mu, min(n, m), max(n, m))
    if key not in _cache:
        _cache[key] = Q_window(n, m, q, s0_of(a), d, L, mu)
    return _cache[key]


def n_near_of(h: int) -> int:
    return max(32, h + 16)


def m_c_of(h: int) -> int:
    return n_near_of(h) + 8


def t_atoms(d: int, mu: float, L: float) -> float:
    s = 0.0
    for _n, p, k in interior_atoms(mu):
        s += abs(wn(d, p, k)) * theta_op_bound(k * math.log(p), L)
    return s


def row_at(name: str, h: int, mu: float = MU, L: float = L) -> dict:
    cf = CHARS[name]
    d = cf["d"]
    tat = t_atoms(d, mu, L)
    n_near = n_near_of(h)
    m_c = m_c_of(h)
    H = np.zeros((h, h))
    for i in range(h):
        for j in range(i, h):
            v = Q(name, i, j, mu, L)
            H[i, j] = v
            H[j, i] = v
    lam_h = float(np.linalg.eigvalsh(H)[0])
    dim = n_near - h
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(h, n_near)):
        for j, m in enumerate(range(h, n_near)):
            T[i, j] = Q(name, n, m, mu, L)
    dd = np.diag(T)
    A = (T - np.diag(dd)) * np.outer(1.0 / np.sqrt(dd), 1.0 / np.sqrt(dd))
    rho_n = float(np.linalg.norm(A, 2))
    qmin_far = min(Q(name, n, n, mu, L) for n in range(n_near, m_c))
    off_far = (
        0.5 * HILBERT_HANKEL
        + 1.0 / (4.0 * n_near)
        + r_frob_bound(n_near)
        + tat
    )
    rho_far = off_far / qmin_far
    b2 = 0.0
    weights = [wn(d, p, k) for _n, p, k in interior_atoms(mu)]
    for n in range(h, n_near):
        qnn = Q(name, n, n, mu, L)
        for m in range(n_near, m_c):
            b2 += Q(name, n, m, mu, L) ** 2 / (
                qnn * Q(name, m, m, mu, L)
            )
        b2 += 0.25 / max(n + m_c - 1, 1) / (qnn * qmin_far)
        for w in weights:
            if abs(w) > 0.0:
                b2 += (2.0 * abs(w) / PI) ** 2 / max(m_c - n - 1, 1) / (
                    qnn * qmin_far
                )
    rho = block_norm(rho_n, math.sqrt(b2), rho_far)
    C = np.array(
        [
            [Q(name, i, m, mu, L) for m in range(h, n_near)]
            for i in range(h)
        ],
        float,
    )
    cdc = C @ np.diag(1.0 / dd) @ C.T
    cfar = np.zeros((h, h))
    for k in range(n_near, m_c):
        ck = np.array([Q(name, i, k, mu, L) for i in range(h)])
        cfar += np.outer(ck, ck) / Q(name, k, k, mu, L)
    s_diag = float(np.linalg.eigvalsh(H - cdc)[0])
    s_exact = float(np.linalg.eigvalsh(H - C @ np.linalg.inv(T) @ C.T)[0])
    eat = cdc + cfar
    s_lo = (
        float(np.linalg.eigvalsh(H - eat / (1.0 - rho))[0])
        if rho < 1.0
        else None
    )
    return {
        "name": name,
        "h": h,
        "mu": mu,
        "chi2": kronecker(d, 2),
        "chi3": kronecker(d, 3),
        "lamH": lam_h,
        "rho_near": rho_n,
        "rho_far": rho_far,
        "rho": rho,
        "t_atoms": tat,
        "s_diag": s_diag,
        "s_exact": s_exact,
        "s_lo": s_lo,
        "s_lo_pos": bool(s_lo is not None and s_lo > 0.0),
    }


def mu3_matches_qnm() -> bool:
    cf = CHARS["chi3"]
    q, d, a = cf["q"], cf["d"], cf["a"]
    s0, w2 = s0_of(a), w2_of(d)
    a_win = Q_window(0, 0, q, s0, d, LOG3, 3.0)
    a_old = Q_nm(0, 0, q, s0, w2, LOG3)
    b_win = Q_window(1, 1, q, s0, d, LOG3, 3.0)
    b_old = Q_nm(1, 1, q, s0, w2, LOG3)
    return abs(a_win - a_old) < 1e-14 and abs(b_win - b_old) < 1e-14


def step_is_taken() -> bool:
    return False


def run() -> dict:
    _cache.clear()
    print("grids six-character quorum", flush=True)
    grids: dict[str, list] = {}
    for name in GRID:
        rows = []
        for h in HEADS:
            r = row_at(name, h)
            rows.append(r)
            slo = f"{r['s_lo']:+.4f}" if r["s_lo"] is not None else "  —"
            print(
                f"  {name:5s} h={h:2d}  lamH={r['lamH']:.5f}  "
                f"ρ={r['rho']:.3f}  Slo={slo}",
                flush=True,
            )
        grids[name] = rows
    snaps: list = []
    by3 = {r["h"]: r for r in grids["chi3"]}
    by5 = {r["h"]: r for r in grids["chi5"]}
    by4 = {r["h"]: r for r in grids["chi4"]}
    by8 = {r["h"]: r for r in grids["chi8"]}
    by7 = {r["h"]: r for r in grids["chi7"]}
    by17 = {r["h"]: r for r in grids["chi17"]}
    q_ok = mu3_matches_qnm()
    pred_ok = (
        interior_primes(MU) == [2, 3]
        and LOG2 < 0.5 * L
        and theta_op_bound(LOG2, L) == 2.0
        and theta_op_bound(math.log(3.0), L) == 1.0
        and q_ok
        and by3[4]["lamH"] < 0.0
        and (not by3[4]["s_lo_pos"])
        and by3[4]["s_exact"] < 0.0
        and (not by5[2]["s_lo_pos"])
        and by5[8]["s_lo_pos"]
        and (not by4[4]["s_lo_pos"])
        and by4[8]["s_lo_pos"]
        and by8[2]["s_lo_pos"]
        and by7[2]["s_lo_pos"]
        and by17[2]["s_lo_pos"]
    )
    return {
        "mu": MU,
        "L": L,
        "primes": interior_primes(MU),
        "theta_op_log2": theta_op_bound(LOG2, L),
        "theta_op_log3": theta_op_bound(math.log(3.0), L),
        "mu3_matches_qnm": q_ok,
        "heads": list(HEADS),
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "grids": grids,
        "snaps": snaps,
        "cache_size": len(_cache),
    }


def main() -> int:
    print(
        f"μ={MU} L=log 5; primes {{2,3}}; Θ(log 2)≤2; T infinite; not Galerkin",
        flush=True,
    )
    data = run()
    print(
        f"qnm_match={data['mu3_matches_qnm']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-mu5.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
