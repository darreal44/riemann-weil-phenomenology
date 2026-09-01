# B1/B2 on a depth-adequate Dirichlet window: chi_{-8} at mu=16.
# Usage: python3 lemma_B_chi.py [name] [mu] [NB]
import os, sys, time
import mpmath as mp
import numpy.polynomial.legendre as NL
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kronecker import chi_tab

name = sys.argv[1] if len(sys.argv) > 1 else 'chim8'
mu = float(sys.argv[2]) if len(sys.argv) > 2 else 16.0
NB = int(sys.argv[3]) if len(sys.argv) > 3 else 28
R = 8
CHARS = {
    'chim8': dict(q=8,  d=-8,  a=1),
    'chi20': dict(q=20, d=-20, a=1),
    'chi23': dict(q=23, d=-23, a=1),
    'chi3':  dict(q=3,  d=-3,  a=1),
}
cf = CHARS[name]
q, a = cf['q'], cf['a']
tab = chi_tab(cf['d'], q)
mp.mp.dps = 42
t0 = time.time()
L = mp.log(mp.mpf(mu))
s0 = mp.mpf(1)/4 + mp.mpf(a)/2
om = [2*mp.pi*n/L for n in range(NB+1)]
DEG = 12
xr0, _ = NL.leggauss(DEG)
xr, wr = [], []
for x0 in xr0:
    x = mp.mpf(float(x0))
    for _ in range(5):
        P = mp.legendre(DEG, x); Pm = mp.legendre(DEG-1, x)
        dP = DEG*(x*P - Pm)/(x*x - 1); x = x - P/dP
    P = mp.legendre(DEG, x); Pm = mp.legendre(DEG-1, x)
    dP = DEG*(x*P - Pm)/(x*x - 1)
    xr.append(x); wr.append(2/((1-x*x)*dP*dP))
NPANEL = 3*NB + 12
nodes, wts = [], []
for p in range(NPANEL):
    aa, bb = L*p/NPANEL, L*(p+1)/NPANEL; h = (bb-aa)/2
    for x, w in zip(xr, wr):
        nodes.append(aa + h*(x+1)); wts.append(w*h)
K = len(nodes)
SIN = [[mp.sin(om[n]*y) for y in nodes] for n in range(NB+1)]
COS = [[mp.cos(om[n]*y) for y in nodes] for n in range(NB+1)]
LY = [(L-y)/L for y in nodes]
D2 = [wts[k]*2*mp.e**(-2*s0*nodes[k])/(1-mp.e**(-2*nodes[k])) for k in range(K)]
EC = [mp.e**(-(2-2*s0)*nodes[k]) for k in range(K)]
CST = mp.log(mp.mpf(q)/mp.pi) - mp.euler - mp.log(1-mp.e**(-2*L))

def th_nodes(n, m):
    if n==0 and m==0: return [2*LY[k] for k in range(K)], mp.mpf(2)
    if n==0 or m==0:
        j=max(n,m); a2=-2/(mp.sqrt(2)*mp.pi*j)
        return [a2*SIN[j][k] for k in range(K)], mp.mpf(0)
    if n==m:
        return [2*(LY[k]*COS[n][k]-SIN[n][k]/(2*mp.pi*n)) for k in range(K)], mp.mpf(2)
    a2=2/(mp.pi*(m*m-n*n))
    return [a2*(n*SIN[n][k]-m*SIN[m][k]) for k in range(K)], mp.mpf(0)

def th_at(n, m, y):
    if n==0 and m==0: return 2*(L-y)/L
    if n==0 or m==0:
        j=max(n,m); return -2*mp.sin(om[j]*y)/(mp.sqrt(2)*mp.pi*j)
    if n==m: return 2*((L-y)*mp.cos(om[n]*y)/L-mp.sin(om[n]*y)/(2*mp.pi*n))
    return 2*(n*mp.sin(om[n]*y)-m*mp.sin(om[m]*y))/(mp.pi*(m*m-n*n))

# prime powers p^k < mu with chi(p^k) != 0
small = [2,3,5,7,11,13,17,19,23,29,31]
cap = int(float(mp.e**L)+1e-9)
towers = {}
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
        towers.setdefault(p, []).append((mp.log(x), tab[x % q]*mp.log(p)/mp.sqrt(x)))
    x += 1
primes = sorted(towers)
print(f'{name} mu={mu} primes={primes} towers={[ (p,len(towers[p])) for p in primes ]}')

NP = NB+1
S = mp.matrix(NP)
Tp = {p: mp.matrix(NP) for p in primes}
for n in range(NP):
    for m in range(n, NP):
        th, F0 = th_nodes(n, m)
        arch = F0/2*CST + mp.mpf('0.5')*mp.fsum(D2[k]*(F0*EC[k]-th[k]) for k in range(K))
        tw = mp.mpf(0)
        for p in primes:
            tp = mp.fsum(w*th_at(n,m,lg) for lg,w in towers[p])
            Tp[p][n,m] = tp; Tp[p][m,n] = tp
            tw += tp
        S[n,m] = arch - tw; S[m,n] = S[n,m]
E, V = mp.eigsy(S)
ell = [float(-mp.log(abs(E[i]))) if E[i] != 0 else 0 for i in range(min(R+2, NP))]
print(f'[{time.time()-t0:.0f}s] ell={ [round(x,2) for x in ell] }')

def restrict(M, V, R):
    out = mp.matrix(R)
    for i in range(R):
        for j in range(i, R):
            s = mp.mpf(0)
            for a in range(NP):
                for b in range(NP):
                    s += V[a,i]*M[a,b]*V[b,j]
            out[i,j] = s; out[j,i] = s
    return out

print(f'\n{"p":>4} {"j":>3} {"k":>3} {"Mjj":>9} {"Mkk":>9} {"Mjk":>9} {"det2":>9} B1 B2')
ok = 0
for p in primes:
    Mr = restrict(Tp[p], V, R)
    # silent = min |diag|, speak = max |M_silent,*|
    silent = min(range(R), key=lambda i: abs(float(Mr[i,i])))
    speak = max([k for k in range(R) if k != silent], key=lambda k: abs(float(Mr[silent,k])))
    # also report best indefinite pair
    best = None
    for i in range(R):
        for k in range(i+1, R):
            det = float(Mr[i,i])*float(Mr[k,k]) - float(Mr[i,k])**2
            if best is None or det < best[0]:
                best = (det, i, k, float(Mr[i,i]), float(Mr[k,k]), float(Mr[i,k]))
    mjj, mkk, mjk = float(Mr[silent,silent]), float(Mr[speak,speak]), float(Mr[silent,speak])
    det2 = mjj*mkk - mjk*mjk
    b1 = abs(mjj) < 0.2
    b2 = abs(mjk) > 0.12
    flag = 'yes' if (b1 and b2) or best[0] < -0.02 else 'no'
    if flag == 'yes':
        ok += 1
    print(f'{p:4d} {silent:3d} {speak:3d} {mjj:9.4f} {mkk:9.4f} {mjk:9.4f} {det2:9.4f} '
          f'{"y" if b1 else "n":>2} {"y" if b2 else "n":>2}  best_det={best[0]:.4f} pair=({best[1]},{best[2]}) {flag}')
print(f'{ok}/{len(primes)} primes have a negative 2x2 on the R={R} radical  ({time.time()-t0:.0f}s)')
