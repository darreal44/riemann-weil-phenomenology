# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# w₂=0 Hankel-only: λ_H of χ₃/χ₅ goes negative. Not a take. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "ql-schur-hankel-only.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-hankel-only.md")
SRC = os.path.join(ROOT, "code", "ql_schur_hankel_only.py")


def test_not_a_take():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "KILL"
    assert data["step_taken"] is False
    assert data["chi3_hank_s_lo_pos"] is False


def test_stripping_theta_kills_the_head():
    data = json.load(open(JSON, encoding="utf-8"))
    by = {r["name"]: r for r in data["rows"]}
    assert by["chi3"]["full_s_lo"] < 0.0
    assert by["chi3"]["hank_lamH"] < -0.15
    assert by["chi5"]["full_s_lo"] > 0.02
    assert by["chi5"]["hank_lamH"] < -0.15
    assert abs(by["chi8"]["full_s_lo"] - by["chi8"]["hank_s_lo"]) < 1e-6
    assert abs(by["chi4"]["full_s_lo"] - by["chi4"]["hank_s_lo"]) < 1e-6


def test_driver_and_note():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert "w2=0" in src or "0.0" in src
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "not a take" in text.lower() or "Not taken" in text
    assert "Hankel" in text
    assert "-0.21" in text or "−0.21" in text or "-0.2037" in text
