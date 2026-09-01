# chi7 is still climbing, not a second chi3 (notebook 30).
CHI7_MU30 = 16.23
CHI7_MU38 = 17.34
CHI3_CLUSTER = 16.94


def test_chi7_climbs():
    assert CHI7_MU38 > CHI7_MU30


def test_chi7_already_above_chi3_cluster_at_ell_58():
    assert CHI7_MU38 > CHI3_CLUSTER
