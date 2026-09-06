# Exact split hat ψ = jump + r. Finite trig polynomials, no RH.
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from edge_expansion import hat_psi, jump_term, remainder_r, psi0  # noqa: E402


def test_split_holds_for_random_coefficient_vectors():
    rng = np.random.default_rng(0)
    L = math.log(16.0)
    om_max = 2 * math.pi * 8 / L
    for _ in range(8):
        v = rng.normal(size=9)
        v = v / np.linalg.norm(v)
        for g in (om_max * 1.3, om_max * 2.0, om_max * 5.0, 40.0):
            lhs = hat_psi(v, g, L)
            rhs = jump_term(v, g, L) + remainder_r(v, g, L)
            assert abs(lhs - rhs) < 1e-10 * (1 + abs(lhs)), (g, lhs, rhs)


def test_constant_mode_has_vanishing_remainder():
    L = math.log(11.0)
    v = np.array([1.0] + [0.0] * 6)
    g = 20.0
    assert abs(remainder_r(v, g, L)) < 1e-15
    assert abs(hat_psi(v, g, L) - jump_term(v, g, L)) < 1e-12
    assert abs(psi0(v, L) - L ** -0.5) < 1e-15


def test_ker_psi0_cancels_the_jump():
    # e₁ = (√2, −1, 0)/√3 has ψ(0)=0, so hat = r.
    s3 = math.sqrt(3.0)
    v = np.array([math.sqrt(2.0) / s3, -1.0 / s3, 0.0])
    L = math.log(16.0)
    assert abs(psi0(v, L)) < 1e-12
    g = 15.0
    assert abs(jump_term(v, g, L)) < 1e-12
    assert abs(hat_psi(v, g, L) - remainder_r(v, g, L)) < 1e-10
