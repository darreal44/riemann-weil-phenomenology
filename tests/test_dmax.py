# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Linear algebra of D_max: no eigsy. Light.
import math
import os
import sys

CODE = os.path.join(os.path.dirname(__file__), "..", "code")
sys.path.insert(0, CODE)
from dmax import D_max, D_max_kernel, load_zeros, n_hats, kernel_lower  # noqa: E402

PI2 = math.pi**2


def test_n_hats_at_band_edge():
    L = math.log(16.0)
    NB = 10
    omax = 2 * math.pi * NB / L
    assert n_hats(omax, L, NB) == NB  # n = 0..NB-1 strictly below; n=NB sits on the edge
    assert n_hats(omax + 1e-9, L, NB) == NB + 1


def test_kernel_lower_matches_continuous_Dmax():
    cases = (
        ("zeros500.pkl", 11.0, 40),
        ("zeros_chi5_weyl.pkl", 16.0, 46),
        ("zeros_chi3_weyl.pkl", 16.0, 46),
        ("zeros_chi29_weyl.pkl", 38.0, 66),
    )
    for zf, mu, NB in cases:
        Z = load_zeros(zf)
        D = D_max(Z, mu, NB)
        K = D_max_kernel(Z, mu, NB)
        # n(ω) counts the constant hat; continuous D_max does not. O(1).
        assert K >= math.floor(D), (zf, D, K)
        assert K <= math.ceil(D) + 2, (zf, D, K)


def test_desert_then_nyquist_comb_has_positive_D():
    """Arbitrary nodes: a hole then a comb still produces D_max from the hole."""
    mu, NB = 16.0, 20
    L = math.log(mu)
    nu = 2 * math.pi / L
    gamma1 = 6.0
    Z = [gamma1 + k * 1.2 * nu for k in range(40)]
    D = D_max(Z, mu, NB)
    K = D_max_kernel(Z, mu, NB)
    assert D > 2.0, D
    assert K >= 2
    desert = gamma1 * L / (2 * math.pi) - 1
    assert D >= desert - 0.05, (D, desert)


def test_kernel_nonnegative_everywhere():
    Z = load_zeros("zeros_chi5_weyl.pkl")
    mu, NB = 16.0, 30
    L = math.log(mu)
    omax = 2 * math.pi * NB / L
    for g in list(Z[:20]) + [omax]:
        assert kernel_lower(Z, mu, NB, g) >= 0
