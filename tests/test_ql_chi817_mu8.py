# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₁₇ dies at μ=8; χ₈ still takes. Prereg KILL. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_chi817_mu8 import HEADS, MU8, NAMES, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-chi817-mu8.md")
JSON = os.path.join(ROOT, "report", "ql-chi817-mu8.json")
NOTE = os.path.join(ROOT, "notes", "ql-chi817-mu8.md")
SRC = os.path.join(ROOT, "code", "ql_chi817_mu8.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "χ₁₇ still takes" in text.replace("\n", " ") or "chi17" in text.lower()


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "ql_neumann_pk" in src
    assert "Copyright" in src
    assert NAMES == ("chi8", "chi17")
    assert MU8 == 8.0
    assert HEADS[0] == 2
    assert step_is_taken() is False


def test_json_kill_chi17_dies():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "KILL"
    assert data["chi17_takes_8"] is False
    assert 24 in data["taken8"]["chi8"]
    assert data["taken8"]["chi17"] == []
    assert data["taken11"] is None
    assert data["weil_positive"] is False
    by = {(r["name"], r["mu"], r["h"]): r for r in data["rows"]}
    assert by[("chi8", 8.0, 16)]["ns"] == [2, 3, 4, 5, 7]


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "KILL" in text
    assert "χ₁₇" in text or "chi17" in text.lower()
    assert "LICENSE.md" in text
