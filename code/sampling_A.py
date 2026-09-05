#!/usr/bin/env python3
"""Sampling constant A on Iᶜ from Lemma 2.

    λ_min(Gram) ≥ A exp(−π τ γ1)
    ⇒  A_hat = λ_min(Gram) · exp(π τ γ1)

    python code/sampling_A.py chi29 22 36
"""
from __future__ import annotations

import math
import os
import pickle
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    name, mu, NB = sys.argv[1], float(sys.argv[2]), int(sys.argv[3])
    z = np.array(
        sorted(float(x) for x in pickle.load(open(os.path.join(HERE, f"zeros_{name}_weyl.pkl"), "rb")))
    )
    z = z[z > 1e-12]
    g1 = float(z[0])
    L = math.log(mu)
    tau = L / 2
    om = np.array([2 * math.pi * n / L for n in range(NB + 1)])
    zz = z[(z > 1e-12) & (z < om[-1] * 1.1)]
    rows = []
    for g in zz:
        s = math.sin(g * L / 2)
        v = np.empty_like(om)
        v[0] = 2 * s / (g * math.sqrt(L))
        v[1:] = math.sqrt(2 / L) * s * 2 * g / (g * g - om[1:] ** 2)
        rows.append(v)
    ev = np.sort(np.linalg.eigvalsh(2 * np.array(rows).T @ np.array(rows)))
    lam0 = float(ev[0])
    slep = math.pi * tau * g1
    Ahat = lam0 * math.exp(slep) if lam0 > 0 else float("nan")
    print(
        f"[{name} mu={mu} N={NB+1}] g1={g1:.3f} τ={tau:.3f}  "
        f"πτγ1={slep:.2f}  lam0={lam0:.4e}  A_hat={Ahat:.3e}  nz={len(zz)}"
    )


if __name__ == "__main__":
    main()
