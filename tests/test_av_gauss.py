# 3-point Gauss of A(v) on [0,1]: closed θ_v, regular limit at 0, remainder from code.
import math
import os
import sys

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_gauss import (  # noqa: E402
    GAUSS_NODES,
    GAUSS_WEIGHTS,
    L16,
    V,
    a_integrand,
    gauss3_unit,
    kernel,
    kernel_limit_0,
    remainder_bound,
    th,
    theta_v,
    theta_v_prime_0,
)
from H_2plane_independent import theta_vec  # noqa: E402


def test_closed_theta_v_matches_theta_vec():
    L = mp.log(16)
    v = [mp.mpf(x) for x in V]
    for yf in (0.0, 0.113, 0.25, 0.5, 0.75, 1.0, math.log(2), math.log(3), float(L)):
        closed = theta_v(yf, L16, V)
        vec = float(theta_vec(v, v, mp.mpf(yf), L))
        if abs(vec) < 1e-12:
            assert abs(closed) < 1e-10, (yf, closed, vec)
        else:
            assert abs(closed / vec - 1) < 1e-9, (yf, closed, vec)


def test_th_table_matches_h2plane():
    import H_2plane_independent as h2

    L = mp.log(16)
    y = mp.mpf("0.7")
    for n in range(3):
        for m in range(3):
            a = th(n, m, 0.7, L16)
            b = float(h2.th(n, m, y, L))
            assert abs(a - b) < 1e-12, (n, m, a, b)


def test_kernel_limit_is_minus_three_minus_theta_prime():
    c = kernel_limit_0()
    expect = -3.0 - theta_v_prime_0()
    assert abs(c - expect) < 1e-15
    assert abs(c + 2.962) < 0.002
    k_small = kernel(1e-8)
    assert abs(k_small - c) < 1e-5
    assert math.isfinite(a_integrand(0.0))


def test_gauss_nodes_and_weights_are_origins():
    s = math.sqrt(3.0 / 5.0)
    assert abs(GAUSS_NODES[0] - (0.5 - 0.5 * s)) < 1e-15
    assert abs(GAUSS_NODES[1] - 0.5) < 1e-15
    assert abs(GAUSS_NODES[2] - (0.5 + 0.5 * s)) < 1e-15
    assert abs(sum(GAUSS_WEIGHTS) - 1.0) < 1e-15
    assert GAUSS_NODES[0] > 0.11


def test_gauss3_vs_mpmath_integral_of_same_a():
    gval = gauss3_unit(a_integrand)
    true = float(mp.quad(lambda y: a_integrand(float(y)), [0, 1]))
    rem, d6 = remainder_bound(a_integrand)
    assert rem >= 0 and d6 > 0
    assert abs(gval - true) < max(5e-5, rem)
    # origin's I_{[0,1]} ≈ -0.70065 is this integral, not a hardcoded oracle
    assert abs(true + 0.70065) < 0.002
    assert abs(gval + 0.70065) < 0.002
