# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# H11 from Laplace-quad + elementary theta matches cert_2plane. ~3 s.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from H11_independent import H11


def test_H11_matches_2plane_projection():
    ref = dict(chi5=9.31467e-5, chi3=2.17859e-4, chi4=1.17863e-3, chi8=1.7067e-3, chi13=0.211858)
    for name, r in ref.items():
        _, _, H = H11(name, 16, 30)
        assert abs(float(H) / r - 1) < 1e-4, (name, float(H), r)
        assert float(H) > 0
