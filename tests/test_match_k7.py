# 1-1 matching at K=7, N=17 (notebook 53).
COS = (0.8334, 0.8108, 0.7996, 0.7521, 0.6145, 0.4956, 0.2665)


def test_k7_min_is_plunge_not_core():
    assert COS[-1] < 0.30
    assert min(COS[:5]) > 0.60


def test_k7_mean_below_k4():
    assert sum(COS) / len(COS) < 0.70
