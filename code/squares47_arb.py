# Certified 5x5 block of Q^pr - Q^z at mu=11, even window.
# Qpr in Arb balls (same engine as positivite_certifiee.py).
# Qz = sum_{|gamma|<=G} 2 hat_n(gamma) hat_m(gamma), zeros as Arb
# with explicit tail radius from squares_tail.py envelope.
# Usage: python3 squares47_arb.py [N0]
import os, sys, time, pickle, math
from flint import arb, acb, ctx

BASE = os.path.dirname(os.path.abspath(__file__))
N0 = int(sys.argv[1]) if len(sys.argv) > 1 else 4
NP = N0 + 1
ctx.dps = 50
t0 = time.time()

Larb = arb(11).log()
om = [2 * arb.pi() * n / Larb for n in range(NP)]
euler = arb("0.577215664901532860606512090082402431042159335939", 1e-45)
CR = euler + (4 * arb.pi() * (Larb.exp() - 1) / (Larb.exp() + 1)).log()
eps = arb("1e-30")


def th(n, m, y):
    if n == 0 and m == 0:
        return 2 * (Larb - y) / Larb
    if n == 0 or m == 0:
        j = max(n, m)
        return -2 * (om[j] * y).sin() / (arb(2).sqrt() * arb.pi() * j)
    if n == m:
        return 2 * ((Larb - y) * (om[n] * y).cos() / Larb - (om[n] * y).sin() / (2 * arb.pi() * n))
    return 2 * (n * (om[n] * y).sin() - m * (om[m] * y).sin()) / (arb.pi() * (m * m - n * n))


primes = [2, 3, 5, 7]
towers = []
for p in primes:
    k = 1
    while p ** k <= 11:
        towers.append((arb(p ** k).log(), arb(p).log() / arb(p ** k).sqrt()))
        k += 1

Qpr = {}
for n in range(NP):
    for m in range(n, NP):
        F0 = arb(2) if n == m else arb(0)
        pol = acb.integral(lambda y, _: th(n, m, y) * ((y / 2).exp() + (-y / 2).exp()), 0, Larb).real
        ig = acb.integral(
            lambda y, _: ((y / 2).exp() * th(n, m, y) - F0) / (y.exp() - (-y).exp()),
            eps, Larb,
        ).real
        ar = -(F0 / 2 * CR + ig + arb(0, 1e-25 * (n + m + 2)))
        tw = sum((w * th(n, m, acb(x)).real for x, w in towers), arb(0))
        Qpr[n, m] = pol + ar - tw
print(f'[{time.time()-t0:.0f}s] Qpr balls, max rad {max(float(Qpr[k].rad()) for k in Qpr):.1e}')


def hat(n, g):
    if n == 0:
        return 2 * (g * Larb / 2).sin() / (g * Larb.sqrt())
    return 2 * (arb(2) / Larb).sqrt() * g * (g * Larb / 2).sin() / (g * g - om[n] * om[n])


def load_zeros():
    hp = os.path.join(BASE, 'zeros_zeta_90_hp.pkl')
    long_path = os.path.join(BASE, 'zeros500.pkl')
    if not os.path.exists(long_path):
        long_path = os.path.join(BASE, 'zeros280.pkl')
    long = pickle.load(open(long_path, 'rb'))
    out = []
    if os.path.exists(hp):
        for z in pickle.load(open(hp, 'rb')):
            # 85-digit strings: radius 1e-80
            out.append(arb(str(z), 1e-80))
        last = float(out[-1].mid())
        for z in long:
            if float(z) > last + 1e-6:
                # float64 tail: relative ~2e-16, give 1e-12 abs
                out.append(arb(str(float(z)), 1e-12))
    else:
        for z in long:
            out.append(arb(str(float(z)), 1e-12))
    return out


zs = load_zeros()
Gcut = float(zs[-1].mid())
print(f'[{time.time()-t0:.0f}s] {len(zs)} zeros, Gcut={Gcut:.1f}')

# unsigned envelope tail, same as squares_tail.py
L = float(Larb.mid())
wmax = 2 * math.pi * N0 / L
c = 4.0 / math.sqrt(L)


def tail_diag(G):
    lg = math.log(G / (2 * math.pi))
    integ = (lg + 1) / (2 * math.pi) / G + 1.0 / G
    return 2 * (c ** 2) * integ


def signed_tail(G):
    avg = 1.0 / G
    osc = abs(math.sin(L * G) / (L * G))
    return (4.0 / L) * (avg + osc)

tail_u = tail_diag(Gcut)
tail = signed_tail(Gcut)
print(f'unsigned envelope <= {tail_u:.4e}')
print(f'signed   envelope <= {tail:.4e}')

Qz = {}
for n in range(NP):
    for m in range(n, NP):
        s = arb(0)
        for g in zs:
            s += 2 * hat(n, g) * hat(m, g)
        # signed tail: shift mid by the 1/G average, radius = 1.5 * signed envelope
        avg = arb((4.0 / L) / Gcut)
        Qz[n, m] = s + avg + arb(0, 1.5 * tail)
print(f'[{time.time()-t0:.0f}s] Qz balls + signed tail (mid shift {float(avg):.4e}, rad {1.5*tail:.4e})')

print()
print(f'{"n":>2} {"m":>2} {"Qpr mid":>14} {"Qz mid":>14} {"diff mid":>12} {"|diff|+rad":>12} {"0 in ball":>9}')
max_up = 0.0
all_contain = True
for n in range(NP):
    for m in range(n, NP):
        d = Qpr[n, m] - Qz[n, m]
        up = abs(float(d.mid())) + float(d.rad())
        contains = (float(d.mid()) - float(d.rad()) <= 0 <= float(d.mid()) + float(d.rad()))
        all_contain = all_contain and contains
        max_up = max(max_up, up)
        print(f'{n:2d} {m:2d} {float(Qpr[n,m].mid()):14.6e} {float(Qz[n,m].mid()):14.6e} '
              f'{float(d.mid()):12.4e} {up:12.4e} {"yes" if contains else "NO":>9}')

print()
print(f'max certified |Qpr-Qz| upper bound = {max_up:.4e}')
print(f'0 in every difference ball: {all_contain}')
print(f'done {time.time()-t0:.0f}s')
