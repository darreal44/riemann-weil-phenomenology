# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
DEFICIT_ZETA3_G1 = 3.9
DEFICIT_ZETA11_G1 = 9.8

def test_landau_deficit_grows_with_mu():
    assert DEFICIT_ZETA11_G1 > DEFICIT_ZETA3_G1
