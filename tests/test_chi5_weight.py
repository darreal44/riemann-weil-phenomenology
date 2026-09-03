# chi5 silence / (s_inf w); notebook 90-91
R11, R16, R22 = 0.25, 0.235, 0.215
R30_INTERIOR = (0.199, 0.197, 0.196, 0.198)  # p=11,13,17,19 at mu=30
TARGET = 0.19


def test_ratio_falls_toward_target():
    assert R11 > R16 > R22 > TARGET


def test_mu30_interior_hits_019():
    assert all(abs(r - TARGET) < 0.012 for r in R30_INTERIOR)
    assert abs(sum(R30_INTERIOR)/4 - TARGET) < 0.01
