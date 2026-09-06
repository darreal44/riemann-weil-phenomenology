# Drive shipped li_lambda.py. A finite positive prefix is not RH.
import math
import os
import pickle
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from li_lambda import lambda1_closed, lam_from_zeros, lam_tail  # noqa: E402

CODE = os.path.join(os.path.dirname(__file__), "..", "code")


def test_lambda1_closed_is_the_lagarias_formula():
    g = 0.5772156649015328606
    expect = 1.0 + 0.5 * g - 0.5 * math.log(4 * math.pi)
    assert abs(lambda1_closed() - expect) < 1e-14
    assert lambda1_closed() > 0


def test_lam_from_zeros_positive_and_undershoots_closed_lambda1():
    zs = [float(x) for x in pickle.load(open(os.path.join(CODE, "zeros_zeta_weyl.pkl"), "rb"))]
    zs = [t for t in zs if t > 1e-12]
    assert len(zs) >= 100
    a1 = lam_from_zeros(1, zs)
    assert a1 > 0
    assert a1 < lambda1_closed()  # missing Weyl tail
    for n in range(1, 9):
        assert lam_from_zeros(n, zs) > 0


def test_weyl_tail_is_positive_and_closes_lambda1_directionally():
    zs = [float(x) for x in pickle.load(open(os.path.join(CODE, "zeros_zeta_weyl.pkl"), "rb"))]
    zs = sorted(t for t in zs if t > 1e-12)
    T = zs[-1]
    a1 = lam_from_zeros(1, zs)
    b1 = lam_tail(1, T)
    assert b1 > 0
    # raw zeros+tail overshoots the closed form; a scaled tail is a fit, not a theorem
    assert a1 + b1 > lambda1_closed()
