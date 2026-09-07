# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₇ sliver on (5.1, 7]. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_chi7_mu57 import HEADS, MUS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-chi7-mu57.md")
JSON = os.path.join(ROOT, "report", "ql-chi7-mu57.json")
NOTE = os.path.join(ROOT, "notes", "ql-chi7-mu57.md")
SRC = os.path.join(ROOT, "code", "ql_chi7_mu57.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "ql_neumann_pk" in src
    assert MUS[0] == 5.1 and MUS[-1] == 7.0
    assert HEADS == (16, 24)
    assert step_is_taken() is False


def test_json():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    taken = {float(k): v for k, v in data["taken"].items()}
    assert 24 in taken[5.1]
    assert taken[7.0] == []
    assert data["weil_positive"] is False


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "LICENSE.md" in text
