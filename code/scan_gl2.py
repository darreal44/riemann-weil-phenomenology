#!/usr/bin/env python3
"""Zero-side Gram slope for GL(2) lists (elliptic curves).

Prime-side Q for these L-functions is not the Dirichlet assemble()
of scan_s.py (wrong Gamma, wrong a_p). This script uses only the
harvested zeros — the same Gram as report/gram_mode_*.json.

    python3 code/scan_gl2.py 11a1 22 36 50
    python3 code/scan_gl2.py 11a1 38 66 42
"""
from __future__ import annotations

import math
import os
import pickle
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CURVES = ("11a1", "19a1", "32a1", "37a1", "43a1", "53a1", "61a1", "67a1")


def zeros(name):
    p = os.path.join(HERE, f"zeros_{name}_weyl.pkl")
    return np.array(sorted(float(x) for x in pickle.load(open(p, "rb"))))


def hat(g, L, om):
    s = np.sin(g * L / 2)
    v = np.empty_like(om)
    v[0] = 2 * s / (g * math.sqrt(L))
    v[1:] = math.sqrt(2 / L) * s * 2 * g / (g * g - om[1:] ** 2)
    return v


def gram(name, mu, NB):
    z = zeros(name)
    L = math.log(mu)
    om = np.array([2 * math.pi * n / L for n in range(NB + 1)])
    zz = z[z < om[-1] * 1.1]
    Ph = np.array([hat(g, L, om) for g in zz])
    ev, evc = np.linalg.eigh(2 * Ph.T @ Ph)
    if ev[0] <= 0:
        raise RuntimeError(f"indefinite Gram {name} mu={mu}")
    v0 = evc[:, 0]
    p = v0 ** 2
    p /= p.sum()
    neff = 1.0 / float(p @ p)
    kbar = float(p @ np.arange(len(p)))
    ell = [-math.log(max(float(x), 1e-300)) for x in ev[:6]]
    ratio = float(ev[1] / ev[0])
    print(
        f"[{name} mu={mu} N={NB+1} Gram] "
        f"lam0={ev[0]:.3e}  ell={[round(x, 2) for x in ell]}  "
        f"N_eff={neff:.2f} kbar={kbar:.2f} l1/l0={ratio:.2e}",
        flush=True,
    )
    return float(ev[0]), ell


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "11a1"
    if name not in CURVES:
        sys.exit(f"unknown curve {name}, have {CURVES}")
    if not os.path.exists(os.path.join(HERE, f"zeros_{name}_weyl.pkl")):
        sys.exit(f"missing zeros_{name}_weyl.pkl — harvest_gl2 first")
    if len(sys.argv) >= 5:
        windows = [(float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))]
    else:
        windows = [(22.0, 36, 50), (38.0, 66, 42)]
    rows = []
    for mu, NB, _dps in windows:
        lam0, ell = gram(name, mu, NB)
        rows.append((mu, ell[0], lam0))
    if len(rows) >= 2:
        s = (rows[1][1] - rows[0][1]) / (rows[1][0] - rows[0][0])
        print(
            f"SLOPE {name} Gram: s_hat = {s:.3f}  "
            f"ell({rows[0][0]})={rows[0][1]:.2f}  ell({rows[1][0]})={rows[1][1]:.2f}"
        )


if __name__ == "__main__":
    main()
