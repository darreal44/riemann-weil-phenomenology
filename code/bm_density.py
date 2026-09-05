#!/usr/bin/env python3
"""Sliding Beurling densities of a harvested zero list.

    python3 code/bm_density.py chi29 50
"""
from __future__ import annotations

import math
import os
import pickle
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def zeros(name):
    return np.array(
        sorted(float(x) for x in pickle.load(open(os.path.join(HERE, f"zeros_{name}_weyl.pkl"), "rb")))
    )


def Dpm(z, r):
    T = z[-1]
    xs = np.arange(0.0, max(T - r, 0.0), max(r / 4.0, 1.0))
    if len(xs) < 3:
        return None
    c = np.searchsorted(z, xs + r) - np.searchsorted(z, xs)
    return float(c.min() / r), float(c.max() / r), int(len(xs))


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "chi29"
    r = float(sys.argv[2]) if len(sys.argv) > 2 else 50.0
    z = zeros(name)
    d = Dpm(z, r)
    if not d:
        print("short list")
        return
    Dm, Dp, n = d
    print(f"{name} T={z[-1]:.1f} n={len(z)} r={r:.0f} windows={n}")
    print(f"  D-={Dm:.3f}  D+={Dp:.3f}")
    for mu in (11, 22, 38):
        tau = math.log(mu) / 2.0
        th = tau / math.pi
        print(f"  μ={mu} τ/π={th:.3f}  D- > τ/π ? {Dm > th}")


if __name__ == "__main__":
    main()
