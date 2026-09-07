# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₃ H₁₆ vs μ through 7 and 8=2³. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_H16_mu import HEAD, MUS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-H16-mu.md")
JSON = os.path.join(ROOT, "report", "ql-H16-mu.json")
NOTE = os.path.join(ROOT, "notes", "ql-H16-mu.md")
SRC = os.path.join(ROOT, "code", "ql_H16_mu.py")
OLD = os.path.join(ROOT, "report", "ql-schur-pk-mu5.json")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "8.1" in text
    assert "disproof" in text.lower() or "not a disproof" in text.replace(
        "\n", " "
    )


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "Q_pk" in src
    assert "block_norm" not in src
    assert HEAD == 16
    assert MUS[-1] == 8.1
    assert step_is_taken() is False


def test_json_ns_and_no_jump():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["any_negative"] is False
    assert abs(data["dlam_T7"]) < 1e-2
    assert abs(data["dlam_8"]) < 1e-2
    by = {r["mu"]: r for r in data["rows"]}
    assert by[5.0]["ns"] == [2, 3, 4]
    assert by[7.1]["ns"] == [2, 3, 4, 5, 7]
    assert by[8.1]["ns"] == [2, 3, 4, 5, 7, 8]
    old = json.load(open(OLD, encoding="utf-8"))
    old16 = [r for r in old["rows"] if r["h"] == 16][0]["lamH"]
    assert abs(by[5.0]["lamH"] - old16) < 1e-12
    assert by[8.1]["lamH"] > 0
    assert by[8.1]["lamH"] < by[5.0]["lamH"]


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not a disproof" in text or "Not Weil-negative" in text
    assert "collaps" in text
