#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""I_{[0,1]} N=4 quadratic mesh, not N=1 (#83).

Uniform nodes on [0, y_min]. On each slab, m_i = g''(right
end) and q_i matches the 1-jet of g at the left end.
Then floor / tinf / chord. Integrate a_lo = ½ w g_lo.
Not Weil. Not RH.

    python code/av_I01_mesh.py
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import a_from_g, g, g_p, gauss_on  # noqa: E402
from av_I01_envelope import envelope_points  # noqa: E402
from av_I01_quad import gppp_negative_on_well  # noqa: E402
from av_I01_switch import I1L_LO, WINDOW, true_I01  # noqa: E402
from av_enclose import CST, p_of_v  # noqa: E402
from av_gpp import g_pp  # noqa: E402

N_MESH = 4


def mesh_points() -> dict:
    """Uniform N=4 nodes on [0, y_min] plus envelope points."""
    pts = dict(envelope_points())
    ymin = pts["ymin"]
    nodes = [ymin * i / N_MESH for i in range(N_MESH + 1)]
    g_at = [g(y) for y in nodes]
    gp_at = [g_p(y) for y in nodes]
    m_at = [g_pp(nodes[i + 1]) for i in range(N_MESH)]
    pts["nodes"] = nodes
    pts["g_at"] = g_at
    pts["gp_at"] = gp_at
    pts["m_at"] = m_at
    pts["n_mesh"] = N_MESH
    return pts


def q_piece(y: float, i: int, pts: dict) -> float:
    yi = pts["nodes"][i]
    t = y - yi
    return pts["g_at"][i] + pts["gp_at"][i] * t + 0.5 * pts["m_at"][i] * t * t


def g_lo(y: float, pts: dict | None = None) -> float:
    """Broken parabolas on [0, y_min], then floor / tinf / chord."""
    if pts is None:
        pts = mesh_points()
    y = float(y)
    if y <= 0.0:
        return 0.0
    nodes = pts["nodes"]
    ymin, ymeet, yinf = pts["ymin"], pts["ymeet"], pts["yinf"]
    if y <= ymin:
        i = min(int(y / (ymin / N_MESH)), N_MESH - 1)
        if y > nodes[i + 1]:
            i = min(i + 1, N_MESH - 1)
        return q_piece(y, i, pts)
    if y <= ymeet:
        return pts["gmin"]
    if y <= yinf:
        return pts["ginf"] + pts["gpinf"] * (y - yinf)
    slope = (pts["g1"] - pts["ginf"]) / (1.0 - yinf)
    return pts["ginf"] + slope * (y - yinf)


def a_lo(y: float, pts: dict | None = None) -> float:
    if pts is None:
        pts = mesh_points()
    return a_from_g(float(y), g_lo(y, pts))


def mesh_I01(pts: dict | None = None, n: int = 48) -> tuple[float, float]:
    """∫ a_lo on mesh slabs plus tail pieces. Returns (I_lo, piece list)."""
    if pts is None:
        pts = mesh_points()
    nodes = pts["nodes"]
    ymeet, yinf = pts["ymeet"], pts["yinf"]

    def alo(y: float) -> float:
        return a_lo(max(y, 1e-15), pts)

    pieces = []
    pieces.append(gauss_on(alo, 1e-15, nodes[1], n))
    for i in range(1, N_MESH):
        pieces.append(gauss_on(alo, nodes[i], nodes[i + 1], n))
    pieces.append(gauss_on(alo, nodes[-1], ymeet, n))
    pieces.append(gauss_on(alo, ymeet, yinf, n))
    pieces.append(gauss_on(alo, yinf, 1.0, n))
    return sum(pieces), pieces


def step_is_taken() -> bool:
    return False


def run() -> dict:
    pts = mesh_points()
    gppp_ok = gppp_negative_on_well(pts)
    i_lo, pieces = mesh_I01(pts)
    i_true = true_I01()
    gap = i_true - i_lo
    p = p_of_v()
    q_lo = CST + i_lo + I1L_LO - p
    closes = gap < WINDOW
    kill = (not gppp_ok) or gap < WINDOW or gap >= 0.047
    return {
        "n_mesh": N_MESH,
        "ymin": pts["ymin"],
        "yinf": pts["yinf"],
        "ymeet": pts["ymeet"],
        "nodes": pts["nodes"],
        "m_at": pts["m_at"],
        "gmin": pts["gmin"],
        "g_prime_0": pts["gp0"],
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
        "I_{[0,1]} N=4 quadratic mesh; not Weil, not RH",
        flush=True,
    )
    data = run()
    print(
        f"  N={data['n_mesh']}  ymin={data['ymin']:.4f}  "
        f"nodes={[round(x, 4) for x in data['nodes']]}",
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
        "av-I01-mesh.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
