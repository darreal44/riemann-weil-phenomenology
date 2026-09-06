# Rational witness χ₅ μ=16: Arb enclosure of Q(v)>0. Origin left A(v) on [0,1].
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from H_2plane_independent import theta_vec  # noqa: E402
import mpmath as mp  # noqa: E402

flint = pytest.importorskip("flint")
from av_witness import certify, v_rat  # noqa: E402
from H2_arb import theta_vec as theta_vec_arb, _arb  # noqa: E402


def test_theta_v_matches_three_hat_table():
    mp.mp.dps = 30
    L = mp.log(16)
    s26 = mp.sqrt(26)
    v = [4 / s26, -3 / s26, 1 / s26]
    arb, acb, ctx = _arb()
    ctx.dps = 40
    va = v_rat(arb)
    La = arb(16).log()
    for yf in (0.2, 0.5, 1.0, 1.59, math.log(2), math.log(3)):
        tf = float(theta_vec(v, v, mp.mpf(yf), L))
        ta = theta_vec_arb(va, va, arb(yf), La, arb)
        assert abs(float(ta.mid()) / tf - 1) < 1e-10, (yf, tf, ta)


def test_Q_witness_ball_excludes_zero():
    r = certify(50)
    Q = r["Q"]
    mid, rad = float(Q.mid()), float(Q.rad())
    assert mid > 0, Q
    assert rad < mid, (mid, rad, Q)
    # room quoted in rational-witness-chi5-mu16.md
    assert 0.002 < mid < 0.01, mid


def test_A_split_matches_full_arch_and_sits_in_the_window():
    r = certify(50)
    A, As = r["A"], r["A_split"]
    assert abs(float((A - As).mid())) < 1e-8
    amid = float(A.mid())
    arad = float(A.rad())
    # window that keeps Q>0 after P_rest ±0.003
    lo, hi = -0.8303, -0.8244
    assert amid - arad > lo
    assert amid + arad < hi


def test_CST_is_the_elementary_constant():
    r = certify(40)
    # log(5/π) − γ − log(1 − 1/256)
    expect = math.log(5 / math.pi) - 0.5772156649015328606 - math.log(1 - 1 / 256)
    assert abs(float(r["CST"].mid()) - expect) < 1e-12


def test_almost_all_of_A_int_is_on_unit_interval():
    r = certify(50)
    h01 = float((r["I01"] / 2).mid())
    h1L = float((r["I1L"] / 2).mid())
    assert h01 < -0.69 and h01 > -0.72
    assert h1L < -0.01 and h1L > -0.03
    assert abs(h01) > 20 * abs(h1L)
