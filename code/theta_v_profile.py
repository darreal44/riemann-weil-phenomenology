#!/usr/bin/env python3
"""Θ_v from the zero-Gram ground state, vs  y e^y.

    python3 code/theta_v_profile.py zeta 16 32
"""
from __future__ import annotations

import math
import os
import pickle
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def zeros(name):
    p = os.path.join(HERE, f"zeros_{name}_weyl.pkl")
    return np.array(sorted(float(x) for x in pickle.load(open(p, "rb"))))


def hat(g, L, om):
    s = np.sin(g * L / 2.0)
    v = np.empty_like(om)
    v[0] = 2 * s / (g * math.sqrt(L))
    v[1:] = math.sqrt(2 / L) * s * 2 * g / (g * g - om[1:] ** 2)
    return v


def theta_nm(n, m, y, L, om):
    if n == 0 and m == 0:
        return 2 * (L - y) / L
    if n == 0 or m == 0:
        j = max(n, m)
        return -2 * np.sin(om[j] * y) / (math.sqrt(2) * math.pi * j)
    if n == m:
        return 2 * ((L - y) * np.cos(om[n] * y) / L - np.sin(om[n] * y) / (2 * math.pi * n))
    return 2 * (n * np.sin(om[n] * y) - m * np.sin(om[m] * y)) / (math.pi * (m * m - n * n))


def theta_v(v, y, L, om):
    N = len(v)
    t = 0.0
    for n in range(N):
        for m in range(N):
            t += v[n] * v[m] * theta_nm(n, m, y, L, om)
    return t


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "zeta"
    mu = float(sys.argv[2]) if len(sys.argv) > 2 else 16.0
    NB = int(sys.argv[3]) if len(sys.argv) > 3 else 32
    L = math.log(mu)
    om = np.array([2 * math.pi * n / L for n in range(NB + 1)])
    z = zeros(name)
    zz = z[z < om[-1] * 1.1]
    Ph = np.array([hat(g, L, om) for g in zz])
    ev, evc = np.linalg.eigh(2 * Ph.T @ Ph)
    v0 = evc[:, 0]
    if v0[0] < 0:
        v0 = -v0
    print(f"{name} mu={mu} L={L:.3f} NB={NB} nzeros={len(zz)} lam0={ev[0]:.3e}")
    print(f"{'y':>6} {'Θ':>12} {'-lnΘ':>8} {'y e^y':>8} {'ratio':>8}")
    ys = np.linspace(0.2, L * 0.95, 12)
    for y in ys:
        t = theta_v(v0, y, L, om)
        if t <= 0:
            print(f"{y:6.3f} {t:12.3e}   (non pos)")
            continue
        nlt = -math.log(t)
        yey = y * math.exp(y)
        print(f"{y:6.3f} {t:12.3e} {nlt:8.3f} {yey:8.3f} {nlt/yey:8.3f}")


if __name__ == "__main__":
    main()
