# Synthetic tail at Gmax=20000 (notebook 33).
RESIDUAL_11 = 0.709e-3
RESIDUAL_4000 = 1.458e-3


def test_doubling_G_cuts_residual():
    assert RESIDUAL_11 < 0.8e-3
    assert RESIDUAL_11 < 0.6 * RESIDUAL_4000
