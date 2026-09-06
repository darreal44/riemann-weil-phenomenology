#!/usr/bin/env python3
"""Second derivative of g = 2 e^{-3y/2} − θ_v on [1, y*].

    python3 code/av_gpp.py
"""
from __future__ import annotations
import math
from av_gauss import L16, V, theta_v, th


def th_pp(n, m, y, L=L16):
    om = lambda k: 2.0 * math.pi * k / L
    if n == 0 and m == 0:
        return 0.0
    if n == 0 or m == 0:
        j = max(n, m)
        return 2.0 * (om(j) ** 2) * math.sin(om(j) * y) / (math.sqrt(2.0) * math.pi * j)
    if n == m:
        w = om(n)
        u = (L - y) / L
        return 2.0 * (
            (2.0 * w / L) * math.sin(w * y)
            - u * (w ** 2) * math.cos(w * y)
            + (w ** 2) * math.sin(w * y) / (2.0 * math.pi * n)
        )
    return (
        2.0
        * (
            -n * (om(n) ** 2) * math.sin(om(n) * y)
            + m * (om(m) ** 2) * math.sin(om(m) * y)
        )
        / (math.pi * (m * m - n * n))
    )


def theta_v_pp(y, L=L16, v=V):
    acc = 0.0
    for n in range(3):
        for m in range(3):
            acc += v[n] * v[m] * th_pp(n, m, y, L)
    return acc


def g_pp(y, L=L16, v=V):
    return 4.5 * math.exp(-1.5 * y) - theta_v_pp(y, L, v)


def range_on(a, b, n=400):
    h = (b - a) / n
    vals = [g_pp(a + i * h) for i in range(n + 1)]
    return min(vals), max(vals)


if __name__ == "__main__":
    mn, mx = range_on(1.0, 1.59)
    print(f"g'' on [1, 1.59]: [{mn:.4f}, {mx:.4f}]")
    print(f"theta_v''(1.2)={theta_v_pp(1.2):.4f}  g''(1.2)={g_pp(1.2):.4f}")
