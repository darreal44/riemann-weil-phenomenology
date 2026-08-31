# Coherence des artefacts de certification a mu=11 : tables lisibles, temoins JSON valides,
# bornes negatives sur tout sous-ensemble propre, complet non certifie, table <-> JSON coherents.
# Usage : python3 tests/test_cert_mu11.py   (stdlib seule, <1 s)
import json, os, re
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code')
rows = {}
for line in open(os.path.join(BASE, 'quorum_cert_zeta_mu11.txt')):
    if line.startswith('#'): continue
    m = re.match(r"\[(.*)\] : ([+-][0-9.]+)", line)
    S = tuple(sorted(int(x) for x in m.group(1).split(',') if x.strip()))
    rows[S] = float(m.group(2))
assert len(rows) == 16
full = (2,3,5,7)
for S, u in rows.items():
    if S != full: assert u < -0.3, (S, u, "sous-ensemble propre non certifie negatif !")
assert abs(rows[full]) < 1e-3, "le complet devrait etre ~0 (non certifiable)"
d = json.load(open(os.path.join(BASE, 'witnesses_zeta_mu11.json')))
assert d['kind'] == 'zeta' and d['mu'] == 11 and len(d['witnesses']) == 16
for e in d['witnesses']:
    assert len(e['w']) == 47
    float.fromhex(e['w'][0])  # dyadiques exacts relisibles
    S = tuple(sorted(e['S']))
    assert abs(e['certified_upper'] - rows[S]) < 5e-6, (S, "table et JSON divergent")
print("test_cert_mu11 : OK (16 lignes, 15 propres < -0.3, complet ~0, JSON <-> table coherents)")
