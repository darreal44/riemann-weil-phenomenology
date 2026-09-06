#!/usr/bin/env python3
"""Edge value of the ground state vs depth, across windows (notebook 125-126).

For each window (L-function, mu): assemble the prime-side Q (spectro / spectro_zeta), take the
ground state v, and record
    ell_Q   = -ln lambda_0
    edge    = -2 ln |psi(0)|,   psi(0) = (v_0 + sqrt2 * sum_{n>=1} v_n) / sqrt(L)   (value at the window edge)
    R       = ell_Q - edge                                  (Grok's edge-doubling residual)
    tau*g1  = (L/2) * gamma_1                                (Slepian parameter of the desert)
Question (notebook 126): does the edge value alone follow tau*gamma_1 with the dispersion of ell_Q?

Resumable: appends one JSON line per window to report/edge-value-scan.jsonl and rewrites
report/edge-value-scan.md from all lines. Heavy windows (mu >= 38) take minutes each: run on the server.

usage:  python3 code/edge_value_scan.py [window ...]      window = name:mu[:NB:dps], e.g. chi5:16 chi3:38:66:70
        python3 code/edge_value_scan.py all               (the eleven windows of lemma2-ell-fit.md + zeta 11, 16)
"""
import os, sys, io, json, time, pickle, contextlib
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from kronecker import chi_tab
from scan_s import CHARS
OUT_JSONL = os.path.join(ROOT, 'report', 'edge-value-scan.jsonl')
OUT_MD = os.path.join(ROOT, 'report', 'edge-value-scan.md')

DEFAULT = ['zeta:11', 'zeta:16', 'chi5:16', 'chi5:38', 'chi3:16', 'chi3:38', 'chi3:80', 'chi4:16', 'chi4:38',
           'chi8:16', 'chi13:16', 'chi29:38', 'chi31:38']
def default_NB_dps(mu):
    if mu <= 11: return 40, 50
    if mu <= 16: return 46, 60
    if mu <= 22: return 52, 65
    if mu <= 38: return 66, 75
    return 80, 90

def load_module(fname):
    src = open(os.path.join(HERE, fname)).read()
    src = src.replace("    E, V = mp.eigsy(S)", "    import builtins; builtins._SCAP = S; E, V = mp.eigsy(S)")
    ns = {'__name__': 'spectro_mod'}
    exec(compile(src.replace("if __name__ == '__main__':", "if False:"), fname, 'exec'), ns)
    return ns

def gamma1(name):
    for f in (f'zeros_{name}_weyl.pkl', f'zeros_{name}_150.pkl', f'zeros_{name}.pkl', 'zeros500.pkl' if name == 'zeta' else None):
        if f and os.path.exists(os.path.join(HERE, f)):
            Z = sorted(float(str(x)) for x in pickle.load(open(os.path.join(HERE, f), 'rb')))
            return Z[0]
    return None

def one(window, nsZ, nsC):
    parts = window.split(':'); name = parts[0]; mu = float(parts[1])
    NB, dps = default_NB_dps(mu)
    if len(parts) > 2: NB = int(parts[2])
    if len(parts) > 3: dps = int(parts[3])
    mp.mp.dps = dps; NP = NB + 1; L = mp.log(mu)
    import builtins
    t0 = time.time()
    with contextlib.redirect_stdout(io.StringIO()):
        if name == 'zeta':
            nsZ['run'](mp.mpf(mu), NB, dps, 12, K=1)
        else:
            c = CHARS[name]; tab = chi_tab(c['d'], c['q'])
            nsC['run'](mp.mpf(mu), NB, dps, 12, K=1, q=c['q'], tab=tab, apar=c['a'])
    S = builtins._SCAP
    E, V = mp.eigsy(S); lam0 = E[0]; v = [V[i, 0] for i in range(NP)]
    psi0 = (v[0] + mp.sqrt(2) * mp.fsum(v[1:])) / mp.sqrt(L)
    g1 = gamma1(name)
    rec = dict(window=window, name=name, mu=mu, NB=NB, dps=dps, lambda0=float(lam0) if lam0 > 0 else None,
               lambda0_str=mp.nstr(lam0, 6), ell=float(-mp.log(lam0)) if lam0 > 0 else None,
               edge=float(-2 * mp.log(abs(psi0))), psi0=mp.nstr(psi0, 6), gamma1=g1,
               tau_g1=float(L / 2 * g1) if g1 else None, seconds=round(time.time() - t0))
    rec['R'] = (rec['ell'] - rec['edge']) if rec['ell'] is not None else None
    return rec

def write_md():
    rows = [json.loads(l) for l in open(OUT_JSONL)] if os.path.exists(OUT_JSONL) else []
    seen = {}
    for r in rows: seen[r['window']] = r
    lines = ["# Edge value of the ground state vs depth (notebook 125-126)", "",
             "ell_Q = -ln lambda_0 ; edge = -2 ln|psi(0)| ; R = ell - edge ; tau*g1 = (L/2) gamma_1.", "",
             "| window | NB | dps | lambda_0 | ell_Q | edge | ell/edge | R | tau*g1 | ell/(tau g1) | edge/(tau g1) |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for w in sorted(seen, key=lambda k: (seen[k]['name'], seen[k]['mu'])):
        r = seen[w]
        if r['ell'] is None:
            lines.append(f"| {w} | {r['NB']} | {r['dps']} | {r['lambda0_str']} | (lambda_0 <= 0: precision) | {r['edge']:.2f} | — | — | — | — | — |"); continue
        tg = r['tau_g1']
        lines.append(f"| {w} | {r['NB']} | {r['dps']} | {r['lambda0_str']} | {r['ell']:.2f} | {r['edge']:.2f} | {r['ell']/r['edge']:.3f} | {r['R']:+.2f} | "
                     + (f"{tg:.2f} | {r['ell']/tg:.2f} | {r['edge']/tg:.2f} |" if tg else "— | — | — |"))
    open(OUT_MD, 'w').write("\n".join(lines) + "\n")

if __name__ == '__main__':
    args = sys.argv[1:] or ['all']
    windows = DEFAULT if args == ['all'] else args
    nsZ = load_module('spectro_zeta.py'); nsC = load_module('spectro.py')
    done = set()
    if os.path.exists(OUT_JSONL):
        done = {json.loads(l)['window'] for l in open(OUT_JSONL)}
    for w in windows:
        if w in done:
            print(f"[{w}] deja fait, saute"); continue
        rec = one(w, nsZ, nsC)
        with open(OUT_JSONL, 'a') as f: f.write(json.dumps(rec) + "\n")
        print(f"[{w}] NB={rec['NB']} dps={rec['dps']} lambda0={rec['lambda0_str']} ell={rec['ell'] if rec['ell'] is None else round(rec['ell'],2)} edge={rec['edge']:.2f} R={rec['R'] if rec['R'] is None else round(rec['R'],2)} tau*g1={rec['tau_g1'] and round(rec['tau_g1'],2)} [{rec['seconds']}s]", flush=True)
        write_md()
    print("table :", OUT_MD)
