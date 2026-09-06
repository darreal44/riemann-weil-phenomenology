#!/usr/bin/env python3
"""Marginal weight of each in-band zero in the depth (notebook 128-130).

For a window (L-function, mu, N, dps): build the zero Gram G = sum_gamma 2 c(gamma) c(gamma)^T over the
harvested zeros, lambda_0 = min eig(G) (= the depth, to the tail), and for each in-band zero gamma_k
    w(gamma_k) = ln lambda_0(G) - ln lambda_0(G minus gamma_k)      (nats: how much that zero deepens the well)
plus fictitious zeros in the desert (fill weights), the Nyquist crossing gamma_c where the cumulative count
N(gamma) overtakes gamma L / 2pi, and a linear fit w = w0 (1 - gamma/gamma_c) below the crossing.

Full mode removes every in-band zero (~N eigen-decompositions of an N x N matrix in mpmath at the given
dps: minutes to tens of minutes per window) -> server. --quick removes 4 zeros and fills 2 points (~1-2 min).

usage: python3 code/marginal_weights.py [--quick] name:mu[:NB:dps] ...
       python3 code/marginal_weights.py all            (default set)
outputs: report/marginal-weights.jsonl (one line per window, resumable), report/marginal-weights.md
"""
import os, sys, json, time, math, pickle
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
OUT_JSONL = os.path.join(ROOT, 'report', 'marginal-weights.jsonl'); OUT_MD = os.path.join(ROOT, 'report', 'marginal-weights.md')
DEFAULT = ['zeta:8:40:60', 'zeta:11:40:60', 'zeta:16:40:65', 'zeta:11:60:90', 'chi3:16:46:65', 'chi5:16:46:65', 'chi4:16:46:65',
           'chi8:16:46:65', 'chi13:16:46:60', 'chi3:38:66:80', 'chi5:38:66:80', 'chi29:22:52:60', '11a1:11:24:50', '11a1:22:36:60']
FILLS = {'zeta': [4.0, 7.0, 10.0], 'default_frac': [0.3, 0.55, 0.8]}   # fictitious zeros; characters/curves: fractions of gamma_1

def zeros_of(name):
    for f in (f'zeros_{name}_weyl.pkl', f'zeros_{name}_150.pkl', f'zeros_{name}.pkl', 'zeros500.pkl' if name == 'zeta' else None):
        if f and os.path.exists(os.path.join(HERE, f)):
            return sorted(float(str(x)) for x in pickle.load(open(os.path.join(HERE, f), 'rb'))), f
    raise FileNotFoundError(name)

def analyse(name, mu, NB, dps, quick):
    mp.mp.dps = dps; NP = NB + 1; L = mp.log(mu); om = [2*mp.pi*n/L for n in range(NP)]; omax = float(om[NB])
    Z, zf = zeros_of(name); cache = {}
    def cvec(g):
        if g in cache: return cache[g]
        gg = mp.mpf(g); sn = mp.sin(gg*L/2)
        c = mp.matrix([2*sn/(gg*mp.sqrt(L))] + [mp.sqrt(2/L)*sn*2*gg/(gg*gg-om[n]*om[n]) for n in range(1, NP)]); cache[g] = c; return c
    def gram(zs):
        G = mp.matrix(NP, NP)
        for g in zs:
            c = cvec(g)
            for i in range(NP):
                for j in range(i, NP): G[i, j] += 2*c[i]*c[j]
        for i in range(NP):
            for j in range(i): G[i, j] = G[j, i]
        return G
    def lam(zs):
        e = mp.eigsy(gram(zs), eigvals_only=True)[0]
        return e if e > 0 else None
    t0 = time.time(); base = lam(Z)
    if base is None: return dict(window=f"{name}:{mu:g}:{NB}:{dps}", error="lambda_0 <= 0 at this dps (increase dps)")
    inb = [g for g in Z if g < omax]; nyq = float(L)/(2*math.pi)
    D = [(g, g*nyq - (k+1)) for k, g in enumerate(inb)]
    gc = None
    for k in range(1, len(D)):
        if D[k-1][1] > 0 >= D[k][1]: gc = D[k-1][0] + (D[k][0]-D[k-1][0])*D[k-1][1]/(D[k-1][1]-D[k][1]); break
    ks = [0, 1, len(inb)//3, 2*len(inb)//3] if quick else list(range(len(inb)))
    weights = []
    for k in ks:
        g = inb[k]; v = lam([x for x in Z if x != g])
        weights.append([g, float(mp.log(base/v)) if v else None])
    fills = FILLS['zeta'] if name == 'zeta' else [round(f*inb[0], 3) for f in FILLS['default_frac']]
    if quick: fills = fills[:2]
    fillw = []
    for g in fills:
        v = lam(Z + [g]); fillw.append([g, float(mp.log(v/base)) if v else None])
    # linear fit below the crossing (or over all if no crossing)
    pts = [(g, w) for g, w in weights if w is not None and (gc is None or g < gc)]
    fit = None
    if len(pts) >= 3:
        import numpy as np
        A = np.array([[1.0, -g] for g, _ in pts]); y = np.array([w for _, w in pts])
        (w0, w0_over_gc), *_ = np.linalg.lstsq(A, y, rcond=None)
        fit = dict(w0=float(w0), gamma_c_fit=float(w0/w0_over_gc) if w0_over_gc else None)
    return dict(window=f"{name}:{mu:g}:{NB}:{dps}", name=name, mu=mu, NB=NB, dps=dps, zeros_file=zf, n_zeros=len(Z), omega_max=omax,
                n_inband=len(inb), nyquist_places=NB, ell=float(-mp.log(base)), gamma_1=inb[0], gamma_c_crossing=gc,
                weights=weights, fills=fillw, fit=fit, quick=quick, seconds=round(time.time()-t0))

def write_md():
    rows = [json.loads(l) for l in open(OUT_JSONL)] if os.path.exists(OUT_JSONL) else []
    seen = {r['window']: r for r in rows}
    out = ["# Marginal weights of in-band zeros (notebook 128-130)", "",
           "w(gamma) = ln lambda_0(G) - ln lambda_0(G \\ gamma) ; gamma_c = Nyquist crossing (gamma L/2pi = N(gamma)) ; fit w = w0 (1 - gamma/gamma_c).", "",
           "| window | ell | in-band / places | omega_max | gamma_1 | w(gamma_1) | w(mid) | gamma_c (cross) | fit w0 | fit gamma_c | fills (gamma: nats) |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for w in sorted(seen):
        r = seen[w]
        if 'error' in r: out.append(f"| {w} | {r['error']} |"); continue
        ws = [x for x in r['weights'] if x[1] is not None]; wmid = ws[len(ws)//2][1] if ws else float('nan')
        gc = f"{r['gamma_c_crossing']:.1f}" if r['gamma_c_crossing'] else "none (sub-Nyquist)"
        fit = r['fit'] or {}
        out.append(f"| {w} | {r['ell']:.1f} | {r['n_inband']} / {r['nyquist_places']} | {r['omega_max']:.1f} | {r['gamma_1']:.2f} | {ws[0][1]:.2f} | {wmid:.2f} | {gc} | "
                   + (f"{fit['w0']:.2f} | {fit['gamma_c_fit']:.1f} |" if fit and fit.get('gamma_c_fit') else "— | — |")
                   + " " + ", ".join(f"{g}: {v:+.1f}" for g, v in r['fills'] if v is not None) + " |")
    open(OUT_MD, 'w').write("\n".join(out) + "\n")

if __name__ == '__main__':
    args = sys.argv[1:]; quick = '--quick' in args; args = [a for a in args if a != '--quick'] or ['all']
    windows = DEFAULT if args == ['all'] else args
    done = {json.loads(l)['window'] for l in open(OUT_JSONL)} if os.path.exists(OUT_JSONL) else set()
    for w in windows:
        parts = w.split(':'); name = parts[0]; mu = float(parts[1]); NB = int(parts[2]) if len(parts) > 2 else 46; dps = int(parts[3]) if len(parts) > 3 else 60
        key = f"{name}:{mu:g}:{NB}:{dps}"
        if key in done and not quick: print(f"[{key}] deja fait"); continue
        rec = analyse(name, mu, NB, dps, quick)
        with open(OUT_JSONL, 'a') as f: f.write(json.dumps(rec) + "\n")
        if 'error' in rec: print(f"[{key}] {rec['error']}"); continue
        ws = [x for x in rec['weights'] if x[1] is not None]
        print(f"[{key}] ell={rec['ell']:.1f} inband {rec['n_inband']}/{rec['nyquist_places']} omega_max={rec['omega_max']:.1f} w(g1)={ws[0][1]:.2f} gamma_c={rec['gamma_c_crossing']} fills={[(g, round(v,2)) for g, v in rec['fills']]} fit={rec['fit']} [{rec['seconds']}s]", flush=True)
        write_md()
    print("table :", OUT_MD)
