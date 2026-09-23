# Copyright (c) 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Certification Arb du JEU COMPLET du quorum (zeta, mu=11, NB=46) : Q_{2,3,5,7} est definie
# positive sur V (47 modes), et son plus petit quotient de Rayleigh a une borne inferieure > 0.
# Complement de quorum_general.py, dont les 15 sous-ensembles propres sont certifies < 0 :
# la ligne 16 de la table. Le theoreme sur les zeros n'en dit rien de plus que Turing (T0 = 2 pi mu).
#
# Usage : python3 quorum_full_pd.py freeze    -> construit Q en boules (eps=1e-58, dps=85), diagonalise
#                                                le MILIEU (mpmath), gele V et v_1 en dyadiques EXACTS,
#                                                certifie, ecrit witnesses_zeta_mu11_full.json et
#                                                quorum_cert_zeta_mu11_full.txt
#         python3 quorum_full_pd.py verify    -> rejoue V et v_1 geles sur une matrice Q reconstruite,
#                                                SANS solveur propre : Gershgorin en boules sur V^T Q V,
#                                                sur V^T V, et le quotient certifie de v_1
#
# Certificat (congruence -- loi d'inertie de Sylvester -- puis Gershgorin, tout en boules Arb) :
#   V inversible (V^T V a diagonale dominante en boules) et B = V^T Q V a diagonale dominante en boules
#   => B definie positive => Q definie positive sur V (la congruence conserve la positivite, pas les
#   valeurs propres). Borne numerique publiee : lambda_min(Q) >= m_B / M_V avec m_B = min_i [lower(B_ii) -
#   sum_{j!=i} upper(|B_ij|)] (Gershgorin bas) et M_V = max_i [(V^T V)_ii + sum_{j!=i} |(V^T V)_ij|]
#   (Gershgorin haut) >= lambda_max(V^T V) ; car x^T Q x = y^T B y >= m_B |y|^2 >= (m_B / M_V) |x|^2, y = V^{-1} x.
#   lower(Q(v_1)/|v_1|^2) > 0 est une seconde ligne, plus faible (une direction), a cote.
# Reglage : eps = 1e-58 (queue du lemme : 1000(n+m+2) eps <= 9.4e-54 par entree), dps = 85,
#   gamma d'Euler par arb.const_euler() (boule certifiee ; la chaine de 48 chiffres de quorum_general.py
#   etait TRONQUEE : boule juste, milieu trop petit de 9.236e-49, ce qui decale chaque valeur propre du
#   milieu de +9.236e-49 -- invisible aux rayons 1e-10 des sous-ensembles propres, 26 % sur lambda_1).
#   Marge attendue : somme de ligne de Gershgorin <= 46*47*9.4e-54 ~ 2e-50 contre lambda_1 ~ 3.58e-48.
import sys, json, time, os
import mpmath as mp
from flint import arb, acb, ctx, fmpz

BASE = os.path.dirname(os.path.abspath(__file__))
MU, NB = 11, 46
EPS, DPS = '1e-58', 85
WIT = os.path.join(BASE, 'witnesses_zeta_mu11_full.json')
CERT = os.path.join(BASE, 'quorum_cert_zeta_mu11_full.txt')
NL = chr(10)

def _down(x):
    """Trois ulps vers -inf : absorbe les arrondis au plus proche des deux float() et de l'operation flottante."""
    import math
    for _ in range(3):
        x = math.nextafter(x, -math.inf)
    return x

def _up(x):
    """Trois ulps vers +inf, meme raison."""
    import math
    for _ in range(3):
        x = math.nextafter(x, math.inf)
    return x

def build(mu, NB, dps, eps_str):
    """Memes th, tours, integrales et queue du lemme que quorum_general.run ; euler certifie."""
    ctx.dps = dps
    NP = NB + 1
    Larb = arb(mu).log()
    om = [2*arb.pi()*n/Larb for n in range(NP)]
    def th(n, m, y):
        if n == 0 and m == 0: return 2*(Larb - y)/Larb
        if n == 0 or m == 0:
            j = max(n, m); return -2*(om[j]*y).sin()/(arb(2).sqrt()*arb.pi()*j)
        if n == m: return 2*((Larb - y)*(om[n]*y).cos()/Larb - (om[n]*y).sin()/(2*arb.pi()*n))
        return 2*(n*(om[n]*y).sin() - m*(om[m]*y).sin())/(arb.pi()*(m*m - n*n))
    primes = [2, 3, 5, 7]
    towers = {p: [(arb(p**k).log(), arb(p).log()/arb(p**k).sqrt())
                  for k in range(1, 9) if p**k < mu - 1e-9] for p in primes}
    eps = arb(eps_str); eps_f = float(eps_str)
    euler = arb.const_euler()
    CR = euler + (4*arb.pi()*(Larb.exp()-1)/(Larb.exp()+1)).log()
    Q = {}
    for n in range(NP):
        for m in range(n, NP):
            F0 = arb(2) if n == m else arb(0)
            tail = arb(0, eps_f*1000*(n+m+2))
            P = acb.integral(lambda y,_: th(n,m,y)*((y/2).exp()+(-y/2).exp()), 0, Larb).real
            ig = acb.integral(lambda y,_: ((y/2).exp()*th(n,m,y)-F0)/(y.exp()-(-y).exp()), eps, Larb).real
            A = -(F0/2*CR + ig + tail)
            T = sum((-sum((w*th(n,m,acb(x)).real for x,w in towers[p]), arb(0)) for p in primes), arb(0))
            Q[(n,m)] = P + A + T
    return Q, NP, float(euler.rad())

def g(Q, n, m):
    return Q[(n,m)] if n <= m else Q[(m,n)]

def dyadic_str(x):
    s, man, e, bc = mp.mpf(x)._mpf_
    return "%s%d*2^%d" % ("-" if s else "", int(man), int(e))

def arb_from_dyadic(s):
    neg = s.startswith('-')
    man, e = s.lstrip('-').split('*2^')
    v = arb(fmpz(int(man))) * arb(2)**int(e)
    return -v if neg else v

def arb_to_mpf(x):
    man, e = x.mid().man_exp()
    return mp.mpf(int(man)) * mp.mpf(2)**int(e)

def gershgorin_lower(B, n):
    """min_i [ lower(B_ii) - sum_{j!=i} upper(|B_ij|) ], borne INFERIEURE de la marge ; > 0 => B definie positive."""
    worst = None
    for i in range(n):
        d = B[i][i]
        lo = d.mid() - d.rad()
        s = arb(0)
        for j in range(n):
            if j != i:
                s += abs(B[i][j])
        m = lo - (s.mid() + s.rad())
        margin = _down(float(m.mid()) - float(m.rad()))
        if worst is None or margin < worst[0]:
            worst = (margin, i)
    return worst

def gershgorin_upper(A, n):
    """max_i [ upper(A_ii) + sum_{j!=i} upper(|A_ij|) ] >= lambda_max(A), en boules."""
    best = None
    for i in range(n):
        s = A[i][i]
        for j in range(n):
            if j != i:
                s += abs(A[i][j])
        v = _up(float(s.mid()) + float(s.rad()))
        if best is None or v > best:
            best = v
    return best

def certify(Q, NP, Va, v1a):
    """Va : matrice de passage (listes de arb exacts, Va[r][c]) ; v1a : temoin (arb exacts)."""
    QV = [[sum((g(Q, r, k) * Va[k][c] for k in range(NP)), arb(0)) for c in range(NP)] for r in range(NP)]
    B = [[sum((Va[k][i] * QV[k][j] for k in range(NP)), arb(0)) for j in range(NP)] for i in range(NP)]
    marge_B, i_B = gershgorin_lower(B, NP)
    VtV = [[sum((Va[k][i] * Va[k][j] for k in range(NP)), arb(0)) for j in range(NP)] for i in range(NP)]
    marge_V, i_V = gershgorin_lower(VtV, NP)
    M_V = gershgorin_upper(VtV, NP)
    lam_min_Q_lower = _down(marge_B / M_V) if (M_V > 0 and marge_B > 0) else float('-inf')
    q = sum((v1a[n]*v1a[n]*g(Q,n,n) for n in range(NP)), arb(0))
    q += sum((2*v1a[n]*v1a[m]*g(Q,n,m) for n in range(NP) for m in range(n+1, NP)), arb(0))
    ray = q / sum((x*x for x in v1a), arb(0))
    lower = _down(float(ray.mid()) - float(ray.rad()))
    radB = _up(max(float(B[i][j].rad()) for i in range(NP) for j in range(NP)))
    return {"gershgorin_margin_B": marge_B, "row_B": i_B, "gershgorin_margin_VtV": marge_V, "row_VtV": i_V,
            "lambda_max_VtV_upper": M_V, "lambda_min_Q_lower": lam_min_Q_lower,
            "rayleigh_mid": float(ray.mid()), "rayleigh_rad": float(ray.rad()), "certified_lower": lower,
            "rad_max_B": radB, "positive_definite": (marge_B > 0 and marge_V > 0)}

def run(mode):
    t0 = time.time()
    Q, NP, euler_rad = build(MU, NB, DPS, EPS)
    radQ = max(float(Q[k].rad()) for k in Q)
    print(f"[zeta mu={MU} NB={NB}] {NP*(NP+1)//2} paires certifiees, eps={EPS}, dps={DPS}, rayon max d'entree {radQ:.3e}, {time.time()-t0:.0f}s")
    if mode == 'freeze':
        mp.mp.dps = DPS
        M = mp.matrix(NP, NP)
        for n in range(NP):
            for m in range(NP):
                M[n, m] = arb_to_mpf(g(Q, n, m))
        E, V = mp.eigsy(M)
        order = sorted(range(NP), key=lambda i: E[i])
        Vd = [[dyadic_str(V[r, order[c]]) for c in range(NP)] for r in range(NP)]   # colonnes triees, lambda croissant
        v1d = [Vd[r][0] for r in range(NP)]
        lam = [mp.nstr(E[i], 15) for i in order]
        print(f"  milieu : lambda_1 = {lam[0]} ; lambda_2 = {lam[1]} ; lambda_max = {lam[-1]}")
    else:
        w = json.load(open(WIT))
        Vd, v1d, lam = w['V_dyadic'], w['v1_dyadic'], w['lambda_mid']
        print(f"  temoins geles relus : {WIT}")
    Va = [[arb_from_dyadic(Vd[r][c]) for c in range(NP)] for r in range(NP)]
    v1a = [arb_from_dyadic(s) for s in v1d]
    res = certify(Q, NP, Va, v1a)
    print(f"  Gershgorin(V^T Q V) marge min {res['gershgorin_margin_B']:+.4e} (ligne {res['row_B']}) ; rayon max de B {res['rad_max_B']:.3e}")
    print(f"  Gershgorin(V^T V)   marge min {res['gershgorin_margin_VtV']:+.4e} (ligne {res['row_VtV']}) ; lambda_max(V^T V) <= 1 + {res['lambda_max_VtV_upper']-1:.3e}")
    print(f"  => lambda_min(Q) >= m_B / M_V = {res['lambda_min_Q_lower']:+.6e}   (la congruence conserve la positivite, pas les valeurs propres)")
    print(f"  Q(v_1)/|v_1|^2 : mid {res['rayleigh_mid']:+.6e} rad {res['rayleigh_rad']:.3e} -> borne INFERIEURE {res['certified_lower']:+.6e}")
    verdict = "DEFINIE POSITIVE sur V (certifie)" if res['positive_definite'] else "NON CERTIFIEE"
    print(f"  complet {{2,3,5,7}} : {verdict} ; borne inf du quotient {'> 0' if res['certified_lower'] > 0 else 'NON certifiee'} ; total {time.time()-t0:.0f}s")
    if mode == 'freeze':
        json.dump({"kind": "zeta", "mu": MU, "NB": NB, "eps": EPS, "dps": DPS, "S": [2, 3, 5, 7],
                   "lambda_mid": lam, "v1_dyadic": v1d, "V_dyadic": Vd, **res}, open(WIT, 'w'))
        with open(CERT, 'w') as f:
            f.write(f"# zeta, mu={MU}, NB={NB}, eps={EPS}, ctx.dps={DPS} ; rayon max des entrees certifiees = {radQ:.3e} ; rayon d'Euler = {euler_rad:.1e}" + NL)
            f.write("# jeu COMPLET : certificat par congruence (inertie de Sylvester) + Gershgorin en boules sur V^T Q V (V exacte dyadique, gelee) ; temoin v_1 dyadique" + NL)
            f.write(f"lambda_min(Q_{{2,3,5,7}}) >= m_B / M_V = {res['lambda_min_Q_lower']:+.6e}   (m_B = marge de Gershgorin sur B = {res['gershgorin_margin_B']:+.4e} ; M_V = borne haute de Gershgorin sur V^T V = 1 + {res['lambda_max_VtV_upper']-1:.2e})" + NL)
            f.write(f"[2, 3, 5, 7] : borne INFERIEURE du quotient du temoin v_1 : {res['certified_lower']:+.6e}  (mid {res['rayleigh_mid']:+.6e}, rayon {res['rayleigh_rad']:.2e})" + NL)
            f.write(f"Gershgorin(V^T V) : marge basse {res['gershgorin_margin_VtV']:+.4e} (inversibilite) ; rayon max de B = {res['rad_max_B']:.3e}" + NL)
            f.write(f"VERDICT : Q_{{2,3,5,7}} {verdict} ; temoins : {os.path.basename(WIT)} ; rejeu : python3 quorum_full_pd.py verify" + NL)
        print(f"  ecrit : {CERT} ; {WIT}")

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'verify'
    assert mode in ('freeze', 'verify'), "mode : freeze | verify"
    run(mode)
