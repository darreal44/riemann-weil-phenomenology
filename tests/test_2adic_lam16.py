# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Lambda=16 2-adic peak shape (notebook 97)
W = {16: -0.397, 32: -0.289, 48: -0.137, 64: 0.007, 80: 0.140}
PEAK_SIGNFLIP_CPU = 48


def test_mass_rises_with_cpu():
    assert W[16] < W[32] < W[48] < W[64] < W[80]


def test_peak_becomes_positive():
    assert W[64] > 0 and W[80] > W[64]
