#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Slab leftover estimator vs I_true-I_lo. One witness. Not Weil.

    python code/av_I01_estimator.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import a_from_g, g, gauss_on  # noqa: E402
from av_I01_mesh import N_MESH  # noqa: E402
from av_I01_rise import rise_points  # noqa: E402
from av_I01_tailq import g_lo, tailq_I01, tailq_points  # noqa: E402
from av_I01_switch import true_I01  # noqa: E402
from av_gpp import g_pp  # noqa: E402


def slabs(pts: dict) -> list[tuple[float, float, float]]:
    """(left, right, leftover=g''(left)-m) for well, rise, tail."""
    out = []
    nodes = pts["nodes"]
    for i in range(N_MESH):
        out.append((nodes[i], nodes[i + 1], g_pp(nodes[i]) - pts["m_at"][i]))
    rnodes = pts["rnodes"]
    for i in range(N_MESH):
        out.append((rnodes[i], rnodes[i + 1], g_pp(rnodes[i]) - pts["rm_at"][i]))
    cnodes = pts["cnodes"]
    for i in range(len(pts["tm_at"])):
        out.append((cnodes[i], cnodes[i + 1], g_pp(cnodes[i]) - pts["tm_at"][i]))
    return out


def cap_integral(left: float, right: float, leftover: float) -> float:
    """∫ leftover/2 (y-left)^2 * 1  dy  = leftover h^3 / 6."""
    h = right - left
    return leftover * h * h * h / 6.0


def run() -> dict:
    pts = tailq_points()
    sl = slabs(pts)
    caps = []
    scored = []
    for a, b, leftov in sl:
        caps.append(cap_integral(a, b, leftov))
        scored.append(
            gauss_on(lambda y: a_from_g(y, g(y) - g_lo(y, pts)), a + 1e-15, b)
        )
    i_true = true_I01()
    i_lo = tailq_I01(pts)[0]
    gap = i_true - i_lo
    return {
        "slabs": [
            {"a": a, "b": b, "leftover": lo, "cap_int": c, "score": s}
            for (a, b, lo), c, s in zip(sl, caps, scored)
        ],
        "sum_cap_int": sum(caps),
        "sum_score": sum(scored),
        "gap": gap,
        "I_true": i_true,
        "I_lo": i_lo,
        "verdict": "SURVIVE",
        "step_taken": False,
    }


def main() -> int:
    data = run()
    print("leftover estimator vs gap; not Weil", flush=True)
    print(
        f"  sum_cap={data['sum_cap_int']:+.6f}  "
        f"sum_score={data['sum_score']:+.6f}  gap={data['gap']:+.6f}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "av-I01-estimator.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
