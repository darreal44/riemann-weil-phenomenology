# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# C(G) convergence (notebook 47).
C11 = (0.1873, 0.1869, 0.1910, 0.1899)
PRED11 = 0.1807
C13_500 = 0.1770
PRED13 = 0.1778


def test_mu11_already_flat():
    assert max(C11) - min(C11) < 0.006
    assert all(c > PRED11 for c in C11)


def test_mu13_reaches_prediction():
    assert abs(C13_500 / PRED13 - 1) < 0.02
