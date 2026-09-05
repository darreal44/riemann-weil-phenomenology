# Two-window slope s(χ) for chim8 / chi20 / chi23.
# Usage: python3 scan_s.py chim8 [mu NB dps]
# Default protocol: (5.5, 24, 40) then (11, 32, 45) — depth-adequate for s ≲ 1.5.
import os, sys, time, pickle
import mpmath as mp
import numpy.polynomial.legendre as NL

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from kronecker import chi_tab

CHARS = {
    'chim8': dict(q=8,  d=-8,  a=1),
    'chi20': dict(q=20, d=-20, a=1),
    'chi23': dict(q=23, d=-23, a=1),
    'chi11': dict(q=11, d=-11, a=1),
    'chi13': dict(q=13, d=13,  a=0),
    'chi5':  dict(q=5,  d=5,   a=0),
    'chi8':  dict(q=8,  d=8,   a=0),
    'chi7':  dict(q=7,  d=-7,  a=1),
    'chi29': dict(q=29, d=29,  a=0),
    'chi17': dict(q=17, d=17,  a=0),
    'chi3':  dict(q=3,  d=-3,  a=1),
    'chi4':  dict(q=4,  d=-4,  a=1),
    'chi12': dict(q=12, d=12,  a=0),
    'chi15': dict(q=15, d=-15, a=1),
    'chi19': dict(q=19, d=-19, a=1),
    'chi21': dict(q=21, d=21,  a=0),
    'chi24e': dict(q=24, d=24,  a=0),
    'chi24o': dict(q=24, d=-24, a=1),
    'chi31': dict(q=31, d=-31, a=1),
}

def assemble(name, mu, NB, dps, DEG=12):
    if name in (
        "11a1", "19a1", "32a1", "37a1", "43a1", "53a1", "61a1", "67a1",
    ):
        raise SystemExit(
            f"{name} is GL(2): use  python3 code/scan_gl2.py {name} 22 36 50"
        )
    cf = CHARS[name]
    q, a = cf['q'], cf['a']
    tab = chi_tab(cf['d'], q)
    mp.mp.dps = dps
    t0 = time.time()
    L = mp.log(mp.mpf(mu))
    s0 = mp.mpf(1)/4 + mp.mpf(a)/2
    om = [2*mp.pi*n/L for n in range(NB+1)]
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

    ppts = []
    x = 2
    cap = int(float(mp.e**L) + 1e-9)
    small = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83]
    while x <= cap:
        y2, p = x, None
        for qq in small:
            if y2 % qq == 0:
                p = qq
                while y2 % qq == 0: y2 //= qq
                break
        if p and y2 == 1 and tab[x % q] != 0:
            ppts.append((mp.log(x), tab[x % q]*mp.log(p)/mp.sqrt(x)))
        x += 1

    S = mp.matrix(NB+1)
    for n in range(NB+1):
        for m in range(n, NB+1):
            th, F0 = th_nodes(n, m)
            arch = F0/2*CST + mp.mpf('0.5')*mp.fsum(D2[k]*(F0*EC[k]-th[k]) for k in range(K))
            v = arch - mp.fsum(w*th_at(n,m,lg) for lg,w in ppts)
            S[n,m] = v; S[m,n] = v
    E, V = mp.eigsy(S)
    pairs = sorted([(E[i], i) for i in range(NB+1)], key=lambda z: float(z[0]))
    lam = [p[0] for p in pairs[:8]]
    ell = [float(-mp.log(abs(l))) if l != 0 else float('inf') for l in lam]
    i0 = pairs[0][1]
    v0 = [float(V[n, i0]) for n in range(NB+1)]
    p2 = [x*x for x in v0]
    s2 = sum(p2) or 1.0
    p2 = [x/s2 for x in p2]
    neff = 1.0 / sum(x*x for x in p2)
    kbar = sum(k*p2[k] for k in range(NB+1))
    ratio = float(abs(pairs[1][0]/pairs[0][0])) if pairs[0][0] != 0 else float('inf')
    print(f"[{name} mu={mu} N={NB+1} dps={dps}] lam0={mp.nstr(lam[0],4)}  "
          f"ell={[round(x,2) for x in ell[:6]]}  "
          f"N_eff={neff:.2f} kbar={kbar:.2f} l1/l0={ratio:.2e}  "
          f"{time.time()-t0:.0f}s", flush=True)
    dump = os.environ.get('DUMP_MODE')
    if dump:
        import json
        out = {
            'name': name, 'mu': float(mu), 'NB': NB, 'dps': dps,
            'lam': [float(x) for x in lam],
            'ell': ell[:8],
            'v0': v0,
            'N_eff': neff, 'kbar': kbar, 'l1_over_l0': ratio,
        }
        path = dump if dump not in ('1', 'true', 'yes') else os.path.join(
            os.path.dirname(BASE), 'report', f'mode_{name}_mu{int(mu)}.json')
        os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
        json.dump(out, open(path, 'w'), indent=2)
        print(f'  dumped {path}', flush=True)
    return float(lam[0]), ell, time.time()-t0


if __name__ == '__main__':
    name = sys.argv[1]
    windows = [(5.5, 24, 40), (11.0, 32, 45)]
    if len(sys.argv) >= 5:
        windows = [(float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))]
    rows = []
    for mu, NB, dps in windows:
        lam0, ell, dt = assemble(name, mu, NB, dps)
        rows.append((mu, ell[0], lam0, dt))
    if len(rows) >= 2:
        s = (rows[1][1] - rows[0][1]) / (rows[1][0] - rows[0][0])
        print(f"SLOPE {name}: s_hat_two_point = {s:.3f}   "
              f"ell({rows[0][0]})={rows[0][1]:.2f}  ell({rows[1][0]})={rows[1][1]:.2f}")
