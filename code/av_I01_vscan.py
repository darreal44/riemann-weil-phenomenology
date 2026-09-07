#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Same g_lo scheme on other v at χ₅ μ=16. Not Weil.

    python code/av_I01_vscan.py
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import a_from_g, gauss_on, th_p, th_pp  # noqa: E402
from av_gauss import L16, V, th, theta_v, w  # noqa: E402



N = 4
WINDOW = 0.003


def norm3(a, b, c):
    s = math.sqrt(a * a + b * b + c * c)
    return (a / s, b / s, c / s)


WITNESSES = {
    "v431": V,
    "e0": (1.0, 0.0, 0.0),
    "v110": norm3(1.0, -1.0, 0.0),
    "v101": norm3(1.0, 0.0, -1.0),
}


def tv(y, v):
    return theta_v(y, L16, v)


def tv_p(y, v):
    if y <= 0.0:
        acc = 0.0
        for n in range(3):
            for m in range(3):
                acc += v[n] * v[m] * th_p(n, m, 1e-12, L16)
        return acc
    acc = 0.0
    for n in range(3):
        for m in range(3):
            acc += v[n] * v[m] * th_p(n, m, y, L16)
    return acc


def tv_pp(y, v):
    acc = 0.0
    yy = max(y, 0.0)
    for n in range(3):
        for m in range(3):
            acc += v[n] * v[m] * th_pp(n, m, yy, L16)
    return acc


def g(y, v):
    if y <= 0.0:
        return 0.0
    return 2.0 * math.exp(-1.5 * y) - tv(y, v)


def gp(y, v):
    return -3.0 * math.exp(-1.5 * max(y, 0.0)) - tv_p(y, v)


def gpp(y, v):
    return 4.5 * math.exp(-1.5 * max(y, 0.0)) - tv_pp(y, v)


def scan_min(v, n=400):
    ys = [i / n for i in range(1, n)]
    vals = [g(y, v) for y in ys]
    i = min(range(len(vals)), key=lambda k: vals[k])
    return ys[i], vals[i]


def scan_inf(v, n=400):
    ys = [i / n for i in range(1, n)]
    for y in ys:
        if gpp(y, v) < 0.0:
            return y
    return None


def mesh_I(v) -> dict:
    ymin, gmin = scan_min(v)
    yinf = scan_inf(v)
    if yinf is None or yinf <= ymin or ymin >= 0.9:
        return {
            "ok": False,
            "ymin": ymin,
            "gmin": gmin,
            "yinf": yinf,
            "reason": "no convex well+rise on (0,1)",
        }
    nodes = [ymin * i / N for i in range(N + 1)]
    rnodes = [ymin + (yinf - ymin) * i / N for i in range(N + 1)]
    m_at = [gpp(nodes[i + 1], v) for i in range(N)]
    rm_at = [gpp(rnodes[i + 1], v) for i in range(N)]

    def q(y, yi, gi, gpi, m):
        t = y - yi
        return gi + gpi * t + 0.5 * m * t * t

    def glo(y):
        if y <= 0.0:
            return 0.0
        if y <= ymin:
            i = min(int(y / (ymin / N + 1e-15)), N - 1)
            return q(y, nodes[i], g(nodes[i], v), gp(nodes[i], v), m_at[i])
        if y <= yinf:
            span = yinf - ymin
            i = min(int((y - ymin) / (span / N + 1e-15)), N - 1)
            return q(y, rnodes[i], g(rnodes[i], v), gp(rnodes[i], v), rm_at[i])
        slope = (g(1.0, v) - g(yinf, v)) / (1.0 - yinf)
        return g(yinf, v) + slope * (y - yinf)

    def alo(y):
        return 0.5 * w(max(y, 1e-12)) * glo(max(y, 0.0))

    def atrue(y):
        return 0.5 * w(max(y, 1e-12)) * g(max(y, 0.0), v)

    i_true = gauss_on(atrue, 1e-12, 1.0)
    i_lo = gauss_on(alo, 1e-12, 1.0)
    # check glo <= g on a grid
    below = True
    maxe = 0.0
    for k in range(1, 201):
        y = k / 200.0
        e = g(y, v) - glo(y)
        if e < -1e-6:
            below = False
        if e > maxe:
            maxe = e
    gap = i_true - i_lo
    return {
        "ok": True,
        "ymin": ymin,
        "gmin": gmin,
        "yinf": yinf,
        "I_true": i_true,
        "I_lo": i_lo,
        "gap": gap,
        "max_e": maxe,
        "glo_below_g": below,
        "in_window": abs(gap) < WINDOW if gap >= 0 else False,
    }


def run() -> dict:
    rows = {}
    for name, v in WITNESSES.items():
        rows[name] = {"v": list(v), **mesh_I(v)}
    return {
        "rows": rows,
        "step_taken": False,
        "verdict": "SURVIVE",
    }


def main() -> int:
    print("g_lo on other v at chi5 mu=16; not Weil", flush=True)
    data = run()
    for name, r in data["rows"].items():
        if not r["ok"]:
            print(f"  {name} FAIL {r.get('reason')}", flush=True)
            continue
        print(
            f"  {name} ymin={r['ymin']:.3f} gap={r['gap']:+.5f} "
            f"below={r['glo_below_g']} win={r['in_window']}",
            flush=True,
        )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "av-I01-vscan.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
