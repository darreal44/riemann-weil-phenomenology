#!/usr/bin/env python3
"""Θ_v of the prime-side Q ground state at mu=11 (zeta, small basis)."""
import math
import time

import mpmath as mp
import numpy as np

mp.mp.dps = 25
L = mp.log(11)
N0 = 8
NP = N0 + 1
om = [2 * mp.pi * n / L for n in range(NP)]
EU = mp.euler
CR = EU + mp.log(4 * mp.pi * (mp.e**L - 1) / (mp.e**L + 1))


def theta(n, m, y):
    if n == 0 and m == 0:
        return 2 * (L - y) / L
    if n == 0 or m == 0:
        j = max(n, m)
        return -2 * mp.sin(om[j] * y) / (mp.sqrt(2) * mp.pi * j)
    if n == m:
        return 2 * ((L - y) * mp.cos(om[n] * y) / L - mp.sin(om[n] * y) / (2 * mp.pi * n))
    return 2 * (n * mp.sin(om[n] * y) - m * mp.sin(om[m] * y)) / (mp.pi * (m * m - n * n))


primes = [2, 3, 5, 7]
towers = []
for p in primes:
    k = 1
    while p**k <= 11:
        towers.append((mp.log(p**k), mp.log(p) / mp.sqrt(p**k)))
        k += 1

t0 = time.time()
Q = mp.matrix(NP)
for n in range(NP):
    for m in range(n, NP):
        F0 = mp.mpf(2) if n == m else mp.mpf(0)
        pol = mp.quad(lambda y: theta(n, m, y) * (mp.e ** (y / 2) + mp.e ** (-y / 2)), [0, L])
        ig = mp.quad(lambda y: (mp.e ** (y / 2) * theta(n, m, y) - F0) / (mp.e**y - mp.e ** (-y)), [0, L])
        ar = -(F0 / 2 * CR + ig)
        tw = mp.fsum(w * theta(n, m, lg) for lg, w in towers)
        Q[n, m] = Q[m, n] = pol + ar - tw
print(f"Q {NP}x{NP} in {time.time()-t0:.0f}s")

ev = mp.eigsy(Q, eigvals_only=False)
lams = [float(ev[0][i]) for i in range(NP)]
idx = int(np.argmin(lams))
print("λ:", [f"{x:.3e}" for x in sorted(lams)[:4]], "imin", idx, "lam0", lams[idx])
v = np.array([float(ev[1][i, idx]) for i in range(NP)])
if v[0] < 0:
    v = -v

print(f"{'y':>6} {'Θ':>12} {'-ln|Θ|':>8} {'y e^y':>8} {'r':>8}")
for yf in np.linspace(0.15, float(L) * 0.92, 14):
    y = mp.mpf(float(yf))
    t = sum(v[n] * v[m] * float(theta(n, m, y)) for n in range(NP) for m in range(NP))
    yey = yf * math.exp(yf)
    if t > 0:
        nlt = -math.log(t)
        print(f"{yf:6.3f} {t:12.3e} {nlt:8.3f} {yey:8.3f} {nlt/yey:8.3f}")
    else:
        print(f"{yf:6.3f} {t:12.3e}   (non pos)")
