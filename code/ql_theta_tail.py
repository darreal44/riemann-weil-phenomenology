#!/usr/bin/env python3
"""‖Θ(log 2)‖ ≤ 1 on W_{log 3}, because y ≥ L/2.

#58 used the discrete Hilbert bound ‖Θ‖≤2. The interior
prime sits at y=log 2 ≥ L/2 (2≥√3): overlap halves are
disjoint, so |θ_f(log 2)| ≤ 1 for hat-unit f. Plug t2_op=|w₂|
into the Schur tail. Not Galerkin. Not RH.

    python code/ql_theta_tail.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kronecker import kronecker  # noqa: E402
from ql_operator_bound import CHARS, LOG2, LOG3, s0_of, w2_of  # noqa: E402
from ql_schur_tail import (  # noqa: E402
    HEAD,
    HILBERT_HANKEL,
    M_C,
    N_DIAG,
    Q_nm,
    SCAN_S00,
    SCAN_S11,
    c_tail_sq,
    r_frob_bound,
    theta_hat,
)


def y_at_least_half_window(y: float = LOG2, L: float = LOG3) -> bool:
    """Interior prime 2 on (log 2, log 3]: y/L = log 2 / log 3 ≥ 1/2."""
    return y >= 0.5 * L


def theta_op_bound(y: float = LOG2, L: float = LOG3) -> float:
    """|θ_f(y)| ≤ 1 (hat-unit) if y ≥ L/2; else CS vs θ(0)=2."""
    return 1.0 if y_at_least_half_window(y, L) else 2.0


def theta_matrix(n0: int, n1: int, y: float = LOG2) -> np.ndarray:
    """Θ_{nm}(y) for n,m in [n0, n1)."""
    dim = n1 - n0
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(n0, n1)):
        for j in range(i, dim):
            v = theta_hat(n, n0 + j, y)
            T[i, j] = v
            T[j, i] = v
    return T


def theta_finite_op(n0: int = HEAD, n1: int = 40, y: float = LOG2) -> float:
    """‖Θ(y)‖₂ on span{φ_n : n0 ≤ n < n1}."""
    T = theta_matrix(n0, n1, y)
    return float(np.linalg.norm(T, 2))


def row_of(name: str, theta_op: float) -> dict:
    cf = CHARS[name]
    q, d, a = cf["q"], cf["d"], cf["a"]
    s0 = s0_of(a)
    w2 = w2_of(d)
    chi2 = kronecker(d, 2)
    H = np.zeros((HEAD, HEAD))
    for i in range(HEAD):
        for j in range(i, HEAD):
            v = Q_nm(i, j, q, s0, w2)
            H[i, j] = v
            H[j, i] = v
    lamH = float(np.linalg.eigvalsh(H)[0])
    diags = [Q_nm(n, n, q, s0, w2) for n in range(HEAD, N_DIAG)]
    qmin = min(diags)
    qmin_at = HEAD + int(np.argmin(np.array(diags)))
    cfrob_sq = 0.0
    for i in range(HEAD):
        for j in range(HEAD, M_C):
            cfrob_sq += Q_nm(i, j, q, s0, w2) ** 2
        cfrob_sq += c_tail_sq(i, M_C, w2)
    c_frob = math.sqrt(cfrob_sq)
    r_f = r_frob_bound(HEAD)
    hankel = 0.5 * HILBERT_HANKEL + 1.0 / (4.0 * HEAD)
    t2 = abs(w2) * theta_op
    off_op = hankel + r_f + t2
    delta = qmin - off_op
    beta = lamH - (c_frob * c_frob) / delta if delta > 0.0 else None
    return {
        "name": name,
        "chi2": chi2,
        "w2": w2,
        "lamH": lamH,
        "qmin": qmin,
        "qmin_at": qmin_at,
        "c_frob": c_frob,
        "hankel_op": hankel,
        "r_frob": r_f,
        "t2_op": t2,
        "t2_op_old": abs(w2) * 2.0,
        "off_op": off_op,
        "delta": delta,
        "beta": beta,
        "beta_pos": bool(beta is not None and beta > 0.0),
        "S00_match": abs(float(H[0, 0]) - SCAN_S00[name]) < 1e-8,
        "S11_match": abs(float(H[1, 1]) - SCAN_S11[name]) < 1e-8,
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    assert y_at_least_half_window()
    th_op = theta_op_bound()
    th_fin = theta_finite_op(HEAD, 40)
    th_full = theta_finite_op(0, 40)
    rows = [row_of(name, th_op) for name in ("chi5", "chi8", "chi4", "chi3")]
    by = {r["name"]: r for r in rows}
    pred_ok = (
        th_fin <= 1.001
        and th_full <= 1.001
        and (not by["chi5"]["beta_pos"])
        and (not by["chi3"]["beta_pos"])
        and by["chi8"]["beta_pos"]
        and by["chi5"]["delta"] < 0.0
    )
    return {
        "L": LOG3,
        "log2": LOG2,
        "y_over_L": LOG2 / LOG3,
        "y_ge_half": True,
        "theta_op_bound": th_op,
        "theta_finite_tail": th_fin,
        "theta_finite_full": th_full,
        "step_taken": step_is_taken(),
        "chi8_taken": by["chi8"]["beta_pos"],
        "chi5_taken": by["chi5"]["beta_pos"],
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        "L=log 3; ‖Θ(log 2)‖≤1 because y≥L/2; Schur t2=|w₂|; not Galerkin",
        flush=True,
    )
    data = run()
    print(
        f"  y/L={data['y_over_L']:.4f}  ‖Θ‖_bound={data['theta_op_bound']}  "
        f"finite tail={data['theta_finite_tail']:.6f}  "
        f"full={data['theta_finite_full']:.6f}",
        flush=True,
    )
    for r in data["rows"]:
        b = f"{r['beta']:+.4f}" if r["beta"] is not None else "−∞"
        print(
            f"  {r['name']:4s} t2 {r['t2_op_old']:.3f}→{r['t2_op']:.3f}  "
            f"δ={r['delta']:+.4f}  β={b}",
            flush=True,
        )
    print(
        f"chi8_taken={data['chi8_taken']}  chi5_taken={data['chi5_taken']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-theta-tail.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
