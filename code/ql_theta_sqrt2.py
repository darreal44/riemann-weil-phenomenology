#!/usr/bin/env python3
"""‖Θ(y)‖ ≤ √2 on W_L for L/4 ≤ y < L/2, then Neumann Q_pk χ₃ μ=5.

Mass partition on the half-window, not a finite section of Θ.
Finite sections must not exceed the cap (Courant the other way).
Not Galerkin of Q̂_L. Not RH.

    python code/ql_theta_sqrt2.py
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
from ql_schur_tail import HILBERT_HANKEL, r_frob_bound, theta_hat  # noqa: E402
from ql_theta_tail import theta_op_bound  # noqa: E402

SQRT2 = math.sqrt(2.0)
MU = 5.0
L5 = math.log(MU)
S0 = s0_of(1)
HEADS = (2, 4, 8, 16, 20, 24)
NS_THETA = (8, 16, 32, 48, 64)
_cache: dict[tuple[int, int], float] = {}


def in_sqrt2_band(y: float, L: float) -> bool:
    """L/4 ≤ y < L/2: shift pair on the half-window is disjoint."""
    return (0.25 * L) <= y < (0.5 * L)


def theta_op_cap(y: float, L: float) -> float:
    """#59 if y ≥ L/2; √2 in the mid band; else 2."""
    if y >= 0.5 * L:
        return 1.0
    if y >= 0.25 * L:
        return SQRT2
    return 2.0


def mass_majorant(alpha: float, beta: float, mu1: float, mu2: float) -> float:
    """2√(αβ)+2√(α μ₂)+μ₁, the |θ| bound of the partition."""
    return (
        2.0 * math.sqrt(max(alpha, 0.0) * max(beta, 0.0))
        + 2.0 * math.sqrt(max(alpha, 0.0) * max(mu2, 0.0))
        + mu1
    )


def mass_majorant_at_most_sqrt2() -> bool:
    """Elementary CS: the partition bound never exceeds √2 on the simplex."""
    grid = (0.0, 0.1, 0.25, 0.5, 0.75, 1.0)
    for a in grid:
        for b in grid:
            for m2 in grid:
                m1 = 1.0 - a - b - m2
                if m1 < -1e-15:
                    continue
                if m1 < 0.0:
                    m1 = 0.0
                if mass_majorant(a, b, m1, m2) > SQRT2 + 1e-12:
                    return False
    return True


def theta_matrix(n1: int, y: float, L: float) -> np.ndarray:
    T = np.zeros((n1, n1))
    for i in range(n1):
        for j in range(i, n1):
            v = theta_hat(i, j, y, L)
            T[i, j] = v
            T[j, i] = v
    return T


def theta_finite_op(n1: int, y: float, L: float) -> float:
    return float(np.linalg.norm(theta_matrix(n1, y, L), 2))


def Q(n: int, m: int) -> float:
    key = (min(n, m), max(n, m))
    if key not in _cache:
        _cache[key] = Q_pk(n, m, Q3, S0, D3, L5, MU)
    return _cache[key]


def t_atoms_with(cap_fn) -> float:
    s = 0.0
    for k in interior_ns(MU):
        s += abs(wn(D3, k)) * cap_fn(math.log(k), L5)
    return s


def row_at(h: int, tat: float) -> dict:
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
    y = LOG2
    hyp = in_sqrt2_band(y, L5)
    norms = [theta_finite_op(n, y, L5) for n in NS_THETA]
    lemma_ok = hyp and all(n <= SQRT2 + 1e-9 for n in norms) and norms[-1] > 1.41
    mass_ok = mass_majorant_at_most_sqrt2()
    tat2 = t_atoms_with(theta_op_bound)
    tat = t_atoms_with(theta_op_cap)
    rows = [row_at(h, tat) for h in HEADS]
    by = {r["h"]: r for r in rows}
    old_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-pk-mu5.json",
    )
    old = json.load(open(old_path, encoding="utf-8"))
    old_by = {r["h"]: r for r in old["rows"]}
    slo16 = by[16]["s_lo"]
    slo24 = by[24]["s_lo"]
    pred_ok = (
        lemma_ok
        and mass_ok
        and tat < tat2
        and slo16 is not None
        and slo16 > 0.0
        and slo24 is not None
        and slo24 > 0.0
        and slo16 + 1e-15 >= old_by[16]["s_lo"]
        and slo24 + 1e-15 >= old_by[24]["s_lo"]
        and theta_op_cap(math.log(3.0), L5) == 1.0
        and theta_op_cap(math.log(4.0), L5) == 1.0
        and theta_op_cap(y, L5) == SQRT2
    )
    return {
        "mu": MU,
        "L": L5,
        "y": y,
        "y_over_L": y / L5,
        "in_band": hyp,
        "sqrt2": SQRT2,
        "theta_norms": [{"N": n, "op": v} for n, v in zip(NS_THETA, norms)],
        "mass_majorant_ok": mass_ok,
        "t_atoms_cap2": tat2,
        "t_atoms_sqrt2": tat,
        "rows": rows,
        "s_lo16_cap2": old_by[16]["s_lo"],
        "s_lo24_cap2": old_by[24]["s_lo"],
        "lemma_holds": lemma_ok,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
    }


def main() -> int:
    print(
        "‖Θ‖≤√2 on [L/4,L/2); Neumann Q_pk χ₃ μ=5; not RH",
        flush=True,
    )
    data = run()
    print(
        f"  in_band={data['in_band']}  y/L={data['y_over_L']:.4f}  "
        f"mass_ok={data['mass_majorant_ok']}",
        flush=True,
    )
    for row in data["theta_norms"]:
        print(
            f"  ‖Θ_N‖ N={row['N']:2d}  {row['op']:.9f}  √2={SQRT2:.9f}",
            flush=True,
        )
    print(
        f"  t_atoms 2→√2  {data['t_atoms_cap2']:.6f} → {data['t_atoms_sqrt2']:.6f}",
        flush=True,
    )
    for r in data["rows"]:
        slo = f"{r['s_lo']:+.6e}" if r["s_lo"] is not None else "  —"
        print(
            f"  h={r['h']:2d}  lamH={r['lamH']:+.6e}  ρ={r['rho']:.3f}  "
            f"Slo={slo}",
            flush=True,
        )
    print(
        f"lemma_holds={data['lemma_holds']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-theta-sqrt2.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
