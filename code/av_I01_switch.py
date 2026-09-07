#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""I_{[0,1]} tangent/floor switch on g, not the parent 3-piece.

g = 2 e^{−3y/2} − θ_v. Convex ⇒ every tangent lies below g.
The tangent at 0 is g'(0) y. The tangent at the min is the
floor g_min. They meet at y_sw = g_min / g'(0). Then the
concave tail is the chord of g. Integrate a_lo = ½ w g_lo,
not a itself. Not the chord of θ. Not RH.

    python code/av_I01_switch.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import (  # noqa: E402
    a_from_g,
    bisect_root,
    g,
    g_p,
    g_pp,
    gauss_on,
)
from av_enclose import CST, p_of_v  # noqa: E402
from av_gauss import a_integrand, kernel_limit_0  # noqa: E402

WINDOW = 0.003
# Cauchy tail lower bound of ∫_1^L a from av-enclose-cauchy:
# I1L − rem = −0.018500 − 1.25e-5.
I1L_LO = -0.018513


def critical_points() -> dict:
    """y_min, y_inf from shipped g', g''; y_sw = g_min / g'(0)."""
    ymin = bisect_root(g_p, 0.05, 0.7)
    yinf = bisect_root(g_pp, 0.6, 0.95)
    gmin = g(ymin)
    gp0 = kernel_limit_0()
    ysw = gmin / gp0
    g1 = g(1.0)
    ginf = g(yinf)
    return {
        "ymin": ymin,
        "yinf": yinf,
        "ysw": ysw,
        "gmin": gmin,
        "gp0": gp0,
        "g1": g1,
        "ginf": ginf,
    }


def g_lo(y: float, pts: dict | None = None) -> float:
    """Lower comparison: tangent on [0, y_sw], floor to y_inf, chord after."""
    if pts is None:
        pts = critical_points()
    y = float(y)
    if y <= 0.0:
        return 0.0
    ysw, yinf = pts["ysw"], pts["yinf"]
    if y <= ysw:
        return pts["gp0"] * y
    if y <= yinf:
        return pts["gmin"]
    slope = (pts["g1"] - pts["ginf"]) / (1.0 - yinf)
    return pts["ginf"] + slope * (y - yinf)


def a_lo(y: float, pts: dict | None = None) -> float:
    """Comparison integrand ½ w g_lo. Not a()."""
    if pts is None:
        pts = critical_points()
    return a_from_g(float(y), g_lo(y, pts))


def true_I01() -> float:
    """Real integral of the shipped A-integrand a on [0, 1]."""
    return gauss_on(lambda y: a_integrand(max(y, 1e-15)), 1e-15, 1.0)


def switch_I01(pts: dict | None = None, n: int = 48) -> tuple[float, float, float, float]:
    """∫ a_lo on the three pieces. Returns (I1, I2, I3, I_lo)."""
    if pts is None:
        pts = critical_points()
    ysw, yinf = pts["ysw"], pts["yinf"]

    def alo(y: float) -> float:
        return a_lo(max(y, 1e-15), pts)

    i1 = gauss_on(alo, 1e-15, ysw, n)
    i2 = gauss_on(alo, ysw, yinf, n)
    i3 = gauss_on(alo, yinf, 1.0, n)
    return i1, i2, i3, i1 + i2 + i3


def step_is_taken() -> bool:
    return False


def run() -> dict:
    pts = critical_points()
    i1, i2, i3, i_lo = switch_I01(pts)
    i_true = true_I01()
    gap = i_true - i_lo
    p = p_of_v()
    q_lo = CST + i_lo + I1L_LO - p
    closes = gap < WINDOW
    kill = gap < WINDOW or gap >= 0.20 or pts["ysw"] >= pts["ymin"]
    return {
        "ymin": pts["ymin"],
        "yinf": pts["yinf"],
        "ysw": pts["ysw"],
        "gmin": pts["gmin"],
        "g_prime_0": pts["gp0"],
        "g1": pts["g1"],
        "ginf": pts["ginf"],
        "I_true": i_true,
        "I_lo": i_lo,
        "I_lo_tangent": i1,
        "I_lo_floor": i2,
        "I_lo_chord": i3,
        "gap": gap,
        "CST": CST,
        "P": p,
        "I1L_lo": I1L_LO,
        "Q_lo": q_lo,
        "closes_window": closes,
        "step_taken": step_is_taken(),
        "verdict": "KILL" if kill else "SURVIVE",
    }


def main() -> int:
    print(
        "I_{[0,1]} tangent/floor switch; not RH",
        flush=True,
    )
    data = run()
    print(
        f"  y_sw={data['ysw']:.4f}  ymin={data['ymin']:.4f}  "
        f"yinf={data['yinf']:.4f}  gmin={data['gmin']:+.4f}",
        flush=True,
    )
    print(
        f"  I_true={data['I_true']:+.6f}  I_lo={data['I_lo']:+.6f}  "
        f"gap={data['gap']:+.6f}",
        flush=True,
    )
    print(
        f"  pieces tan={data['I_lo_tangent']:+.4f}  "
        f"floor={data['I_lo_floor']:+.4f}  "
        f"chord={data['I_lo_chord']:+.4f}",
        flush=True,
    )
    print(
        f"  Q_lo={data['Q_lo']:+.4f}  closes={data['closes_window']}",
        flush=True,
    )
    print(f"verdict={data['verdict']}", flush=True)
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "av-I01-switch.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
