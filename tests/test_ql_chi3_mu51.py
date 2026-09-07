# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₃ take dies at μ=5.1. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_chi3_mu51 import HEADS, MUS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-chi3-mu51.md")
JSON = os.path.join(ROOT, "report", "ql-chi3-mu51.json")
NOTE = os.path.join(ROOT, "notes", "ql-chi3-mu51.md")
SRC = os.path.join(ROOT, "code", "ql_chi3_mu51.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "5.1" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "ql_neumann_pk" in src
    assert "Copyright" in src
    assert MUS == (5.0, 5.1)
    assert HEADS == (16, 24)
    assert step_is_taken() is False


def test_json_dies_at_arrival():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["dies_at_arrival"] is True
    assert data["take_at_51"] is False
    assert data["weil_positive"] is False
    by = {(r["mu"], r["h"]): r for r in data["rows"]}
    assert by[(5.0, 16)]["s_lo_pos"] is True
    assert by[(5.1, 16)]["s_lo_pos"] is False
    assert by[(5.1, 16)]["ns"] == [2, 3, 4, 5]
    byf = {f["mu"]: f for f in data["far"]}
    assert byf[5.1]["t_atoms"] > byf[5.0]["t_atoms"]


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "arrival" in text
    assert "LICENSE.md" in text
