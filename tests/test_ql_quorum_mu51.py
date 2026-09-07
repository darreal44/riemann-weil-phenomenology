# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# T₅ at 5.1 kills only χ₃. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_quorum_mu51 import GRID, MU, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-quorum-mu51.md")
JSON = os.path.join(ROOT, "report", "ql-quorum-mu51.json")
NOTE = os.path.join(ROOT, "notes", "ql-quorum-mu51.md")
SRC = os.path.join(ROOT, "code", "ql_quorum_mu51.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "ql_neumann_pk" in src
    assert MU == 5.1
    assert "chi17" in GRID
    assert step_is_taken() is False


def test_json():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["taken"]["chi3"] == []
    assert 24 in data["taken"]["chi7"]
    assert data["n_taken"] == 5
    assert data["weil_positive"] is False


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "LICENSE.md" in text
