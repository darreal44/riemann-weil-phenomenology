# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Prolate Rayleigh stays O(0.1) as lambda_min dives (notebook 64).
ROWS = [(3, 9.4e-2, 1.0e-7), (5, 1.1e-1, 4.6e-15)]


def test_rayleigh_stays_order_one_tenth():
    for mu, ray, lam in ROWS:
        assert 1e-2 < ray < 1.0
        assert ray / lam > 1e5
