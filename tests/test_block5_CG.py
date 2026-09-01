# 5x5 after scaled C/G (notebook 50).
REMS = {('00', 500): -2.56e-6, ('01', 500): -3.61e-6, ('11', 500): -5.10e-6}
G = 811.18


def test_all_three_micro():
    assert all(abs(v) < 1e-5 for v in REMS.values())


def test_scale_sqrt2_and_2():
    # C0n/C00 = sqrt2, Cnm/C00 = 2 is the prediction; remainders share sign and 1e-6 size
    r00, r01, r11 = REMS[('00', 500)], REMS[('01', 500)], REMS[('11', 500)]
    assert r00 < 0 and r01 < 0 and r11 < 0
    assert abs(r01 / r00 - 1.41) < 0.3
