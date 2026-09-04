RATIO_MU3 = 2.56
RATIO_CHI5_30 = 5.11

def test_desert_slepian_factor_grows():
    assert 2 < RATIO_MU3 < 3
    assert RATIO_CHI5_30 > RATIO_MU3
