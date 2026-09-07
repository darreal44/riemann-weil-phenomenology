#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""I_{[0,1]} leftover-driven adaptive mesh on well+rise.

Split the slab with largest leftover = g''(left)−m_i.
Eight extra cuts (N=8 budget). Tail parabolas of tailq stay.
Not Kronrod on a. Not Weil.

    python code/av_I01_adapt.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import a_from_g, g, g_p, gauss_on  # noqa: E402
from av_I01_rise import gppp_negative_on_convex  # noqa: E402
from av_I01_switch import I1L_LO, WINDOW, true_I01  # noqa: E402
from av_I01_tailq import q_tail, tailq_points  # noqa: E402
from av_enclose import CST, p_of_v  # noqa: E402
from av_gpp import g_pp  # noqa: E402

N_EXTRA = 8
PARENT_GAP = 0.002793


def leftover(a: float, b: float) -> float:
    """g''(left) − m, m = g''(right). Positive while g'' decreases."""
    return g_pp(a) - g_pp(b)


def adapt_points() -> dict:
    """Uniform 4+4, then N_EXTRA leftover bisections on [0, y_inf]."""
    pts = dict(tailq_points())
    nodes = list(pts["nodes"]) + list(pts["rnodes"][1:])
    splits = []
    for _ in range(N_EXTRA):
        lefts = [leftover(nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)]
        i = max(range(len(lefts)), key=lambda k: lefts[k])
        mid = 0.5 * (nodes[i] + nodes[i + 1])
        splits.append(
            {
                "i": i,
                "lo": nodes[i],
                "hi": nodes[i + 1],
                "mid": mid,
                "leftover": lefts[i],
            }
        )
        nodes.insert(i + 1, mid)
    g_at = [g(y) for y in nodes]
    gp_at = [g_p(y) for y in nodes]
    m_at = [g_pp(nodes[i + 1]) for i in range(len(nodes) - 1)]
    lefts = [leftover(nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)]
    pts["anodes"] = nodes
    pts["ag_at"] = g_at
    pts["agp_at"] = gp_at
    pts["am_at"] = m_at
    pts["leftovers"] = lefts
    pts["splits"] = splits
    pts["n_extra"] = N_EXTRA
    return pts


def q_adapt(y: float, i: int, pts: dict) -> float:
    yi = pts["anodes"][i]
    t = y - yi
    return pts["ag_at"][i] + pts["agp_at"][i] * t + 0.5 * pts["am_at"][i] * t * t


def _slab(y: float, nodes: list[float]) -> int:
    if y <= nodes[0]:
        return 0
    for i in range(len(nodes) - 1):
        if y <= nodes[i + 1]:
            return i
    return len(nodes) - 2


def g_lo(y: float, pts: dict | None = None) -> float:
    if pts is None:
        pts = adapt_points()
    y = float(y)
    if y <= 0.0:
        return 0.0
    yinf = pts["yinf"]
    if y <= yinf:
        return q_adapt(y, _slab(y, pts["anodes"]), pts)
    cnodes = pts["cnodes"]
    i = _slab(y, cnodes)
    if y > cnodes[i + 1]:
        i = min(i + 1, len(cnodes) - 2)
    return q_tail(y, i, pts)


def a_lo(y: float, pts: dict | None = None) -> float:
    if pts is None:
        pts = adapt_points()
    return a_from_g(float(y), g_lo(y, pts))


def adapt_I01(pts: dict | None = None, n: int = 48) -> tuple[float, list]:
    if pts is None:
        pts = adapt_points()
    anodes, cnodes = pts["anodes"], pts["cnodes"]

    def alo(y: float) -> float:
        return a_lo(max(y, 1e-15), pts)

    pieces = [gauss_on(alo, 1e-15, anodes[1], n)]
    for i in range(1, len(anodes) - 1):
        pieces.append(gauss_on(alo, anodes[i], anodes[i + 1], n))
    for i in range(len(cnodes) - 1):
        pieces.append(gauss_on(alo, cnodes[i], cnodes[i + 1], n))
    return sum(pieces), pieces


def step_is_taken() -> bool:
    return False


def run() -> dict:
    pts = adapt_points()
    convex_ok = gppp_negative_on_convex(pts)
    i_lo, pieces = adapt_I01(pts)
    i_true = true_I01()
    gap = i_true - i_lo
    q_lo = CST + i_lo + I1L_LO - p_of_v()
    kill = (not convex_ok) or gap >= PARENT_GAP
    return {
        "ymin": pts["ymin"],
        "yinf": pts["yinf"],
        "anodes": pts["anodes"],
        "leftovers": pts["leftovers"],
        "splits": pts["splits"],
        "n_extra": N_EXTRA,
        "n_convex_slabs": len(pts["anodes"]) - 1,
        "gppp_negative": convex_ok,
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
    print(
        "I_{[0,1]} leftover-driven adaptive mesh; not Weil, not RH",
        flush=True,
    )
    data = run()
    print(
        f"  n_extra={data['n_extra']}  n_convex={data['n_convex_slabs']}  "
        f"anodes={[round(x, 4) for x in data['anodes']]}",
        flush=True,
    )
    print(
        f"  leftovers={[round(x, 3) for x in data['leftovers']]}",
        flush=True,
    )
    print(
        f"  I_true={data['I_true']:+.6f}  I_lo={data['I_lo']:+.6f}  "
        f"gap={data['gap']:+.6f}  Q_lo={data['Q_lo']:+.4f}  "
        f"closes={data['closes_window']}",
        flush=True,
    )
    print(f"verdict={data['verdict']}", flush=True)
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "av-I01-adapt.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
