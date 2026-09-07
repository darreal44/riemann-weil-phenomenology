#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""W_log3 Neumann on primitive χ beyond the six cells.

c_L^*≥0 on W_{log 3} is the class step. Six cells already take.
This is the rest of scan_s, same L, T infinite. Not (∀χ). Not RH.

    python code/ql_class_mu3.py
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
from ql_schur_tail import HILBERT_HANKEL, Q_nm, r_frob_bound  # noqa: E402
from ql_theta_tail import theta_op_bound  # noqa: E402

MORE = {
    "chim8": dict(q=8, d=-8, a=1),
    "chi11": dict(q=11, d=-11, a=1),
    "chi12": dict(q=12, d=12, a=0),
    "chi13": dict(q=13, d=13, a=0),
    "chi15": dict(q=15, d=-15, a=1),
    "chi19": dict(q=19, d=-19, a=1),
    "chi20": dict(q=20, d=-20, a=1),
    "chi21": dict(q=21, d=21, a=0),
    "chi23": dict(q=23, d=-23, a=1),
    "chi24e": dict(q=24, d=24, a=0),
    "chi24o": dict(q=24, d=-24, a=1),
    "chi29": dict(q=29, d=29, a=0),
    "chi31": dict(q=31, d=-31, a=1),
}
HEADS = (2, 4)
N_NEAR0 = 32
M_C = 40
_cache: dict[tuple[str, int, int], float] = {}


def Q(name: str, n: int, m: int) -> float:
    cf = MORE[name]
    key = (name, min(n, m), max(n, m))
    if key not in _cache:
        _cache[key] = Q_nm(n, m, cf["q"], s0_of(cf["a"]), w2_of(cf["d"]))
    return _cache[key]


def row_at(name: str, h: int) -> dict:
    cf = MORE[name]
    w2 = w2_of(cf["d"])
    chi2 = kronecker(cf["d"], 2)
    n_near = max(N_NEAR0, h + 16)
    m_c = n_near + 8
    H = np.zeros((h, h))
    for i in range(h):
        for j in range(i, h):
            v = Q(name, i, j)
            H[i, j] = v
            H[j, i] = v
    lam_h = float(np.linalg.eigvalsh(H)[0])
    dim = n_near - h
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(h, n_near)):
        for j, m in enumerate(range(h, n_near)):
            T[i, j] = Q(name, n, m)
    d = np.diag(T)
    A = (T - np.diag(d)) * np.outer(1.0 / np.sqrt(d), 1.0 / np.sqrt(d))
    rho_n = float(np.linalg.norm(A, 2))
    qmin_far = min(Q(name, n, n) for n in range(n_near, m_c))
    tat = abs(w2) * theta_op_bound()
    off_far = 0.5 * HILBERT_HANKEL + 1.0 / (4.0 * n_near) + r_frob_bound(n_near) + tat
    rho_far = off_far / qmin_far
    b2 = 0.0
    for n in range(h, n_near):
        qnn = Q(name, n, n)
        for m in range(n_near, m_c):
            b2 += Q(name, n, m) ** 2 / (qnn * Q(name, m, m))
        b2 += 0.25 / max(n + m_c - 1, 1) / (qnn * qmin_far)
        if abs(w2) > 0.0:
            b2 += (2.0 * abs(w2) / PI) ** 2 / max(m_c - n - 1, 1) / (
                qnn * qmin_far
            )
    rho = block_norm(rho_n, math.sqrt(b2), rho_far)
    C = np.array(
        [[Q(name, i, m) for m in range(h, n_near)] for i in range(h)], float
    )
    cdc = C @ np.diag(1.0 / d) @ C.T
    cfar = np.zeros((h, h))
    for k in range(n_near, m_c):
        ck = np.array([Q(name, i, k) for i in range(h)])
        cfar += np.outer(ck, ck) / Q(name, k, k)
    s_lo = (
        float(np.linalg.eigvalsh(H - (cdc + cfar) / (1.0 - rho))[0])
        if rho < 1.0
        else None
    )
    return {
        "name": name,
        "q": cf["q"],
        "a": cf["a"],
        "chi2": chi2,
        "h": h,
        "lamH": lam_h,
        "rho": rho,
        "rho_far": rho_far,
        "s_lo": s_lo,
        "s_lo_pos": bool(s_lo is not None and s_lo > 0.0),
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    _cache.clear()
    rows = []
    taken = {}
    for name in MORE:
        hits = []
        for h in HEADS:
            r = row_at(name, h)
            rows.append(r)
            if r["s_lo_pos"]:
                hits.append(h)
        taken[name] = hits
    n_take = sum(1 for hs in taken.values() if hs)
    pred_ok = n_take == len(MORE)
    return {
        "mu": 3.0,
        "n_chi": len(MORE),
        "n_take": n_take,
        "taken": taken,
        "rows": rows,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
    }


def main() -> int:
    print("W_log3 Neumann beyond six cells; not (forall chi); not RH", flush=True)
    data = run()
    print(f"  take {data['n_take']}/{data['n_chi']}", flush=True)
    for name, hs in data["taken"].items():
        print(f"  {name:8s} h={hs if hs else '—'}", flush=True)
    print(f"verdict={data['verdict']}", flush=True)
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-class-mu3.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
