#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Neumann Q_pk at μ=5, χ₃. T infinite. Not Galerkin. Not RH.

    python code/ql_schur_pk_mu5.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import PI, s0_of  # noqa: E402
from ql_q_pk import D3, Q3, Q_pk, interior_ns, wn  # noqa: E402
from ql_schur_neumann import block_norm  # noqa: E402
from ql_schur_tail import HILBERT_HANKEL, r_frob_bound  # noqa: E402
from ql_theta_tail import theta_op_bound  # noqa: E402

MU = 5.0
L = math.log(MU)
S0 = s0_of(1)
HEADS = (2, 4, 8, 16, 20, 24)
_cache: dict[tuple[int, int], float] = {}


def Q(n: int, m: int) -> float:
    key = (min(n, m), max(n, m))
    if key not in _cache:
        _cache[key] = Q_pk(n, m, Q3, S0, D3, L, MU)
    return _cache[key]


def t_atoms() -> float:
    s = 0.0
    for k in interior_ns(MU):
        s += abs(wn(D3, k)) * theta_op_bound(math.log(k), L)
    return s


def row_at(h: int) -> dict:
    tat = t_atoms()
    n_near = max(32, h + 16)
    m_c = n_near + 8
    H = np.zeros((h, h))
    for i in range(h):
        for j in range(i, h):
            v = Q(i, j)
            H[i, j] = v
            H[j, i] = v
    lam_h = float(np.linalg.eigvalsh(H)[0])
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
        + tat
    )
    rho_far = off_far / qmin_far
    b2 = 0.0
    weights = [wn(D3, k) for k in interior_ns(MU)]
    for n in range(h, n_near):
        qnn = Q(n, n)
        for m in range(n_near, m_c):
            b2 += Q(n, m) ** 2 / (qnn * Q(m, m))
        b2 += 0.25 / max(n + m_c - 1, 1) / (qnn * qmin_far)
        for w in weights:
            if abs(w) > 0.0:
                b2 += (2.0 * abs(w) / PI) ** 2 / max(m_c - n - 1, 1) / (
                    qnn * qmin_far
                )
    rho = block_norm(rho_n, math.sqrt(b2), rho_far)
    C = np.array(
        [[Q(i, m) for m in range(h, n_near)] for i in range(h)], float
    )
    cdc = C @ np.diag(1.0 / d) @ C.T
    cfar = np.zeros((h, h))
    for k in range(n_near, m_c):
        ck = np.array([Q(i, k) for i in range(h)])
        cfar += np.outer(ck, ck) / Q(k, k)
    s_lo = (
        float(np.linalg.eigvalsh(H - (cdc + cfar) / (1.0 - rho))[0])
        if rho < 1.0
        else None
    )
    return {
        "h": h,
        "lamH": lam_h,
        "rho": rho,
        "rho_far": rho_far,
        "t_atoms": tat,
        "s_lo": s_lo,
        "s_lo_pos": bool(s_lo is not None and s_lo > 0.0),
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    _cache.clear()
    rows = [row_at(h) for h in HEADS]
    by = {r["h"]: r for r in rows}
    pred_ok = (not by[2]["s_lo_pos"]) and (not by[4]["s_lo_pos"])
    return {
        "mu": MU,
        "name": "chi3",
        "ns": interior_ns(MU),
        "heads": list(HEADS),
        "chi3_taken": any(r["s_lo_pos"] for r in rows if r["h"] in (2, 4)),
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print("Neumann Q_pk μ=5 χ₃; T infinite; not Galerkin; not RH", flush=True)
    data = run()
    for r in data["rows"]:
        slo = f"{r['s_lo']:+.6e}" if r["s_lo"] is not None else "  —"
        print(
            f"  h={r['h']:2d}  lamH={r['lamH']:+.6e}  ρ={r['rho']:.3f}  "
            f"Slo={slo}",
            flush=True,
        )
    print(
        f"chi3_taken_h24={data['chi3_taken']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-pk-mu5.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
