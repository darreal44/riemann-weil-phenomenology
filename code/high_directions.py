# High squares of Q vs zero evaluators chat(gamma_k).
# The grail hook after MUSIC-from-the-radical: do the TOP eigendirections
# of the prime-side Q line up with chat(gamma_k)?
# Usage: python3 high_directions.py [N0]
import os, sys, time, pickle
import mpmath as mp

BASE = os.path.dirname(os.path.abspath(__file__))
N0 = int(sys.argv[1]) if len(sys.argv) > 1 else 12
mp.mp.dps = 35
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
# eigsy: ascending eigenvalues
print('lambda[:4]', [mp.nstr(E[i], 3) for i in range(4)])
print('lambda[-4:]', [mp.nstr(E[NP - 1 - i], 3) for i in range(4)])


def hat(n, g):
    if n == 0:
        return 2 * mp.sin(g * L / 2) / (g * mp.sqrt(L)) if g else mp.sqrt(L)
    return 2 * mp.sqrt(2 / L) * g * mp.sin(g * L / 2) / (g * g - om[n] * om[n])


zs = [mp.mpf(z) for z in pickle.load(open(os.path.join(BASE, 'zeros_zeta_90_hp.pkl'), 'rb'))]
K = min(12, len(zs))
chats = []
for k in range(K):
    c = [hat(n, zs[k]) for n in range(NP)]
    nrm = mp.sqrt(mp.fsum(x * x for x in c))
    chats.append([x / nrm for x in c])

print(f'\n{"k":>3} {"gamma":>10} {"best_top":>9} {"cos":>8} {"best_bot":>9} {"cos":>8} {"||chat||":>10}')
align_top = []
for k in range(K):
    best_t, ct = None, -1
    best_b, cb = None, -1
    nrm_raw = mp.sqrt(mp.fsum(hat(n, zs[k]) ** 2 for n in range(NP)))
    for j in range(NP):
        # column j of V
        cos = abs(mp.fsum(V[n, j] * chats[k][n] for n in range(NP)))
        if j >= NP - 6:  # six largest
            if cos > ct:
                ct, best_t = float(cos), j
        if j < 6:  # six smallest
            if cos > cb:
                cb, best_b = float(cos), j
    # also global best
    glob = max(range(NP), key=lambda j: abs(float(mp.fsum(V[n, j] * chats[k][n] for n in range(NP)))))
    gcos = abs(float(mp.fsum(V[n, glob] * chats[k][n] for n in range(NP))))
    align_top.append((k, float(zs[k]), best_t, ct, glob, gcos))
    print(f'{k+1:3d} {float(zs[k]):10.4f} {best_t:9d} {ct:8.4f} {best_b:9d} {cb:8.4f} {float(nrm_raw):10.3f}  glob={glob} {gcos:.4f}')

print('\nTop-6 eigendirections (largest lambda) vs nearest zero evaluator:')
for j in range(NP - 1, NP - 7, -1):
    best, bc = None, -1
    for k in range(K):
        cos = abs(float(mp.fsum(V[n, j] * chats[k][n] for n in range(NP))))
        if cos > bc:
            bc, best = cos, k
    print(f'  eig {j:2d}  lambda={mp.nstr(E[j], 4)}  -> gamma_{best+1}={float(zs[best]):.4f}  cos={bc:.4f}')
print(f'done {time.time()-t0:.0f}s')
