# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# C = Lambda(mu)/(4 sqrt(mu)) (notebook 46).
import math
ROWS = [
    (11, 0.1899, math.log(11) / math.sqrt(11) / 4),
    (13, 0.1770, math.log(13) / math.sqrt(13) / 4),
    (16, 0.0422, math.log(2) / 4 / 4),
    (9, 0.1036, math.log(3) / (4 * 3)),
]


def test_endpoint_weight_names_C():
    for mu, C, pred in ROWS:
        tol = 0.15 if mu == 9 else 0.08
        assert abs(C / pred - 1) < tol, (mu, C, pred)
