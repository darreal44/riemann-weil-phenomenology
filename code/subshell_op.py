#!/usr/bin/env python3
"""One lacunary term = one 2-adic unit sub-shell.

F^{(n)}_{·,j} = (1/2) Fab(cell_j, 2^n x)     n = 0,1,...
F^{inv}_{·,j} = (1/2) Fab(cell_j, x/2)
Full semi-local F = sum_n F^{(n)} - F^{inv}.

Compress to [0,1], report HS^2 and λ_max of each piece.
"""
from __future__ import annotations

import sys

import numpy as np

sys.path.insert(0, ".")
from semilocal import Fab


def piece(R: float, N: int, scale: float) -> np.ndarray:
    edges = np.linspace(0.0, R, N + 1)
    mids = 0.5 * (edges[:-1] + edges[1:])
    F = np.empty((N, N))
    for j in range(N):
        F[:, j] = 0.5 * Fab(edges[j], edges[j + 1], scale * mids)
    n1 = int(round(N / R))
    return 0.5 * (F[:n1, :n1] + F[:n1, :n1].T)


def stats(A: np.ndarray) -> tuple[float, float]:
    ev = np.linalg.eigvalsh(A)
    return float((ev**2).sum()), float(ev.max())


if __name__ == "__main__":
    R, N = 4.0, 80
    print(f"R={R} N={N} h={R/N}")
    print(f"{'n':>4} {'scale':>8} {'sumλ²':>10} {'λmax':>10}")
    total = None
    acc = None
    for n in range(12):
        A = piece(R, N, 2.0**n)
        s2, lm = stats(A)
        print(f"{n:4d} {2.0**n:8.1f} {s2:10.4f} {lm:10.4f}")
        acc = A if acc is None else acc + A
    Ainv = piece(R, N, 0.5)
    s2, lm = stats(Ainv)
    print(f"{'inv':>4} {0.5:8.1f} {s2:10.4f} {lm:10.4f}")
    Afull = acc - Ainv
    s2, lm = stats(Afull)
    print(f"{'Σ-inv':>4} {'':>8} {s2:10.4f} {lm:10.4f}")
    # cross terms: ||sum||^2 vs sum || ||^2
    pieces = [piece(R, N, 2.0**n) for n in range(12)]
    sum_hs = sum(stats(P)[0] for P in pieces)
    print(f"sum_n ||F^(n)||_HS^2 = {sum_hs:.4f}")
    print(f"||sum F^(n)||_HS^2   = {stats(acc)[0]:.4f}")
    print(f"cross = latter - former (negative => shells interfere)")
