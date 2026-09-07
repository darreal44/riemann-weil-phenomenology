# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# E(gaussian) is not the ground state (notebook 60).
COS_K_V = 0.00107


def test_naive_arithmetic_image_misses_ground_state():
    assert COS_K_V < 0.05
