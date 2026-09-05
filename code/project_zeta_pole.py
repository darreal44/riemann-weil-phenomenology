#!/usr/bin/env python3
"""Project out the pole mode of Q_ζ and print the rest.

    python code/project_zeta_pole.py 2 6 25 8
"""
from __future__ import annotations

import sys
import time

import mpmath as mp
import numpy as np
import numpy.polynomial.legendre as NL


def assemble(mu, NB, dps, DEG):
    mp.mp.dps = dps
    t0 = time.time()
    L = mp.log(mp.mpf(mu))
    om = [2 * mp.pi * n / L for n in range(NB + 1)]
    NPANEL = 5 * NB + 20
    xr0, _ = NL.leggauss(DEG)
    xr, wr = [], []
    for x0 in xr0:
        x = mp.mpf(float(x0))
        for _ in range(6):
            P_ = mp.legendre(DEG, x)
            Pm = mp.legendre(DEG - 1, x)
            dP = DEG * (x * P_ - Pm) / (x * x - 1)
            x = x - P_ / dP
        P_ = mp.legendre(DEG, x)
        Pm = mp.legendre(DEG - 1, x)
        dP = DEG * (x * P_ - Pm) / (x * x - 1)
        xr.append(x)
        wr.append(2 / ((1 - x * x) * dP * dP))
    nodes, wts = [], []
    for p in range(NPANEL):
        a, b = L * p / NPANEL, L * (p + 1) / NPANEL
        h = (b - a) / 2
        for x, w in zip(xr, wr):
            nodes.append(a + h * (x + 1))
            wts.append(w * h)
    Kn = len(nodes)
    SIN = [[mp.sin(om[n] * y) for y in nodes] for n in range(NB + 1)]
    COS = [[mp.cos(om[n] * y) for y in nodes] for n in range(NB + 1)]
    LY = [(L - y) / L for y in nodes]
    W1 = [wts[k] * (mp.e ** (nodes[k] / 2) + mp.e ** (-nodes[k] / 2)) for k in range(Kn)]
    E2 = [mp.e ** (nodes[k] / 2) for k in range(Kn)]
    DD = [wts[k] / (mp.e ** nodes[k] - mp.e ** (-nodes[k])) for k in range(Kn)]
    CR = mp.euler + mp.log(4 * mp.pi * (mp.e ** L - 1) / (mp.e ** L + 1))

    def th_nodes(n, m):
        if n == 0 and m == 0:
            return [2 * LY[k] for k in range(Kn)], mp.mpf(2)
        if n == 0 or m == 0:
            j = max(n, m)
            a2 = -2 / (mp.sqrt(2) * mp.pi * j)
            return [a2 * SIN[j][k] for k in range(Kn)], mp.mpf(0)
        if n == m:
            return [
                2 * (LY[k] * COS[n][k] - SIN[n][k] / (2 * mp.pi * n)) for k in range(Kn)
            ], mp.mpf(2)
        a2 = 2 / (mp.pi * (m * m - n * n))
        return [a2 * (n * SIN[n][k] - m * SIN[m][k]) for k in range(Kn)], mp.mpf(0)

    def th_at(n, m, y):
        if n == 0 and m == 0:
            return 2 * (L - y) / L
        if n == 0 or m == 0:
            j = max(n, m)
            return -2 * mp.sin(om[j] * y) / (mp.sqrt(2) * mp.pi * j)
        if n == m:
            return 2 * (
                (L - y) * mp.cos(om[n] * y) / L - mp.sin(om[n] * y) / (2 * mp.pi * n)
            )
        return 2 * (n * mp.sin(om[n] * y) - m * mp.sin(om[m] * y)) / (
            mp.pi * (m * m - n * n)
        )

    cap = int(float(mp.e ** L) + 1e-9)
    primes = [p for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] if p <= cap]
    towers = {p: [] for p in primes}
    for p in primes:
        n = p
        while n <= cap:
            towers[p].append((mp.log(n), mp.log(p) / mp.sqrt(n)))
            n *= p

    NP = NB + 1
    S = mp.matrix(NP)
    Pmat = mp.matrix(NP)
    for n in range(NP):
        for m in range(n, NP):
            th, F0 = th_nodes(n, m)
            pole = mp.fsum(th[k] * W1[k] for k in range(Kn))
            arch = -(F0 / 2 * CR + mp.fsum((E2[k] * th[k] - F0) * DD[k] for k in range(Kn)))
            prim = mp.fsum(
                -mp.fsum(w * th_at(n, m, lg) for lg, w in towers[p]) for p in primes
            )
            v = pole + arch + prim
            S[n, m] = S[m, n] = v
            Pmat[n, m] = Pmat[m, n] = pole
    print(f"assembled mu={mu} N={NP} {time.time()-t0:.0f}s")
    return S, Pmat


def npmat(M):
    n = M.rows
    return np.array([[float(M[i, j]) for j in range(n)] for i in range(n)])


def main():
    mu, NB, dps, DEG = float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    S, Pmat = assemble(mu, NB, dps, DEG)
    Q = npmat(S)
    P = npmat(Pmat)
    eQ, vQ = np.linalg.eigh(Q)
    eP, vP = np.linalg.eigh(P)
    # pole direction = top eigenvector of the POLE form (largest)
    u = vP[:, -1]
    proj = np.eye(len(u)) - np.outer(u, u)
    Qp = proj @ Q @ proj
    e = np.sort(np.linalg.eigvalsh(Qp))
    # one exact zero from the projection
    print(f"Q raw  lam[:4] = {np.round(eQ[:4], 6)}")
    print(f"POLE   lam max = {eP[-1]:.4f}  min={eP[0]:.4f}")
    print(f"Q ⊥pole lam[:5] = {np.round(e[:5], 6)}")
    print(f"  (first ~0 is the projected direction)")
    ov = abs(np.dot(vQ[:, 0], u))
    print(f"overlap raw-v0 vs pole-max = {ov:.3f}")


if __name__ == "__main__":
    main()
