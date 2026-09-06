# Discrete Landau: well count = round(D_max), rungs sum to ell_0. Gram of nodes, no RH.
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from dmax import (  # noqa: E402
    D_max,
    D_max_kernel,
    count_above,
    gram_ells,
    load_zeros,
    rungs,
    well_depths,
)

PI2 = math.pi ** 2


def _synth_hole_comb(g1, dens, mu=16.0, NB=24, n=60):
    L = math.log(mu)
    nu = 2 * math.pi / L
    return [g1 + k * dens * nu for k in range(n)], mu, NB


def test_synthetic_well_count_is_round_Dmax():
    Z, mu, NB = _synth_hole_comb(4.0, 1.05)
    D = D_max(Z, mu, NB)
    K = D_max_kernel(Z, mu, NB)
    ells = gram_ells(Z, mu, NB)
    n2 = count_above(ells, 2.0)
    assert D > 1.5
    assert K >= round(D)
    assert n2 == round(D), (D, K, n2, ells[:8])


def test_chi8_chi29_well_count_matches_round_or_ceil_Dmax():
    """round(D) on χ₈ (D=1.77→2); ceil(D) on χ₂₉ (D=1.08→2). Off-by-one is the plunge."""
    Z8 = load_zeros("zeros_chi8_weyl.pkl")
    D8 = D_max(Z8, 16.0, 30)
    n8 = count_above(gram_ells(Z8, 16.0, 30), 2.0)
    assert n8 == round(D8) == 2, (D8, n8)
    Z29 = load_zeros("zeros_chi29_weyl.pkl")
    D29 = D_max(Z29, 38.0, 30)
    n29 = count_above(gram_ells(Z29, 38.0, 30), 2.0)
    assert n29 == math.ceil(D29) == 2, (D29, n29)
    assert abs(n29 - round(D29)) <= 1


def test_rungs_sum_to_ell0_and_mean_is_ell0_over_m():
    Z = load_zeros("zeros_chi5_weyl.pkl")
    ells = gram_ells(Z, 16.0, 46)
    w = well_depths(ells)
    rg = rungs(ells)
    assert len(w) >= 2
    assert abs(sum(rg) - w[0]) < 1e-9
    assert abs(sum(rg) / len(rg) - w[0] / len(w)) < 1e-9
    # short well: both ends near the mean, not the 16→5 of a long well
    assert 8.0 < rg[0] < 18.0
    assert 5.0 < rg[-1] < 16.0


def test_linear_rungs_identity_first_plus_last_is_twice_mean():
    """If δ_k were linear from A to B, mean = (A+B)/2. With mean ~11, A+B~22 (16+5)."""
    Z = load_zeros("zeros_chi5_weyl.pkl")
    ells = gram_ells(Z, 16.0, 46)
    D = D_max(Z, 16.0, 46)
    w = well_depths(ells)
    mean = w[0] / len(w)
    assert abs(mean - w[0] / D) < 0.5  # m = round(D) ≈ D
    assert 9.0 < mean < 13.0
    assert abs(mean - PI2) > 0.2
    assert abs(mean - PI2) < 3.0
