import mpmath as mp, time, sys
import numpy.polynomial.legendre as NL

def run(mu, NB, dps, DEG, K=8):
    mp.mp.dps = dps
    t0 = time.time()
    L = mp.log(mu)
    om = [2*mp.pi*n/L for n in range(NB+1)]
    NPANEL = 5*NB + 20
    xr0, _ = NL.leggauss(DEG)
    xr, wr = [], []
    for x0 in xr0:
        x = mp.mpf(float(x0))
        for _ in range(6):
            P_ = mp.legendre(DEG, x); Pm = mp.legendre(DEG-1, x)
            dP = DEG*(x*P_ - Pm)/(x*x - 1); x = x - P_/dP
        P_ = mp.legendre(DEG, x); Pm = mp.legendre(DEG-1, x)
        dP = DEG*(x*P_ - Pm)/(x*x - 1)
        xr.append(x); wr.append(2/((1-x*x)*dP*dP))
    nodes, wts = [], []
    for p in range(NPANEL):
        a, b = L*p/NPANEL, L*(p+1)/NPANEL; h = (b-a)/2
        for x, w in zip(xr, wr):
            nodes.append(a + h*(x+1)); wts.append(w*h)
    Kn = len(nodes)
    SIN = [[mp.sin(om[n]*y) for y in nodes] for n in range(NB+1)]
    COS = [[mp.cos(om[n]*y) for y in nodes] for n in range(NB+1)]
    LY  = [(L-y)/L for y in nodes]
    W1  = [wts[k]*(mp.e**(nodes[k]/2)+mp.e**(-nodes[k]/2)) for k in range(Kn)]
    E2  = [mp.e**(nodes[k]/2) for k in range(Kn)]
    DD  = [wts[k]/(mp.e**nodes[k]-mp.e**(-nodes[k])) for k in range(Kn)]
    CR  = mp.euler + mp.log(4*mp.pi*(mp.e**L-1)/(mp.e**L+1))

    def th_nodes(n, m):
        if n==0 and m==0: return [2*LY[k] for k in range(Kn)], mp.mpf(2)
        if n==0 or m==0:
            j=max(n,m); a2=-2/(mp.sqrt(2)*mp.pi*j)
            return [a2*SIN[j][k] for k in range(Kn)], mp.mpf(0)
        if n==m: return [2*(LY[k]*COS[n][k]-SIN[n][k]/(2*mp.pi*n)) for k in range(Kn)], mp.mpf(2)
        a2=2/(mp.pi*(m*m-n*n))
        return [a2*(n*SIN[n][k]-m*SIN[m][k]) for k in range(Kn)], mp.mpf(0)
    def th_at(n, m, y):
        if n==0 and m==0: return 2*(L-y)/L
        if n==0 or m==0:
            j=max(n,m); return -2*mp.sin(om[j]*y)/(mp.sqrt(2)*mp.pi*j)
        if n==m: return 2*((L-y)*mp.cos(om[n]*y)/L-mp.sin(om[n]*y)/(2*mp.pi*n))
        return 2*(n*mp.sin(om[n]*y)-m*mp.sin(om[m]*y))/(mp.pi*(m*m-n*n))

    # tours par premier
    cap = int(mp.e**L + 1e-9); sv = [True]*(cap+1)
    for i in range(2, int(cap**0.5)+1):
        if sv[i]:
            for j in range(i*i, cap+1, i): sv[j] = False
    primes = [p for p in range(2, cap+1) if sv[p]]   # all primes <= mu (was hardcoded to 37: a hole above mu=41)
    towers = {p: [] for p in primes}
    for p in primes:
        n = p
        while n <= int(mp.e**L+1e-9):
            towers[p].append((mp.log(n), mp.log(p)/mp.sqrt(n)))
            n *= p

    NP = NB+1
    Pm_ = mp.matrix(NP, NP); Am = mp.matrix(NP, NP)
    Tm = {p: mp.matrix(NP, NP) for p in primes}
    for n in range(NP):
        for m in range(n, NP):
            th, F0 = th_nodes(n, m)
            pole = mp.fsum(th[k]*W1[k] for k in range(Kn))
            arch = -(F0/2*CR + mp.fsum((E2[k]*th[k]-F0)*DD[k] for k in range(Kn)))
            Pm_[n,m]=Pm_[m,n]=pole; Am[n,m]=Am[m,n]=arch
            for p in primes:
                v = -mp.fsum(w*th_at(n,m,lg) for lg,w in towers[p])
                Tm[p][n,m]=Tm[p][m,n]=v
    S = mp.matrix(NP, NP)
    for n in range(NP):
        for m in range(NP):
            S[n,m] = Pm_[n,m] + Am[n,m] + mp.fsum(Tm[p][n,m] for p in primes)
    E, V = mp.eigsy(S)
    print(f"mu={float(mu)}, N={NP}, dps={dps} (assemblage {time.time()-t0:.0f}s)")
    # projections des composantes sur les K etats du bas
    comps = [('POLE', Pm_), ('ARCH', Am)] + [(f'T_{p}', Tm[p]) for p in primes]
    print(f"\n{'k':>2s} {'lambda_k':>11s} | " + " ".join(f"{nm:>9s}" for nm,_ in comps) + " |  somme/lambda")
    for k in range(K):
        v = mp.matrix([V[i,k] for i in range(NP)])
        vals = []
        for nm, C in comps:
            Cv = C*v
            vals.append(mp.fsum(v[i]*Cv[i] for i in range(NP)))
        tot = mp.fsum(vals)
        print(f"{k:2d} {mp.nstr(E[k],3):>11s} | " + " ".join(f"{float(x):+9.3f}" for x in vals) + f" | {mp.nstr(tot/E[k],4)}")
    lam0 = float(E[0])
    ell = [float(-mp.log(abs(E[k]))) if E[k] != 0 else float("inf") for k in range(min(8, NP))]
    return lam0, ell

if __name__ == '__main__':
    run(mp.mpf(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
