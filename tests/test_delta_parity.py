# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Parity does not split Delta_inf (notebook 29).
CHI5_MU30 = 17.27
CHI5_MU38 = 17.99
CHI3_CLUSTER = 16.94
CHI4_CLUSTER = 17.90


def test_chi5_climbs_toward_chi4_not_chi3():
    assert CHI5_MU38 > CHI5_MU30
    assert abs(CHI5_MU38 - CHI4_CLUSTER) < abs(CHI5_MU38 - CHI3_CLUSTER)
