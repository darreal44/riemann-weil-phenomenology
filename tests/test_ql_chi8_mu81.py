# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₈ take dies at 2³. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_chi8_mu81 import HEADS, MUS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-chi8-mu81.md")
JSON = os.path.join(ROOT, "report", "ql-chi8-mu81.json")
NOTE = os.path.join(ROOT, "notes", "ql-chi8-mu81.md")
SRC = os.path.join(ROOT, "code", "ql_chi8_mu81.py")
OLD = os.path.join(ROOT, "report", "ql-chi817-mu8.json")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "8.1" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "ql_neumann_pk" in src
    assert "Copyright" in src
    assert MUS[0] == 8.0 and 8.1 in MUS and 9.1 in MUS
    assert HEADS[-1] == 24
    assert step_is_taken() is False


def test_json_dies_at_8cube():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["alive_after_8"] is False
    taken = {float(k): v for k, v in data["taken"].items()}
    assert taken[8.0] == [24]
    assert taken[8.1] == []
    assert taken[9.1] == []
    assert data["weil_positive"] is False
    by = {(r["mu"], r["h"]): r for r in data["rows"]}
    assert by[(8.1, 24)]["ns"] == [2, 3, 4, 5, 7, 8]
    assert by[(9.1, 24)]["ns"] == [2, 3, 4, 5, 7, 8, 9]
    old = json.load(open(OLD, encoding="utf-8"))
    old24 = [
        r["s_lo"]
        for r in old["rows"]
        if r["name"] == "chi8" and r["h"] == 24
    ][0]
    assert abs(by[(8.0, 24)]["s_lo"] - old24) < 1e-12


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "2³" in text or "8.1" in text
    assert "LICENSE.md" in text
