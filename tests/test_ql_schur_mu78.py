# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Neumann Q_pk χ₃ μ=7,8. Take does not extend. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_schur_mu78 import HEADS, MUS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-neumann-mu78.md")
JSON = os.path.join(ROOT, "report", "ql-schur-mu78.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-mu78.md")
SRC = os.path.join(ROOT, "code", "ql_schur_mu78.py")
OLD = os.path.join(ROOT, "report", "ql-H16-mu.json")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "does not extend" in text.replace("\n", " ")
    assert "Copyright" in text
    assert "LICENSE.md" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "Q_pk" in src
    assert "theta_op_cap" in src
    assert "block_norm" in src
    assert "Copyright" in src
    assert "LICENSE.md" in src
    assert "from scan_s import assemble" not in src
    assert HEADS == (2, 4, 8, 16, 20, 24)
    assert MUS == (7.0, 8.0)
    assert step_is_taken() is False


def test_json_take_does_not_extend():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["take_extends"] is False
    assert data["any_slo_pos"] is False
    assert data["weil_positive"] is False
    assert data["weil_negative"] is False
    by = {(r["mu"], r["h"]): r for r in data["rows"]}
    assert by[(7.0, 16)]["ns"] == [2, 3, 4, 5]
    assert by[(8.0, 16)]["ns"] == [2, 3, 4, 5, 7]
    assert by[(7.0, 16)]["log2_in_band"] is True
    assert by[(8.0, 16)]["log2_in_band"] is True
    assert by[(7.0, 24)]["s_lo"] is not None
    assert by[(7.0, 24)]["s_lo"] < 0
    assert by[(8.0, 24)]["rho"] >= 1.0
    old = json.load(open(OLD, encoding="utf-8"))
    old_by = {r["mu"]: r for r in old["rows"]}
    assert abs(by[(7.0, 16)]["lamH"] - old_by[7.0]["lamH"]) < 1e-12
    assert abs(by[(8.0, 16)]["lamH"] - old_by[8.0]["lamH"]) < 1e-12
    for r in data["rows"]:
        assert r["s_lo_pos"] is False


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "does not extend" in text
    assert "LICENSE.md" in text
    assert "Copyright" in text
