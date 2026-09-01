# chi-20 secant 62->74 (notebook 39).
SECANTS = (0.535, 0.547, 0.563, 0.591, 0.582, 0.622)


def test_0582_was_a_dip():
    assert SECANTS[-1] > SECANTS[-2]
    assert SECANTS[-1] > SECANTS[-3]


def test_steffensen_last_triple():
    a, b, c = SECANTS[-3], SECANTS[-2], SECANTS[-1]
    s = c - (c - b) ** 2 / (c - 2 * b + a)
    assert 0.58 < s < 0.60
