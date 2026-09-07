#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""I_{[0,1]} N=4 supporting parabolas on the concave tail.

m_i = inf g'' = g''(right end) (g'''<0, g'' decreases).
Same 1-jet scheme as the well. Parent is the N=4 chords (#chord).
Not Weil.

    python code/av_I01_tailq.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_chord import N_CHORD, chord_points, gpp_negative_on_tail  # noqa: E402
from av_I01_compare import a_from_g, g, g_p, gauss_on  # noqa: E402
from av_I01_mesh import N_MESH  # noqa: E402
from av_I01_rise import g_lo as rise_g_lo  # noqa: E402
from av_I01_rise import gppp_negative_on_convex  # noqa: E402
from av_I01_switch import I1L_LO, WINDOW, true_I01  # noqa: E402
from av_enclose import CST, p_of_v  # noqa: E402
from av_gpp import g_pp  # noqa: E402

PARENT_GAP = 0.002802


def tailq_points() -> dict:
    pts = dict(chord_points())
    cnodes = pts["cnodes"]
    pts["tg_at"] = [g(y) for y in cnodes]
    pts["tgp_at"] = [g_p(y) for y in cnodes]
    pts["tm_at"] = [g_pp(cnodes[i + 1]) for i in range(N_CHORD)]
    return pts


def q_tail(y: float, i: int, pts: dict) -> float:
    yi = pts["cnodes"][i]
    t = y - yi
    return pts["tg_at"][i] + pts["tgp_at"][i] * t + 0.5 * pts["tm_at"][i] * t * t


def g_lo(y: float, pts: dict | None = None) -> float:
    if pts is None:
        pts = tailq_points()
    y = float(y)
    yinf = pts["yinf"]
    if y <= yinf:
        return rise_g_lo(y, pts)
    span = 1.0 - yinf
    i = min(int((y - yinf) / (span / N_CHORD)), N_CHORD - 1)
    if y > pts["cnodes"][i + 1]:
        i = min(i + 1, N_CHORD - 1)
    return q_tail(y, i, pts)


def a_lo(y: float, pts: dict | None = None) -> float:
    if pts is None:
        pts = tailq_points()
    return a_from_g(float(y), g_lo(y, pts))


def tailq_I01(pts: dict | None = None, n: int = 48) -> tuple[float, list]:
    if pts is None:
        pts = tailq_points()
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
    pts = tailq_points()
    convex_ok = gppp_negative_on_convex(pts)
    tail_ok = gpp_negative_on_tail(pts)
    i_lo, pieces = tailq_I01(pts)
    i_true = true_I01()
    gap = i_true - i_lo
    q_lo = CST + i_lo + I1L_LO - p_of_v()
    kill = (not convex_ok) or (not tail_ok) or gap >= PARENT_GAP
    return {
        "ymin": pts["ymin"],
        "yinf": pts["yinf"],
        "cnodes": pts["cnodes"],
        "tm_at": pts["tm_at"],
        "gppp_negative": convex_ok,
        "gpp_negative_tail": tail_ok,
        "I_true": i_true,
        "I_lo": i_lo,
        "pieces": pieces,
        "gap": gap,
        "Q_lo": q_lo,
        "closes_window": gap < WINDOW,
        "step_taken": step_is_taken(),
        "verdict": "KILL" if kill else "SURVIVE",
    }


def main() -> int:
    print("I_{[0,1]} N=4 parabolas on concave tail; not Weil, not RH", flush=True)
    data = run()
    print(
        f"  tm_at={[round(x, 4) for x in data['tm_at']]}",
        flush=True,
    )
    print(
        f"  I_true={data['I_true']:+.6f}  I_lo={data['I_lo']:+.6f}  "
        f"gap={data['gap']:+.6f}  Q_lo={data['Q_lo']:+.4f}",
        flush=True,
    )
    print(f"verdict={data['verdict']}", flush=True)
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "av-I01-tailq.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
