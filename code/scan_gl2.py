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
    # Maass and new precision requests: pre-compute-gamma/code/scan_gl2.py
"""
from __future__ import annotations

import math
import hashlib
import os
import pickle
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

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


def zeros(name, prec=None, T=None, with_metadata=False):
    """Read a measured snapshot. Its extent does not certify zero completeness.

    T must not exceed the last stored ordinate; precision upgrades and new
    coverage belong to PGC. Multiplicities in the stored list are preserved.
    """
    if prec is not None:
        raise ValueError("precision requests belong to pre-compute-gamma/code/scan_gl2.py")
    p = os.path.join(HERE, f"zeros_{name}_weyl.pkl")
    with open(p, "rb") as handle:
        raw = handle.read()
    z = np.array(sorted(float(x) for x in pickle.loads(raw)))
    if not len(z) or not np.all(np.isfinite(z)) or np.any(z <= 0):
        raise ValueError('snapshot must contain finite positive ordinates; central zeros need a separate term')
    if T is not None and (not math.isfinite(T) or T <= 0 or T > z[-1]):
        raise ValueError(f'requested height {T} exceeds usable snapshot extent {z[-1]}; regenerate in PGC')
    metadata = dict(source=os.path.abspath(p), sha256=hashlib.sha256(raw).hexdigest(),
                    requested_height=T, last_ordinate=float(z[-1]), count=len(z),
                    completeness_certified=False, precision='binary64 snapshot; source error unknown',
                    central_zero='not included', multiplicity='as stored')
    return (z, metadata) if with_metadata else z


def hat(g, L, om):
    s = np.sin(g * L / 2)
    v = np.empty_like(om)
    v[0] = 2 * s / (g * math.sqrt(L))
    v[1:] = math.sqrt(2 / L) * s * 2 * g / (g * g - om[1:] ** 2)
    return v


def gram(name, mu, NB, prec=None):
    L = math.log(mu)
    Tneed = 2.0 * math.pi * NB / L * 1.1
    z = zeros(name, prec=prec, T=Tneed)
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
    argv = sys.argv[1:]
    if any(arg.startswith("-") for arg in argv):
        sys.exit("precompute options belong to pre-compute-gamma/code/scan_gl2.py")
    name = argv[0] if argv else "11a1"
    if name not in CURVES:
        sys.exit(f"unknown published curve {name}; Maass inputs belong to pre-compute-gamma")
    if not os.path.exists(os.path.join(HERE, f"zeros_{name}_weyl.pkl")):
        sys.exit(f"missing zeros_{name}_weyl.pkl; generate inputs in pre-compute-gamma")
    if len(argv) >= 4:
        windows = [(float(argv[1]), int(argv[2]), int(argv[3]))]
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
