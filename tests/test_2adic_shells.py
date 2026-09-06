# Exact 2-adic shell masses and the semi-local sub-shell sum. No Fmat grid, no RH.
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from tau2_local import (  # noqa: E402
    SQRT2,
    bombieri,
    lebesgue_jacobian_at_two,
    mass_at_two,
    raw_weight,
    twisted_inverse,
    twisted_module,
)
from subshells import F_from_shells, shell_term  # noqa: E402
from semilocal import Fab, F_cell  # noqa: E402


def test_raw_weights_on_the_two_dirac_shells():
    assert raw_weight(-1) == 0.5
    assert raw_weight(1) == 1.0
    assert raw_weight(0) == 0.0
    assert abs(twisted_module(-1) - 1.0 / SQRT2) < 1e-15
    assert abs(twisted_module(1) - 1.0 / SQRT2) < 1e-15


def test_mass_at_two_is_one_over_sqrt2_or_sqrt2():
    assert abs(mass_at_two("module") - 1.0 / SQRT2) < 1e-15
    assert abs(mass_at_two("inverse") - SQRT2) < 1e-15
    assert abs(lebesgue_jacobian_at_two() - SQRT2) < 1e-15
    assert abs(bombieri() - math.log(2) / SQRT2) < 1e-15
    # inverse twist at n=+1 is the √2 the Fmat grid heads toward
    assert abs(twisted_inverse(1) - SQRT2) < 1e-15


def test_subshells_sum_to_closed_form():
    xs = np.array([0.31, 0.77, 1.4, 2.9])

    def hat(xi):
        return np.exp(-((np.asarray(xi, float) - 1.0) ** 2))

    full = F_from_shells(hat, xs, nmax=12)
    acc = shell_term(hat, xs, -1)
    for n in range(12):
        acc = acc + shell_term(hat, xs, n)
    assert np.allclose(acc, full, rtol=1e-12, atol=1e-14)


def test_subshells_match_semilocal_F_cell():
    xs = np.array([0.4, 0.8, 1.2])
    a, b = 0.1, 0.3
    closed = F_from_shells(lambda xi: Fab(a, b, xi), xs, nmax=20)
    cell = F_cell(a, b, xs, semilocal=True, NN=20)
    assert np.allclose(closed, cell, rtol=1e-12, atol=1e-14)
