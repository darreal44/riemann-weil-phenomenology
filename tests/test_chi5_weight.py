# chi5 deep-basis silence ratios (notebook 90)
R11_MED, R16_MED, R22_MED = 0.25, 0.235, 0.215
TARGET = 0.19


def test_ratio_falls_toward_target():
    assert R11_MED > R16_MED > R22_MED > TARGET


def test_mu22_cluster():
    cluster = (0.213, 0.215, 0.211, 0.213)
    assert max(cluster) - min(cluster) < 0.01
