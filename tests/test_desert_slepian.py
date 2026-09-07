# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
RATIO_MU3 = 2.56
RATIO_CHI5_30 = 5.11

def test_desert_slepian_factor_grows():
    assert 2 < RATIO_MU3 < 3
    assert RATIO_CHI5_30 > RATIO_MU3
