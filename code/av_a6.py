#!/usr/bin/env python3
"""Chebyshev a^{(6)} of the even integrand on [0,1].

    python3 code/av_a6.py
"""
from __future__ import annotations
import numpy as np
from numpy.polynomial.chebyshev import Chebyshev
from av_gauss import a_integrand, GAUSS3_REMAINDER_COEFF, GAUSS_NODES


def a(y):
    y = float(y)
    return a_integrand(1e-12 if y <= 1e-14 else y)


def cheb_fit(N=24):
    k = np.arange(N + 1)
    x = np.cos(np.pi * k / N)
    y = 0.5 * (x + 1.0)
    vals = np.array([a(yy) for yy in y])
    return Chebyshev.fit(y, vals, deg=N, domain=[0.0, 1.0])


def report(N=24):
    c = cheb_fit(N)
    c6 = c.deriv(6)
    ys = np.linspace(0.05, 1.0, 400)
    v = np.abs(c6(ys))
    m = float(v.max())
    ym = float(ys[int(v.argmax())])
    print(f"N={N} max|a^(6)|[{0.05},1]={m:.4e} at y={ym:.3f}")
    print(f"remainder coeff*M = {GAUSS3_REMAINDER_COEFF * m:.4e}")
    print("a6 at Gauss nodes", [float(c6(y)) for y in GAUSS_NODES])
    print("tail |cheb coeff|", np.abs(c.coef[-6:]))
    return m


if __name__ == "__main__":
    for N in (16, 24, 32):
        report(N)
