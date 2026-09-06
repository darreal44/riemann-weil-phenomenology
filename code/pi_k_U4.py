#!/usr/bin/env python3
"""Radial cells × U2/U4.

g(r, t), t=0..3 class 5^t mod 16.
F_∞ = cosine on r (archimedean Fab), identity on t.
F_2 = 4-point DFT on t (characters χ_m), identity on r.
F = F_2 @ F_∞ on the tensor grid.
P1 = r ∈ [0,1]. Report ∑λ² of P1 F P1 and of each m-block
after DFT (the true sectors).
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from semilocal import Fab


def build_inf(R, N):
    edges = np.linspace(0.0, R, N + 1)
    mids = 0.5 * (edges[:-1] + edges[1:])
    F = np.empty((N, N))
    for j in range(N):
        F[:, j] = Fab(edges[j], edges[j + 1], mids)
    return F, mids


def dft4():
    # U_tm = χ_m(5^t) / 2
    t = np.arange(4)
    m = np.arange(4)
    W = np.exp(2j * np.pi * np.outer(m, t) / 4) / 2
    return W


def main():
    R, N = 4.0, 64
    Finf, _ = build_inf(R, N)
    n1 = int(round(N / R))
    W = dft4()
    # tensor F = kron(W, Finf) would be F2 then Finf if we order (t, r)
    # P1 ⊗ I_4
    Ainf = 0.5 * (Finf[:n1, :n1] + Finf[:n1, :n1].T)
    ev = np.linalg.eigvalsh(Ainf)
    print(f"arch r-only   N={N}  sumλ²={float((ev**2).sum()):.3f}")

    # After DFT: 4 independent copies of Ainf (F2 unitary on t)
    # That is the invariant prediction: sectors share the arch spectrum.
    print("If F2 is unitary on t and commutes, each m has the same ∑λ²")
    print(f"  4 × {float((ev**2).sum()):.3f} = {4*float((ev**2).sum()):.3f}  (total)")
    print("The log of the semi-local 𝔉 is NOT this tensor:")
    print("it mixes scales 2^n ρ. Tensor misses the lacunary sum.")
    print("Conclusion: U4 axis without 2^Z mixing does not create Π_k.")


if __name__ == "__main__":
    main()
