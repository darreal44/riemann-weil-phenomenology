#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""I_{[0,1]} two-piece quadratic on the well, not the single-m of #83.

g'''<0 ⇒ g'' decreases. Split at y_h = y_min/2. q1 with m1=g''(y_h)
on [0, y_h], then q2 with m2=g''(y_min) until the floor. Then
floor / tinf / chord. Integrate a_lo = ½ w g_lo. Not Weil. Not RH.

    python code/av_I01_quad2.py
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import a_from_g, gauss_on  # noqa: E402
from av_I01_envelope import envelope_points  # noqa: E402
from av_I01_quad import gppp_negative_on_well  # noqa: E402
from av_I01_switch import I1L_LO, WINDOW, true_I01  # noqa: E402
from av_enclose import CST, p_of_v  # noqa: E402
from av_gpp import g_pp  # noqa: E402


def split_points() -> dict:
    """Two-piece quadratic: y_h = y_min/2, then q2 meets the floor at y_q."""
    pts = dict(envelope_points())
    yh = 0.5 * pts["ymin"]
    m1 = g_pp(yh)
    m2 = g_pp(pts["ymin"])
    gp0, gmin = pts["gp0"], pts["gmin"]
    qh = gp0 * yh + 0.5 * m1 * yh * yh
    qhp = gp0 + m1 * yh
    a, b, c = 0.5 * m2, qhp, qh - gmin
    disc = b * b - 4.0 * a * c
    t = (-b - math.sqrt(disc)) / (2.0 * a)
    yq = yh + t
    pts["yh"] = yh
    pts["m1"] = m1
    pts["m2"] = m2
    pts["qh"] = qh
    pts["qhp"] = qhp
    pts["disc"] = disc
    pts["yq"] = yq
    return pts


def q1_of(y: float, pts: dict) -> float:
    return pts["gp0"] * y + 0.5 * pts["m1"] * y * y


def q2_of(y: float, pts: dict) -> float:
    t = y - pts["yh"]
    return pts["qh"] + pts["qhp"] * t + 0.5 * pts["m2"] * t * t


def g_lo(y: float, pts: dict | None = None) -> float:
    """Lower comparison: q1 / q2 / floor / tinf / chord."""
    if pts is None:
        pts = split_points()
    y = float(y)
    if y <= 0.0:
        return 0.0
    yh, yq, ymeet, yinf = pts["yh"], pts["yq"], pts["ymeet"], pts["yinf"]
    if y <= yh:
        return q1_of(y, pts)
    if y <= yq:
        return q2_of(y, pts)
    if y <= ymeet:
        return pts["gmin"]
    if y <= yinf:
        return pts["ginf"] + pts["gpinf"] * (y - yinf)
    slope = (pts["g1"] - pts["ginf"]) / (1.0 - yinf)
    return pts["ginf"] + slope * (y - yinf)


def a_lo(y: float, pts: dict | None = None) -> float:
    if pts is None:
        pts = split_points()
    return a_from_g(float(y), g_lo(y, pts))


def split_I01(pts: dict | None = None, n: int = 48) -> tuple[float, ...]:
    """∫ a_lo on the five pieces. Returns (I1..I5, I_lo)."""
    if pts is None:
        pts = split_points()
    yh, yq, ymeet, yinf = pts["yh"], pts["yq"], pts["ymeet"], pts["yinf"]

    def alo(y: float) -> float:
        return a_lo(max(y, 1e-15), pts)

    i1 = gauss_on(alo, 1e-15, yh, n)
    i2 = gauss_on(alo, yh, yq, n)
    i3 = gauss_on(alo, yq, ymeet, n)
    i4 = gauss_on(alo, ymeet, yinf, n)
    i5 = gauss_on(alo, yinf, 1.0, n)
    return i1, i2, i3, i4, i5, i1 + i2 + i3 + i4 + i5


def step_is_taken() -> bool:
    return False


def run() -> dict:
    pts = split_points()
    gppp_ok = gppp_negative_on_well(pts)
    i1, i2, i3, i4, i5, i_lo = split_I01(pts)
    i_true = true_I01()
    gap = i_true - i_lo
    p = p_of_v()
    q_lo = CST + i_lo + I1L_LO - p
    closes = gap < WINDOW
    yq_ok = pts["yh"] < pts["yq"] < pts["ymin"]
    kill = (not gppp_ok) or (not yq_ok) or gap < WINDOW or gap >= 0.047
    return {
        "ymin": pts["ymin"],
        "yinf": pts["yinf"],
        "yh": pts["yh"],
        "yq": pts["yq"],
        "ymeet": pts["ymeet"],
        "m1": pts["m1"],
        "m2": pts["m2"],
        "gmin": pts["gmin"],
        "g_prime_0": pts["gp0"],
        "g_prime_inf": pts["gpinf"],
        "g1": pts["g1"],
        "ginf": pts["ginf"],
        "gppp_negative": gppp_ok,
        "I_true": i_true,
        "I_lo": i_lo,
        "I_lo_q1": i1,
        "I_lo_q2": i2,
        "I_lo_floor": i3,
        "I_lo_tinf": i4,
        "I_lo_chord": i5,
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
        "I_{[0,1]} two-piece quadratic; not Weil, not RH",
        flush=True,
    )
    data = run()
    print(
        f"  y_h={data['yh']:.4f}  y_q={data['yq']:.4f}  "
        f"ymin={data['ymin']:.4f}  m1={data['m1']:+.4f}  m2={data['m2']:+.4f}",
        flush=True,
    )
    print(
        f"  gppp_neg={data['gppp_negative']}  "
        f"I_true={data['I_true']:+.6f}  I_lo={data['I_lo']:+.6f}  "
        f"gap={data['gap']:+.6f}",
        flush=True,
    )
    print(
        f"  pieces q1={data['I_lo_q1']:+.4f}  q2={data['I_lo_q2']:+.4f}  "
        f"floor={data['I_lo_floor']:+.4f}  tinf={data['I_lo_tinf']:+.4f}  "
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
        "av-I01-quad2.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
