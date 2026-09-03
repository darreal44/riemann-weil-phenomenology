# chi5 silence / (s w) vs 0.19
# mu=11: p=2,3,7 ; mu=16: p=2,3,7,11,13
R11 = (0.251, 0.231, 0.256)
R16 = (0.245, 0.219, 0.227, 0.235, 0.249)
TARGET = 0.19


def test_chi5_mu11_not_a_kill():
    assert min(R11) > 0.15 and max(R11) < 0.35


def test_chi5_mu16_not_a_kill():
    assert min(R16) > 0.15 and max(R16) < 0.35


def test_chi5_two_windows_agree():
    assert abs(sum(R11)/len(R11) - sum(R16)/len(R16)) < 0.03
