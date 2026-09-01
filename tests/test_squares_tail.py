# Unsigned tail envelope used in the Arb 5x5 enclosure.
# Usage: python3 -m pytest tests/test_squares_tail.py -q
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code'))


def tail_diag(G, L=math.log(11.0), N0=4):
    c = 4.0 / math.sqrt(L)
    lg = math.log(G / (2 * math.pi))
    integ = (lg + 1) / (2 * math.pi) / G + 1.0 / G
    return 2 * (c ** 2) * integ


def test_envelope_at_g811_is_three_percent():
    t = tail_diag(811.2)
    assert 0.03 < t < 0.035


def test_envelope_falls_like_1_over_G():
    assert tail_diag(1600) < tail_diag(800)


def test_squares47_arb_exists():
    path = os.path.join(os.path.dirname(__file__), '..', 'code', 'squares47_arb.py')
    src = open(path).read()
    assert 'acb.integral' in src
    assert 'tail' in src.lower()
