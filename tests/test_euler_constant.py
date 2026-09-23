# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Garde : toute constante d'Euler codee en chaine dans code/*.py est (a) une boule VALIDE
# (|gamma - milieu| <= rayon declare) et (b) ARRONDIE, pas tronquee (|gamma - milieu| <= 0,5 ulp du
# dernier chiffre) ; et les deux moteurs du quorum (quorum_general.py, quorum_full_pd.py) prennent
# gamma par arb.const_euler(), boule certifiee qui suit la precision de travail.
# Pourquoi (23/09/2026) : quorum_general.py portait "0.5772...939" -- 48 chiffres TRONQUES, rayon
# 1e-45 : boule juste, milieu trop petit de 9,236e-49, ce qui decale CHAQUE valeur propre de la
# matrice MILIEU de +9,236e-49 ; invisible aux rayons 1e-10 des 15 sous-ensembles propres, 26 % sur
# lambda_1 du jeu complet (4,51e-48 lu pour 3,58e-48 vrai). positivite_certifiee.py portait 85 chiffres
# bien arrondis mais un rayon 1e-86 plus petit que l'erreur 4,7e-86 : boule INVALIDE.
# Usage : python3 tests/test_euler_constant.py   (mpmath seule, < 1 s)
import os, re, glob
import mpmath as mp

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code')
mp.mp.dps = 150
gamma = mp.euler
PATTERN = re.compile(r'arb\(\s*"(0\.5772\d+)"\s*(?:,\s*([0-9.eE+-]+))?\s*\)')

found = 0
for f in sorted(glob.glob(os.path.join(BASE, '*.py'))):
    src = open(f, encoding='utf-8', errors='replace').read()
    for m in PATTERN.finditer(src):
        found += 1
        s, rad = m.group(1), m.group(2)
        nd = len(s) - 2
        err = abs(gamma - mp.mpf(s))
        half_ulp = mp.mpf(10) ** (-nd) / 2
        assert err <= half_ulp, (os.path.basename(f), "chaine d'Euler TRONQUEE : erreur %s > 0,5 ulp %s" % (mp.nstr(err, 4), mp.nstr(half_ulp, 2)))
        assert rad is not None, (os.path.basename(f), "chaine d'Euler sans rayon : une valeur exacte affirmee")
        assert err <= mp.mpf(rad), (os.path.basename(f), "boule d'Euler INVALIDE : erreur %s > rayon %s" % (mp.nstr(err, 4), rad))

for name in ('quorum_general.py', 'quorum_full_pd.py'):
    p = os.path.join(BASE, name)
    if os.path.exists(p):
        assert 'arb.const_euler()' in open(p, encoding='utf-8', errors='replace').read(), (name, "gamma doit venir de arb.const_euler()")

print("euler : %d chaine(s) codee(s) controlee(s) (valides et arrondies) ; quorum_general / quorum_full_pd via const_euler : OK" % found)
