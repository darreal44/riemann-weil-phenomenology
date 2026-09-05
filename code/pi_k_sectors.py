#!/usr/bin/env python3
"""K=4 sectors: trivial vs primitive Gauss phases.

A global τ does not change the spectrum of the Hermitian
compression (phase). This script records that, then a
valuation filter: keep only lacunary n ≡ r (mod 2) as a
stand-in for conductor matching on ρ.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from semilocal import Fab, F_cell, build


def sumlam2(A):
    ev = np.linalg.eigvalsh(A)
    return float((ev**2).sum()), ev[np.argsort(-np.abs(ev))[:3]]


def compress(F, R, N):
    n1 = int(round(N / R))
    A = 0.5 * (F[:n1, :n1] + F[:n1, :n1].T)
    return sumlam2(A)


def F_filter(R, N, residue, mod=2, NN=32):
    h = R / N
    edges = np.linspace(0, R, N + 1)
    mids = 0.5 * (edges[:-1] + edges[1:])
    F = np.empty((N, N))
    for j in range(N):
        a, b = edges[j], edges[j + 1]
        s = -Fab(a, b, mids / 2)
        for n in range(NN):
            if n % mod == residue:
                s = s + Fab(a, b, (2.0**n) * mids)
        F[:, j] = 0.5 * s
    return F


def main():
    R, N = 4.0, 120
    F, h, _ = build(R, N, semilocal=True)
    s2, top = compress(F, R, N)
    print(f"triv (m=0)           N={N}  sumλ²={s2:.3f}  top={np.round(top,3)}")
    # global phase: same Hermitian
    print("global τ: same spectrum (phase)")
    for res in (0, 1):
        Fr = F_filter(R, N, res)
        s2, top = compress(Fr, R, N)
        print(f"n≡{res} (mod 2)         N={N}  sumλ²={s2:.3f}  top={np.round(top,3)}")
    F2, _, _ = build(R, 2 * N, semilocal=True)
    s2, top = compress(F2, R, 2 * N)
    print(f"triv N={2*N}            sumλ²={s2:.3f}  top={np.round(top,3)}")


if __name__ == "__main__":
    main()
