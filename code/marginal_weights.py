#!/usr/bin/env python3
"""Marginal weight of each in-band zero in the depth (notebook 128-130).

w(gamma_k) = ln lambda_0(G) - ln lambda_0(G minus gamma_k).

G is built once. Each leave-one-out / fill is a rank-1 update
    G ∓ 2 c(gamma) c(gamma)^T
then one mpmath eigsy — not a rebuild.

--workers   parallel windows (separate processes; mpmath holds the GIL)
--inner     parallel leave-one-out / fills inside a window
On a 3975WX (32c/64t, 64GB): --workers 4 --inner 8 (32 processes). Peak RAM a few GB
(copies of one 40-67 mpmath Gram per inner worker). The A6000 does not
help: eigenvalues are 10^{-20}…10^{-60}, float64 eigh is unusable.

usage: python3 code/marginal_weights.py [--quick] [--workers N] [--inner M] all
"""
import os, sys, json, time, math, pickle, argparse
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
OUT_JSONL = os.path.join(ROOT, 'report', 'marginal-weights.jsonl'); OUT_MD = os.path.join(ROOT, 'report', 'marginal-weights.md')
DEFAULT = ['zeta:8:40:60', 'zeta:11:40:60', 'zeta:16:40:65', 'zeta:11:60:90', 'chi3:16:46:65', 'chi5:16:46:65', 'chi4:16:46:65',
           'chi8:16:46:65', 'chi13:16:46:60', 'chi3:38:66:80', 'chi5:38:66:80', 'chi29:22:52:60', '11a1:11:24:50', '11a1:22:36:60']
FILLS = {'zeta': [4.0, 7.0, 10.0], 'default_frac': [0.3, 0.55, 0.8]}

def zeros_of(name):
    for f in (f'zeros_{name}_weyl.pkl', f'zeros_{name}_150.pkl', f'zeros_{name}.pkl', 'zeros500.pkl' if name == 'zeta' else None):
        if f and os.path.exists(os.path.join(HERE, f)):
            return sorted(float(str(x)) for x in pickle.load(open(os.path.join(HERE, f), 'rb'))), f
    raise FileNotFoundError(name)

def _rank1_eigs(G, c, sign, dps):
    """Smallest eig of G + sign * 2 c c^T. sign=-1 removes a zero, +1 fills."""
    mp.mp.dps = dps
    NP = G.rows
    G2 = mp.matrix(NP)
    two = mp.mpf(2) * sign
    for i in range(NP):
        ci = two * c[i]
        for j in range(i, NP):
            G2[i, j] = G[i, j] + ci * c[j]
        for j in range(i):
            G2[i, j] = G2[j, i]
    e = mp.eigsy(G2, eigvals_only=True)[0]
    return e

def analyse(name, mu, NB, dps, quick, inner=1):
    mp.mp.dps = dps; NP = NB + 1; L = mp.log(mu); om = [2*mp.pi*n/L for n in range(NP)]; omax = float(om[NB])
    Z, zf = zeros_of(name)
    def cvec(g):
        gg = mp.mpf(g); sn = mp.sin(gg*L/2)
        return mp.matrix([2*sn/(gg*mp.sqrt(L))] + [mp.sqrt(2/L)*sn*2*gg/(gg*gg-om[n]*om[n]) for n in range(1, NP)])
    t0 = time.time()
    G = mp.matrix(NP)
    csv = {}
    for g in Z:
        c = cvec(g); csv[g] = c
        for i in range(NP):
            ci2 = 2*c[i]
            for j in range(i, NP):
                G[i, j] += ci2 * c[j]
    for i in range(NP):
        for j in range(i):
            G[i, j] = G[j, i]
    base_e = mp.eigsy(G, eigvals_only=True)[0]
    if base_e <= 0:
        return dict(window=f"{name}:{mu:g}:{NB}:{dps}", error="lambda_0 <= 0 at this dps (increase dps)")
    inb = [g for g in Z if g < omax]; nyq = float(L)/(2*math.pi)
    D = [(g, g*nyq - (k+1)) for k, g in enumerate(inb)]
    gc = None
    for k in range(1, len(D)):
        if D[k-1][1] > 0 >= D[k][1]:
            gc = D[k-1][0] + (D[k][0]-D[k-1][0])*D[k-1][1]/(D[k-1][1]-D[k][1]); break
    ks = [0, 1, len(inb)//3, 2*len(inb)//3] if quick else list(range(len(inb)))
    fills = FILLS['zeta'] if name == 'zeta' else [round(f*inb[0], 3) for f in FILLS['default_frac']]
    if quick: fills = fills[:2]

    jobs = [('w', inb[k], csv[inb[k]], -1) for k in ks] + [('f', g, cvec(g), +1) for g in fills]

    def run_job(job):
        kind, g, c, sign = job
        e = _rank1_eigs(G, c, sign, dps)
        return kind, g, float(e) if e > 0 else None

    results = []
    if inner <= 1 or len(jobs) <= 2:
        results = [run_job(j) for j in jobs]
    else:
        from concurrent.futures import ProcessPoolExecutor
        # spawn workers that receive (G, c, sign, dps) — G is the same object pickled once per task
        with ProcessPoolExecutor(max_workers=min(inner, len(jobs))) as ex:
            futs = [ex.submit(_rank1_eigs, G, j[2], j[3], dps) for j in jobs]
            for j, fut in zip(jobs, futs):
                e = fut.result()
                results.append((j[0], j[1], float(e) if e > 0 else None))

    weights, fillw = [], []
    for kind, g, e in results:
        if kind == 'w':
            weights.append([g, float(mp.log(base_e/e)) if e else None])
        else:
            fillw.append([g, float(mp.log(e/base_e)) if e else None])
    pts = [(g, w) for g, w in weights if w is not None and (gc is None or g < gc)]
    fit = None
    if len(pts) >= 3:
        import numpy as np
        A = np.array([[1.0, -g] for g, _ in pts]); y = np.array([w for _, w in pts])
        (w0, w0_over_gc), *_ = np.linalg.lstsq(A, y, rcond=None)
        fit = dict(w0=float(w0), gamma_c_fit=float(w0/w0_over_gc) if w0_over_gc else None)
    return dict(window=f"{name}:{mu:g}:{NB}:{dps}", name=name, mu=mu, NB=NB, dps=dps, zeros_file=zf, n_zeros=len(Z), omega_max=omax,
                n_inband=len(inb), nyquist_places=NB, ell=float(-mp.log(base_e)), gamma_1=inb[0], gamma_c_crossing=gc,
                weights=weights, fills=fillw, fit=fit, quick=quick, seconds=round(time.time()-t0))

def _analyse_key(args):
    name, mu, NB, dps, quick, inner = args
    return analyse(name, mu, NB, dps, quick, inner)

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
    ap = argparse.ArgumentParser()
    ap.add_argument('--quick', action='store_true')
    ap.add_argument('--workers', type=int, default=int(os.environ.get('JOBS', '1')))
    ap.add_argument('--inner', type=int, default=int(os.environ.get('INNER', '1')))
    ap.add_argument('windows', nargs='*', default=['all'])
    opt = ap.parse_args()
    windows = DEFAULT if opt.windows == ['all'] else opt.windows
    done = {json.loads(l)['window'] for l in open(OUT_JSONL)} if os.path.exists(OUT_JSONL) else set()
    jobs = []
    for w in windows:
        parts = w.split(':'); name = parts[0]; mu = float(parts[1]); NB = int(parts[2]) if len(parts) > 2 else 46; dps = int(parts[3]) if len(parts) > 3 else 60
        key = f"{name}:{mu:g}:{NB}:{dps}"
        if key in done and not opt.quick:
            print(f"[{key}] deja fait"); continue
        jobs.append((name, mu, NB, dps, opt.quick, opt.inner))
    workers = max(1, opt.workers)
    print(f"marginal_weights: {len(jobs)} windows, workers={workers} inner={opt.inner}", flush=True)
    recs = []
    if workers == 1 or len(jobs) <= 1:
        recs = [_analyse_key(j) for j in jobs]
    else:
        from concurrent.futures import ProcessPoolExecutor, as_completed
        with ProcessPoolExecutor(max_workers=min(workers, len(jobs))) as ex:
            futs = {ex.submit(_analyse_key, j): j for j in jobs}
            for fut in as_completed(futs):
                recs.append(fut.result())
    with open(OUT_JSONL, 'a') as f:
        for rec in recs:
            f.write(json.dumps(rec) + "\n")
            key = rec.get('window', '?')
            if 'error' in rec:
                print(f"[{key}] {rec['error']}", flush=True); continue
            ws = [x for x in rec['weights'] if x[1] is not None]
            print(f"[{key}] ell={rec['ell']:.1f} inband {rec['n_inband']}/{rec['nyquist_places']} omega_max={rec['omega_max']:.1f} w(g1)={ws[0][1]:.2f} gamma_c={rec['gamma_c_crossing']} fills={[(g, round(v,2)) for g, v in rec['fills']]} fit={rec['fit']} [{rec['seconds']}s]", flush=True)
    write_md()
    print("table :", OUT_MD)
