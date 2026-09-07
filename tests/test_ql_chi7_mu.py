# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₇ take dies on (5.1, 7]. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_chi7_mu import HEADS, MUS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-chi7-mu.md")
JSON = os.path.join(ROOT, "report", "ql-chi7-mu.json")
NOTE = os.path.join(ROOT, "notes", "ql-chi7-mu.md")
SRC = os.path.join(ROOT, "code", "ql_chi7_mu.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "3.5" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "ql_neumann_pk" in src
    assert "Copyright" in src
    assert MUS[0] == 3.0 and MUS[-1] == 7.0
    assert 5.1 in MUS
    assert HEADS[0] == 2
    assert step_is_taken() is False


def test_json_dies_after_51():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    taken = {float(k): v for k, v in data["taken"].items()}
    assert data["first_dead"] == 7.0
    assert 2 in taken[3.0]
    assert 24 in taken[5.1]
    assert taken[7.0] == []
    assert data["weil_positive"] is False
    by = {(r["mu"], r["h"]): r for r in data["rows"]}
    assert by[(3.0, 2)]["s_lo"] > 0.2
    assert by[(3.0, 2)]["ns"] == [2]
    assert by[(5.1, 2)]["ns"] == [2, 3, 4, 5]


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "Unlike χ₃" in text or "survives T₅" in text
    assert "LICENSE.md" in text
