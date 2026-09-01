# Schematic off-line continuation on V_5 is indefinite for sigma>=0.05
# (notebook sampling-debranges). Not the Weil-Bombieri term.
LAM_LINE = 4.945e-15
LAM_SIG005 = -9.9e6


def test_real_gram_stays_nonneg():
    assert LAM_LINE > 0


def test_schematic_offline_crosses():
    assert LAM_SIG005 < -1.0
