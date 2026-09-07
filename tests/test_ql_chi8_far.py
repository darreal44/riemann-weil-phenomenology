# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# 2³ does not jump χ₈ t_atoms. KILL. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_chi8_far import step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-chi8-far.md")
JSON = os.path.join(ROOT, "report", "ql-chi8-far.json")
NOTE = os.path.join(ROOT, "notes", "ql-chi8-far.md")
SRC = os.path.join(ROOT, "code", "ql_chi8_far.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "t_atoms" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "far_pieces" in src
    assert step_is_taken() is False


def test_json_kill():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "KILL"
    assert abs(data["dt_atoms"]) < 1e-9
    by = {r["mu"]: r for r in data["rows"]}
    assert by[8.1]["ns"] == [2, 3, 4, 5, 7, 8]
    assert by[8.1]["w8"] == 0.0
    assert by[8.1]["rho_far"] < by[8.0]["rho_far"]


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "KILL" in text
    assert "Not RH" in text
    assert "χ₈(8)=0" in text or "chi8(8)" in text.lower()
