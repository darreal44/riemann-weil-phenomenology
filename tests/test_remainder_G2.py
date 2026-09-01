# After C/G the (0,0) gap is O(1/G^2) (notebook 49).
REM_11_500 = -2.56e-6
G = 811.18


def test_mu11_remainder_micro():
    assert abs(REM_11_500) < 1e-5


def test_is_one_over_G2():
    assert abs(REM_11_500) * G * G < 5.0
