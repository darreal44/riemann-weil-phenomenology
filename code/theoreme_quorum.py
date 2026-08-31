# Certification Arb du quorum a mu=11 : 15 temoins de Rayleigh certifies negatifs.
# Usage : python3 theoreme_quorum.py   (7 s ; requiert python-flint)
# Statut : preuve calculee, redaction (phase 3) en attente — table theta a deriver en appendice.
import numpy as np, time, itertools
from flint import arb, acb, ctx
ctx.dps = 22
NB = 46; NP = NB + 1
Larb = arb(11).log()
om = [2*arb.pi()*n/Larb for n in range(NP)]
def th_arb(n, m, y):
    if n == 0 and m == 0: return 2*(Larb - y)/Larb
    if n == 0 or m == 0:
        j = max(n, m); return -2*(om[j]*y).sin()/(arb(2).sqrt()*arb.pi()*j)
    if n == m: return 2*((Larb - y)*(om[n]*y).cos()/Larb - (om[n]*y).sin()/(2*arb.pi()*n))
    return 2*(n*(om[n]*y).sin() - m*(om[m]*y).sin())/(arb.pi()*(m*m - n*n))
euler = arb("0.577215664901532860606512090082402431042159335939", 1e-45)
CR = euler + (4*arb.pi()*(Larb.exp()-1)/(Larb.exp()+1)).log()
eps = arb("1e-15")
P = {}; A = {}; T = {p: {} for p in [2,3,5,7,11]}
towers = {p: [(arb(p**k).log(), arb(p).log()/arb(p**k).sqrt()) for k in range(1,8) if p**k <= 11] for p in [2,3,5,7,11]}
for n in range(NP):
    for m in range(n, NP):
        F0 = arb(2) if n == m else arb(0)
        P[(n,m)] = acb.integral(lambda y,_: th_arb(n,m,y)*((y/2).exp()+(-y/2).exp()), 0, Larb).real
        integ = acb.integral(lambda y,_: ((y/2).exp()*th_arb(n,m,y)-F0)/(y.exp()-(-y).exp()), eps, Larb).real
        A[(n,m)] = -(F0/2*CR + integ + arb(0, float(eps)*1000*(n+m+2)))
        for p in T: T[p][(n,m)] = -sum((w*th_arb(n,m,acb(x)).real for x,w in towers[p]), arb(0))
g = lambda C,n,m: C[(n,m)] if n <= m else C[(m,n)]
Pf = np.array([[float(g(P,n,m).mid()) for m in range(NP)] for n in range(NP)])
Af = np.array([[float(g(A,n,m).mid()) for m in range(NP)] for n in range(NP)])
Tf = {p: np.array([[float(g(T[p],n,m).mid()) for m in range(NP)] for n in range(NP)]) for p in T}
for r in range(4+1):
    for sub in itertools.combinations([2,3,5,7], r):
        Sf = Pf + Af + Tf[11] + sum((Tf[p] for p in sub), np.zeros((NP,NP)))
        w = np.linalg.eigh(0.5*(Sf+Sf.T))[1][:, 0]
        num = arb(0)
        for n in range(NP):
            wn = arb(float(w[n]))
            num += wn*wn*(g(P,n,n)+g(A,n,n)+g(T[11],n,n)+sum((g(T[p],n,n) for p in sub), arb(0)))
            for m in range(n+1, NP):
                num += 2*wn*arb(float(w[m]))*(g(P,n,m)+g(A,n,m)+g(T[11],n,m)+sum((g(T[p],n,m) for p in sub), arb(0)))
        up = float(num.mid()) + float(num.rad())
        print(f"S = {str(set(sub) if sub else '{}'):15s} : Q_S(w) <= {up:+.4f}  " + ("CERTIFIE < 0" if up < 0 else "non certifiable (complet)"))
