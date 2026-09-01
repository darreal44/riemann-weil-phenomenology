# Plateau lock: 2πe sits inside the measured interval; 16 is outside the new rungs.
# Usage: python3 -m pytest tests/test_plateau_constants.py -q
import math

TWOPIE = 2 * math.pi * math.e

# deepest spacings shipped in notebook 22 / PR #10
CHI3 = [(16, 15.88), (22, 16.92), (30, 17.07), (38, 16.82)]
CHI4 = [(30, 17.65), (38, 18.16)]


def test_twopie_value():
    assert abs(TWOPIE - 17.079) < 0.002


def test_chi3_hovers_near_twopie():
    for mu, d in CHI3[1:]:
        assert 16.5 < d < 17.3, (mu, d)


def test_chi4_sits_above_twopie():
    for mu, d in CHI4:
        assert d > TWOPIE


def test_plateau_interval_contains_twopie_not_only_16():
    lo = min(d for _, d in CHI3[1:] + CHI4)
    hi = max(d for _, d in CHI3[1:] + CHI4)
    assert lo < TWOPIE < hi
    assert not (15.5 <= lo and hi <= 16.5)
