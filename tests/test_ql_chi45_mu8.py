# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₄ χ₅ slivers die at μ=8. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_chi45_mu8 import HEADS, MU, NAMES, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-chi45-mu8.md")
JSON = os.path.join(ROOT, "report", "ql-chi45-mu8.json")
NOTE = os.path.join(ROOT, "notes", "ql-chi45-mu8.md")
SRC = os.path.join(ROOT, "code", "ql_chi45_mu8.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "8" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "ql_neumann_pk" in src
    assert "Copyright" in src
    assert NAMES == ("chi4", "chi5")
    assert MU == 8.0
    assert HEADS[0] == 2
    assert step_is_taken() is False


def test_json_no_take():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["early_take"] is False
    assert data["any_take"] is False
    assert data["taken"]["chi4"] == []
    assert data["taken"]["chi5"] == []
    assert data["weil_positive"] is False
    by = {(r["name"], r["h"]): r for r in data["rows"]}
    assert by[("chi4", 16)]["ns"] == [2, 3, 4, 5, 7]


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "do not survive" in text or "die" in text
    assert "LICENSE.md" in text
