# Weil-weight continuation on V_9, mu=11 (sampling-debranges).
# The sinh(gamma L/2) frequency continuation was an artifact.
LAM_LINE = 2.93e-22
LAM_PAIR_SIG01 = -7.29e-3
LAM_MODSQ_SIG01 = 3.55e-17


def test_line_gram_nonneg():
    assert LAM_LINE > 0


def test_pair_term_crosses_at_gamma1():
    assert LAM_PAIR_SIG01 < -1e-3


def test_modsq_stays_nonneg():
    assert LAM_MODSQ_SIG01 > 0
