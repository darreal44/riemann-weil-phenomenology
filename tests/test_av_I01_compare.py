# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# I_{[0,1]} 3-piece misses 0.22. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_compare import step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-I01-compare.md")
JSON = os.path.join(ROOT, "report", "av-I01-compare.json")
NOTE = os.path.join(ROOT, "notes", "av-I01-compare.md")
SRC = os.path.join(ROOT, "code", "av_I01_compare.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "3-piece" in text or "tangent" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "g_p" in src and "g_pp" in src
    assert "gauss_table" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_json_does_not_close():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["closes_window"] is False
    assert abs(data["gauss3"] + 0.70066) < 1e-4
    assert data["gap_3piece"] > 0.15
    assert data["gap_chord"] > 0.15
    assert data["Q_lo_3piece"] < 0
    assert 0.3 < data["ymin"] < 0.5
    assert 0.7 < data["yinf"] < 0.85
    assert data["gmin"] < data["g1"] < 0
    assert len(data["table"]) == 3
    s = sum(r["contrib"] for r in data["table"])
    assert abs(s - data["gauss3"]) < 1e-12


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "still open" in text
    assert "LICENSE.md" in text
