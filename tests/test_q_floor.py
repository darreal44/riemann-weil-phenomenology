# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
C_LOG3 = 5.65e-8
LAM43 = 5.73e-8

def test_mu3_floor_nearby():
    assert abs(LAM43 / C_LOG3 - 1) < 0.05
