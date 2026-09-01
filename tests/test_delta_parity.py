# Parity does not split Delta_inf (notebook 29).
CHI5_MU30 = 17.27
CHI5_MU38 = 17.99
CHI3_CLUSTER = 16.94
CHI4_CLUSTER = 17.90


def test_chi5_climbs_toward_chi4_not_chi3():
    assert CHI5_MU38 > CHI5_MU30
    assert abs(CHI5_MU38 - CHI4_CLUSTER) < abs(CHI5_MU38 - CHI3_CLUSTER)
