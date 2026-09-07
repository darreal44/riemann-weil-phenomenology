#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""I_{[0,1]} N=4 mesh on the convex rise [y_min, y_inf], drop the floor.

Well mesh as in av_I01_mesh. Then broken parabolas through the
rise. Chord after y_inf. Integrate a_lo = ½ w g_lo. Not Weil.

    python code/av_I01_rise.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import a_from_g, g, g_p, gauss_on  # noqa: E402
from av_I01_mesh import N_MESH, mesh_points, q_piece  # noqa: E402
from av_I01_quad import gppp_negative_on_well  # noqa: E402
from av_I01_switch import I1L_LO, WINDOW, true_I01  # noqa: E402
from av_enclose import CST, p_of_v  # noqa: E402
from av_gpp import g_pp, g_ppp  # noqa: E402


def rise_points() -> dict:
    """Well mesh plus uniform N=4 nodes on [y_min, y_inf]."""
    pts = dict(mesh_points())
    ymin, yinf = pts["ymin"], pts["yinf"]
    rnodes = [ymin + (yinf - ymin) * i / N_MESH for i in range(N_MESH + 1)]
    rg_at = [g(y) for y in rnodes]
    rgp_at = [g_p(y) for y in rnodes]
    rm_at = [g_pp(rnodes[i + 1]) for i in range(N_MESH)]
    pts["rnodes"] = rnodes
    pts["rg_at"] = rg_at
    pts["rgp_at"] = rgp_at
    pts["rm_at"] = rm_at
    return pts


def q_rise(y: float, i: int, pts: dict) -> float:
    yi = pts["rnodes"][i]
    t = y - yi
    return pts["rg_at"][i] + pts["rgp_at"][i] * t + 0.5 * pts["rm_at"][i] * t * t


def g_lo(y: float, pts: dict | None = None) -> float:
    """Well mesh, then rise mesh, then chord."""
    if pts is None:
        pts = rise_points()
    y = float(y)
    if y <= 0.0:
        return 0.0
    ymin, yinf = pts["ymin"], pts["yinf"]
    if y <= ymin:
        i = min(int(y / (ymin / N_MESH)), N_MESH - 1)
        return q_piece(y, i, pts)
    if y <= yinf:
        span = yinf - ymin
        i = min(int((y - ymin) / (span / N_MESH)), N_MESH - 1)
        return q_rise(y, i, pts)
    slope = (pts["g1"] - pts["ginf"]) / (1.0 - yinf)
    return pts["ginf"] + slope * (y - yinf)


def a_lo(y: float, pts: dict | None = None) -> float:
    if pts is None:
        pts = rise_points()
    return a_from_g(float(y), g_lo(y, pts))


def gppp_negative_on_convex(pts: dict, n: int = 80) -> bool:
    if not gppp_negative_on_well(pts, n):
        return False
    yinf = pts["yinf"]
    if g_ppp(yinf) >= 0.0:
        return False
    ymin = pts["ymin"]
    for i in range(1, n):
        if g_ppp(ymin + (yinf - ymin) * i / n) >= 0.0:
            return False
    return True


def rise_I01(pts: dict | None = None, n: int = 48) -> tuple[float, list]:
    if pts is None:
        pts = rise_points()
    nodes, rnodes = pts["nodes"], pts["rnodes"]
    yinf = pts["yinf"]

    def alo(y: float) -> float:
        return a_lo(max(y, 1e-15), pts)

    pieces = [gauss_on(alo, 1e-15, nodes[1], n)]
    for i in range(1, N_MESH):
        pieces.append(gauss_on(alo, nodes[i], nodes[i + 1], n))
    for i in range(N_MESH):
        pieces.append(gauss_on(alo, rnodes[i], rnodes[i + 1], n))
    pieces.append(gauss_on(alo, yinf, 1.0, n))
    return sum(pieces), pieces


def step_is_taken() -> bool:
    return False


def run() -> dict:
    pts = rise_points()
    gppp_ok = gppp_negative_on_convex(pts)
    i_lo, pieces = rise_I01(pts)
    i_true = true_I01()
    gap = i_true - i_lo
    p = p_of_v()
    q_lo = CST + i_lo + I1L_LO - p
    closes = gap < WINDOW
    kill = (not gppp_ok) or gap >= 0.0053
    return {
        "ymin": pts["ymin"],
        "yinf": pts["yinf"],
        "rnodes": pts["rnodes"],
        "rm_at": pts["rm_at"],
        "gmin": pts["gmin"],
        "gppp_negative": gppp_ok,
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
    print(
        "I_{[0,1]} mesh on convex rise; not Weil, not RH",
        flush=True,
    )
    data = run()
    print(
        f"  ymin={data['ymin']:.4f}  yinf={data['yinf']:.4f}  "
        f"rnodes={[round(x, 4) for x in data['rnodes']]}",
        flush=True,
    )
    print(
        f"  gppp_neg={data['gppp_negative']}  "
        f"I_true={data['I_true']:+.6f}  I_lo={data['I_lo']:+.6f}  "
        f"gap={data['gap']:+.6f}",
        flush=True,
    )
    print(f"  pieces={[round(x, 4) for x in data['pieces']]}", flush=True)
    print(
        f"  Q_lo={data['Q_lo']:+.4f}  closes={data['closes_window']}",
        flush=True,
    )
    print(f"verdict={data['verdict']}", flush=True)
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "av-I01-rise.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
