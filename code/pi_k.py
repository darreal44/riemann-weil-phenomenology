#!/usr/bin/env python3
"""Finite-level unit projectors on the slice.

Z_2^* / U_K, K=4: U_4 = 1+16 Z_2, four classes.
Not the true Π_k on X_S — a character-sector split of the
radial Fourier already in semilocal.py.

Each sector χ of exact conductor 2^k multiplies the cosine
by the Gauss phase of χ. At this resolution the phase is
replaced by a signed lag: F_χ g(ρ) = ½[∑ ε_χ(n) ĝ(2^n ρ) − ĝ(ρ/2)]
with ε_χ(n) = χ(1+2^{v} ) mock = (-1)^{n·ord} for two nontrivial
characters and +1 for the trivial one.

This is a diagnostic: does ∑λ² per sector stay O(1) when N grows,
or does the log sit in one sector?
"""
from __future__ import annotations

import numpy as np

from semilocal import Fab


def F_cell_chi(a, b, rho, eps, NN=32):
    s = -Fab(a, b, rho / 2)
    for n in range(NN):
        s = s + eps(n) * Fab(a, b, (2.0**n) * rho)
    return 0.5 * s


def sector(R, N, eps):
    h = R / N
    edges = np.linspace(0, R, N + 1)
    mids = 0.5 * (edges[:-1] + edges[1:])
    F = np.empty((N, N))
    for j in range(N):
        F[:, j] = F_cell_chi(edges[j], edges[j + 1], mids, eps)
    n1 = int(round(N / R)) if R >= 1 else N
    A = 0.5 * (F[:n1, :n1] + F[:n1, :n1].T)
    ev = np.linalg.eigvalsh(A)
    return float((ev**2).sum()), ev[np.argsort(-np.abs(ev))[:4]]


def main():
    chars = {
        "triv k<=1": lambda n: 1.0,
        "k=2": lambda n: -1.0 if n % 2 == 0 else 1.0,
        "k=3": lambda n: -1.0 if n % 4 < 2 else 1.0,
        "k=4": lambda n: -1.0 if (n // 2) % 2 == 0 else 1.0,
    }
    print(f"{'sector':<12} {'N':>4} {'sum λ²':>10}  top|λ|")
    for N in (80, 160):
        R = 4.0
        for name, eps in chars.items():
            s2, top = sector(R, N, eps)
            print(f"{name:<12} {N:4d} {s2:10.3f}  {np.round(top, 3)}")


if __name__ == "__main__":
    main()
