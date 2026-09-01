# chi-20 last secant 50->62 (notebook 36).
SECANT_50_62 = 0.582
SHAT_3VAR = 0.44
SHAT_4VAR = 0.57


def test_secant_near_058():
    assert 0.57 < SECANT_50_62 < 0.60


def test_three_var_misses_frozen_s():
    assert SHAT_3VAR / SECANT_50_62 - 1 < -0.20


def test_four_var_accidentally_close():
    assert abs(SHAT_4VAR / SECANT_50_62 - 1) < 0.05
