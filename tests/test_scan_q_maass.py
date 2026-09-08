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
    assert rec["slug"] == "1.0.1.3.1"
    assert 13.5 < rec["R"] < 14.0


def test_alias_is_table1_not_lexicographic():
    assert m.ALIAS["maass2"] == "1.0.1.2.1"
    assert m.ALIAS["maass3"] == "1.0.1.3.1"
    two = m.load_form("maass2")
    assert abs(two["R"] - 12.173) < 0.01
    # 1.0.1.10.1 is a real form and must not be maass2
    ten = m.load_form("1.0.1.10.1")
    assert ten["R"] > 19.0


def test_load_form_11_from_pkl():
    rec = m.load_form("11.0.1.1.1")
    assert rec["N"] == 11
    assert abs(rec["R"] - 2.03309) < 1e-4
    assert rec["an"][1] == 1.0
    assert len(rec["an"]) >= 100


def test_scan_s_sends_maass_to_q():
    import scan_s
    import pytest

    with pytest.raises(SystemExit) as e:
        scan_s.assemble("11.0.1.1.1", 6, 12, 25)
    msg = str(e.value)
    assert "scan_q_maass" in msg
    assert "11.0.1.1.1" in msg
    assert "harvest_gl2" not in msg
