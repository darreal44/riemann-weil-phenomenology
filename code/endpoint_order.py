# Second order at gamma1: |vhat(g1)| / lambda vs |vhat(edge)| / sqrt(lambda).
# Usage: python3 endpoint_order.py chi3    (default mu=16 N=36)
#        python3 endpoint_order.py zeta
import os, sys, time, pickle
import mpmath as mp
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
kind = sys.argv[1] if len(sys.argv) > 1 else 'chi3'
mu_cli = float(sys.argv[2]) if len(sys.argv) > 2 else None
NB_cli = int(sys.argv[3]) if len(sys.argv) > 3 else None
dps_cli = int(sys.argv[4]) if len(sys.argv) > 4 else None


def assemble_chi3(mu=16.0, NB=36, dps=48):
    t0 = time.time()
    src = open(os.path.join(BASE, 'spectro.py')).read()
    src = src.replace(
        "    E, V = mp.eigsy(S)",
        "    import __main__; __main__.PACK = (S, None, None); E, V = mp.eigsy(S); __main__.PACK = (S, E, V)",
    )
    ns = {}
    exec(compile(src.replace("if __name__ == '__main__':", "if False:"), "sc", "exec"), ns)
    ns['run'](mp.mpf(mu), NB, dps, 12, K=1, q=3, tab=[0, 1, -1], apar=1)
    import __main__
    S, E, V = __main__.PACK
    L = mp.log(mp.mpf(mu))
    om = [2 * mp.pi * n / L for n in range(NB + 1)]
    zs = [mp.mpf(z) for z in pickle.load(open(os.path.join(BASE, 'zeros_chi3.pkl'), 'rb'))]
    print(f'assembled chi3 in {time.time()-t0:.0f}s')
    return S, E, V, L, om, zs, mu, NB


def assemble_zeta(mu=11.0, NB=20, dps=40):
    # thin wrapper around high_directions ingredients
    t0 = time.time()
    mp.mp.dps = dps
    L = mp.log(mp.mpf(mu))
    NP = NB + 1
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
        while p ** k <= int(mu):
            towers.append((mp.log(p ** k), mp.log(p) / mp.sqrt(p ** k)))
            k += 1
    Q = mp.matrix(NP)
    for n in range(NP):
        for m in range(n, NP):
            F0 = mp.mpf(2) if n == m else mp.mpf(0)
            pol = mp.quad(lambda y: theta(n, m, y) * (mp.e ** (y / 2) + mp.e ** (-y / 2)), [0, L])
            ig = mp.quad(
                lambda y: (mp.e ** (y / 2) * theta(n, m, y) - F0) / (mp.e ** y - mp.e ** (-y)), [0, L]
            )
            tw = mp.fsum(w * theta(n, m, lg) for lg, w in towers)
            Q[n, m] = pol - (F0 / 2 * CR + ig) - tw
            Q[m, n] = Q[n, m]
    E, V = mp.eigsy(Q)
    zs = [mp.mpf(z) for z in pickle.load(open(os.path.join(BASE, 'zeros_zeta_90_hp.pkl'), 'rb'))]
    print(f'assembled zeta in {time.time()-t0:.0f}s')
    return Q, E, V, L, om, zs, mu, NB


def hat(n, g, L, om):
    if n == 0:
        return 2 * mp.sin(g * L / 2) / (g * mp.sqrt(L))
    den = g * g - om[n] * om[n]
    if abs(float(den)) < 1e-18:
        return mp.mpf(0)
    return 2 * mp.sqrt(2 / L) * g * mp.sin(g * L / 2) / den


def vhat(V, g, L, om, NP):
    return mp.fsum(V[n, 0] * hat(n, g, L, om) for n in range(NP))


def report(kind, pack):
    S, E, V, L, om, zs, mu, NB = pack
    NP = NB + 1
    lam = E[0]
    if lam <= 0:
        print('lambda0 <= 0, skip', lam)
        return
    wmax = float(om[-1])
    vh1 = abs(vhat(V, zs[0], L, om, NP))
    # edge: last in-band zero, else wmax * 0.98
    inband = [z for z in zs if float(z) < wmax]
    g_edge = inband[-1] if inband else mp.mpf(wmax * 0.98)
    vhe = abs(vhat(V, g_edge, L, om, NP))
    sl = float(mp.sqrt(lam))
    fl = float(lam)
    print(f'{kind} mu={mu} N={NP}  lambda0={mp.nstr(lam, 4)}  ell={float(-mp.log(lam)):.2f}')
    print(f'  wmax={wmax:.2f}  g1={float(zs[0]):.4f}  g_edge={float(g_edge):.4f}  n_inband={len(inband)}')
    print(f'  |vh(g1)|    = {mp.nstr(vh1, 4)}')
    print(f'  |vh(edge)|  = {mp.nstr(vhe, 4)}')
    print(f'  |vh(g1)|/λ     = {float(vh1)/fl:.3e}')
    print(f'  |vh(g1)|/√λ    = {float(vh1)/sl:.3e}')
    print(f'  |vh(edge)|/√λ  = {float(vhe)/sl:.3e}')
    print(f'  |vh(edge)|/λ   = {float(vhe)/fl:.3e}')
    print(f'  |vh(g1)|/|vh(edge)| = {float(vh1/vhe):.3e}   √λ = {sl:.3e}')
    # leakage envelope check: ratio vs e^{-tau (wmax-g1)} with tau = ell/(2 wmax)
    ell = float(-mp.log(lam))
    tau = ell / (2 * wmax)
    pred = float(vhe) * mp.e ** (-tau * (wmax - float(zs[0])))
    print(f'  tau=ell/(2 wmax)={tau:.3f}  leak_pred |vh(g1)|={float(pred):.3e}  ratio meas/pred={float(vh1)/float(pred):.3f}')


if __name__ == '__main__':
    if kind == 'zeta':
        report('zeta', assemble_zeta())
    else:
        kw={}
        if mu_cli is not None: kw['mu']=mu_cli
        if NB_cli is not None: kw['NB']=NB_cli
        if dps_cli is not None: kw['dps']=dps_cli
        report('chi3', assemble_chi3(**kw))
