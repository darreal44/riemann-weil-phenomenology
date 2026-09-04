DEFICIT_ZETA3_G1 = 3.9
DEFICIT_ZETA11_G1 = 9.8

def test_landau_deficit_grows_with_mu():
    assert DEFICIT_ZETA11_G1 > DEFICIT_ZETA3_G1
