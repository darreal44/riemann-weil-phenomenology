# Discrete Landau count with threshold vs the unmatched O(log c) plunge.
import math
import os
import pickle
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from dmax import D_max, gram_ells, count_above  # noqa: E402

CODE = os.path.join(os.path.dirname(__file__), "..", "code")


def _zeros(name):
    for f in (f"zeros_{name}_weyl.pkl", "zeros500.pkl" if name == "zeta" else None):
        if f and os.path.exists(os.path.join(CODE, f)):
            return [float(str(x)) for x in pickle.load(open(os.path.join(CODE, f), "rb"))]
    raise FileNotFoundError(name)


def test_chi13_mu16_count_needs_threshold():
    """float64 Gram: χ₁₃ μ=16 is shallow enough that the plunge is visible.

    ζ μ=11 has D_max≈10 and ℓ₀≈107; numpy cannot resolve that well
    (test_depth_law does it in mpmath).
    """
    Z = _zeros("chi13")
    mu, NB = 16.0, 30
    D = D_max(Z, mu, NB)
    ells = gram_ells(Z, mu, NB)
    n2 = count_above(ells, 2.0)
    n05 = count_above(ells, 0.5)
    assert abs(n2 - round(D)) <= 1, (D, n2, ells[:12])
    assert n05 != n2, (n05, n2, D)


def test_mean_rung_is_pi2_plus_unfixed_remainder():
    Z = _zeros("chi8")
    D = D_max(Z, 16.0, 30)
    ells = gram_ells(Z, 16.0, 30)
    rung = float(ells[0] / D)
    rem = rung - math.pi ** 2
    assert 9.0 < rung < 13.0, (rung, D, ells[0])
    assert abs(rem) > 0.2, rem  # not exactly π²
    assert abs(rem) < 3.0, rem  # log(1/A)/D is O(1), A not derived
