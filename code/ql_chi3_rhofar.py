#!/usr/bin/env python3
"""χ₃ ρ_far: larger N_NEAR / 3-layer on the #61 Neumann split.

Same cosine ONB, h=2, T infinite. Hilbert π/2 in off_far
is N-independent in the continuous analog. Not Galerkin
of W_L. Not RH.

    python code/ql_chi3_rhofar.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import CHARS, PI, w2_of  # noqa: E402
from ql_schur_neumann import HEAD, Q, block_norm  # noqa: E402
from ql_schur_tail import HILBERT_HANKEL, r_frob_bound  # noqa: E402
from ql_theta_tail import theta_op_bound  # noqa: E402

NAME = "chi3"
GRIDS = ((24, 40), (32, 40), (40, 56), (48, 64), (64, 80), (80, 96))
THREE = (24, 48, 64)
RHO_NEED = 0.41
QNN_NS = (2, 8, 16, 24, 32, 40, 48, 64, 80)


def off_far(n0: int, t2: float) -> float:
    return (
        0.5 * HILBERT_HANKEL
        + 1.0 / (4.0 * n0)
        + r_frob_bound(n0)
        + t2
    )


def _rho_b(n0: int, n1: int, n2: int, qmin_far: float, w2: float) -> float:
    b2 = 0.0
    for n in range(n0, n1):
        qnn = Q(NAME, n, n)
        for m in range(n1, n2):
            b2 += Q(NAME, n, m) ** 2 / (qnn * Q(NAME, m, m))
        b2 += 0.25 / max(n + n2 - 1, 1) / (qnn * qmin_far)
        if abs(w2) > 0.0:
            b2 += (2.0 * abs(w2) / PI) ** 2 / max(n2 - n - 1, 1) / (
                qnn * qmin_far
            )
    return math.sqrt(b2)


def _schur_bits(
    n_lo: int, n_hi: int, m_c: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    H = np.array(
        [[Q(NAME, i, j) for j in range(HEAD)] for i in range(HEAD)], float
    )
    d = np.array([Q(NAME, n, n) for n in range(n_lo, n_hi)])
    C = np.array(
        [[Q(NAME, i, m) for m in range(n_lo, n_hi)] for i in range(HEAD)],
        float,
    )
    cdc = C @ np.diag(1.0 / d) @ C.T
    cfar = np.zeros((HEAD, HEAD))
    for k in range(n_hi, m_c):
        ck = np.array([Q(NAME, i, k) for i in range(HEAD)])
        cfar += np.outer(ck, ck) / Q(NAME, k, k)
    return H, cdc, cfar


def _s_lo(H: np.ndarray, eat: np.ndarray, rho: float) -> float | None:
    if rho >= 1.0:
        return None
    return float(np.linalg.eigvalsh(H - eat / (1.0 - rho))[0])


def row_at(n_near: int, m_c: int) -> dict:
    w2 = w2_of(CHARS[NAME]["d"])
    t2 = abs(w2) * theta_op_bound()
    dim = n_near - HEAD
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(HEAD, n_near)):
        for j, m in enumerate(range(HEAD, n_near)):
            T[i, j] = Q(NAME, n, m)
    d = np.diag(T)
    A = (T - np.diag(d)) * np.outer(1.0 / np.sqrt(d), 1.0 / np.sqrt(d))
    rho_n = float(np.linalg.norm(A, 2))
    qmin_far = min(Q(NAME, n, n) for n in range(n_near, m_c))
    off = off_far(n_near, t2)
    off_h = off_far(n_near, 0.0)
    rho_far = off / qmin_far
    rho_far_h = off_h / qmin_far
    rho_b = _rho_b(HEAD, n_near, m_c, qmin_far, w2)
    rho = block_norm(rho_n, rho_b, rho_far)
    rho_h = block_norm(rho_n, rho_b, rho_far_h)
    H, cdc, cfar = _schur_bits(HEAD, n_near, m_c)
    eat = cdc + cfar
    lam_h = float(np.linalg.eigvalsh(H)[0])
    s_diag = float(np.linalg.eigvalsh(H - cdc)[0])
    s_lo = _s_lo(H, eat, rho)
    s_lo_h = _s_lo(H, eat, rho_h)
    return {
        "n_near": n_near,
        "M_C": m_c,
        "lamH": lam_h,
        "rho_near": rho_n,
        "rho_B": rho_b,
        "rho_far": rho_far,
        "rho_far_hankel": rho_far_h,
        "rho": rho,
        "rho_hankel": rho_h,
        "qmin_far": qmin_far,
        "off_far": off,
        "s_diag": s_diag,
        "s_lo": s_lo,
        "s_lo_hankel": s_lo_h,
        "s_lo_pos": bool(s_lo is not None and s_lo > 0.0),
        "tr_CDC": float(np.trace(cdc)),
        "tr_Cfar": float(np.trace(cfar)),
    }


def rho_block(n0: int, n1: int) -> tuple[float, float]:
    dim = n1 - n0
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(n0, n1)):
        for j, m in enumerate(range(n0, n1)):
            T[i, j] = Q(NAME, n, m)
    d = np.diag(T)
    A = (T - np.diag(d)) * np.outer(1.0 / np.sqrt(d), 1.0 / np.sqrt(d))
    return float(np.linalg.norm(A, 2)), float(d.min())


def rho_cpl(
    n0a: int,
    n1a: int,
    n0b: int,
    n1b: int,
    qmin_b: float,
    m_tail: int | None,
    w2: float,
) -> float:
    s = 0.0
    for n in range(n0a, n1a):
        qnn = Q(NAME, n, n)
        for m in range(n0b, n1b):
            s += Q(NAME, n, m) ** 2 / (qnn * Q(NAME, m, m))
        if m_tail is not None:
            s += 0.25 / max(n + m_tail - 1, 1) / (qnn * qmin_b)
            if abs(w2) > 0.0:
                s += (2.0 * abs(w2) / PI) ** 2 / max(m_tail - n - 1, 1) / (
                    qnn * qmin_b
                )
    return math.sqrt(s)


def row_3layer(n1: int, n2: int, n3: int) -> dict:
    w2 = w2_of(CHARS[NAME]["d"])
    t2 = abs(w2) * theta_op_bound()
    rho1, qmin1 = rho_block(HEAD, n1)
    rho2, qmin2 = rho_block(n1, n2)
    qmin_far = min(Q(NAME, n, n) for n in range(n2, n3))
    off = off_far(n2, t2)
    rho3 = off / qmin_far
    b12 = rho_cpl(HEAD, n1, n1, n2, qmin2, None, w2)
    b13 = rho_cpl(HEAD, n1, n2, n3, qmin_far, n3, w2)
    b23 = rho_cpl(n1, n2, n2, n3, qmin_far, n3, w2)
    G = np.array(
        [[rho1, b12, b13], [b12, rho2, b23], [b13, b23, rho3]], float
    )
    rho = float(np.linalg.norm(G, 2))
    H, cdc, cfar = _schur_bits(HEAD, n2, n3)
    eat = cdc + cfar
    lam_h = float(np.linalg.eigvalsh(H)[0])
    s_diag = float(np.linalg.eigvalsh(H - cdc)[0])
    s_lo = _s_lo(H, eat, rho)
    return {
        "n1": n1,
        "n2": n2,
        "n3": n3,
        "rho1": rho1,
        "rho2": rho2,
        "rho3": rho3,
        "B12": b12,
        "B13": b13,
        "B23": b23,
        "rho": rho,
        "qmin1": qmin1,
        "qmin2": qmin2,
        "qmin_far": qmin_far,
        "off_far": off,
        "lamH": lam_h,
        "s_diag": s_diag,
        "s_lo": s_lo,
        "s_lo_pos": bool(s_lo is not None and s_lo > 0.0),
    }


def qnn_of(n: int) -> float:
    return Q(NAME, n, n)


def step_is_taken() -> bool:
    return False


def run() -> dict:
    print("2-layer grid", flush=True)
    rows = []
    for n_near, m_c in GRIDS:
        r = row_at(n_near, m_c)
        rows.append(r)
        slo = f"{r['s_lo']:+.4f}" if r["s_lo"] is not None else "−∞"
        print(
            f"  N={r['n_near']:3d} M={r['M_C']:3d}  "
            f"ρN={r['rho_near']:.3f} ρB={r['rho_B']:.3f} "
            f"ρF={r['rho_far']:.3f} ρ={r['rho']:.3f}  "
            f"Sdiag={r['s_diag']:+.4f} Slo={slo}",
            flush=True,
        )
    print("3-layer", flush=True)
    three = row_3layer(*THREE)
    slo = f"{three['s_lo']:+.4f}" if three["s_lo"] is not None else "−∞"
    print(
        f"  n1={three['n1']} n2={three['n2']} n3={three['n3']}  "
        f"ρ1={three['rho1']:.3f} ρ2={three['rho2']:.3f} "
        f"ρ3={three['rho3']:.3f} ρ={three['rho']:.3f}  Slo={slo}",
        flush=True,
    )
    qnns = [{"n": n, "Q_nn": qnn_of(n)} for n in QNN_NS]
    by = {r["n_near"]: r for r in rows}
    chi3_taken = any(r["s_lo_pos"] for r in rows) or three["s_lo_pos"]
    slo_neg = all(r["s_lo"] is not None and r["s_lo"] < 0.0 for r in rows)
    rho_above = all(r["rho"] > RHO_NEED for r in rows)
    far80 = by[80]["rho_far"] >= RHO_NEED
    n_climbs = by[80]["rho_near"] > by[24]["rho_near"]
    sdiag_frozen = all(
        abs(r["s_diag"] - by[32]["s_diag"]) < 0.001 for r in rows
    )
    three_fail = three["rho"] > RHO_NEED and (
        three["s_lo"] is not None and three["s_lo"] < 0.0
    )
    hankel_fail = all(r["rho_hankel"] > RHO_NEED for r in rows)
    pred_ok = (
        slo_neg
        and rho_above
        and far80
        and n_climbs
        and sdiag_frozen
        and three_fail
        and hankel_fail
        and (not chi3_taken)
    )
    return {
        "name": NAME,
        "head": HEAD,
        "grids": [list(g) for g in GRIDS],
        "three": list(THREE),
        "rho_need": RHO_NEED,
        "step_taken": step_is_taken(),
        "chi3_taken": chi3_taken,
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
        "three_layer": three,
        "Q_nn": qnns,
    }


def main() -> int:
    print(
        "χ₃ ρ_far; #61 Neumann; larger N / 3-layer; T infinite; not Galerkin",
        flush=True,
    )
    data = run()
    print(
        f"chi3_taken={data['chi3_taken']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-chi3-rhofar.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
