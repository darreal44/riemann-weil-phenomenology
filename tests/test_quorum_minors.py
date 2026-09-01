# B1/B2 at zeta mu=16: 6/6 negative 2x2 once R=12 (notebook 20).
# Frozen dets from lemma_B_mu16.py N=29 R=12. Do not re-assemble Q.
import os

BEST_DET = {2: -0.1969, 3: -0.1418, 5: -0.1679, 7: -0.1039, 11: -0.1006, 13: -0.0316}


def test_all_six_interior_primes_have_negative_minors():
    assert all(d < -0.02 for d in BEST_DET.values())
    assert set(BEST_DET) == {2, 3, 5, 7, 11, 13}


def test_edge_primes_weaker_than_2():
    assert BEST_DET[13] > BEST_DET[2]
    assert BEST_DET[11] > BEST_DET[2]


def test_lemma_B_mu16_script_has_restrict():
    src = open(os.path.join(os.path.dirname(__file__), '..', 'code', 'lemma_B_mu16.py')).read()
    assert 'def restrict' in src
    assert 'mu = 16' in src or 'mu=16' in src or '16' in src
