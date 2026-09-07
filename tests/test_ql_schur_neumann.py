# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Schur Neumann T^{-1}≤D^{-1}/(1−ρ). Sharper C. Not RH.
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_schur_neumann import block_norm, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-schur-neumann.md")
JSON = os.path.join(ROOT, "report", "ql-schur-neumann.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-neumann.md")
SRC = os.path.join(ROOT, "code", "ql_schur_neumann.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Galerkin" in text
    assert "Not RH" in text
    assert "S_lo(χ₅)>0" in text or "chi5" in text.lower()


def test_block_norm_and_driver():
    assert abs(block_norm(1.0, 0.0, 1.0) - 1.0) < 1e-15
    assert block_norm(0.234, 0.144, 0.449) < 0.53
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert "block_norm" in src
    assert "N_NEAR = 32" in src


def test_json_chi5_taken_chi3_not():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False
    assert step_is_taken() is False
    assert data["chi5_taken"] is True
    assert data["chi3_taken"] is False
    by = {r["name"]: r for r in data["rows"]}
    assert by["chi5"]["rho"] < 1.0
    assert by["chi5"]["s_lo"] > 0.02
    assert by["chi5"]["s_diag"] > 0.04
    assert by["chi3"]["s_lo"] < 0
    assert by["chi8"]["s_lo_pos"] is True
    assert by["chi4"]["s_lo_pos"] is True


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not taken" in text
    assert "(∀ L) Q_L ≥ 0" in text or "(∀ L)" in text
    assert "χ₅" in text or "chi5" in text.lower()
