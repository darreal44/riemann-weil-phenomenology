# Ground state of Q at mu=11 N=9 (notebook 56).
V0 = (0.5982, -0.6941, 0.3780)


def test_alternating_low_modes():
    assert V0[0] > 0 and V0[1] < 0 and V0[2] > 0


def test_mass_on_first_three():
    assert sum(x * x for x in V0) > 0.95
