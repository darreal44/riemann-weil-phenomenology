# RH is not claimed (notebook 52).
import os
NB = os.path.join(os.path.dirname(__file__), '..', 'report', 'le-milieu-des-premiers-v2.md')


def test_section_52_exists():
    t = open(NB).read()
    assert '## 52.' in t
    assert 'pas une preuve' in t


def test_annexe_h_does_not_claim_rh():
    t = open(NB).read()
    h = t[t.find('## Annexe H'):]
    assert 'RH' in h
    assert 'pas une preuve' in h
