#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""I_{[0,1]} quadratic support near 0, not another global tangent.

g = 2 e^{−3y/2} − θ_v. If g'''<0 on [0, y_min] then inf g'' =
g''(y_min)=m, so g(y) ≥ g'(0) y + (m/2) y² on that interval.
Then floor / tinf / chord as in the three-tangent envelope.
Integrate a_lo = ½ w g_lo. Not Weil. Not RH.

    python code/av_I01_quad.py
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import a_from_g, g, gauss_on  # noqa: E402
from av_I01_envelope import envelope_points  # noqa: E402
from av_I01_switch import I1L_LO, WINDOW, true_I01  # noqa: E402
from av_enclose import CST, p_of_v  # noqa: E402
from av_gpp import g_pp, g_ppp  # noqa: E402


def quad_points() -> dict:
    """Envelope points plus m = g''(y_min) and the q/floor meeting y_q."""
    pts = dict(envelope_points())
    m = g_pp(pts["ymin"])
    gp0, gmin = pts["gp0"], pts["gmin"]
    a, b, c = 0.5 * m, gp0, -gmin
    disc = b * b - 4.0 * a * c
    yq = (-b - math.sqrt(disc)) / (2.0 * a)
    pts["m"] = m
    pts["disc"] = disc
    pts["yq"] = yq
    return pts


def q_of(y: float, pts: dict) -> float:
    """Quadratic under-estimator g'(0) y + (m/2) y²."""
    return pts["gp0"] * y + 0.5 * pts["m"] * y * y


def g_lo(y: float, pts: dict | None = None) -> float:
    """Lower comparison: q / floor / tinf / chord."""
    if pts is None:
        pts = quad_points()
    y = float(y)
    if y <= 0.0:
        return 0.0
    yq, ymeet, yinf = pts["yq"], pts["ymeet"], pts["yinf"]
    if y <= yq:
        return q_of(y, pts)
    if y <= ymeet:
        return pts["gmin"]
    if y <= yinf:
        return pts["ginf"] + pts["gpinf"] * (y - yinf)
    slope = (pts["g1"] - pts["ginf"]) / (1.0 - yinf)
    return pts["ginf"] + slope * (y - yinf)


def a_lo(y: float, pts: dict | None = None) -> float:
    """Comparison integrand ½ w g_lo. Not a()."""
    if pts is None:
        pts = quad_points()
    return a_from_g(float(y), g_lo(y, pts))


def gppp_negative_on_well(pts: dict, n: int = 80) -> bool:
    """g'''<0 on [0, y_min] by evaluations of the shipped elementary g_ppp."""
    ymin = pts["ymin"]
    if g_ppp(0.0) >= 0.0 or g_ppp(ymin) >= 0.0:
        return False
    for i in range(1, n):
        if g_ppp(ymin * i / n) >= 0.0:
            return False
    return True


def quad_I01(pts: dict | None = None, n: int = 48) -> tuple[float, float, float, float, float]:
    """∫ a_lo on the four pieces. Returns (I1, I2, I3, I4, I_lo)."""
    if pts is None:
        pts = quad_points()
    yq, ymeet, yinf = pts["yq"], pts["ymeet"], pts["yinf"]

    def alo(y: float) -> float:
        return a_lo(max(y, 1e-15), pts)

    i1 = gauss_on(alo, 1e-15, yq, n)
    i2 = gauss_on(alo, yq, ymeet, n)
    i3 = gauss_on(alo, ymeet, yinf, n)
    i4 = gauss_on(alo, yinf, 1.0, n)
    return i1, i2, i3, i4, i1 + i2 + i3 + i4


def step_is_taken() -> bool:
    return False


def run() -> dict:
    pts = quad_points()
    gppp_ok = gppp_negative_on_well(pts)
    i1, i2, i3, i4, i_lo = quad_I01(pts)
    i_true = true_I01()
    gap = i_true - i_lo
    p = p_of_v()
    q_lo = CST + i_lo + I1L_LO - p
    closes = gap < WINDOW
    yq_ok = pts["ysw"] < pts["yq"] < pts["ymin"]
    kill = (not gppp_ok) or (not yq_ok) or gap < WINDOW or gap >= 0.068
    return {
        "ymin": pts["ymin"],
        "yinf": pts["yinf"],
        "ysw": pts["ysw"],
        "ymeet": pts["ymeet"],
        "yq": pts["yq"],
        "m": pts["m"],
        "gmin": pts["gmin"],
        "g_prime_0": pts["gp0"],
        "g_prime_inf": pts["gpinf"],
        "g1": pts["g1"],
        "ginf": pts["ginf"],
        "gppp_negative": gppp_ok,
        "I_true": i_true,
        "I_lo": i_lo,
        "I_lo_q": i1,
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
        "I_{[0,1]} quadratic support near 0; not Weil, not RH",
        flush=True,
    )
    data = run()
    print(
        f"  y_q={data['yq']:.4f}  y_sw={data['ysw']:.4f}  "
        f"ymin={data['ymin']:.4f}  m={data['m']:+.4f}",
        flush=True,
    )
    print(
        f"  gppp_neg={data['gppp_negative']}  "
        f"I_true={data['I_true']:+.6f}  I_lo={data['I_lo']:+.6f}  "
        f"gap={data['gap']:+.6f}",
        flush=True,
    )
    print(
        f"  pieces q={data['I_lo_q']:+.4f}  "
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
        "av-I01-quad.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
