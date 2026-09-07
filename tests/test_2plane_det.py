# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# det(A-P)>0 on the raised-cosine 2-plane at mu=16, three hats. ~2 s.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from cert_2plane import cert


def test_chi5_2plane_spd():
    r = cert("chi5", 16.0, 40)
    assert r["det"] > 0
    assert r["eig_min"] > 0
    assert abs(float(r["eig_min"] / r["lmin_bound"]) - 1) < 0.01


def test_chi3_chi4_chi8_chi13_2plane_spd():
    for name in ("chi3", "chi4", "chi8", "chi13"):
        r = cert(name, 16.0, 36)
        assert r["det"] > 0, name
        assert r["eig_min"] > 0, name
