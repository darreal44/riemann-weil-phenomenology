# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Drive shipped H_2plane_independent.H2: det(A-P)>0 on the five μ=16 characters.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from H_2plane_independent import H2  # noqa: E402


def test_det_AP_positive_five_characters_mu16():
    for name in ("chi5", "chi3", "chi4", "chi8", "chi13"):
        H, det, ev, parts = H2(name, 16, 28)
        assert float(det) > 0, (name, det)
        assert float(min(ev)) > 0, (name, ev)
        A11, P11 = parts[(0, 0)]
        # Arch and primes are the same order: dropping P would not be a rounding error
        assert abs(float(P11)) > 0.1 * abs(float(A11)), (name, A11, P11)
