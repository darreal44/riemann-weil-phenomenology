#!/usr/bin/env python3
"""Zero-side mode: G = 2 Σ φ(γ)φ(γ)^T in the scan_s cosine basis.

    python3 code/gram_mode.py chi29 22 32
"""
from __future__ import annotations

import json
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


def main():
    name = sys.argv[1]
    mu = float(sys.argv[2])
    NB = int(sys.argv[3]) if len(sys.argv) > 3 else 32
    z = zeros(name)
    L = math.log(mu)
    om = np.array([2 * math.pi * n / L for n in range(NB + 1)])
    zz = z[z < om[-1] * 1.1]
    Ph = np.array([hat(g, L, om) for g in zz])
    ev, evc = np.linalg.eigh(2 * Ph.T @ Ph)
    v0 = evc[:, 0]
    p = v0 ** 2
    p /= p.sum()
    neff = 1.0 / float(p @ p)
    kbar = float(p @ np.arange(NB + 1))
    mz = (Ph @ v0) ** 2
    mz /= mz.sum()
    i = int(np.argmax(mz))
    side = i - 1 if i and mz[i - 1] >= (mz[i + 1] if i + 1 < len(mz) else -1) else min(i + 1, len(mz) - 1)
    lo, hi = sorted((i, side))
    ratio = float(ev[1] / ev[0]) if ev[0] > 0 else float("nan")
    rec = ev[0] > 0 and ratio > 100 and neff < 4 and kbar < 3
    out = {
        "name": name,
        "mu": mu,
        "NB": NB,
        "lam0": float(ev[0]),
        "ell": float(-math.log(ev[0])) if ev[0] > 0 else None,
        "N_eff": neff,
        "kbar": kbar,
        "l1_over_l0": ratio,
        "pair": [float(zz[lo]), float(zz[hi])],
        "pair_mass": float(mz[lo] + mz[hi]),
        "recognized": rec,
        "v0": [float(x) for x in v0],
    }
    print(
        f"[{name} mu={mu} N={NB+1} GRAM] ell={out['ell']} "
        f"N_eff={neff:.2f} kbar={kbar:.2f} l1/l0={ratio:.2e} "
        f"pair={zz[lo]:.2f}-{zz[hi]:.2f} ({100*out['pair_mass']:.0f}%) "
        f"{'OK' if rec else 'NO'}"
    )
    path = os.path.join(os.path.dirname(HERE), "report", f"gram_mode_{name}_mu{int(mu)}.json")
    json.dump(out, open(path, "w"), indent=2)
    print("  dumped", path)


if __name__ == "__main__":
    main()
