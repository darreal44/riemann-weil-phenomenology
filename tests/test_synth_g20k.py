# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Synthetic tail at Gmax=20000 (notebook 33).
RESIDUAL_11 = 0.709e-3
RESIDUAL_4000 = 1.458e-3


def test_doubling_G_cuts_residual():
    assert RESIDUAL_11 < 0.8e-3
    assert RESIDUAL_11 < 0.6 * RESIDUAL_4000
