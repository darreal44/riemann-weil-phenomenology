#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""I_{[0,1]} three-tangent envelope of g, not the switch.

g = 2 e^{−3y/2} − θ_v. Convex on [0, y_inf] ⇒ every tangent
lies below g. Envelope of t0, floor, and the tangent at y_inf,
then the chord on the concave tail. Integrate a_lo = ½ w g_lo.
Not Weil. Not RH.

    python code/av_I01_envelope.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import a_from_g, g, g_p, gauss_on  # noqa: E402
from av_I01_switch import I1L_LO, WINDOW, critical_points, true_I01  # noqa: E402
from av_enclose import CST, p_of_v  # noqa: E402


def envelope_points() -> dict:
    """Switch points plus g'(y_inf) and the floor/tinf meeting y_meet."""
    pts = dict(critical_points())
    gpinf = g_p(pts["yinf"])
    ymeet = pts["yinf"] + (pts["gmin"] - pts["ginf"]) / gpinf
    pts["gpinf"] = gpinf
    pts["ymeet"] = ymeet
    return pts


def g_lo(y: float, pts: dict | None = None) -> float:
    """Lower comparison: t0 / floor / tinf / chord."""
    if pts is None:
        pts = envelope_points()
    y = float(y)
    if y <= 0.0:
        return 0.0
    ysw, ymeet, yinf = pts["ysw"], pts["ymeet"], pts["yinf"]
    if y <= ysw:
        return pts["gp0"] * y
    if y <= ymeet:
        return pts["gmin"]
    if y <= yinf:
        return pts["ginf"] + pts["gpinf"] * (y - yinf)
    slope = (pts["g1"] - pts["ginf"]) / (1.0 - yinf)
    return pts["ginf"] + slope * (y - yinf)


def a_lo(y: float, pts: dict | None = None) -> float:
    """Comparison integrand ½ w g_lo. Not a()."""
    if pts is None:
        pts = envelope_points()
    return a_from_g(float(y), g_lo(y, pts))


def envelope_I01(pts: dict | None = None, n: int = 48) -> tuple[float, float, float, float, float]:
    """∫ a_lo on the four pieces. Returns (I1, I2, I3, I4, I_lo)."""
    if pts is None:
        pts = envelope_points()
    ysw, ymeet, yinf = pts["ysw"], pts["ymeet"], pts["yinf"]

    def alo(y: float) -> float:
        return a_lo(max(y, 1e-15), pts)

    i1 = gauss_on(alo, 1e-15, ysw, n)
    i2 = gauss_on(alo, ysw, ymeet, n)
    i3 = gauss_on(alo, ymeet, yinf, n)
    i4 = gauss_on(alo, yinf, 1.0, n)
    return i1, i2, i3, i4, i1 + i2 + i3 + i4


def step_is_taken() -> bool:
    return False


def run() -> dict:
    pts = envelope_points()
    i1, i2, i3, i4, i_lo = envelope_I01(pts)
    i_true = true_I01()
    gap = i_true - i_lo
    p = p_of_v()
    q_lo = CST + i_lo + I1L_LO - p
    closes = gap < WINDOW
    ymeet_ok = pts["ymin"] < pts["ymeet"] < pts["yinf"]
    kill = gap < WINDOW or gap >= 0.088 or not ymeet_ok
    return {
        "ymin": pts["ymin"],
        "yinf": pts["yinf"],
        "ysw": pts["ysw"],
        "ymeet": pts["ymeet"],
        "gmin": pts["gmin"],
        "g_prime_0": pts["gp0"],
        "g_prime_inf": pts["gpinf"],
        "g1": pts["g1"],
        "ginf": pts["ginf"],
        "I_true": i_true,
        "I_lo": i_lo,
        "I_lo_t0": i1,
        "I_lo_floor": i2,
        "I_lo_tinf": i3,
        "I_lo_chord": i4,
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
        "I_{[0,1]} three-tangent envelope; not Weil, not RH",
        flush=True,
    )
    data = run()
    print(
        f"  y_sw={data['ysw']:.4f}  y_meet={data['ymeet']:.4f}  "
        f"ymin={data['ymin']:.4f}  yinf={data['yinf']:.4f}",
        flush=True,
    )
    print(
        f"  I_true={data['I_true']:+.6f}  I_lo={data['I_lo']:+.6f}  "
        f"gap={data['gap']:+.6f}",
        flush=True,
    )
    print(
        f"  pieces t0={data['I_lo_t0']:+.4f}  "
        f"floor={data['I_lo_floor']:+.4f}  "
        f"tinf={data['I_lo_tinf']:+.4f}  "
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
        "av-I01-envelope.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
