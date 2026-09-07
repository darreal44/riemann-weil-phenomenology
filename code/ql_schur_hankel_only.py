#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Drop B₁^Θ (w₂=0): Off_far is Hankel only. Not a take.

Q_nm = A − w₂ θ(log 2). Setting w₂=0 removes the Θ-codiagonal
and leaves the archimedean Hankel (S_k ⇒ ½/(n+m)). Off_far
loses |w₂|‖Θ‖; ρ_B loses the 2|w₂|/π tail. H, C, T are rebuilt
from A alone. Named in report/w2-impact.md: χ₈,χ₄ already
have w₂=0. This sitting forces that on χ₅ and χ₃.

    python code/ql_schur_hankel_only.py

Not Galerkin of W_L. Not RH. One L.
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import CHARS, PI, s0_of  # noqa: E402
from ql_schur_neumann import (  # noqa: E402
    HEAD,
    M_C,
    N_NEAR,
    block_norm,
    row_of,
)
from ql_schur_tail import HILBERT_HANKEL, Q_nm, r_frob_bound  # noqa: E402

_cache: dict[tuple[str, int, int], float] = {}


def Qh(name: str, n: int, m: int) -> float:
    """Archimedean Q only: w₂=0."""
    cf = CHARS[name]
    q, s0 = cf["q"], s0_of(cf["a"])
    key = (name, min(n, m), max(n, m))
    if key not in _cache:
        _cache[key] = Q_nm(n, m, q, s0, 0.0)
    return _cache[key]


def row_hankel(name: str) -> dict:
    dim = N_NEAR - HEAD
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(HEAD, N_NEAR)):
        for j, m in enumerate(range(HEAD, N_NEAR)):
            T[i, j] = Qh(name, n, m)
    d = np.diag(T)
    A = (T - np.diag(d)) * np.outer(1.0 / np.sqrt(d), 1.0 / np.sqrt(d))
    rho_n = float(np.linalg.norm(A, 2))
    qmin_far = min(Qh(name, n, n) for n in range(N_NEAR, M_C))
    off_far = (
        0.5 * HILBERT_HANKEL + 1.0 / (4.0 * N_NEAR) + r_frob_bound(N_NEAR)
    )
    rho_far = off_far / qmin_far
    b2 = 0.0
    for n in range(HEAD, N_NEAR):
        qnn = Qh(name, n, n)
        for m in range(N_NEAR, M_C):
            b2 += Qh(name, n, m) ** 2 / (qnn * Qh(name, m, m))
        b2 += 0.25 / max(n + M_C - 1, 1) / (qnn * qmin_far)
    rho_b = math.sqrt(b2)
    rho = block_norm(rho_n, rho_b, rho_far)
    H = np.array(
        [[Qh(name, i, j) for j in range(HEAD)] for i in range(HEAD)], float
    )
    C = np.array(
        [[Qh(name, i, m) for m in range(HEAD, N_NEAR)] for i in range(HEAD)],
        float,
    )
    cdc = C @ np.diag(1.0 / d) @ C.T
    cfar = np.zeros((HEAD, HEAD))
    for k in range(N_NEAR, M_C):
        ck = np.array([Qh(name, i, k) for i in range(HEAD)])
        cfar += np.outer(ck, ck) / Qh(name, k, k)
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
        "s_diag": s_diag,
        "s_lo": s_lo,
        "s_lo_pos": bool(s_lo is not None and s_lo > 0.0),
        "off_far": off_far,
        "qmin_far": qmin_far,
    }


def _flt(x):
    if isinstance(x, (float, np.floating)):
        return float(x)
    return x


def main() -> int:
    print(
        "w₂=0: B₁^Θ off, Hankel only. Full Q vs arch. Not a take.",
        flush=True,
    )
    print(
        f"{'χ':4s}  {'S_lo full':>10s}  {'S_lo Hank':>10s}  "
        f"{'λ_H Hank':>9s}  {'ρ Hank':>7s}",
        flush=True,
    )
    rows = []
    for name in ("chi5", "chi8", "chi4", "chi3"):
        full = row_of(name)
        han = row_hankel(name)
        rec = {
            "name": name,
            "full_s_lo": full["s_lo"],
            "full_lamH": full["lamH"],
            "full_rho": full["rho"],
            "hank_s_lo": han["s_lo"],
            "hank_lamH": han["lamH"],
            "hank_rho": han["rho"],
            "hank_s_diag": han["s_diag"],
            "hank_s_lo_pos": han["s_lo_pos"],
        }
        rows.append(rec)
        fs = f"{full['s_lo']:+.4f}" if full["s_lo"] is not None else "−∞"
        hs = f"{han['s_lo']:+.4f}" if han["s_lo"] is not None else "−∞"
        print(
            f"{name:4s}  {fs:>10s}  {hs:>10s}  "
            f"{han['lamH']:+9.4f}  {han['rho']:7.3f}",
            flush=True,
        )
    by = {r["name"]: r for r in rows}
    data = {
        "step_taken": False,
        "verdict": "KILL",
        "why": (
            "Hankel-only is a diagnostic: w₂=0 is not the Weil form "
            "of χ₃. S_lo of that proxy is not a take."
        ),
        "chi3_full_s_lo": by["chi3"]["full_s_lo"],
        "chi3_hank_s_lo": by["chi3"]["hank_s_lo"],
        "chi3_hank_s_lo_pos": by["chi3"]["hank_s_lo_pos"],
        "rows": [{k: _flt(v) for k, v in r.items()} for r in rows],
    }
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-hankel-only.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    print(
        f"chi3 Hankel-only S_lo>0={data['chi3_hank_s_lo_pos']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
