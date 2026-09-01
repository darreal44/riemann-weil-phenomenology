# Audit of Qpr vs Qz on a single entry at mu=11.
# Usage: python3 audit_00.py
import os, pickle
import mpmath as mp

BASE = os.path.dirname(os.path.abspath(__file__))
mp.mp.dps = 40
L = mp.log(11)
Lf = float(L)
CR = mp.euler + mp.log(4 * mp.pi * (mp.e**L - 1) / (mp.e**L + 1))
om1 = 2 * mp.pi / L


def theta(n, m, y):
    if n == 0 and m == 0:
        return 2 * (L - y) / L
    if n == 0 or m == 0:
        j = max(n, m)
        return -2 * mp.sin(om1 * j * y / j) / (mp.sqrt(2) * mp.pi * j) if False else (
            -2 * mp.sin(om1 * y) / (mp.sqrt(2) * mp.pi) if j == 1 else
            -2 * mp.sin((2 * mp.pi * j / L) * y) / (mp.sqrt(2) * mp.pi * j)
        )
    if n == m:
        return 2 * ((L - y) * mp.cos((2 * mp.pi * n / L) * y) / L
                    - mp.sin((2 * mp.pi * n / L) * y) / (2 * mp.pi * n))
    return 2 * (n * mp.sin((2 * mp.pi * n / L) * y) - m * mp.sin((2 * mp.pi * m / L) * y)) / (
        mp.pi * (m * m - n * n)
    )


def hat(n, g):
    if n == 0:
        return 2 * mp.sin(g * L / 2) / (g * mp.sqrt(L))
    wn = 2 * mp.pi * n / L
    return 2 * mp.sqrt(2 / L) * g * mp.sin(g * L / 2) / (g * g - wn * wn)


towers = []
for p in (2, 3, 5, 7):
    k = 1
    while p**k <= 11:
        towers.append((mp.log(p**k), mp.log(p) / mp.sqrt(p**k)))
        k += 1


def qpr_pieces(n, m):
    F0 = mp.mpf(2) if n == m else mp.mpf(0)
    pol = mp.quad(lambda y: theta(n, m, y) * (mp.e ** (y / 2) + mp.e ** (-y / 2)), [0, L])
    ig = mp.quad(
        lambda y: (mp.e ** (y / 2) * theta(n, m, y) - F0) / (mp.e**y - mp.e ** (-y)), [0, L]
    )
    ar = -(F0 / 2 * CR + ig)
    tw = mp.fsum(w * theta(n, m, lg) for lg, w in towers)
    return pol, ar, tw, pol + ar - tw


zs = [mp.mpf(z) for z in pickle.load(open(os.path.join(BASE, 'zeros500.pkl'), 'rb'))]
Gcut = float(zs[-1])


def qz_cut(n, m):
    return mp.fsum(2 * hat(n, g) * hat(m, g) for g in zs)


def tail_rho(pref):
    # int_G^inf pref * rho(t) / t^2 dt, rho = log(t/2pi)/(2pi)
    return pref * mp.quad(
        lambda t: mp.log(t / (2 * mp.pi)) / (2 * mp.pi) / (t * t), [Gcut, mp.inf]
    )


def tail_flat(pref):
    return pref / Gcut


print(f'mu=11 L={Lf:.6f}  Gcut={Gcut:.3f}  nzeros={len(zs)}')
print(f'CR={mp.nstr(CR, 12)}')
print()

# closed form pole 00
pole_cf = 32 * mp.sinh(L / 4) ** 2 / L
print(f'pole_00 closed form {mp.nstr(pole_cf, 12)}')

prefs = {
    (0, 0): 4 / L,
    (0, 1): 4 * mp.sqrt(2) / L,
    (1, 1): 8 / L,
}

for n, m in ((0, 0), (0, 1), (1, 1)):
    pol, ar, tw, qpr = qpr_pieces(n, m)
    qz = qz_cut(n, m)
    pref = prefs[(n, m)]
    tr = tail_rho(pref)
    tf = tail_flat(pref)
    print(f'\n== ({n},{m}) ==')
    print(f'  pole     {mp.nstr(pol, 12)}')
    print(f'  arch     {mp.nstr(ar, 12)}')
    print(f'  towers   {mp.nstr(tw, 12)}')
    print(f'  Qpr      {mp.nstr(qpr, 12)}')
    print(f'  Qz_cut   {mp.nstr(qz, 12)}')
    print(f'  tail rho {mp.nstr(tr, 12)}')
    print(f'  tail 1/G {mp.nstr(tf, 12)}')
    print(f'  Qz+rho   {mp.nstr(qz + tr, 12)}')
    print(f'  Qz+1/G   {mp.nstr(qz + tf, 12)}')
    print(f'  Qpr-(Qz+rho) {mp.nstr(qpr - qz - tr, 6)}')
    print(f'  Qpr-(Qz+1/G) {mp.nstr(qpr - qz - tf, 6)}')
    print(f'  (Qpr-Qz)/Qpr {float((qpr - qz) / qpr):+.4%}')
