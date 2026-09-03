# chi5 mu=11 silence ratios vs 0.19 s w (notebook 89)
R2, R3, R7 = 0.251, 0.231, 0.256
TARGET = 0.19


def test_chi5_not_a_kill():
    rs = (R2, R3, R7)
    assert min(rs) > 0.15 and max(rs) < 0.35


def test_chi5_ratios_cluster():
    assert max(R2, R3, R7) - min(R2, R3, R7) < 0.05
