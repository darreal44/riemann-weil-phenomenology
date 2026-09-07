#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""I_{[0,1]} uniform N=8 well+rise mesh, the named rate test.

q_i matches the 1-jet of g, m_i = g''(right). Tail parabolas
of tailq stay. Not leftover-adaptive. Not Weil.

    python code/av_I01_n8.py
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

N8 = 8
PARENT_GAP = 0.002793
PARENT_CAP = 0.00151


def leftover_cap(nodes: list[float]) -> float:
    """Σ leftover h³/6, leftover = g''(left)−g''(right)."""
    acc = 0.0
    for i in range(len(nodes) - 1):
        h = nodes[i + 1] - nodes[i]
        lo = g_pp(nodes[i]) - g_pp(nodes[i + 1])
        acc += lo * (h ** 3) / 6.0
    return acc


def n8_points() -> dict:
    pts = dict(tailq_points())
    ymin, yinf = pts["ymin"], pts["yinf"]
    wnodes = [ymin * i / N8 for i in range(N8 + 1)]
    rnodes = [ymin + (yinf - ymin) * i / N8 for i in range(N8 + 1)]
    anodes = wnodes + rnodes[1:]
    pts["wnodes"] = wnodes
    pts["r8"] = rnodes
    pts["anodes"] = anodes
    pts["ag_at"] = [g(y) for y in anodes]
    pts["agp_at"] = [g_p(y) for y in anodes]
    pts["am_at"] = [g_pp(anodes[i + 1]) for i in range(len(anodes) - 1)]
    pts["cap"] = leftover_cap(anodes)
    pts["n8"] = N8
    return pts


def q_n8(y: float, i: int, pts: dict) -> float:
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
        pts = n8_points()
    y = float(y)
    if y <= 0.0:
        return 0.0
    yinf = pts["yinf"]
    if y <= yinf:
        return q_n8(y, _slab(y, pts["anodes"]), pts)
    return q_tail(y, _slab(y, pts["cnodes"]), pts)


def a_lo(y: float, pts: dict | None = None) -> float:
    if pts is None:
        pts = n8_points()
    return a_from_g(float(y), g_lo(y, pts))


def n8_I01(pts: dict | None = None, n: int = 48) -> tuple[float, list]:
    if pts is None:
        pts = n8_points()
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
    pts = n8_points()
    convex_ok = gppp_negative_on_convex(pts)
    i_lo, pieces = n8_I01(pts)
    i_true = true_I01()
    gap = i_true - i_lo
    q_lo = CST + i_lo + I1L_LO - p_of_v()
    cap = pts["cap"]
    cap_ratio = cap / PARENT_CAP
    kill = (not convex_ok) or gap >= PARENT_GAP or cap_ratio > 0.5
    return {
        "n8": N8,
        "ymin": pts["ymin"],
        "yinf": pts["yinf"],
        "anodes": pts["anodes"],
        "n_convex_slabs": len(pts["anodes"]) - 1,
        "cap": cap,
        "cap_ratio": cap_ratio,
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
    print("I_{[0,1]} uniform N=8 well+rise; not Weil, not RH", flush=True)
    data = run()
    print(
        f"  n_convex={data['n_convex_slabs']}  "
        f"cap={data['cap']:.6f}  cap_ratio={data['cap_ratio']:.3f}",
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
        "av-I01-n8.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
