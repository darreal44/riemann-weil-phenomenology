# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Algebraic max of the #72 mass majorant is √2."""
import math

SQRT2 = math.sqrt(2.0)


def majorant(a, b, m1, m2):
    return 2.0 * math.sqrt(max(a, 0.0) * max(b, 0.0)) + 2.0 * math.sqrt(
        max(a, 0.0) * max(m2, 0.0)
    ) + m1


def test_equality_case():
    assert abs(majorant(0.5, 0.25, 0.0, 0.25) - SQRT2) < 1e-15


def test_interior_below():
    assert majorant(1.0 / 3, 1.0 / 3, 1.0 / 3, 0.0) < SQRT2
    assert majorant(0.0, 0.0, 1.0, 0.0) == 1.0


def test_grid_never_exceeds():
    g = [i / 20.0 for i in range(21)]
    for a in g:
        for b in g:
            for m2 in g:
                m1 = 1.0 - a - b - m2
                if m1 < -1e-12:
                    continue
                m1 = max(m1, 0.0)
                assert majorant(a, b, m1, m2) <= SQRT2 + 1e-12


def test_boundary_formula():
    # x^2 > 1/3, d=0, r=0: phi = 2√2 x √(1-x^2)
    x2 = 0.5
    x = math.sqrt(x2)
    phi = 2.0 * SQRT2 * x * math.sqrt(1.0 - x2)
    assert abs(phi - SQRT2) < 1e-15
