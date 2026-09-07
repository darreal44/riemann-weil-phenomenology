# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
import scan_q_maass as m

def test_load_and_satake():
    rec = m.load_form("maass1")
    assert rec["N"] == 1
    assert 9 < rec["R"] < 10
    assert rec["an"][1] == 1.0
    pts = m.lambda_pts(rec["an"], cap=6, Ncond=1)
    assert len(pts) >= 3
    # a2 < 0 => first weight negative
    assert pts[0][1] < 0

def test_alias_maass3():
    rec = m.load_form("maass3")
    assert rec["R"] > 40
