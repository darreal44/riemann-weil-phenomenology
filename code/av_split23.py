#!/usr/bin/env python3
"""Split Q(v) = (A − P₂ − P₃) − P_rest for v=(4,−3,1)/√26 on χ₅.

P₂₃ is n=2 and n=3 only (not 4, 8, 9). One μ, not a slope.

    python code/av_split23.py 16
    python code/av_split23.py 150
"""
from __future__ import annotations

import math
import sys

import mpmath as mp
import numpy as np
import numpy.polynomial.legendre as NL

from scan_s import CHARS, chi_tab

V_RAW = np.array([4.0, -3.0, 1.0])
V = V_RAW / np.linalg.norm(V_RAW)


def _primes(n: int) -> list[int]:
    sv = [False, False] + [True] * (n - 1)
    p = 2
    while p * p <= n:
        if sv[p]:
            for k in range(p * p, n + 1, p):
                sv[k] = False
        p += 1
    return [i for i in range(2, n + 1) if sv[i]]


def split_AP(mu: float, dps: int = 40, DEG: int = 12) -> dict:
    """A(v), P23, Prest, Q on χ₅, three hats. Unconditional pairing."""
    cf = CHARS["chi5"]
    q, a = cf["q"], cf["a"]
    tab = chi_tab(cf["d"], q)
    mp.mp.dps = dps
    L = mp.log(mp.mpf(mu))
    s0 = mp.mpf("0.25") + mp.mpf(a) / 2
    om = [2 * mp.pi * n / L for n in range(3)]
    NPANEL = max(24, int(10 * float(L)))
    xr0, _ = NL.leggauss(DEG)
    xr, wr = [], []
    for x0 in xr0:
        x = mp.mpf(float(x0))
        for _ in range(5):
            P = mp.legendre(DEG, x)
            Pm = mp.legendre(DEG - 1, x)
            dP = DEG * (x * P - Pm) / (x * x - 1)
            x = x - P / dP
        P = mp.legendre(DEG, x)
        Pm = mp.legendre(DEG - 1, x)
        dP = DEG * (x * P - Pm) / (x * x - 1)
        xr.append(x)
        wr.append(2 / ((1 - x * x) * dP * dP))
    nodes, wts = [], []
    for p in range(NPANEL):
        aa, bb = L * p / NPANEL, L * (p + 1) / NPANEL
        h = (bb - aa) / 2
        for x, w in zip(xr, wr):
            nodes.append(aa + h * (x + 1))
            wts.append(w * h)
    K = len(nodes)
    SIN = [[mp.sin(om[n] * y) for y in nodes] for n in range(3)]
    COS = [[mp.cos(om[n] * y) for y in nodes] for n in range(3)]
    LY = [(L - y) / L for y in nodes]
    D2 = [
        wts[k] * 2 * mp.e ** (-2 * s0 * nodes[k]) / (1 - mp.e ** (-2 * nodes[k]))
        for k in range(K)
    ]
    EC = [mp.e ** (-(2 - 2 * s0) * nodes[k]) for k in range(K)]
    CST = mp.log(mp.mpf(q) / mp.pi) - mp.euler - mp.log(1 - mp.e ** (-2 * L))

    def th_nodes(n, m):
        if n == 0 and m == 0:
            return [2 * LY[k] for k in range(K)], mp.mpf(2)
        if n == 0 or m == 0:
            j = max(n, m)
            a2 = -2 / (mp.sqrt(2) * mp.pi * j)
            return [a2 * SIN[j][k] for k in range(K)], mp.mpf(0)
        if n == m:
            return [
                2 * (LY[k] * COS[n][k] - SIN[n][k] / (2 * mp.pi * n))
                for k in range(K)
            ], mp.mpf(2)
        a2 = 2 / (mp.pi * (m * m - n * n))
        return [
            a2 * (n * SIN[n][k] - m * SIN[m][k]) for k in range(K)
        ], mp.mpf(0)

    def th_at(n, m, y):
        if n == 0 and m == 0:
            return 2 * (L - y) / L
        if n == 0 or m == 0:
            j = max(n, m)
            return -2 * mp.sin(om[j] * y) / (mp.sqrt(2) * mp.pi * j)
        if n == m:
            return 2 * (
                (L - y) * mp.cos(om[n] * y) / L
                - mp.sin(om[n] * y) / (2 * mp.pi * n)
            )
        return 2 * (
            n * mp.sin(om[n] * y) - m * mp.sin(om[m] * y)
        ) / (mp.pi * (m * m - n * n))

    A = np.zeros((3, 3))
    for n in range(3):
        for m in range(n, 3):
            th, F0 = th_nodes(n, m)
            arch = float(
                F0 / 2 * CST
                + mp.mpf("0.5")
                * mp.fsum(D2[k] * (F0 * EC[k] - th[k]) for k in range(K))
            )
            A[n, m] = A[m, n] = arch
    Av = float(V @ A @ V)

    primes = _primes(int(mu))
    p23 = 0.0
    prest = 0.0
    for p in primes:
        n = p
        while n <= mu + 1e-12:
            if tab[n % q] != 0:
                w = float(tab[n % q] * mp.log(p) / mp.sqrt(n))
                lg = mp.log(n)
                Th = np.zeros((3, 3))
                for i in range(3):
                    for j in range(3):
                        Th[i, j] = float(th_at(i, j, lg))
                term = float(V @ Th @ V) * w
                if n in (2, 3):
                    p23 += term
                else:
                    prest += term
            n *= p
    gap = Av - p23
    Q = gap - prest
    return {
        "mu": float(mu),
        "A": Av,
        "P23": p23,
        "Prest": prest,
        "A_minus_P23": gap,
        "Q": Q,
        "crossed": bool(gap < prest),
    }


def main() -> None:
    mus = [float(x) for x in sys.argv[1:]] or [16.0, 50.0, 150.0]
    print(f"{'μ':>6} {'A':>10} {'P23':>10} {'A-P23':>10} {'Prest':>10} {'Q':>10}  cross")
    for mu in mus:
        r = split_AP(mu)
        print(
            f"{r['mu']:6.0f} {r['A']:10.4f} {r['P23']:10.4f} "
            f"{r['A_minus_P23']:10.4f} {r['Prest']:10.4f} {r['Q']:10.4f}  "
            f"{'YES' if r['crossed'] else 'no'}",
            flush=True,
        )


if __name__ == "__main__":
    main()
