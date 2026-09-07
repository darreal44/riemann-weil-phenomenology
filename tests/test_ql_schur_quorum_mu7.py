# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Quorum Neumann μ=7. χ₃ not alone. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_schur_quorum_mu7 import GRID, HEADS, MU, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-schur-quorum-mu7.md")
JSON = os.path.join(ROOT, "report", "ql-schur-quorum-mu7.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-quorum-mu7.md")
SRC = os.path.join(ROOT, "code", "ql_schur_quorum_mu7.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "six" in text.lower() or "quorum" in text.lower()


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "ql_neumann_pk" in src
    assert "Copyright" in src
    assert MU == 7.0
    assert GRID[0] == "chi3"
    assert "chi17" in GRID
    assert HEADS[0] == 2
    assert step_is_taken() is False


def test_json_chi3_not_alone():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["chi3_taken"] is False
    assert data["n_taken"] == 4
    assert data["weil_positive"] is False
    assert data["taken"]["chi3"] == []
    assert data["taken"]["chi7"] == []
    assert 8 in data["taken"]["chi8"]
    assert 4 in data["taken"]["chi17"]
    assert 24 in data["taken"]["chi5"]
    assert 24 in data["taken"]["chi4"]
    by = {(r["name"], r["h"]): r for r in data["rows"]}
    assert by[("chi3", 16)]["ns"] == [2, 3, 4, 5]


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not the unique" in text or "not alone" in text
    assert "LICENSE.md" in text
