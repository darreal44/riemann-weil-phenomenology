# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Double-limit Hankel cutoff: eσ depends on M/N, not N. Not Hartman. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_hankel_weyl_N import HALF_PI  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "ql-hankel-weyl-N.json")
NOTE = os.path.join(ROOT, "notes", "ql-hankel-weyl-N.md")
SRC = os.path.join(ROOT, "code", "ql_hankel_weyl_N.py")
REM = os.path.join(ROOT, "notes", "remaining-before-rh.md")


def _data():
    return json.load(open(JSON, encoding="utf-8"))


def test_not_a_take():
    data = _data()
    assert data["verdict"] == "KILL"
    assert data["step_taken"] is False
    assert data["b_toward_zero"] is False
    assert data["b_min"] > 0.4


def test_matched_ratio_independent_of_N():
    data = _data()
    s4 = data["ratio_slices"]["4"]
    s8 = data["ratio_slices"]["8"]
    assert s4["spread"] < 0.01
    assert s8["spread"] < 0.01
    assert abs(data["spread_ratio4"] - s4["spread"]) < 1e-15
    # raising N does not drop eσ at fixed ratio
    assert min(s4["e_sigma"]) > 1.22
    assert max(s4["e_sigma"]) < 1.24


def test_b_does_not_go_to_zero():
    data = _data()
    assert data["b16"] > 0.5
    assert data["b128"] > data["b16"]
    assert data["b32"] > 0.5


def test_driver_and_note():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert ".csv" not in src
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "Not a take" in text or "Not taken" in text
    assert "Hartman" in text
    assert "0.005" in text or "independent" in text.lower()
    rem = open(REM, encoding="utf-8").read()
    assert "## 8j." in rem
    assert "ql_hankel_weyl_N" in rem
