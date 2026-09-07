#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""g_lo at s₀=3/4 (odd Bose), same v, μ=16. Not another v on χ₅.

    g = 2 e^{−y/2} − θ_v
    w = 2 e^{−3y/2}/(1−e^{−2y})

If the convex well dies, g_lo is an even/χ₅ artefact. Not Weil.

    python code/av_I01_odd.py
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import gauss_on, theta_v_p, theta_v_pp  # noqa: E402
from av_I01_vscan import N, WINDOW  # noqa: E402
from av_gauss import V, theta_v  # noqa: E402
from av_odd_app import g_odd, g_odd_pp, w_odd  # noqa: E402


def g(y: float) -> float:
    if y <= 0.0:
        return 0.0
    return g_odd(y)


def gp(y: float) -> float:
    yy = max(y, 0.0)
    return -math.exp(-0.5 * yy) - theta_v_p(yy)


def gpp(y: float) -> float:
    return g_odd_pp(y)


def a_true(y: float) -> float:
    yy = max(y, 1e-12)
    return 0.5 * w_odd(yy) * g(yy)


def scan_min(n: int = 400) -> tuple[float, float]:
    ys = [i / n for i in range(1, n)]
    vals = [g(y) for y in ys]
    i = min(range(len(vals)), key=lambda k: vals[k])
    return ys[i], vals[i]


def scan_inf(n: int = 400):
    ys = [i / n for i in range(1, n)]
    for y in ys:
        if gpp(y) < 0.0:
            return y
    return None


def mesh_I() -> dict:
    ymin, gmin = scan_min()
    yinf = scan_inf()
    gp0 = gp(0.0)
    gpp0 = gpp(0.0)
    if yinf is None or yinf <= ymin or ymin >= 0.9 or gpp0 <= 0.0:
        return {
            "ok": False,
            "ymin": ymin,
            "gmin": gmin,
            "yinf": yinf,
            "gp0": gp0,
            "gpp0": gpp0,
            "reason": "no convex well+rise on (0,1)",
        }
    nodes = [ymin * i / N for i in range(N + 1)]
    rnodes = [ymin + (yinf - ymin) * i / N for i in range(N + 1)]
    m_at = [gpp(nodes[i + 1]) for i in range(N)]
    rm_at = [gpp(rnodes[i + 1]) for i in range(N)]

    def q(y, yi, gi, gpi, m):
        t = y - yi
        return gi + gpi * t + 0.5 * m * t * t

    def glo(y):
        if y <= 0.0:
            return 0.0
        if y <= ymin:
            i = min(int(y / (ymin / N + 1e-15)), N - 1)
            return q(y, nodes[i], g(nodes[i]), gp(nodes[i]), m_at[i])
        if y <= yinf:
            span = yinf - ymin
            i = min(int((y - ymin) / (span / N + 1e-15)), N - 1)
            return q(y, rnodes[i], g(rnodes[i]), gp(rnodes[i]), rm_at[i])
        slope = (g(1.0) - g(yinf)) / (1.0 - yinf)
        return g(yinf) + slope * (y - yinf)

    def alo(y):
        return 0.5 * w_odd(max(y, 1e-12)) * glo(max(y, 0.0))

    i_true = gauss_on(a_true, 1e-12, 1.0)
    i_lo = gauss_on(alo, 1e-12, 1.0)
    below = True
    for k in range(1, 201):
        yy = k / 200.0
        if glo(yy) > g(yy) + 1e-6:
            below = False
    gap = i_true - i_lo
    return {
        "ok": True,
        "ymin": ymin,
        "gmin": gmin,
        "yinf": yinf,
        "gp0": gp0,
        "gpp0": gpp0,
        "I_true": i_true,
        "I_lo": i_lo,
        "gap": gap,
        "glo_below_g": below,
        "in_window": bool(gap >= 0.0 and gap < WINDOW),
        "g_lo": glo,
        "a_lo": alo,
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    row = mesh_I()
    # χ does not enter g; s₀ does. Same g for every odd χ at this v, L.
    kill = (not row["ok"]) or (row.get("glo_below_g") is False)
    out = {k: v for k, v in row.items() if k not in ("g_lo", "a_lo")}
    out.update(
        {
            "s0": 0.75,
            "chi": "chi3",
            "v": list(V),
            "step_taken": step_is_taken(),
            "verdict": "KILL" if kill else "SURVIVE",
            "artefact": (not row["ok"]),
        }
    )
    return out


def main() -> int:
    print("g_lo at s0=3/4 odd Bose, same v mu=16; not Weil", flush=True)
    data = run()
    if not data.get("ok"):
        print(f"  WELL DEAD  {data.get('reason')}  artefact={data['artefact']}", flush=True)
    else:
        print(
            f"  ymin={data['ymin']:.4f}  yinf={data['yinf']:.4f}  "
            f"gp0={data['gp0']:+.3f}  gpp0={data['gpp0']:+.3f}",
            flush=True,
        )
        print(
            f"  I_true={data['I_true']:+.6f}  I_lo={data['I_lo']:+.6f}  "
            f"gap={data['gap']:+.6f}  win={data['in_window']}",
            flush=True,
        )
    print(f"verdict={data['verdict']}", flush=True)
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "av-I01-odd.json",
    )
    clean = {k: v for k, v in data.items() if k not in ("g_lo", "a_lo")}
    with open(out, "w", encoding="utf-8") as f:
        json.dump(clean, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
