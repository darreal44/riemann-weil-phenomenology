#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Chebyshev a^{(6)} of the odd integrand on [0,1].

    python3 code/av_a6_odd.py
"""
from __future__ import annotations

import os
import sys

import numpy as np
from numpy.polynomial.chebyshev import Chebyshev

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_enclose_odd import a_odd  # noqa: E402
from av_gauss import GAUSS3_REMAINDER_COEFF, GAUSS_NODES  # noqa: E402


def cheb_fit(N=24):
    k = np.arange(N + 1)
    x = np.cos(np.pi * k / N)
    y = 0.5 * (x + 1.0)
    vals = np.array([a_odd(float(yy) if yy > 1e-14 else 1e-12) for yy in y])
    return Chebyshev.fit(y, vals, deg=N, domain=[0.0, 1.0])


def report(N=24):
    c = cheb_fit(N)
    c6 = c.deriv(6)
    ys = np.linspace(0.05, 1.0, 400)
    v = np.abs(c6(ys))
    m = float(v.max())
    ym = float(ys[int(v.argmax())])
    print(f"odd N={N} max|a^(6)|[0.05,1]={m:.4e} at y={ym:.3f}")
    print(f"remainder coeff*M = {GAUSS3_REMAINDER_COEFF * m:.4e}")
    print("a6 at Gauss nodes", [float(c6(y)) for y in GAUSS_NODES])
    return m


if __name__ == "__main__":
    for N in (16, 24, 32):
        report(N)
