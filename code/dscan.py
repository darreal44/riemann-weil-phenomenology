import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
import mpmath as mp, pickle, time, sys, os
import numpy as np
import numpy.polynomial.legendre as NL

CHARS = {
 'chi3': dict(q=3, tab=[0,1,-1], a=1),
 'chi4': dict(q=4, tab=[0,1,0,-1], a=1),
 'chi5': dict(q=5, tab=[0,1,-1,-1,1], a=0),
 'chi7': dict(q=7, tab=[0,1,1,-1,1,-1,-1], a=1),
 'chi8': dict(q=8, tab=[0,1,0,-1,0,-1,0,1], a=0),
 'chi11': dict(q=11, tab=[0,1,-1,1,1,1,-1,-1,-1,1,-1], a=1),
 'chi12': dict(q=12, tab=[0,1,0,0,0,-1,0,-1,0,0,0,1], a=0),
 'chi13': dict(q=13, tab=[0,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1], a=0),
 'chi15': dict(q=15, tab=[0,1,1,0,1,0,0,-1,1,0,0,-1,0,-1,-1], a=1),
 'chi24o': dict(q=24, tab=[0,1,0,0,0,1,0,1,0,0,0,1,0,-1,0,0,0,-1,0,-1,0,0,0,-1], a=1),
 'chi19': dict(q=19, tab=[0,1,-1,-1,1,1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1], a=1),
 'chi17': dict(q=17, tab=[0, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1], a=0),
 'chi21': dict(q=21, tab=[0, 1, -1, 0, 1, 1, 0, 0, -1, 0, -1, -1, 0, -1, 0, 0, 1, 1, 0, -1, 1], a=0),
 'chi20': dict(q=20, tab=[0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1], a=1),
 'chi24e': dict(q=24, tab=[0,1,0,0,0,1,0,-1,0,0,0,-1,0,-1,0,0,0,-1,0,1,0,0,0,1], a=0),
}

def Lchi(s, q, tab):
    return q**(-s)*mp.fsum(tab[r]*mp.zeta(s, mp.mpf(r)/q) for r in range(1, q) if tab[r])

def Lam(t, q, tab, a):
    s = mp.mpf('0.5') + 1j*t
    return mp.re((mp.mpf(q)/mp.pi)**((s+a)/2)*mp.gamma((s+a)/2)*Lchi(s, q, tab))

def harvest_zeros(name, q, tab, a, tmax=85):
    fn = f'zeros_{name}.pkl'
    if os.path.exists(fn): return pickle.load(open(fn,'rb'))
    mp.mp.dps = 22
    zs, step = [], mp.mpf('0.04')
    t = mp.mpf('0.01'); prev = Lam(t, q, tab, a)
    while t < tmax:
        t2 = t + step; cur = Lam(t2, q, tab, a)
        if prev*cur < 0:
            zs.append(float(mp.findroot(lambda x: Lam(x, q, tab, a), (t, t2), solver='bisect')))
        prev, t = cur, t2
    pickle.dump(zs, open(fn,'wb'))
    return zs

def run(name, mu, NB, dps, DEG=14):
    cf = CHARS[name]; q, tab, a = cf['q'], cf['tab'], cf['a']
    zs = harvest_zeros(name, q, tab, a)
    mp.mp.dps = dps
    t0 = time.time()
    L = mp.log(mu); s0 = mp.mpf(1)/4 + mp.mpf(a)/2
    om = [2*mp.pi*n/L for n in range(NB+1)]
    xr0, _ = NL.leggauss(DEG)
    xr, wr = [], []
    for x0 in xr0:
        x = mp.mpf(float(x0))
        for _ in range(6):
            P = mp.legendre(DEG, x); Pm = mp.legendre(DEG-1, x)
            dP = DEG*(x*P - Pm)/(x*x - 1); x = x - P/dP
        P = mp.legendre(DEG, x); Pm = mp.legendre(DEG-1, x)
        dP = DEG*(x*P - Pm)/(x*x - 1)
        xr.append(x); wr.append(2/((1-x*x)*dP*dP))
    NPANEL = 4*NB + 16
    nodes, wts = [], []
    for p in range(NPANEL):
        aa, bb = L*p/NPANEL, L*(p+1)/NPANEL; h = (bb-aa)/2
        for x, w in zip(xr, wr):
            nodes.append(aa + h*(x+1)); wts.append(w*h)
    K = len(nodes)
    SIN = [[mp.sin(om[n]*y) for y in nodes] for n in range(NB+1)]
    COS = [[mp.cos(om[n]*y) for y in nodes] for n in range(NB+1)]
    LY  = [(L-y)/L for y in nodes]
    D2 = [wts[k]*2*mp.e**(-2*s0*nodes[k])/(1-mp.e**(-2*nodes[k])) for k in range(K)]
    EC = [mp.e**(-(2-2*s0)*nodes[k]) for k in range(K)]
    CST = mp.log(mp.mpf(q)/mp.pi) - mp.euler - mp.log(1-mp.e**(-2*L))

    def th_nodes(n, m):
        if n==0 and m==0: return [2*LY[k] for k in range(K)], mp.mpf(2)
        if n==0 or m==0:
            j=max(n,m); a2=-2/(mp.sqrt(2)*mp.pi*j)
            return [a2*SIN[j][k] for k in range(K)], mp.mpf(0)
        if n==m: return [2*(LY[k]*COS[n][k]-SIN[n][k]/(2*mp.pi*n)) for k in range(K)], mp.mpf(2)
        a2=2/(mp.pi*(m*m-n*n))
        return [a2*(n*SIN[n][k]-m*SIN[m][k]) for k in range(K)], mp.mpf(0)
    def th_at(n, m, y):
        if n==0 and m==0: return 2*(L-y)/L
        if n==0 or m==0:
            j=max(n,m); return -2*mp.sin(om[j]*y)/(mp.sqrt(2)*mp.pi*j)
        if n==m: return 2*((L-y)*mp.cos(om[n]*y)/L-mp.sin(om[n]*y)/(2*mp.pi*n))
        return 2*(n*mp.sin(om[n]*y)-m*mp.sin(om[m]*y))/(mp.pi*(m*m-n*n))

    ppts = []
    x = 2
    while x <= int(mp.e**L+1e-9):
        y2, p = x, None
        for qq in [2,3,5,7,11,13,17,19,23,29,31,37]:
            if y2 % qq == 0:
                p = qq
                while y2 % qq == 0: y2 //= qq
                break
        if p and y2 == 1 and tab[x % q] != 0:
            ppts.append((mp.log(x), tab[x % q]*mp.log(p)/mp.sqrt(x)))
        x += 1

    S = mp.matrix(NB+1, NB+1)
    for n in range(NB+1):
        for m in range(n, NB+1):
            th, F0 = th_nodes(n, m)
            arch = F0/2*CST + mp.mpf('0.5')*mp.fsum(D2[k]*(F0*EC[k]-th[k]) for k in range(K))
            v = arch - mp.fsum(w*th_at(n,m,lg) for lg,w in ppts)
            S[n,m] = v; S[m,n] = v

    # validation legere cote zeros
    Lf = float(L); omf = [2*np.pi*n/Lf for n in range(NB+1)]
    yg = np.linspace(0, Lf, 5000)
    def th_np(n, m, y):
        if n==0 and m==0: return 2*(Lf-y)/Lf
        return 2*(n*np.sin(omf[n]*y)-m*np.sin(omf[m]*y))/(np.pi*(m*m-n*n))
    rats = []
    for a2, b2 in [(0,0),(2,3)]:
        th = th_np(a2,b2,yg)
        rats.append(float(S[a2,b2])/sum(np.trapezoid(th*np.cos(g*yg), yg) for g in zs))

    E, V = mp.eigsy(S)
    lam = [E[i] for i in range(min(10, NB+1))]
    c = [V[i,0] for i in range(NB+1)]
    if c[0] < 0: c = [-u for u in c]
    def vhat(z):
        s = c[0]*(2*mp.sin(z*L/2)/z/mp.sqrt(L) if abs(z)>mp.mpf('1e-20') else mp.sqrt(L))
        for n in range(1, NB+1):
            s += c[n]*2*mp.sqrt(2/L)*z*mp.sin(z*L/2)/(z*z-om[n]*om[n])
        return s
    mp.mp.dps = 28
    def Xic(z): return Lam(z, q, tab, a)
    ca = Xic(0)/vhat(mp.mpf('1e-20'))
    g1 = zs[0]
    zgrid = [mp.mpf(k)*3/20 + mp.mpf('0.041') for k in range(0, 200)]
    xg = [Xic(z) for z in zgrid]; Xmax = max(abs(u) for u in xg)
    res = [abs(ca*vhat(z)-x2) for z, x2 in zip(zgrid, xg)]
    infra = max(r for z, r in zip(zgrid, res) if float(z) < g1-0.5)
    mil = max(r for z, r in zip(zgrid, res) if g1+0.8 < float(z) < 30 and min(abs(float(z)-g) for g in zs[:12]) > 0.8)
    # Phi_chi et recouvrement
    zq0, zw0 = NL.leggauss(60)
    zn, zw = [], []
    for (za, zb) in [(0,8),(8,25),(25,70)]:
        h = (zb-za)/2.0
        for t2, w2 in zip(zq0, zw0):
            zn.append(mp.mpf(za + h*(float(t2)+1))); zw.append(mp.mpf(h*float(w2)))
    XiZ = [Xic(u) for u in zn]
    def Phi(x2): return mp.fsum(zw[k]*XiZ[k]*mp.cos(zn[k]*x2) for k in range(len(zn)))/mp.pi
    xq0, wq0 = NL.leggauss(36)
    half = L/2
    xq = [half*(mp.mpf(float(t2))+1)/2 for t2 in xq0]; wq = [half*mp.mpf(float(w))/2 for w in wq0]
    P3 = [Phi(u) for u in xq]
    def vx(x2):
        s = c[0]/mp.sqrt(L)
        for nn in range(1, NB+1):
            s += c[nn]*(-1)**nn*mp.sqrt(2/L)*mp.cos(om[nn]*x2)
        return s
    ovl = 2*mp.fsum(wq[k]*vx(xq[k])*P3[k] for k in range(len(xq)))
    nPhi = mp.sqrt(2*mp.fsum(wq[k]*P3[k]**2 for k in range(len(xq))))
    par = 'pair' if a==0 else 'impair'
    print(f"[{name} q={q} {par}] mu={float(mu)} : gamma_1={g1:.3f} | ratios {rats[0]:.3f},{rats[1]:.3f} | "
          f"lam_min={mp.nstr(lam[0],3)} (echelle {[mp.nstr(l,2) for l in lam[1:10]]})")
    print(f"    residu infra={float(infra/Xmax):.3f} mid={float(mil/Xmax):.4f} | c_z0={mp.nstr(ca,5)} "
          f"c_proj={mp.nstr(nPhi*nPhi/ovl,6)} ||Phi||={mp.nstr(nPhi,6)} ovl={mp.nstr(ovl/nPhi,6)} | {time.time()-t0:.0f}s", flush=True)

if __name__ == '__main__':
    name = sys.argv[1]
    for mu, NB, dps in [(mp.mpf('5.5'), 24, 45), (mp.mpf('11'), 40, 52)]:
        run(name, mu, NB, dps)
