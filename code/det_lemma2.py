#!/usr/bin/env python3
"""Expand det(A-P) in the Lemma-2 frame {e1, e2}.

    python3 code/det_lemma2.py chi5 16
"""
from __future__ import annotations
import math, sys
import numpy as np
import mpmath as mp
import numpy.polynomial.legendre as NL
from scan_s import CHARS, chi_tab

def th_hat(n, m, y, L):
    om = 2 * math.pi / L
    if n == 0 and m == 0:
        return 2 * (L - y) / L
    if n == 0 or m == 0:
        j = max(n, m)
        return -2 * math.sin(om * j * y) / (math.sqrt(2) * math.pi * j)
    if n == m:
        return 2 * ((L - y) * math.cos(om * n * y) / L - math.sin(om * n * y) / (2 * math.pi * n))
    return 2 * (n * math.sin(om * n * y) - m * math.sin(om * m * y)) / (math.pi * (m * m - n * n))


def frame_vectors():
    e1 = np.array([math.sqrt(2), -1.0]) / math.sqrt(3.0)
    e2 = np.array([1.0, math.sqrt(2)]) / math.sqrt(3.0)
    e2 = e2 - e1 * (e1 @ e2)
    e2 = e2 / np.linalg.norm(e2)
    return e1, e2


def main(name="chi5", mu=16, dps=25):
    e1, e2 = frame_vectors()
    cf = CHARS[name]
    q, a = cf["q"], cf["a"]
    tab = chi_tab(cf["d"], q)
    mp.mp.dps = dps
    Lm = mp.log(mp.mpf(mu))
    L = float(Lm)
    s0 = 0.25 + 0.5 * a
    NB, DEG = 3, 12
    om = [2 * mp.pi * n / Lm for n in range(2)]
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
    NPANEL = 3 * NB + 12
    for p in range(NPANEL):
        aa, bb = Lm * p / NPANEL, Lm * (p + 1) / NPANEL
        h = (bb - aa) / 2
        for x, w in zip(xr, wr):
            nodes.append(aa + h * (x + 1))
            wts.append(w * h)
    K = len(nodes)
    SIN = [[mp.sin(om[n] * y) for y in nodes] for n in range(2)]
    COS = [[mp.cos(om[n] * y) for y in nodes] for n in range(2)]
    LY = [(Lm - y) / Lm for y in nodes]
    D2 = [wts[k] * 2 * mp.e ** (-2 * mp.mpf(s0) * nodes[k]) / (1 - mp.e ** (-2 * nodes[k])) for k in range(K)]
    EC = [mp.e ** (-(2 - 2 * mp.mpf(s0)) * nodes[k]) for k in range(K)]
    CST = mp.log(mp.mpf(q) / mp.pi) - mp.euler - mp.log(1 - mp.e ** (-2 * Lm))

    def th_nodes(n, m):
        if n == 0 and m == 0:
            return [2 * LY[k] for k in range(K)], mp.mpf(2)
        j = max(n, m)
        a2 = -2 / (mp.sqrt(2) * mp.pi * j)
        return [a2 * SIN[j][k] for k in range(K)], mp.mpf(0)

    Ahat = np.zeros((2, 2))
    for n in range(2):
        for m in range(n, 2):
            th, F0 = th_nodes(n, m)
            arch = float(F0 / 2 * CST + mp.mpf("0.5") * mp.fsum(D2[k] * (F0 * EC[k] - th[k]) for k in range(K)))
            Ahat[n, m] = Ahat[m, n] = arch
    A = np.array([[e1 @ Ahat @ e1, e1 @ Ahat @ e2], [e2 @ Ahat @ e1, e2 @ Ahat @ e2]])
    print(f"{name} mu={mu}")
    print("A\n", A)
    P = np.zeros((2, 2))
    print(f"{'n':>4} {'P11':>10} {'P12':>10} {'P22':>10}")
    cap = int(mu + 1e-9)
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    x = 2
    while x <= cap:
        y2, p = x, None
        for qq in small:
            if y2 % qq == 0:
                p = qq
                while y2 % qq == 0:
                    y2 //= qq
                break
        if p and y2 == 1 and tab[x % q] != 0:
            lg = math.log(x)
            w = tab[x % q] * math.log(p) / math.sqrt(x)
            ths = np.zeros((2, 2))
            for n in range(2):
                for m in range(2):
                    ths[n, m] = th_hat(n, m, lg, L)
            Pf = np.array([[e1 @ ths @ e1, e1 @ ths @ e2], [e2 @ ths @ e1, e2 @ ths @ e2]]) * w
            P += Pf
            print(f"{x:4d} {Pf[0,0]:10.4f} {Pf[0,1]:10.4f} {Pf[1,1]:10.4f}")
        x += 1
    H = A - P
    det = float(H[0, 0] * H[1, 1] - H[0, 1] ** 2)
    print("P\n", P)
    print("H\n", H)
    print(f"det={det:.6e}  tr={H[0,0]+H[1,1]:.6e}  lmin~{det/(H[0,0]+H[1,1]):.6e}")


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "chi5"
    mu = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    main(name, mu)
