#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
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
_PCG = os.path.join(os.path.dirname(HERE), "pre-compute-gamma", "code")
if os.path.isdir(_PCG):
    sys.path.insert(0, _PCG)

CURVES = (
    "11a1", "19a1", "32a1", "37a1", "43a1", "53a1", "61a1", "67a1",
    "zeta",
    "delta",
    "delta_chi5",
    "delta_chi4",
    "11a1_chi5",
    "sym2_11a1",
    "sym2_delta",
)


def zeros(name):
    if os.path.isdir(_PCG):
        try:
            from tools import load_zeros

            z = load_zeros(name)
            if getattr(z, "size", 0):
                return np.asarray(z, dtype=float)
        except (ImportError, KeyError, FileNotFoundError, OSError):
            pass
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
        print(
            f"[{name} mu={mu} N={NB+1} Gram] INDEF lam0={ev[0]:.3e} "
            f"(desert artifact; zeta/chi5: use prime-side Q)",
            flush=True,
        )
        return float(ev[0]), [float("nan")] * 6
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
    try:
        from maass_table1 import is_maass_name
    except ImportError:
        def is_maass_name(name):
            return None

    maass = is_maass_name(name)
    if maass:
        if not os.path.isdir(_PCG):
            sys.exit(
                f"{name} is Maass: init the private submodule\n"
                f"  git submodule update --init pre-compute-gamma"
            )
        name = maass
    elif name not in CURVES:
        sys.exit(f"unknown curve {name}, have {CURVES}")
    elif not os.path.exists(os.path.join(HERE, f"zeros_{name}_weyl.pkl")):
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
