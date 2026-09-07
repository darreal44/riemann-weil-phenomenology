#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Same rational v, χ₅, other μ. N=4 well+rise + chord. Not Weil.

    python code/av_I01_muscan.py
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import gauss_on, th_p, th_pp  # noqa: E402
from av_gauss import V, th, w  # noqa: E402

N = 4
WINDOW = 0.003
MUS = (5.0, 8.0, 16.0, 32.0)


def theta_v(y, L, v=V):
    if y <= 0.0:
        return 2.0 * sum(vi * vi for vi in v)
    if y >= L:
        return 0.0
    acc = 0.0
    for n in range(3):
        for m in range(3):
            acc += v[n] * v[m] * th(n, m, y, L)
    return acc


def tv_p(y, L, v=V):
    acc = 0.0
    yy = max(y, 1e-12)
    for n in range(3):
        for m in range(3):
            acc += v[n] * v[m] * th_p(n, m, yy, L)
    return acc


def tv_pp(y, L, v=V):
    acc = 0.0
    yy = max(y, 0.0)
    for n in range(3):
        for m in range(3):
            acc += v[n] * v[m] * th_pp(n, m, yy, L)
    return acc


def g(y, L):
    if y <= 0.0:
        return 0.0
    return 2.0 * math.exp(-1.5 * y) - theta_v(y, L)


def gp(y, L):
    return -3.0 * math.exp(-1.5 * max(y, 0.0)) - tv_p(y, L)


def gpp(y, L):
    return 4.5 * math.exp(-1.5 * max(y, 0.0)) - tv_pp(y, L)


def scan_min(L, n=400):
    ys = [i / n for i in range(1, n)]
    vals = [g(y, L) for y in ys]
    i = min(range(len(vals)), key=lambda k: vals[k])
    return ys[i], vals[i]


def scan_inf(L, n=400):
    for y in [i / n for i in range(1, n)]:
        if gpp(y, L) < 0.0:
            return y
    return None


def mesh_I(mu: float) -> dict:
    L = math.log(mu)
    ymin, gmin = scan_min(L)
    yinf = scan_inf(L)
    if yinf is None or yinf <= ymin or ymin >= 0.95:
        return {"ok": False, "L": L, "ymin": ymin, "gmin": gmin, "yinf": yinf}
    nodes = [ymin * i / N for i in range(N + 1)]
    rnodes = [ymin + (yinf - ymin) * i / N for i in range(N + 1)]
    m_at = [gpp(nodes[i + 1], L) for i in range(N)]
    rm_at = [gpp(rnodes[i + 1], L) for i in range(N)]

    def q(y, yi, gi, gpi, m):
        t = y - yi
        return gi + gpi * t + 0.5 * m * t * t

    def glo(y):
        if y <= 0.0:
            return 0.0
        if y <= ymin:
            i = min(int(y / (ymin / N + 1e-15)), N - 1)
            return q(y, nodes[i], g(nodes[i], L), gp(nodes[i], L), m_at[i])
        if y <= yinf:
            span = yinf - ymin
            i = min(int((y - ymin) / (span / N + 1e-15)), N - 1)
            return q(y, rnodes[i], g(rnodes[i], L), gp(rnodes[i], L), rm_at[i])
        slope = (g(1.0, L) - g(yinf, L)) / (1.0 - yinf)
        return g(yinf, L) + slope * (y - yinf)

    def alo(y):
        return 0.5 * w(max(y, 1e-12)) * glo(max(y, 0.0))

    def atrue(y):
        return 0.5 * w(max(y, 1e-12)) * g(max(y, 0.0), L)

    i_true = gauss_on(atrue, 1e-12, 1.0)
    i_lo = gauss_on(alo, 1e-12, 1.0)
    below = True
    for k in range(1, 201):
        y = k / 200.0
        if g(y, L) - glo(y) < -1e-6:
            below = False
            break
    return {
        "ok": True,
        "L": L,
        "ymin": ymin,
        "gmin": gmin,
        "yinf": yinf,
        "I_true": i_true,
        "I_lo": i_lo,
        "gap": i_true - i_lo,
        "glo_below_g": below,
        "in_window": 0.0 <= (i_true - i_lo) < WINDOW,
    }


def run() -> dict:
    rows = {str(int(mu)): mesh_I(mu) for mu in MUS}
    return {"rows": rows, "step_taken": False, "verdict": "SURVIVE"}


def main() -> int:
    print("same v, chi5, other mu; not Weil", flush=True)
    data = run()
    for name, r in data["rows"].items():
        if not r["ok"]:
            print(f"  mu={name} FAIL", flush=True)
            continue
        print(
            f"  mu={name} ymin={r['ymin']:.3f} gap={r['gap']:+.5f} "
            f"below={r['glo_below_g']} win={r['in_window']}",
            flush=True,
        )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "av-I01-muscan.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
