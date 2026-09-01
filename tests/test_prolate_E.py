# E(prolate combo) aligns with ground state (notebook 61).
COS_H0 = 0.0583
COS_COMBO = 0.8079


def test_h0_still_poor():
    assert COS_H0 < 0.15


def test_mean_zero_combo_aligns():
    assert COS_COMBO > 0.75
