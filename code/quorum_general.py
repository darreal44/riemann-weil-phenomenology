# Certification Arb generalisee du quorum : zeta ou chi3, mu et base parametres.
# Usage : python3 quorum_general.py <mu> <NB> <dps> <zeta|chi3>
import numpy as np, sys, time, itertools, os
BASE = os.path.dirname(os.path.abspath(__file__))
from flint import arb, acb, ctx

def run(mu, NB, dps, kind, mode='freeze'):
    assert mu <= 22, 'liste de premiers codee jusque 19 : etendre primes[] pour mu > 22'
    t0 = time.time(); ctx.dps = dps
    NP = NB + 1
    Larb = arb(mu).log()
    om = [2*arb.pi()*n/Larb for n in range(NP)]
    def th(n, m, y):
        if n == 0 and m == 0: return 2*(Larb - y)/Larb
        if n == 0 or m == 0:
            j = max(n, m); return -2*(om[j]*y).sin()/(arb(2).sqrt()*arb.pi()*j)
        if n == m: return 2*((Larb - y)*(om[n]*y).cos()/Larb - (om[n]*y).sin()/(2*arb.pi()*n))
        return 2*(n*(om[n]*y).sin() - m*(om[m]*y).sin())/(arb.pi()*(m*m - n*n))
    chi = (lambda n: [0,1,-1][n % 3]) if kind == 'chi3' else (lambda n: 1)
    primes = [p for p in [2,3,5,7,11,13,17,19] if p < mu - 1e-9 and chi(p) != 0]
    towers = {p: [(arb(p**k).log(), chi(p**k)*arb(p).log()/arb(p**k).sqrt())
                  for k in range(1, 9) if p**k < mu - 1e-9] for p in primes}
    eps = arb("1e-15")
    euler = arb("0.577215664901532860606512090082402431042159335939", 1e-45)
    P = {}; A = {}; T = {p: {} for p in primes}
    if kind == 'zeta':
        CR = euler + (4*arb.pi()*(Larb.exp()-1)/(Larb.exp()+1)).log()
    else:
        s0 = arb(3)/4
        CST = (arb(3)/arb.pi()).log() - euler - (1 - (-2*Larb).exp()).log()
    for n in range(NP):
        for m in range(n, NP):
            F0 = arb(2) if n == m else arb(0)
            tail = arb(0, 1e-15*1000*(n+m+2))
            if kind == 'zeta':
                P[(n,m)] = acb.integral(lambda y,_: th(n,m,y)*((y/2).exp()+(-y/2).exp()), 0, Larb).real
                ig = acb.integral(lambda y,_: ((y/2).exp()*th(n,m,y)-F0)/(y.exp()-(-y).exp()), eps, Larb).real
                A[(n,m)] = -(F0/2*CR + ig + tail)
            else:
                P[(n,m)] = arb(0)
                ig = acb.integral(lambda y,_: (-2*s0*y).exp()*(F0*(-(2-2*s0)*y).exp()-th(n,m,y))/(1-(-2*y).exp()), eps, Larb).real
                A[(n,m)] = F0/2*CST + ig + tail
            for p in primes:
                T[p][(n,m)] = -sum((w*th(n,m,acb(x)).real for x,w in towers[p]), arb(0))
    g = lambda C,n,m: C[(n,m)] if n <= m else C[(m,n)]
    radmax = max(float(M[k].rad()) for M in [P, A] + list(T.values()) for k in M)
    print(f"[{kind} mu={mu}] {NP*(NP+1)//2} paires certifiees, premiers interieurs {primes}, {time.time()-t0:.0f}s")
    Pf = np.array([[float(g(P,n,m).mid()) for m in range(NP)] for n in range(NP)])
    Af = np.array([[float(g(A,n,m).mid()) for m in range(NP)] for n in range(NP)])
    Tf = {p: np.array([[float(g(T[p],n,m).mid()) for m in range(NP)] for n in range(NP)]) for p in primes}
    res = []; frozen = []
    loaded = None
    if mode == 'verify':
        import json
        loaded = {tuple(e['S']): e['w'] for e in json.load(open(os.path.join(BASE, f"witnesses_{kind}_mu{mu}.json")))['witnesses']}
    for r in range(len(primes)+1):
        for sub in itertools.combinations(primes, r):
            if loaded is not None and tuple(sorted(sub)) in loaded:
                w = np.array([float.fromhex(h) for h in loaded[tuple(sorted(sub))]])
            else:
                Sf = Pf + Af + sum((Tf[p] for p in sub), np.zeros((NP,NP)))
                w = np.linalg.eigh(0.5*(Sf+Sf.T))[1][:,0]
            frozen.append({'S': sorted(sub), 'w': [float(x).hex() for x in w]})
            wa = [arb(float(x)) for x in w]
            # scalaires par composante
            def quad(C):
                s = arb(0)
                for n in range(NP):
                    s += wa[n]*wa[n]*g(C,n,n)
                    for m in range(n+1, NP):
                        s += 2*wa[n]*wa[m]*g(C,n,m)
                return s
            q = quad(P) + quad(A) + sum((quad(T[p]) for p in sub), arb(0))
            up = float(q.mid()) + float(q.rad())
            res.append((set(sub), up, float(q.rad())))
    proper = [x for x in res if x[0] != set(primes)]
    ok = [x for x in proper if x[1] < 0]
    qradmax = max(x[2] for x in res)
    print(f"  sous-ensembles propres : {len(proper)} ; CERTIFIES < 0 : {len(ok)}")
    worst = max(proper, key=lambda x: x[1]); best = min(proper, key=lambda x: x[1])
    print(f"  pire (le plus proche de 0) : S={worst[0]} borne {worst[1]:+.4f} ; plus violent : S={best[0]} borne {best[1]:+.4f}")
    full = [x for x in res if x[0] == set(primes)][0]
    print(f"  complet : borne sup {full[1]:+.6f} (non certifiable attendu)")
    with open(os.path.join(BASE, f"quorum_cert_{kind}_mu{mu}.txt"), "w") as f:
        f.write(f"# {kind}, mu={mu}, NB={NB}, ctx.dps={dps} ; rayon max des entrees certifiees = {radmax:.3e} ; rayon max des quotients = {qradmax:.3e}\n")
        f.write(f"# borne = mid + rad du quotient de Rayleigh certifie (Arb) ; temoins : witnesses_{kind}_mu{mu}.json (dyadiques exacts)\n")
        for s, u, rr in res: f.write(f"{sorted(s)} : {u:+.6f}  (rayon {rr:.2e})\n")
    if mode == 'freeze':
        import json
        for e, (s, u, rr) in zip(frozen, res): e['certified_upper'] = u; e['radius'] = rr
        json.dump({'kind': kind, 'mu': mu, 'NB': NB, 'witnesses': frozen}, open(os.path.join(BASE, f"witnesses_{kind}_mu{mu}.json"), "w"))
        print(f"  temoins geles : witnesses_{kind}_mu{mu}.json")
    print(f"  table complete : quorum_cert_{kind}_mu{mu}.txt ; total {time.time()-t0:.0f}s")

if __name__ == '__main__':
    run(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else 'freeze')
