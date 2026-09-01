# Prime-side vs zero-side identity on V at mu=11.
# Q^pr from pole + archimedean - towers; Q^z = sum_gamma hat(eta_n)(g) hat(eta_m)(g).
# Usage: python3 squares47.py [N0]     N0 = last basis index (default 6; 46 = full 47-dim)
import sys, time, pickle, os
import mpmath as mp
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
N0 = int(sys.argv[1]) if len(sys.argv) > 1 else 6
mp.mp.dps = 40
t0 = time.time()
L = mp.log(11)
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

Qpr = mp.matrix(NP)
for n in range(NP):
    for m in range(n, NP):
        F0 = mp.mpf(2) if n == m else mp.mpf(0)
        pol = mp.quad(lambda y: theta(n, m, y) * (mp.e**(y / 2) + mp.e**(-y / 2)), [0, L])
        ig = mp.quad(lambda y: (mp.e**(y / 2) * theta(n, m, y) - F0) / (mp.e**y - mp.e**(-y)), [0, L])
        ar = -(F0 / 2 * CR + ig)
        tw = mp.fsum(w * theta(n, m, lg) for lg, w in towers)
        Qpr[n, m] = pol + ar - tw
        Qpr[m, n] = Qpr[n, m]
print(f'[{time.time()-t0:.0f}s] Qpr assembled, dim={NP}')

def hat(n, g):
    if n == 0:
        return 2 * mp.sin(g * L / 2) / (g * mp.sqrt(L)) if g else mp.sqrt(L)
    return 2 * mp.sqrt(2 / L) * g * mp.sin(g * L / 2) / (g * g - om[n] * om[n])

zs = pickle.load(open(os.path.join(BASE, 'zeros280.pkl'), 'rb'))
Qz = mp.matrix(NP)
for n in range(NP):
    for m in range(n, NP):
        # even window: each positive gamma is paired with -gamma, same hats
        Qz[n, m] = 2 * mp.fsum(hat(n, mp.mpf(g)) * hat(m, mp.mpf(g)) for g in zs)
        Qz[m, n] = Qz[n, m]
print(f'[{time.time()-t0:.0f}s] Qz assembled from {len(zs)} zeros, gamma_last={zs[-1]:.1f}')

absdiff = max(abs(float(Qpr[n, m] - Qz[n, m])) for n in range(NP) for m in range(n, NP))
reldiag = max(abs(float((Qpr[n, n] - Qz[n, n]) / Qpr[n, n])) for n in range(NP) if Qpr[n, n] != 0)
print(f'max |Qpr-Qz| on upper triangle = {absdiff:.3e}')
print(f'max relative |diag Qpr-Qz|     = {reldiag:.3e}')
print('diag Qpr:', [mp.nstr(Qpr[n, n], 5) for n in range(min(NP, 6))])
print('diag Qz :', [mp.nstr(Qz[n, n], 5) for n in range(min(NP, 6))])
print(f'done in {time.time()-t0:.0f}s')
