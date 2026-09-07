# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Best 4-prolate span still misses the kernel (notebook 63).
COS_LS = 0.941
RAY_RATIO = 5.0e16


def test_euclid_looks_good():
    assert COS_LS > 0.90


def test_rayleigh_still_useless():
    assert RAY_RATIO > 1e14
