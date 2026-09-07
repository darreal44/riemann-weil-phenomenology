#!/usr/bin/env python3
"""Schur with Neumann T^{-1} ≤ D^{-1}/(1−ρ), not ‖C‖_F²/δ.

A = D^{-1/2} Off D^{-1/2} split near/coupling/far.
ρ = block-norm(ρ_N, ρ_B, ρ_far). If ρ<1, S ≥ H − CDC/(1−ρ).
Named in chi5-hankel-not-enough.md: sharper C, not a smaller
Hilbert constant. Not Galerkin of W_L. Not RH.

    python code/ql_schur_neumann.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import CHARS, PI, s0_of, w2_of  # noqa: E402
from ql_schur_tail import HILBERT_HANKEL, Q_nm, r_frob_bound  # noqa: E402
from ql_theta_tail import theta_op_bound  # noqa: E402

HEAD = 2
N_NEAR = 32
M_C = 40

_cache: dict[tuple[str, int, int], float] = {}


def Q(name: str, n: int, m: int) -> float:
    cf = CHARS[name]
    q, s0, w2 = cf["q"], s0_of(cf["a"]), w2_of(cf["d"])
    key = (name, min(n, m), max(n, m))
    if key not in _cache:
        _cache[key] = Q_nm(n, m, q, s0, w2)
    return _cache[key]


def block_norm(a: float, b: float, c: float) -> float:
    """‖[[a,b],[b,c]]‖₂."""
    return 0.5 * (a + c + math.sqrt((a - c) ** 2 + 4.0 * b * b))


def row_of(name: str) -> dict:
    w2 = w2_of(CHARS[name]["d"])
    dim = N_NEAR - HEAD
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(HEAD, N_NEAR)):
        for j, m in enumerate(range(HEAD, N_NEAR)):
            T[i, j] = Q(name, n, m)
    d = np.diag(T)
    A = (T - np.diag(d)) * np.outer(1.0 / np.sqrt(d), 1.0 / np.sqrt(d))
    rho_n = float(np.linalg.norm(A, 2))
    qmin_far = min(Q(name, n, n) for n in range(N_NEAR, M_C))
    off_far = (
        0.5 * HILBERT_HANKEL
        + 1.0 / (4.0 * N_NEAR)
        + r_frob_bound(N_NEAR)
        + abs(w2) * theta_op_bound()
    )
    rho_far = off_far / qmin_far
    b2 = 0.0
    for n in range(HEAD, N_NEAR):
        qnn = Q(name, n, n)
        for m in range(N_NEAR, M_C):
            b2 += Q(name, n, m) ** 2 / (qnn * Q(name, m, m))
        b2 += 0.25 / max(n + M_C - 1, 1) / (qnn * qmin_far)
        if abs(w2) > 0.0:
            b2 += (2.0 * abs(w2) / PI) ** 2 / max(M_C - n - 1, 1) / (
                qnn * qmin_far
            )
    rho_b = math.sqrt(b2)
    rho = block_norm(rho_n, rho_b, rho_far)
    H = np.array(
        [[Q(name, i, j) for j in range(HEAD)] for i in range(HEAD)], float
    )
    C = np.array(
        [[Q(name, i, m) for m in range(HEAD, N_NEAR)] for i in range(HEAD)],
        float,
    )
    cdc = C @ np.diag(1.0 / d) @ C.T
    cfar = np.zeros((HEAD, HEAD))
    for k in range(N_NEAR, M_C):
        ck = np.array([Q(name, i, k) for i in range(HEAD)])
        cfar += np.outer(ck, ck) / Q(name, k, k)
    lam_h = float(np.linalg.eigvalsh(H)[0])
    s_diag = float(np.linalg.eigvalsh(H - cdc)[0])
    if rho < 1.0:
        s_lo = float(np.linalg.eigvalsh(H - (cdc + cfar) / (1.0 - rho))[0])
    else:
        s_lo = None
    return {
        "name": name,
        "lamH": lam_h,
        "rho_near": rho_n,
        "rho_B": rho_b,
        "rho_far": rho_far,
        "rho": rho,
        "qmin_far": qmin_far,
        "s_diag": s_diag,
        "s_lo": s_lo,
        "s_lo_pos": bool(s_lo is not None and s_lo > 0.0),
        "tr_CDC": float(np.trace(cdc)),
        "tr_Cfar": float(np.trace(cfar)),
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    _cache.clear()
    rows = [row_of(name) for name in ("chi5", "chi8", "chi4", "chi3")]
    by = {r["name"]: r for r in rows}
    pred_ok = (
        by["chi5"]["s_lo_pos"]
        and by["chi8"]["s_lo_pos"]
        and by["chi4"]["s_lo_pos"]
        and (not by["chi3"]["s_lo_pos"])
        and by["chi5"]["rho"] < 1.0
    )
    return {
        "head": HEAD,
        "n_near": N_NEAR,
        "M_C": M_C,
        "step_taken": step_is_taken(),
        "chi5_taken": by["chi5"]["s_lo_pos"],
        "chi3_taken": by["chi3"]["s_lo_pos"],
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
        "cache_size": len(_cache),
    }


def main() -> int:
    print(
        "Schur Neumann T^{-1}≤D^{-1}/(1−ρ); sharper C; not Frob/δ; not Galerkin",
        flush=True,
    )
    data = run()
    for r in data["rows"]:
        slo = f"{r['s_lo']:+.4f}" if r["s_lo"] is not None else "−∞"
        print(
            f"  {r['name']:4s} ρ={r['rho']:.3f} (N={r['rho_near']:.3f} "
            f"B={r['rho_B']:.3f} far={r['rho_far']:.3f})  "
            f"Sdiag={r['s_diag']:+.4f}  Slo={slo}",
            flush=True,
        )
    print(
        f"chi5_taken={data['chi5_taken']}  chi3_taken={data['chi3_taken']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-neumann.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
