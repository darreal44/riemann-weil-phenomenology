# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₇ vs χ₁₇: same t_atoms, qmin_far split. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_chi7_vs_chi17 import MU, NAMES, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-chi7-vs-chi17.md")
JSON = os.path.join(ROOT, "report", "ql-chi7-vs-chi17.json")
NOTE = os.path.join(ROOT, "notes", "ql-chi7-vs-chi17.md")
SRC = os.path.join(ROOT, "code", "ql_chi7_vs_chi17.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "χ₇(7)=0" in text.replace("\n", " ") or "chi(7)" in text.lower()


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "far_pieces" in src
    assert "Copyright" in src
    assert MU == 7.0
    assert NAMES == ("chi7", "chi17")
    assert step_is_taken() is False


def test_json_same_tatoms_qmin_gap():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["explained"] is True
    by = {r["name"]: r for r in data["rows"]}
    assert by["chi7"]["ns"] == [2, 3, 4, 5]
    assert by["chi7"]["chi2"] == 1
    assert by["chi17"]["chi2"] == 1
    assert by["chi7"]["weights"]["chi7_at_7"] == 0.0
    assert abs(by["chi7"]["t_atoms"] - by["chi17"]["t_atoms"]) < 1e-6
    assert by["chi17"]["qmin_far"] > by["chi7"]["qmin_far"]
    assert by["chi7"]["rho_far"] < 1.0
    assert by["chi17"]["rho_far"] < 1.0


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "t_atoms identical" in text or "same t_atoms" in text
    assert "LICENSE.md" in text
