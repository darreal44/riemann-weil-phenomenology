# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# 1-1 matching at N=21 (notebook 31).
MEAN = 0.598
MIN = 0.137
CORE_MIN = 0.61  # first six


def test_full_k8_min_is_noise():
    assert MIN < 0.20


def test_core_still_aligned():
    assert CORE_MIN > 0.60
    assert MEAN > 0.50
