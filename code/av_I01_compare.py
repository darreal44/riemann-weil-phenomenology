#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""I_{[0,1]} by hand: Gauss-3 table of θ_nm, and a 3-piece bound on g.

g = 2 e^{−3y/2} − θ_v. Tangent / floor / chord. Chord of θ is the
other direction. Neither closes the A-window. Not RH.

    python code/av_I01_compare.py
"""
from __future__ import annotations

import json
import math
import os
import sys

from numpy.polynomial.legendre import leggauss

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_enclose import CST, p_of_v  # noqa: E402
from av_gauss import (  # noqa: E402
    GAUSS_NODES,
    GAUSS_WEIGHTS,
    L16,
    V,
    a_integrand,
    gauss3_unit,
    kernel_limit_0,
    th,
    theta_v,
    theta_v_prime_0,
    w,
)

PI = math.pi
SQRT2 = math.sqrt(2.0)


def omega(k: int, L: float = L16) -> float:
    return 2.0 * PI * k / L


def th_p(n: int, m: int, y: float, L: float = L16) -> float:
    """∂_y θ_nm, elementary."""
    if n > m:
        n, m = m, n
    if n == 0 and m == 0:
        return -2.0 / L
    om = lambda k: omega(k, L)
    if n == 0:
        j = m
        return -2.0 * om(j) * math.cos(om(j) * y) / (SQRT2 * PI * j)
    if n == m:
        o = om(n)
        return 2.0 * (
            -math.cos(o * y) / L
            - (L - y) * o * math.sin(o * y) / L
            - math.cos(o * y) / (2.0 * PI * n) * o
        )
    # n < m, both ≥ 1
    on, om_ = om(n), om(m)
    return (
        2.0
        * (n * on * math.cos(on * y) - m * om_ * math.cos(om_ * y))
        / (PI * (m * m - n * n))
    )


def th_pp(n: int, m: int, y: float, L: float = L16) -> float:
    """∂_yy θ_nm."""
    if n > m:
        n, m = m, n
    if n == 0 and m == 0:
        return 0.0
    om = lambda k: omega(k, L)
    if n == 0:
        j = m
        o = om(j)
        return 2.0 * o * o * math.sin(o * y) / (SQRT2 * PI * j)
    if n == m:
        o = om(n)
        # 2 [ -cos/L - (L-y) o sin/L - o cos /(2π n) ]'
        return 2.0 * (
            o * math.sin(o * y) / L
            + o * math.sin(o * y) / L
            - (L - y) * o * o * math.cos(o * y) / L
            + o * o * math.sin(o * y) / (2.0 * PI * n)
        )
    on, om_ = om(n), om(m)
    return (
        2.0
        * (-(n * on * on) * math.sin(on * y) + m * om_ * om_ * math.sin(om_ * y))
        / (PI * (m * m - n * n))
    )


def theta_v_p(y: float, L: float = L16, v=V) -> float:
    if y <= 0.0:
        return theta_v_prime_0(L, v)
    acc = 0.0
    for n in range(3):
        for m in range(3):
            acc += v[n] * v[m] * th_p(n, m, y, L)
    return acc


def theta_v_pp(y: float, L: float = L16, v=V) -> float:
    acc = 0.0
    for n in range(3):
        for m in range(3):
            acc += v[n] * v[m] * th_pp(n, m, y, L)
    return acc


def g(y: float) -> float:
    if y <= 0.0:
        return 0.0
    return 2.0 * math.exp(-1.5 * y) - theta_v(y)


def g_p(y: float) -> float:
    """g' = −3 e^{−3y/2} − θ_v'."""
    if y <= 0.0:
        return kernel_limit_0()
    return -3.0 * math.exp(-1.5 * y) - theta_v_p(y)


def g_pp(y: float) -> float:
    """g'' = 4.5 e^{−3y/2} − θ_v''."""
    yy = max(y, 0.0)
    return 4.5 * math.exp(-1.5 * yy) - theta_v_pp(yy)


def bisect_root(f, lo: float, hi: float, n: int = 80) -> float:
    flo, fhi = f(lo), f(hi)
    if flo == 0.0:
        return lo
    if fhi == 0.0:
        return hi
    if flo * fhi > 0.0:
        raise ValueError(f"no sign change on [{lo}, {hi}]")
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if flo * fm <= 0.0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def gauss_on(f, a: float, b: float, n: int = 48) -> float:
    x, wt = leggauss(n)
    h = (b - a) / 2.0
    m = (a + b) / 2.0
    acc = 0.0
    for xi, wj in zip(x, wt):
        acc += float(wj) * h * f(m + h * float(xi))
    return acc


def gauss_table() -> list[dict]:
    rows = []
    for y, wt in zip(GAUSS_NODES, GAUSS_WEIGHTS):
        ths = {}
        for n in range(3):
            for m in range(n, 3):
                ths[f"th{n}{m}"] = th(n, m, y, L16)
        tv = theta_v(y)
        wy = w(y)
        ay = a_integrand(y)
        rows.append(
            {
                "y": y,
                "weight": wt,
                "w": wy,
                "theta_v": tv,
                "EC": math.exp(-1.5 * y),
                "g": 2.0 * math.exp(-1.5 * y) - tv,
                "a": ay,
                "contrib": wt * ay,
                "ths": ths,
            }
        )
    return rows


def a_from_g(y: float, gg: float) -> float:
    if y <= 1e-14:
        return 0.5 * kernel_limit_0()
    return 0.5 * w(y) * gg


def step_is_taken() -> bool:
    return False


def run() -> dict:
    ymin = bisect_root(g_p, 0.05, 0.7)
    yinf = bisect_root(g_pp, 0.6, 0.95)
    gmin = g(ymin)
    gp0 = kernel_limit_0()
    g1 = g(1.0)
    ginf = g(yinf)
    th1 = theta_v(1.0)

    def g_lo(y: float) -> float:
        if y <= ymin:
            return gp0 * y
        if y <= yinf:
            return gmin
        return ginf + (g1 - ginf) / (1.0 - yinf) * (y - yinf)

    def a_lo(y: float) -> float:
        return a_from_g(y, g_lo(y))

    def a_chord_th(y: float) -> float:
        ch = 2.0 + (th1 - 2.0) * y
        if y <= 1e-14:
            return 0.5 * (-3.0 - (th1 - 2.0))
        return 0.5 * w(y) * (2.0 * math.exp(-1.5 * y) - ch)

    I_true = gauss_on(lambda y: a_integrand(max(y, 1e-15)), 1e-15, 1.0)
    I_lo = gauss_on(a_lo, 1e-15, 1.0)
    I_chord = gauss_on(lambda y: a_chord_th(max(y, 1e-15)), 1e-15, 1.0)
    g3 = gauss3_unit(a_integrand)
    table = gauss_table()
    g3_from_table = sum(r["contrib"] for r in table)
    P = p_of_v()
    # A = CST + ∫_0^1 a + ∫_1^L a. Tail enclosed ~ −0.0185; use 0 for a
    # lower-bound test of the [0,1] piece only: Q_lo_piece = CST + I_lo + I1L_lo - P
    # I1L_lo from av-enclose-cauchy is −0.018500 − 1.25e-5 ≈ −0.01851
    I1L_lo = -0.018513
    Q_lo_3piece = CST + I_lo + I1L_lo - P
    gap_lo = I_true - I_lo
    gap_chord = I_chord - I_true
    pred_ok = (
        abs(g3 + 0.70066) < 1e-4
        and gap_lo > 0.15
        and gap_chord > 0.15
        and Q_lo_3piece < 0.0
        and ymin < yinf < 1.0
        and gmin < g1 < 0.0
        and g_pp(0.2) > 0.0
        and g_pp(0.9) < 0.0
    )
    return {
        "ymin": ymin,
        "yinf": yinf,
        "gmin": gmin,
        "g_prime_0": gp0,
        "g1": g1,
        "theta_1": th1,
        "I_true": I_true,
        "I_3piece_lo": I_lo,
        "I_chord_th": I_chord,
        "gap_3piece": gap_lo,
        "gap_chord": gap_chord,
        "gauss3": g3,
        "gauss3_table_sum": g3_from_table,
        "CST": CST,
        "P": P,
        "Q_lo_3piece": Q_lo_3piece,
        "closes_window": gap_lo < 0.003,
        "table": table,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
    }


def main() -> int:
    print(
        "I_{[0,1]} Gauss-3 table and 3-piece g; not RH",
        flush=True,
    )
    data = run()
    print(
        f"  ymin={data['ymin']:.4f}  yinf={data['yinf']:.4f}  "
        f"gmin={data['gmin']:+.4f}",
        flush=True,
    )
    print("  Gauss3 nodes:", flush=True)
    for r in data["table"]:
        print(
            f"    y={r['y']:.6f}  θ={r['theta_v']:.6f}  a={r['a']:+.6f}  "
            f"w_G={r['weight']:.6f}  contrib={r['contrib']:+.6f}",
            flush=True,
        )
    print(
        f"  Gauss3={data['gauss3']:+.6f}  I_true={data['I_true']:+.6f}",
        flush=True,
    )
    print(
        f"  3-piece lo={data['I_3piece_lo']:+.4f}  gap={data['gap_3piece']:+.4f}",
        flush=True,
    )
    print(
        f"  chord θ   ={data['I_chord_th']:+.4f}  gap={data['gap_chord']:+.4f}",
        flush=True,
    )
    print(
        f"  Q_lo_3piece={data['Q_lo_3piece']:+.4f}  closes={data['closes_window']}",
        flush=True,
    )
    print(f"verdict={data['verdict']}", flush=True)
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "av-I01-compare.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
