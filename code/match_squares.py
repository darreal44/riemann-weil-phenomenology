# 1-1 assignment of top eigendirections of Q to zero evaluators.
# Greedy: largest unused cosine, no reuse of eig or zero.
# Usage: python3 match_squares.py [N0]
import os, sys, time, pickle
import mpmath as mp

BASE = os.path.dirname(os.path.abspath(__file__))
N0 = int(sys.argv[1]) if len(sys.argv) > 1 else 12
mp.mp.dps = 30
t0 = time.time()
L = mp.log(11)
NP = N0 + 1
om = [2 * mp.pi * n / L for n in range(NP)]
CR = mp.euler + mp.log(4 * mp.pi * (mp.e**L - 1) / (mp.e**L + 1))

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
    while p**k <= 11:
        towers.append((mp.log(p**k), mp.log(p)/mp.sqrt(p**k))); k += 1

Q = mp.matrix(NP)
for n in range(NP):
    for m in range(n, NP):
        F0 = mp.mpf(2) if n == m else mp.mpf(0)
        pol = mp.quad(lambda y: theta(n, m, y)*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
        ig = mp.quad(lambda y: (mp.e**(y/2)*theta(n,m,y)-F0)/(mp.e**y-mp.e**(-y)), [0, L])
        tw = mp.fsum(w*theta(n,m,lg) for lg,w in towers)
        Q[n,m] = pol-(F0/2*CR+ig)-tw; Q[m,n]=Q[n,m]
E, V = mp.eigsy(Q)

def hat(n, g):
    if n == 0:
        return 2*mp.sin(g*L/2)/(g*mp.sqrt(L))
    return 2*mp.sqrt(2/L)*g*mp.sin(g*L/2)/(g*g-om[n]*om[n])

zs = [mp.mpf(z) for z in pickle.load(open(os.path.join(BASE,'zeros_zeta_90_hp.pkl'),'rb'))]
wmax = float(om[-1])
inband = [z for z in zs if float(z) < wmax]
K = min(len(inband), 8)
chats = []
for k in range(K):
    c = [hat(n, inband[k]) for n in range(NP)]
    nrm = mp.sqrt(mp.fsum(x*x for x in c))
    chats.append([x/nrm for x in c])

# cosine matrix: rows = top K eigs (largest lambda), cols = first K in-band zeros
top = list(range(NP-1, NP-1-K, -1))
C = [[abs(float(mp.fsum(V[n,j]*chats[k][n] for n in range(NP)))) for k in range(K)] for j in top]

# greedy 1-1
used_e, used_z = set(), set()
pairs = []
flat = sorted(((C[a][b], a, b) for a in range(K) for b in range(K)), reverse=True)
for cos, a, b in flat:
    if a in used_e or b in used_z:
        continue
    used_e.add(a); used_z.add(b)
    pairs.append((top[a], float(E[top[a]]), b+1, float(inband[b]), cos))

print(f'N={NP} wmax={wmax:.1f} K={K}  [{time.time()-t0:.0f}s]')
print(f'{"eig":>4} {"lambda":>10} {"-> k":>5} {"gamma":>10} {"cos":>8}')
for eig, lam, k, g, cos in pairs:
    print(f'{eig:4d} {lam:10.4f} {k:5d} {g:10.4f} {cos:8.4f}')
print('mean cos', sum(p[-1] for p in pairs)/len(pairs))
print('min cos', min(p[-1] for p in pairs))
