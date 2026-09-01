# Endpoint law C = |vhat_0(gamma1)| / lambda_0 on the zeta mu=11 block.
# Also a finite-zero check of Prop A: G.vhat vs (lambda/2).vhat.
# Usage: python3 endpoint_C.py [N0]
import os, sys, time, pickle
import mpmath as mp

BASE = os.path.dirname(os.path.abspath(__file__))
N0 = int(sys.argv[1]) if len(sys.argv) > 1 else 8
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


towers = []
for p in (2, 3, 5, 7):
    k = 1
    while p ** k <= 11:
        towers.append((mp.log(p ** k), mp.log(p) / mp.sqrt(p ** k)))
        k += 1

Q = mp.matrix(NP)
for n in range(NP):
    for m in range(n, NP):
        F0 = mp.mpf(2) if n == m else mp.mpf(0)
        pol = mp.quad(lambda y: theta(n, m, y) * (mp.e ** (y / 2) + mp.e ** (-y / 2)), [0, L])
        ig = mp.quad(lambda y: (mp.e ** (y / 2) * theta(n, m, y) - F0) / (mp.e ** y - mp.e ** (-y)), [0, L])
        tw = mp.fsum(w * theta(n, m, lg) for lg, w in towers)
        Q[n, m] = pol - (F0 / 2 * CR + ig) - tw
        Q[m, n] = Q[n, m]
print(f'[{time.time()-t0:.0f}s] Qpr dim={NP}')

E, V = mp.eigsy(Q)
lam0 = E[0]
v = [V[n, 0] for n in range(NP)]
print(f'lambda0={mp.nstr(lam0, 5)}  ell0={float(-mp.log(abs(lam0))):.2f}')


def hat(n, g):
    if n == 0:
        return 2 * mp.sin(g * L / 2) / (g * mp.sqrt(L)) if g else mp.sqrt(L)
    return 2 * mp.sqrt(2 / L) * g * mp.sin(g * L / 2) / (g * g - om[n] * om[n])


hp = os.path.join(BASE, 'zeros_zeta_90_hp.pkl')
zs = [mp.mpf(z) for z in pickle.load(open(hp, 'rb'))]
print(f'{len(zs)} hp zeros, g1={float(zs[0]):.6f}  glast={float(zs[-1]):.1f}')


def vhat(g):
    return mp.fsum(v[n] * hat(n, g) for n in range(NP))


vh = [vhat(g) for g in zs]
c = abs(float(vh[0] / lam0))
print(f'|vhat(g1)|={mp.nstr(abs(vh[0]), 5)}')
print(f'C = |vhat(g1)|/lambda0 = {c:.3f}')
print('first five |vhat(gk)|/lambda0:', [round(abs(float(vh[k] / lam0)), 3) for k in range(5)])

# Prop A on the truncated Gram of these zeros
K = len(zs)
# (G vhat)_j = sum_k <hat(gj), hat(gk)> vhat_k
# <hat(gj),hat(gk)> = sum_n hat_n(gj) hat_n(gk)
hats = [[hat(n, g) for n in range(NP)] for g in zs]
Gv = []
for j in range(min(8, K)):
    s = mp.mpf(0)
    for k in range(K):
        gram = mp.fsum(hats[j][n] * hats[k][n] for n in range(NP))
        s += gram * vh[k]
    Gv.append(s)

print('Prop A (truncated zeros): (G vhat)_j  vs  (lambda0/2) vhat_j')
for j in range(len(Gv)):
    rhs = (lam0 / 2) * vh[j]
    rel = float(abs(Gv[j] - rhs) / (abs(rhs) + mp.mpf('1e-80')))
    print(f'  j={j}  Gv={mp.nstr(Gv[j], 4)}  rhs={mp.nstr(rhs, 4)}  rel={rel:.2e}')
print(f'done {time.time()-t0:.0f}s')
