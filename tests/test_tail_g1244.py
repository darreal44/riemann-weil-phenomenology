# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# C=0.190 holds at G=1244 (notebook 45).
GAP_850 = 1.524e-4
G_850 = 1243.54
C = 0.190


def test_product_at_g1244():
    assert abs(GAP_850 * G_850 - C) / C < 0.03
