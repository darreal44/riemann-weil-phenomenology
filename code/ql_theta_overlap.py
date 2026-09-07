#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Three coverings of #72: |θ| ≤ 2√(αβ)+2√(αμ₂)+μ₁ is the overlap count.

Simplex ≤ √2 is already a theorem. This module identifies the
five x-intervals / three covering types that make the CS bound.
Without that count the χ₃ μ=5 take is retroactive. Not Weil.

    python code/ql_theta_overlap.py
"""
from __future__ import annotations

import json
import math
import os
import sys

from numpy.polynomial.legendre import leggauss

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import LOG2  # noqa: E402
from ql_schur_tail import theta_hat  # noqa: E402
from ql_theta_sqrt2 import SQRT2, L5, mass_majorant  # noqa: E402

L5 = float(L5)
Y_TAKE = float(LOG2)


def gauss_on(f, a: float, b: float, n: int = 48) -> float:
    if b <= a + 1e-15:
        return 0.0
    x, wt = leggauss(n)
    h = (b - a) / 2.0
    m = (a + b) / 2.0
    acc = 0.0
    for xi, wj in zip(x, wt):
        acc += float(wj) * h * f(m + h * float(xi))
    return acc


def in_strict_band(y: float, L: float) -> bool:
    """L/3 ≤ y < L/2: reverse(A) ⊂ M, four disjoint pieces."""
    return (L / 3.0) <= y < (0.5 * L)


def partition(y: float, L: float) -> dict:
    """A, M1, M2, C on [0, L/2]. Empty M1 if y < L/3."""
    a_hi = 0.5 * L - y
    m2_lo = 2.0 * y - 0.5 * L
    half = 0.5 * L
    return {
        "A": (0.0, a_hi),
        "M1": (a_hi, m2_lo) if m2_lo > a_hi else (a_hi, a_hi),
        "M2": (max(m2_lo, a_hi), y),
        "C": (y, half),
        "half": half,
    }


def covering_x(y: float, L: float) -> dict:
    """Five x-intervals of the integrand, three covering types."""
    a_hi = 0.5 * L - y
    m2_lo = 2.0 * y - 0.5 * L
    return {
        "AC_minus": (y - 0.5 * L, 0.0),
        "AM2": (0.0, a_hi),
        "M1": (a_hi, m2_lo) if m2_lo > a_hi else (a_hi, a_hi),
        "M2": (max(m2_lo, a_hi), y),
        "AC_plus": (y, 0.5 * L),
    }


def interval_len(ab: tuple[float, float]) -> float:
    return max(0.0, ab[1] - ab[0])


def partition_covers_half(y: float, L: float) -> bool:
    p = partition(y, L)
    pieces = [p["A"], p["M1"], p["M2"], p["C"]]
    if abs(sum(interval_len(s) for s in pieces) - 0.5 * L) > 1e-12:
        return False
    ends = sorted((s[0], s[1]) for s in pieces if interval_len(s) > 1e-15)
    if abs(ends[0][0]) > 1e-12 or abs(ends[-1][1] - 0.5 * L) > 1e-12:
        return False
    for i in range(len(ends) - 1):
        if abs(ends[i][1] - ends[i + 1][0]) > 1e-12:
            return False
    return True


def covering_covers_integrand(y: float, L: float) -> bool:
    cov = covering_x(y, L)
    total = sum(interval_len(cov[k]) for k in cov)
    return abs(total - (L - y)) < 1e-12


def f_from_h(h, L: float):
    s2 = math.sqrt(2.0)
    half = 0.5 * L

    def f(x: float) -> float:
        ax = abs(x)
        if ax > half + 1e-15:
            return 0.0
        return h(min(ax, half)) / s2

    return f


def inner_T(f, y: float, L: float) -> float:
    """⟨f, T_y f⟩ = ∫_{y−L/2}^{L/2} f(x) f(x−y) dx."""
    return gauss_on(lambda x: f(x) * f(x - y), y - 0.5 * L, 0.5 * L)


def pair_inners(f, y: float, L: float) -> dict:
    cov = covering_x(y, L)
    out = {}
    for name, ab in cov.items():
        out[name] = gauss_on(lambda x, yy=y: f(x) * f(x - yy), ab[0], ab[1])
    return out


def masses_of_h(h, y: float, L: float) -> dict:
    p = partition(y, L)

    def mass(ab):
        return gauss_on(lambda t: h(t) ** 2, ab[0], ab[1])

    return {
        "alpha": mass(p["A"]),
        "beta": mass(p["C"]),
        "mu1": mass(p["M1"]),
        "mu2": mass(p["M2"]),
    }


def h_constant(L: float):
    c = math.sqrt(2.0 / L)
    return lambda t, cc=c: cc


def h_cosine(L: float):
    """Normalized cos(2π t/L) on [0, L/2]."""
    om = 2.0 * math.pi / L

    def raw(t: float) -> float:
        return math.cos(om * t)

    nrm = math.sqrt(gauss_on(lambda t: raw(t) ** 2, 0.0, 0.5 * L))
    return lambda t, n=nrm: raw(t) / n


def theta_of_h(h, y: float, L: float) -> float:
    return 2.0 * inner_T(f_from_h(h, L), y, L)


def majorant_of_h(h, y: float, L: float) -> float:
    m = masses_of_h(h, y, L)
    return mass_majorant(m["alpha"], m["beta"], m["mu1"], m["mu2"])


def step_is_taken() -> bool:
    return False


def run() -> dict:
    L, y = L5, Y_TAKE
    ys = [L / 3.0, 0.4 * L, y, 0.45 * L, 0.49 * L]
    part_ok = all(in_strict_band(yy, L) and partition_covers_half(yy, L) for yy in ys)
    cov_ok = all(covering_covers_integrand(yy, L) for yy in ys)
    hs = {"const": h_constant(L), "cos": h_cosine(L)}
    checks = []
    all_ok = part_ok and cov_ok
    for name, h in hs.items():
        for yy in ys:
            f = f_from_h(h, L)
            I = inner_T(f, yy, L)
            pairs = pair_inners(f, yy, L)
            s = sum(pairs.values())
            th = 2.0 * I
            maj = majorant_of_h(h, yy, L)
            ok = abs(s - I) < 1e-9 and th <= maj + 1e-9
            all_ok = all_ok and ok
            checks.append(
                {
                    "h": name,
                    "y": yy,
                    "I": I,
                    "pair_sum": s,
                    "theta": th,
                    "majorant": maj,
                    "ok": ok,
                }
            )
    th00 = theta_hat(0, 0, y, L)
    th_const = theta_of_h(h_constant(L), y, L)
    y_over_L = y / L
    pred_ok = (
        all_ok
        and in_strict_band(y, L)
        and (1.0 / 3.0) < y_over_L < 0.5
        and abs(th_const - th00) < 1e-9
        and abs(th00 - 2.0 * (L - y) / L) < 1e-12
    )
    p = partition(y, L)
    return {
        "L": L,
        "y": y,
        "y_over_L": y_over_L,
        "in_strict_band": in_strict_band(y, L),
        "partition": {k: list(v) if isinstance(v, tuple) else v for k, v in p.items()},
        "covering": {k: list(v) for k, v in covering_x(y, L).items()},
        "part_ok": part_ok,
        "cov_ok": cov_ok,
        "theta_hat00": th00,
        "theta_const": th_const,
        "checks": checks,
        "sqrt2": SQRT2,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
    }


def main() -> int:
    print("three coverings of #72; not Weil, not RH", flush=True)
    data = run()
    print(
        f"  y/L={data['y_over_L']:.4f}  strict_band={data['in_strict_band']}  "
        f"part={data['part_ok']}  cov={data['cov_ok']}",
        flush=True,
    )
    print(
        f"  theta_hat00={data['theta_hat00']:.6f}  "
        f"theta_const={data['theta_const']:.6f}",
        flush=True,
    )
    for c in data["checks"]:
        print(
            f"  {c['h']:5s} y={c['y']:.4f}  θ={c['theta']:+.4f}  "
            f"maj={c['majorant']:.4f}  ok={c['ok']}",
            flush=True,
        )
    print(f"verdict={data['verdict']}", flush=True)
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-theta-overlap.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
