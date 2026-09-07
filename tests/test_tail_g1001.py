# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# 0.190/G holds at G=1001 (notebook 44).
GAP_650 = 1.925e-4
G_650 = 1001.35
C = 0.190


def test_product_still_C():
    assert abs(GAP_650 * G_650 - C) / C < 0.03
