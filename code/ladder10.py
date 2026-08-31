import mpmath as mp, pickle, time, sys
import numpy as np


EU = mp.euler

def run(mu, NB, NPANEL, DEG):
    t0 = time.time()
    L = mp.log(mu)
    om = [2*mp.pi*n/L for n in range(NB+1)]

    # ---- quadrature composite Gauss-Legendre precalculee sur [0,L] ----
    xs, ws = mp.polyroots([mp.legendre(DEG, mp.mpf(0)).__class__ and 0] ) if False else (None,None)
    # noeuds GL de reference via mpmath
    ref = mp.taylor(lambda x: mp.legendre(DEG, x), 0, DEG)
    import numpy.polynomial.legendre as NL
    xr0, _ = NL.leggauss(DEG)
    xr, wr = [], []
    for x0 in xr0:                                # raffinage Newton en mp
        x = mp.mpf(float(x0))
        for _ in range(6):
            P  = mp.legendre(DEG, x); Pm = mp.legendre(DEG-1, x)
            dP = DEG*(x*P - Pm)/(x*x - 1)
            x  = x - P/dP
        P  = mp.legendre(DEG, x); Pm = mp.legendre(DEG-1, x)
        dP = DEG*(x*P - Pm)/(x*x - 1)
        xr.append(x); wr.append(2/((1 - x*x)*dP*dP))
    nodes, wts = [], []
    for p in range(NPANEL):
        a = L*p/NPANEL; b = L*(p+1)/NPANEL; h = (b-a)/2
        for x, w in zip(xr, wr):
            nodes.append(a + h*(x+1)); wts.append(w*h)
    K = len(nodes)

    # ---- tables trig ----
    SIN = [[mp.sin(om[n]*y) for y in nodes] for n in range(NB+1)]
    COS = [[mp.cos(om[n]*y) for y in nodes] for n in range(NB+1)]
    LY  = [(L - y)/L for y in nodes]
    W1  = [wts[k]*(mp.e**(nodes[k]/2) + mp.e**(-nodes[k]/2)) for k in range(K)]
    E2 = [mp.e**(nodes[k]/2) for k in range(K)]
    DD = [wts[k]/(mp.e**nodes[k] - mp.e**(-nodes[k])) for k in range(K)]
    tprep = time.time()-t0

    def theta_nodes(n, m):
        if n == 0 and m == 0:
            return [2*LY[k] for k in range(K)], mp.mpf(2)
        if n == 0 or m == 0:
            j = max(n,m); a = -2/(mp.sqrt(2)*mp.pi*j)
            return [a*SIN[j][k] for k in range(K)], mp.mpf(0)
        if n == m:
            a = 1/(mp.pi*n)
            return [2*(LY[k]*COS[n][k] - SIN[n][k]/(2*mp.pi*n)) for k in range(K)], mp.mpf(2)
        a = 2/(mp.pi*(m*m-n*n))
        return [a*(n*SIN[n][k] - m*SIN[m][k]) for k in range(K)], mp.mpf(0)

    CR = EU + mp.log(4*mp.pi*(mp.e**L-1)/(mp.e**L+1))
    ppts = []
    x = 2
    while x <= int(mp.e**L + 1e-9):
        y = x; p = None
        for q in [2,3,5,7,11,13,17,19,23]:
            if y % q == 0:
                p = q
                while y % q == 0: y //= q
                break
        if p and y == 1: ppts.append((mp.log(x), mp.log(p)/mp.sqrt(x)))
        x += 1

    def theta_at(n, m, y):
        if n == 0 and m == 0: return 2*(L-y)/L
        if n == 0 or m == 0:
            j = max(n,m); return -2*mp.sin(om[j]*y)/(mp.sqrt(2)*mp.pi*j)
        if n == m: return 2*((L-y)*mp.cos(om[n]*y)/L - mp.sin(om[n]*y)/(2*mp.pi*n))
        return 2*(n*mp.sin(om[n]*y) - m*mp.sin(om[m]*y))/(mp.pi*(m*m-n*n))

    S = mp.matrix(NB+1, NB+1)
    for n in range(NB+1):
        for m in range(n, NB+1):
            th, F0 = theta_nodes(n, m)
            W02 = mp.fsum(th[k]*W1[k] for k in range(K))
            WRi = mp.fsum((E2[k]*th[k] - F0)*DD[k] for k in range(K))
            Wp  = mp.fsum(w*theta_at(n,m,lg) for lg,w in ppts)
            v = W02 - (F0/2*CR + WRi) - Wp
            S[n,m] = v; S[m,n] = v
    tmat = time.time()-t0

    # ---- validation cote zeros (float64) ----
    zeros = pickle.load(open('zeros280.pkl','rb'))
    Lf = float(L); omf = [2*np.pi*n/Lf for n in range(NB+1)]
    def theta_np(n, m, y):
        if n==0 and m==0: return 2*(Lf-y)/Lf
        if n==0 or m==0:
            j=max(n,m); return -2*np.sin(omf[j]*y)/(np.sqrt(2)*np.pi*j)
        if n==m: return 2*((Lf-y)*np.cos(omf[n]*y)/Lf - np.sin(omf[n]*y)/(2*np.pi*n))
        return 2*(n*np.sin(omf[n]*y)-m*np.sin(omf[m]*y))/(np.pi*(m*m-n*n))
    yg = np.linspace(0, Lf, 6000)
    rats = []
    for a,b in [(0,0),(1,2),(3,3)]:
        th = theta_np(a,b,yg)
        zs = sum(2*np.trapezoid(th*np.cos(g*yg), yg) for g in zeros)
        rats.append(float(S[a,b])/zs)

    E, V = mp.eigsy(S)
    lam = [E[i] for i in range(NB+1)]
    c = [V[i,0] for i in range(NB+1)]
    if c[0] < 0: c = [-x for x in c]

    def vhat(z):
        s = c[0]*(2*mp.sin(z*L/2)/z/mp.sqrt(L) if abs(z) > mp.mpf('1e-20') else mp.sqrt(L))
        for n in range(1, NB+1):
            s += c[n]*2*mp.sqrt(2/L)*z*mp.sin(z*L/2)/(z*z-om[n]*om[n])
        return s
    def Xi(z):
        s = mp.mpf(0.5)+1j*z
        return mp.re(s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s))

    ca = Xi(0)/vhat(mp.mpf('1e-25'))
    zg = [mp.mpf(k)/10 + mp.mpf('0.037') for k in range(0, 301)]
    xg = [Xi(z) for z in zg]; vg = [ca*vhat(z) for z in zg]
    res = [v-x for v,x in zip(vg,xg)]
    Xmax = max(abs(x) for x in xg)
    infra  = [abs(r) for z,r in zip(zg,res) if z < 13]
    milieu = [abs(r) for z,r in zip(zg,res) if 15 < z < 30 and min(abs(float(z)-g) for g in [21.0220,25.0109]) > 1.0]
    i1 = min(range(len(zg)), key=lambda i: abs(float(zg[i])-14.1347))
    print(f"=== mu={float(mu)}, L={float(L):.4f}, N={NB+1} fcts paires, {K} noeuds, dps={mp.mp.dps} ===")
    print(f"  prep {tprep:.0f}s, matrice {tmat:.0f}s")
    print(f"  ratios premiers/zeros (3 entrees) : {[f'{r:.4f}' for r in rats]}")
    print(f"  vp les plus basses : {[mp.nstr(l,3) for l in lam[:10]]}")
    print(f"  (echelle seule, {time.time()-t0:.0f}s)")
    return

if __name__ == '__main__':
    mu = mp.mpf(sys.argv[1]); NB = int(sys.argv[2])
    mp.mp.dps = int(sys.argv[3]); DEG = int(sys.argv[4])
    run(mu, NB, NPANEL=5*NB+20, DEG=DEG)
