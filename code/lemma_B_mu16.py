# B1/B2 at mu=16: assemble Q, restrict each tower T_p to the first R
# eigenvectors, print 2x2 minors. mpmath, zeta, even window.
# Usage: python3 lemma_B_mu16.py [NB] [R]
import sys, time
import mpmath as mp

NB = int(sys.argv[1]) if len(sys.argv) > 1 else 28
R = int(sys.argv[2]) if len(sys.argv) > 2 else 8
mp.mp.dps = 40
t0 = time.time()
mu = 16
L = mp.log(mu)
NP = NB + 1
om = [2*mp.pi*n/L for n in range(NP)]
EU = mp.euler
CR = EU + mp.log(4*mp.pi*(mp.e**L - 1)/(mp.e**L + 1))

def theta(n, m, y):
    if n == 0 and m == 0:
        return 2*(L-y)/L
    if n == 0 or m == 0:
        j = max(n, m)
        return -2*mp.sin(om[j]*y)/(mp.sqrt(2)*mp.pi*j)
    if n == m:
        return 2*((L-y)*mp.cos(om[n]*y)/L - mp.sin(om[n]*y)/(2*mp.pi*n))
    return 2*(n*mp.sin(om[n]*y) - m*mp.sin(om[m]*y))/(mp.pi*(m*m-n*n))

primes = [p for p in (2, 3, 5, 7, 11, 13) if p < mu]
towers = {p: [] for p in primes}
for p in primes:
    k = 1
    while p**k < mu - 1e-12:
        towers[p].append((mp.log(p**k), mp.log(p)/mp.sqrt(p**k)))
        k += 1

# assemble Q and T_p
Q = mp.matrix(NP)
Tp = {p: mp.matrix(NP) for p in primes}
for n in range(NP):
    for m in range(n, NP):
        F0 = mp.mpf(2) if n == m else mp.mpf(0)
        pol = mp.quad(lambda y: theta(n, m, y)*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
        ig = mp.quad(lambda y: (mp.e**(y/2)*theta(n, m, y)-F0)/(mp.e**y-mp.e**(-y)), [0, L])
        ar = -(F0/2*CR + ig)
        tw = mp.mpf(0)
        for p in primes:
            tp = mp.fsum(w*theta(n, m, lg) for lg, w in towers[p])
            Tp[p][n, m] = tp
            Tp[p][m, n] = tp
            tw += tp
        Q[n, m] = pol + ar - tw
        Q[m, n] = Q[n, m]
print(f'[{time.time()-t0:.0f}s] Q assembled dim={NP} primes={primes}')

E, V = mp.eigsy(Q)
ell = [float(-mp.log(abs(E[i]))) if E[i] != 0 else 0.0 for i in range(min(R+2, NP))]
print('ell[:R+2]', [round(x, 2) for x in ell])

# columns of V are eigenvectors; take first R (smallest eigenvalues)
def restrict(M, V, R):
    # M_R = V_R^T M V_R
    out = mp.matrix(R)
    for i in range(R):
        for j in range(i, R):
            s = mp.mpf(0)
            for a in range(NP):
                for b in range(NP):
                    s += V[a, i]*M[a, b]*V[b, j]
            out[i, j] = s
            out[j, i] = s
    return out

print(f'\n{"p":>4} {"j":>3} {"k":>3} {"Mjj":>9} {"Mkk":>9} {"Mjk":>9} {"det2":>9} best_det pair')
ok = 0
for p in primes:
    Mr = restrict(Tp[p], V, R)
    silent = min(range(R), key=lambda i: abs(float(Mr[i, i])))
    speak = max([k for k in range(R) if k != silent],
                key=lambda k: abs(float(Mr[silent, k])))
    best = None
    for i in range(R):
        for k in range(i + 1, R):
            det = float(Mr[i, i]) * float(Mr[k, k]) - float(Mr[i, k]) ** 2
            if best is None or det < best[0]:
                best = (det, i, k, float(Mr[i, i]), float(Mr[k, k]), float(Mr[i, k]))
    mjj = float(Mr[silent, silent])
    mkk = float(Mr[speak, speak])
    mjk = float(Mr[silent, speak])
    det2 = mjj * mkk - mjk * mjk
    flag = 'yes' if best[0] < -0.02 else 'no'
    if flag == 'yes':
        ok += 1
    print(f'{p:4d} {silent:3d} {speak:3d} {mjj:9.4f} {mkk:9.4f} {mjk:9.4f} {det2:9.4f} '
          f'{best[0]:8.4f} ({best[1]},{best[2]}) {flag}')
print(f'{ok}/{len(primes)} primes have a negative 2x2 on the R={R} radical  ({time.time()-t0:.0f}s)')
