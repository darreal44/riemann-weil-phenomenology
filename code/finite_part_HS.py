#!/usr/bin/env python3
"""Finite part of ||P1 F P1||_HS^2.

The log is in 1/h = N/R (cells per unit), not in N.
  pf = sum λ² − 0.65 log2(N/R)
plateaus near −0.20 at Λ=R=4, NN≥12.
"""
from __future__ import annotations

import sys

import numpy as np

sys.path.insert(0, ".")
from semilocal import Fab

C_LOG = 0.65


def sum_lambda2(R: float, N: int, NN: int = 16) -> float:
    edges = np.linspace(0.0, R, N + 1)
    mids = 0.5 * (edges[:-1] + edges[1:])
    F = np.empty((N, N))
    for j in range(N):
        a, b = edges[j], edges[j + 1]
        s = -Fab(a, b, mids / 2.0)
        for n in range(NN):
            s = s + Fab(a, b, (2.0**n) * mids)
        F[:, j] = 0.5 * s
    n1 = int(round(N / R))
    A = 0.5 * (F[:n1, :n1] + F[:n1, :n1].T)
    return float((np.linalg.eigvalsh(A) ** 2).sum())


if __name__ == "__main__":
    print(f"{'R':>4} {'N':>5} {'1/h':>6} {'sum':>8} {'c log2(1/h)':>12} {'pf':>8}")
    for R, N in ((4, 40), (4, 80), (4, 120), (4, 160), (4, 200), (2, 80), (5, 200)):
        s = sum_lambda2(R, N)
        invh = N / R
        print(
            f"{R:4.0f} {N:5d} {invh:6.1f} {s:8.3f} "
            f"{C_LOG * np.log2(invh):12.3f} {s - C_LOG * np.log2(invh):8.3f}"
        )
