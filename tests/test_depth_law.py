# The depth law ell ~ 11 D_max and the discrete Landau count (notebook 133-134). Recomputing; ~30 s.
import os, math, pickle, numpy as np, mpmath as mp
CODE = os.path.join(os.path.dirname(__file__), '..', 'code')
def _zeros(f): return sorted(float(str(x)) for x in pickle.load(open(os.path.join(CODE, f), 'rb')))
def _Dmax(Z, mu, NB):
    L = math.log(mu); nyq = L/(2*math.pi); omax = 2*math.pi*NB/L
    inb = [g for g in Z if g < omax]
    return max([g*nyq - (k+1) for k, g in enumerate(inb)] + [omax*nyq - len(inb)])
def _ladder(Z, mu, NB, dps, kmax=12):
    mp.mp.dps = dps; NP = NB+1; L = mp.log(mu); om = [2*mp.pi*n/L for n in range(NP)]
    G = mp.matrix(NP, NP)
    for g in Z:
        gg = mp.mpf(g); sn = mp.sin(gg*L/2)
        c = [2*sn/(gg*mp.sqrt(L))] + [mp.sqrt(2/L)*sn*2*gg/(gg*gg-om[n]*om[n]) for n in range(1, NP)]
        for i in range(NP):
            for j in range(i, NP): G[i, j] += 2*c[i]*c[j]
    for i in range(NP):
        for j in range(i): G[i, j] = G[j, i]
    E = mp.eigsy(G, eigvals_only=True)
    return [float(-mp.log(E[k])) if E[k] > 0 else float('nan') for k in range(min(kmax, NP))]

def test_discrete_landau_count_zeta_mu11():
    Z = _zeros('zeros500.pkl'); mu, NB = 11.0, 30
    D = _Dmax(Z, mu, NB); ell = _ladder(Z, mu, NB, 55)
    small = sum(1 for e in ell if e > 2.0)
    assert round(D) == small, (D, ell)                      # 11 free dimensions -> 11 small eigenvalues at N=31
    assert abs(ell[0]/D - 11.0) < 2.0, (ell[0], D)          # ell ~ 11 D_max

def test_discrete_landau_count_chi5_mu16_above_nyquist():
    Z = _zeros('zeros_chi5_weyl.pkl'); mu, NB = 16.0, 30
    D = _Dmax(Z, mu, NB); ell = _ladder(Z, mu, NB, 45)
    inb = sum(1 for g in Z if g < 2*math.pi*NB/math.log(mu))
    assert inb > NB + 1                                      # above Nyquist: N+1-m < 0, the count must come from D_max
    assert round(D) == sum(1 for e in ell if e > 2.0), (D, ell)

def test_depth_law_from_stored_windows():
    """ell measured (edge-value-scan, server) vs 11 D_max from the zero lists, for the well-conditioned windows."""
    import json
    rows = {json.loads(l)['window']: json.loads(l) for l in open(os.path.join(CODE, '..', 'report', 'edge-value-scan.jsonl'))}
    for w, zf in (('zeta:11', 'zeros500.pkl'), ('chi3:16', 'zeros_chi3_weyl.pkl'), ('chi5:16', 'zeros_chi5_weyl.pkl'), ('chi4:38', 'zeros_chi4_weyl.pkl'), ('chi8:16', 'zeros_chi8_weyl.pkl')):
        r = rows[w]; D = _Dmax(_zeros(zf), r['mu'], r['NB'])
        assert abs(r['ell']/(11.0*D) - 1) < 0.08, (w, r['ell'], D)
