# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# 0.44% bias falls as 0.190/G (notebook 43).
GAPS = {143: 1.309e-3, 237: 0.790e-3, 396: 0.482e-3, 811: 0.234e-3}
C = 0.190


def test_one_over_G():
    for G, gap in GAPS.items():
        assert abs(gap - C / G) / gap < 0.03
