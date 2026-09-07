#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""I_{[0,1]} N=4 linear mesh (chords) on the concave tail.

Well+rise as in av_I01_rise. Then broken chords on [y_inf, 1].
Integrate a_lo = ½ w g_lo. Not Weil.

    python code/av_I01_chord.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import a_from_g, g, gauss_on  # noqa: E402
from av_I01_mesh import N_MESH  # noqa: E402
from av_I01_rise import gppp_negative_on_convex, rise_points  # noqa: E402
from av_I01_rise import g_lo as rise_g_lo  # noqa: E402
from av_I01_switch import I1L_LO, WINDOW, true_I01  # noqa: E402
from av_enclose import CST, p_of_v  # noqa: E402
from av_gpp import g_pp  # noqa: E402

N_CHORD = 4
PARENT_GAP = 0.00315


def chord_points() -> dict:
    pts = dict(rise_points())
    yinf = pts["yinf"]
    cnodes = [yinf + (1.0 - yinf) * i / N_CHORD for i in range(N_CHORD + 1)]
    cg_at = [g(y) for y in cnodes]
    pts["cnodes"] = cnodes
    pts["cg_at"] = cg_at
    return pts


def chord_piece(y: float, i: int, pts: dict) -> float:
    a, b = pts["cnodes"][i], pts["cnodes"][i + 1]
    ga, gb = pts["cg_at"][i], pts["cg_at"][i + 1]
    return ga + (gb - ga) * (y - a) / (b - a)


def g_lo(y: float, pts: dict | None = None) -> float:
    if pts is None:
        pts = chord_points()
    y = float(y)
    yinf = pts["yinf"]
    if y <= yinf:
        return rise_g_lo(y, pts)
    span = 1.0 - yinf
    i = min(int((y - yinf) / (span / N_CHORD)), N_CHORD - 1)
    if y > pts["cnodes"][i + 1]:
        i = min(i + 1, N_CHORD - 1)
    return chord_piece(y, i, pts)


def a_lo(y: float, pts: dict | None = None) -> float:
    if pts is None:
        pts = chord_points()
    return a_from_g(float(y), g_lo(y, pts))


def gpp_negative_on_tail(pts: dict, n: int = 80) -> bool:
    yinf = pts["yinf"]
    if g_pp(yinf + 1e-9) >= 0.0 or g_pp(1.0) >= 0.0:
        return False
    for i in range(1, n):
        if g_pp(yinf + (1.0 - yinf) * i / n) >= 0.0:
            return False
    return True


def chord_I01(pts: dict | None = None, n: int = 48) -> tuple[float, list]:
    if pts is None:
        pts = chord_points()
    nodes, rnodes, cnodes = pts["nodes"], pts["rnodes"], pts["cnodes"]

    def alo(y: float) -> float:
        return a_lo(max(y, 1e-15), pts)

    pieces = [gauss_on(alo, 1e-15, nodes[1], n)]
    for i in range(1, N_MESH):
        pieces.append(gauss_on(alo, nodes[i], nodes[i + 1], n))
    for i in range(N_MESH):
        pieces.append(gauss_on(alo, rnodes[i], rnodes[i + 1], n))
    for i in range(N_CHORD):
        pieces.append(gauss_on(alo, cnodes[i], cnodes[i + 1], n))
    return sum(pieces), pieces


def step_is_taken() -> bool:
    return False


def run() -> dict:
    pts = chord_points()
    convex_ok = gppp_negative_on_convex(pts)
    tail_ok = gpp_negative_on_tail(pts)
    i_lo, pieces = chord_I01(pts)
    i_true = true_I01()
    gap = i_true - i_lo
    p = p_of_v()
    q_lo = CST + i_lo + I1L_LO - p
    closes = gap < WINDOW
    kill = (not convex_ok) or (not tail_ok) or gap >= PARENT_GAP
    return {
        "ymin": pts["ymin"],
        "yinf": pts["yinf"],
        "cnodes": pts["cnodes"],
        "gppp_negative": convex_ok,
        "gpp_negative_tail": tail_ok,
        "I_true": i_true,
        "I_lo": i_lo,
        "pieces": pieces,
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
    print("I_{[0,1]} N=4 chords on concave tail; not Weil, not RH", flush=True)
    data = run()
    print(
        f"  yinf={data['yinf']:.4f}  "
        f"cnodes={[round(x, 4) for x in data['cnodes']]}",
        flush=True,
    )
    print(
        f"  gppp_neg={data['gppp_negative']}  tail_neg={data['gpp_negative_tail']}  "
        f"I_true={data['I_true']:+.6f}  I_lo={data['I_lo']:+.6f}  "
        f"gap={data['gap']:+.6f}",
        flush=True,
    )
    print(f"  Q_lo={data['Q_lo']:+.4f}  closes={data['closes_window']}", flush=True)
    print(f"verdict={data['verdict']}", flush=True)
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "av-I01-chord.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
