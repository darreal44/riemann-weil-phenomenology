# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# S_T = H−C T_near^{-1} C*; χ₃ dies in the far envelope. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "ql-schur-Tnear.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-Tnear.md")
SRC = os.path.join(ROOT, "code", "ql_schur_Tnear.py")


def test_not_a_take():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "KILL"
    assert data["step_taken"] is False
    assert data["chi3_s_T_pos"] is True
    assert data["chi3_s_lo_pos"] is False


def test_chi3_dies_in_far_envelope_only():
    data = json.load(open(JSON, encoding="utf-8"))
    by = {r["name"]: r for r in data["rows"]}
    c3 = by["chi3"]
    assert c3["lamH"] > 0.018
    assert c3["s_diag"] > 0.007
    assert c3["s_T"] > c3["s_diag"]
    assert c3["s_T"] > 0.009
    assert c3["s_lo"] < 0.0
    assert c3["tmin"] > 1.0
    assert c3["rho"] < 1.0
    assert by["chi5"]["s_T"] > 0.04
    assert by["chi5"]["s_lo"] > 0.02


def test_driver_is_local():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert "T_near" in src or "solve(T" in src


def test_note_does_not_claim_rh_or_infinite_S():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not\nRH." in text or "Not RH" in text
    assert "infinite" in text.lower() or "tail" in text.lower()
    assert "Not\ntaken" in text or "not a take" in text.lower()
    assert "+0.0097" in text or "0.0097" in text
    assert "far" in text.lower()
