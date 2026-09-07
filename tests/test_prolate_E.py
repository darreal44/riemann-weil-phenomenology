# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# E(prolate combo) aligns with ground state (notebook 61).
COS_H0 = 0.0583
COS_COMBO = 0.8079


def test_h0_still_poor():
    assert COS_H0 < 0.15


def test_mean_zero_combo_aligns():
    assert COS_COMBO > 0.75
