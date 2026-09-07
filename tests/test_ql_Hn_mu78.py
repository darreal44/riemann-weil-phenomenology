# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₃ H_n vs n at μ=7,8. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_Hn_mu78 import HEADS, MUS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-Hn-mu78.md")
JSON = os.path.join(ROOT, "report", "ql-Hn-mu78.json")
NOTE = os.path.join(ROOT, "notes", "ql-Hn-mu78.md")
SRC = os.path.join(ROOT, "code", "ql_Hn_mu78.py")
OLD = os.path.join(ROOT, "report", "ql-H16-mu.json")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "48" in text
    assert "disproof" in text.lower() or "not a disproof" in text.replace(
        "\n", " "
    )


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "Q_pk" in src
    assert "block_norm" not in src
    assert "Copyright" in src
    assert "LICENSE.md" in src
    assert HEADS == (16, 24, 32, 48)
    assert MUS == (7.0, 8.0)
    assert step_is_taken() is False


def test_json_courant_positive():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["courant_ok"] is True
    assert data["any_negative"] is False
    by = {(r["mu"], r["h"]): r for r in data["rows"]}
    assert by[(7.0, 16)]["ns"] == [2, 3, 4, 5]
    assert by[(8.0, 16)]["ns"] == [2, 3, 4, 5, 7]
    old = json.load(open(OLD, encoding="utf-8"))
    old_by = {r["mu"]: r for r in old["rows"]}
    assert abs(by[(7.0, 16)]["lamH"] - old_by[7.0]["lamH"]) < 1e-12
    assert abs(by[(8.0, 16)]["lamH"] - old_by[8.0]["lamH"]) < 1e-12
    for mu in (7.0, 8.0):
        lams = [by[(mu, h)]["lamH"] for h in HEADS]
        for i in range(len(lams) - 1):
            assert lams[i] + 1e-15 >= lams[i + 1]
        assert lams[-1] > 0


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not a disproof" in text or "Not Weil-negative" in text
    assert "LICENSE.md" in text
