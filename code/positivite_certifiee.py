# Positivite de Weil certifiee sur la fenetre mu=11 : Q > 0 par congruence + Gershgorin + Sylvester.
# Methode : entrees de Q en boules Arb (dps 90, rayons <= 1e-55) ; V = vecteurs propres flottants
# (mpmath dps 100, precision INDIFFERENTE a la rigueur) ; M = V^T Q V certifiee en boules ;
# M strictement diagonale-dominante positive => M > 0 => V inversible => Q > 0 (Sylvester).
# Ligne critique = le rasoir : M_00 = 3.58317e-48 +/- 3e-54, hors-diag <= 8.5e-54. ~150 s.
import time
import mpmath as mp
from flint import arb, acb, ctx
t0 = time.time()
ctx.dps = 90
NB = 46; NP = NB + 1
Larb = arb(11).log()
om = [2*arb.pi()*n/Larb for n in range(NP)]
def th(n, m, y):
    if n == 0 and m == 0: return 2*(Larb - y)/Larb
    if n == 0 or m == 0:
        j = max(n, m); return -2*(om[j]*y).sin()/(arb(2).sqrt()*arb.pi()*j)
    if n == m: return 2*((Larb - y)*(om[n]*y).cos()/Larb - (om[n]*y).sin()/(2*arb.pi()*n))
    return 2*(n*(om[n]*y).sin() - m*(om[m]*y).sin())/(arb.pi()*(m*m - n*n))
euler = arb("0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369", 1e-86)
CR = euler + (4*arb.pi()*(Larb.exp()-1)/(Larb.exp()+1)).log()
eps = arb("1e-60")
primes = [2,3,5,7,11]
towers = {p: [(arb(p**k).log(), arb(p).log()/arb(p**k).sqrt()) for k in range(1,9) if p**k <= 11] for p in primes}
Q = {}
for n in range(NP):
    for m in range(n, NP):
        F0 = arb(2) if n == m else arb(0)
        pol = acb.integral(lambda y,_: th(n,m,y)*((y/2).exp()+(-y/2).exp()), 0, Larb).real
        ig = acb.integral(lambda y,_: ((y/2).exp()*th(n,m,y)-F0)/(y.exp()-(-y).exp()), eps, Larb).real
        ar = -(F0/2*CR + ig + arb(0, 1e-60*1000*(n+m+2)))
        tw = sum((sum((w*th(n,m,acb(x)).real for x,w in towers[p]), arb(0)) for p in primes), arb(0))
        Q[(n,m)] = pol + ar - tw
print(f"[{time.time()-t0:.0f}s] rayon max entree = {max(float(Q[k].rad()) for k in Q):.1e}")
g = lambda n,m: Q[(n,m)] if n <= m else Q[(m,n)]
mp.mp.dps = 100
Qf = mp.matrix(NP, NP)
for n in range(NP):
    for m in range(NP):
        Qf[n,m] = mp.mpf(g(n,m).mid().str(95, radius=False))
E, V = mp.eigsy(Qf)
print(f"[{time.time()-t0:.0f}s] lambda_min flottant = {mp.nstr(E[0],4)}")
Va = [[arb(mp.nstr(V[i,k], 95)) for k in range(NP)] for i in range(NP)]
QV = [[sum((g(i,j)*Va[j][k] for j in range(NP)), arb(0)) for k in range(NP)] for i in range(NP)]
worst = None
for k in range(NP):
    Mkk = sum((Va[i][k]*QV[i][k] for i in range(NP)), arb(0))
    off = arb(0)
    for l in range(NP):
        if l == k: continue
        Mkl = sum((Va[i][k]*QV[i][l] for i in range(NP)), arb(0))
        off += abs(Mkl.mid()) + Mkl.rad()
    lo = float((Mkk - off).mid()) - float((Mkk - off).rad())
    if worst is None or lo < worst[0]: worst = (lo, k)
    if lo <= 0:
        print(f"ligne {k} NON certifiee ({lo:.2e})"); raise SystemExit(1)
print(f"[{time.time()-t0:.0f}s] CERTIFIE : Q(mu=11) definie positive (pire marge Gershgorin {worst[0]:.2e}, ligne {worst[1]})")
