# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Newton/Steffensen on chi-20 secants (notebook 38).
def steffensen(a, b, c):
    return c - (c - b) ** 2 / (c - 2 * b + a)

def test_last_triple_steffensen():
    assert abs(steffensen(0.563, 0.591, 0.582) - 0.584) < 0.002

def test_rising_triple_does_not_land_in_band():
    s = steffensen(0.535, 0.547, 0.563)
    assert s < 0.57
