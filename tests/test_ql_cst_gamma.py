# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# CST+Gauss is not C_A_lo. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_cst_gamma import step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-cst-gamma.md")
JSON = os.path.join(ROOT, "report", "ql-cst-gamma.json")
NOTE = os.path.join(ROOT, "notes", "ql-cst-gamma.md")
SRC = os.path.join(ROOT, "code", "ql_cst_gamma.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "arch_00 ≠ C_A_lo" in text or "≠ C_A_lo" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "C_A_lo" in src
    assert "psi_s0" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_json_gap():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["identified"] is False
    by = {(r["name"], r["mu"]): r for r in data["rows"]}
    assert abs(by[("chi3", 3.0)]["gap_arch_CA"]) > 0.7
    assert abs(by[("chi5", 3.0)]["gap_arch_CA"]) > 1.0
    assert by[("chi3", 3.0)]["C_A_lo"] > by[("chi3", 3.0)]["gamma_inf"]


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not identified" in text.replace("\n", " ") or "classical Γ" in text
