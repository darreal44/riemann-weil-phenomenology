# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₃ H₁₆ on (5, 7]. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_H16_mu57 import HEAD, MUS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-H16-mu57.md")
JSON = os.path.join(ROOT, "report", "ql-H16-mu57.json")
NOTE = os.path.join(ROOT, "notes", "ql-H16-mu57.md")
SRC = os.path.join(ROOT, "code", "ql_H16_mu57.py")
OLD = os.path.join(ROOT, "report", "ql-H16-mu.json")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "5.1" in text
    assert "6.5" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "Q_pk" in src
    assert "block_norm" not in src
    assert "Copyright" in src
    assert HEAD == 16
    assert MUS[0] == 5.0
    assert MUS[-1] == 7.0
    assert 5.1 in MUS
    assert step_is_taken() is False


def test_json_smooth_collapse():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["any_negative"] is False
    assert abs(data["dlam_T5"]) < 1e-2
    by = {r["mu"]: r for r in data["rows"]}
    assert by[5.0]["ns"] == [2, 3, 4]
    assert by[5.1]["ns"] == [2, 3, 4, 5]
    assert by[7.0]["ns"] == [2, 3, 4, 5]
    old = json.load(open(OLD, encoding="utf-8"))
    old_by = {r["mu"]: r for r in old["rows"]}
    assert abs(by[5.0]["lamH"] - old_by[5.0]["lamH"]) < 1e-12
    assert abs(by[7.0]["lamH"] - old_by[7.0]["lamH"]) < 1e-12
    assert by[7.0]["lamH"] < by[5.1]["lamH"]
    assert by[5.1]["lamH"] < by[5.0]["lamH"]
    assert by[5.1]["H00"] > by[5.0]["H00"]
    for mu in MUS:
        assert by[mu]["lamH"] > 0


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not a cran" in text or "Smooth" in text
    assert "LICENSE.md" in text
