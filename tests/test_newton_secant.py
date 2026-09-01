# Newton/Steffensen on chi-20 secants (notebook 38).
def steffensen(a, b, c):
    return c - (c - b) ** 2 / (c - 2 * b + a)

def test_last_triple_steffensen():
    assert abs(steffensen(0.563, 0.591, 0.582) - 0.584) < 0.002

def test_rising_triple_does_not_land_in_band():
    s = steffensen(0.535, 0.547, 0.563)
    assert s < 0.57
