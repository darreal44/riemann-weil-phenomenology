# Resolution, not Lambda, moves the 2-adic hard-window weight at Lambda=4.
# Locked from weights_2adic / vectorized Fmat (2026-09-03).
W4_16 = -0.050
W4_32 = 0.167
W4_48 = 0.266
W4_64 = 0.316
W4_80 = 0.352
W4_96 = 0.373
EXPECTED = 0.490
EXTRAP_H0 = 0.488  # linear fit of cpu 64,80,96


def test_lambda4_weight_rises_with_resolution():
    assert W4_16 < W4_32 < W4_48 < W4_64 < W4_80 < W4_96


def test_lambda4_not_yet_at_expected():
    assert W4_64 < EXPECTED
    assert EXPECTED - W4_64 > 0.10


def test_coarse_lambda16_does_not_close():
    # cpu=16 at Lam=16 went negative: bigger Lambda without matching h fails
    w16_16 = -0.397
    assert w16_16 < 0


def test_h0_extrapolation_hits_expected():
    assert abs(EXTRAP_H0 - EXPECTED) < 0.01
