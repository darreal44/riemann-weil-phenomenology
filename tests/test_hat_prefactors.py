# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Entry-dependent out-of-band hat prefactors (notebook 40).
import math
L = math.log(11.0)
G = 811.2
MEAS = {(0, 0): 2.15e-3, (0, 1): 3.04e-3, (1, 1): 4.30e-3}
PRED = {
    (0, 0): (4 / L) / G,
    (0, 1): (4 * math.sqrt(2) / L) / G,
    (1, 1): (8 / L) / G,
}


def test_single_ratio_everywhere():
    ratios = [MEAS[k] / PRED[k] for k in MEAS]
    assert all(1.03 < r < 1.06 for r in ratios)
    assert max(ratios) - min(ratios) < 0.002
