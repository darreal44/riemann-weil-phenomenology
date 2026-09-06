#!/usr/bin/env python3
"""Q(v) for v = (4,-3,1)/sqrt(26) at chi5 mu=16.

    python3 code/rational_witness.py
"""
from __future__ import annotations
import math
import numpy as np
import mpmath as mp
import numpy.polynomial.legendre as NL
from scan_s import CHARS, chi_tab


def main(mu=16, dps=30):
    raw = np.array([4.0, -3.0, 1.0])
    v = raw / np.linalg.norm(raw)
    print("v = (4,-3,1)/sqrt(26) =", v)
    cf = CHARS["chi5"]
    q, a = cf["q"], cf["a"]
    tab = chi_tab(cf["d"], q)
    mp.mp.dps = dps
    L = mp.log(mp.mpf(mu))
    s0 = mp.mpf("0.25") + mp.mpf(a) / 2
    om = [2 * mp.pi * n / L for n in range(3)]
    DEG, NPANEL = 12, 24
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
    D2 = [wts[k] * 2 * mp.e ** (-2 * s0 * nodes[k]) / (1 - mp.e ** (-2 * nodes[k])) for k in range(K)]
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
            return [2 * (LY[k] * COS[n][k] - SIN[n][k] / (2 * mp.pi * n)) for k in range(K)], mp.mpf(2)
        a2 = 2 / (mp.pi * (m * m - n * n))
        return [a2 * (n * SIN[n][k] - m * SIN[m][k]) for k in range(K)], mp.mpf(0)

    def th_at(n, m, y):
        if n == 0 and m == 0:
            return 2 * (L - y) / L
        if n == 0 or m == 0:
            j = max(n, m)
            return -2 * mp.sin(om[j] * y) / (mp.sqrt(2) * mp.pi * j)
        if n == m:
            return 2 * ((L - y) * mp.cos(om[n] * y) / L - mp.sin(om[n] * y) / (2 * mp.pi * n))
        return 2 * (n * mp.sin(om[n] * y) - m * mp.sin(om[m] * y)) / (mp.pi * (m * m - n * n))

    A = np.zeros((3, 3))
    for n in range(3):
        for m in range(n, 3):
            th, F0 = th_nodes(n, m)
            arch = float(F0 / 2 * CST + mp.mpf("0.5") * mp.fsum(D2[k] * (F0 * EC[k] - th[k]) for k in range(K)))
            A[n, m] = A[m, n] = arch
    Av = float(v @ A @ v)
    print("A(v)", Av)
    P = 0.0
    print(f"{'n':>4} {'wθ':>12}")
    x = 2
    small = [2, 3, 5, 7, 11, 13]
    while x <= mu:
        y2, p = x, None
        for qq in small:
            if y2 % qq == 0:
                p = qq
                while y2 % qq == 0:
                    y2 //= qq
                break
        if p and y2 == 1 and tab[x % q] != 0:
            w = float(tab[x % q] * mp.log(p) / mp.sqrt(x))
            Th = np.zeros((3, 3))
            lg = mp.log(x)
            for n in range(3):
                for m in range(3):
                    Th[n, m] = float(th_at(n, m, lg))
            term = float(v @ Th @ v) * w
            P += term
            print(f"{x:4d} {term:12.6f}")
        x += 1
    print("P(v)", P)
    print("Q(v)=A-P", Av - P)


if __name__ == "__main__":
    main()
