#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Neumann Q_pk, χ₃, μ=7 and μ=8. Identified form. Cap √2.

Does the W_log5 take extend? T infinite. Not Galerkin of W_L.
Not RH.

    python code/ql_schur_mu78.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import LOG2, PI, s0_of  # noqa: E402
from ql_q_pk import D3, Q3, Q_pk, interior_ns, wn  # noqa: E402
from ql_schur_neumann import block_norm  # noqa: E402
from ql_schur_tail import HILBERT_HANKEL, r_frob_bound  # noqa: E402
from ql_theta_sqrt2 import in_sqrt2_band, theta_op_cap  # noqa: E402

S0 = s0_of(1)
HEADS = (2, 4, 8, 16, 20, 24)
MUS = (7.0, 8.0)
_cache: dict[tuple[float, int, int], float] = {}


def Q(mu: float, n: int, m: int) -> float:
    L = math.log(mu)
    key = (mu, min(n, m), max(n, m))
    if key not in _cache:
        _cache[key] = Q_pk(n, m, Q3, S0, D3, L, mu)
    return _cache[key]


def t_atoms(mu: float) -> float:
    L = math.log(mu)
    s = 0.0
    for k in interior_ns(mu):
        s += abs(wn(D3, k)) * theta_op_cap(math.log(k), L)
    return s


def row_at(mu: float, h: int) -> dict:
    L = math.log(mu)
    tat = t_atoms(mu)
    n_near = max(32, h + 16)
    m_c = n_near + 8
    H = np.zeros((h, h))
    for i in range(h):
        for j in range(i, h):
            v = Q(mu, i, j)
            H[i, j] = v
            H[j, i] = v
    lam_h = float(np.linalg.eigvalsh(H)[0])
    dim = n_near - h
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(h, n_near)):
        for j, m in enumerate(range(h, n_near)):
            T[i, j] = Q(mu, n, m)
    d = np.diag(T)
    A = (T - np.diag(d)) * np.outer(1.0 / np.sqrt(d), 1.0 / np.sqrt(d))
    rho_n = float(np.linalg.norm(A, 2))
    qmin_far = min(Q(mu, n, n) for n in range(n_near, m_c))
    off_far = (
        0.5 * HILBERT_HANKEL
        + 1.0 / (4.0 * n_near)
        + r_frob_bound(n_near)
        + tat
    )
    rho_far = off_far / qmin_far
    b2 = 0.0
    weights = [wn(D3, k) for k in interior_ns(mu)]
    for n in range(h, n_near):
        qnn = Q(mu, n, n)
        for m in range(n_near, m_c):
            b2 += Q(mu, n, m) ** 2 / (qnn * Q(mu, m, m))
        b2 += 0.25 / max(n + m_c - 1, 1) / (qnn * qmin_far)
        for w in weights:
            if abs(w) > 0.0:
                b2 += (2.0 * abs(w) / PI) ** 2 / max(m_c - n - 1, 1) / (
                    qnn * qmin_far
                )
    rho = block_norm(rho_n, math.sqrt(b2), rho_far)
    C = np.array(
        [[Q(mu, i, m) for m in range(h, n_near)] for i in range(h)], float
    )
    cdc = C @ np.diag(1.0 / d) @ C.T
    cfar = np.zeros((h, h))
    for k in range(n_near, m_c):
        ck = np.array([Q(mu, i, k) for i in range(h)])
        cfar += np.outer(ck, ck) / Q(mu, k, k)
    s_lo = (
        float(np.linalg.eigvalsh(H - (cdc + cfar) / (1.0 - rho))[0])
        if rho < 1.0
        else None
    )
    return {
        "mu": mu,
        "h": h,
        "L": L,
        "ns": interior_ns(mu),
        "lamH": lam_h,
        "rho": rho,
        "rho_far": rho_far,
        "t_atoms": tat,
        "s_lo": s_lo,
        "s_lo_pos": bool(s_lo is not None and s_lo > 0.0),
        "log2_in_band": in_sqrt2_band(LOG2, L),
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    _cache.clear()
    rows = [row_at(mu, h) for mu in MUS for h in HEADS]
    by = {(r["mu"], r["h"]): r for r in rows}
    old_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-H16-mu.json",
    )
    old = json.load(open(old_path, encoding="utf-8"))
    old_by = {r["mu"]: r for r in old["rows"]}
    any_take = any(r["s_lo_pos"] for r in rows)
    pred_ok = (
        by[(7.0, 16)]["ns"] == [2, 3, 4, 5]
        and by[(8.0, 16)]["ns"] == [2, 3, 4, 5, 7]
        and abs(by[(7.0, 16)]["lamH"] - old_by[7.0]["lamH"]) < 1e-12
        and abs(by[(8.0, 16)]["lamH"] - old_by[8.0]["lamH"]) < 1e-12
        and by[(7.0, 16)]["log2_in_band"]
        and by[(8.0, 16)]["log2_in_band"]
        and (not any_take)
        and all(by[(mu, 16)]["lamH"] > 0.0 for mu in MUS)
    )
    return {
        "mus": list(MUS),
        "heads": list(HEADS),
        "any_slo_pos": any_take,
        "take_extends": any_take,
        "weil_positive": False,
        "weil_negative": False,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        "Neumann Q_pk χ₃ μ=7 and 8; √2 cap; T infinite; not RH",
        flush=True,
    )
    data = run()
    for mu in MUS:
        print(f"μ={mu:.0f}", flush=True)
        for r in data["rows"]:
            if r["mu"] != mu:
                continue
            slo = f"{r['s_lo']:+.6e}" if r["s_lo"] is not None else "  —"
            print(
                f"  h={r['h']:2d}  lamH={r['lamH']:+.6e}  ρ={r['rho']:.3f}  "
                f"Slo={slo}",
                flush=True,
            )
    print(
        f"take_extends={data['take_extends']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-mu78.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
