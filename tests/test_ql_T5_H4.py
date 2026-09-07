# T₅ on H₄ at μ=5.1. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_T5_H4 import step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-T5-H4.md")
JSON = os.path.join(ROOT, "report", "ql-T5-H4.json")
NOTE = os.path.join(ROOT, "notes", "ql-T5-H4.md")
SRC = os.path.join(ROOT, "code", "ql_T5_H4.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "5.1" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "Q_pk" in src
    assert "block_norm" not in src
    assert step_is_taken() is False


def test_json():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    by = {(r["name"], r["mu"]): r for r in data["rows"]}
    assert by[("chi3", 5.1)]["ns"] == [2, 3, 4, 5]
    assert by[("chi3", 5.0)]["ns"] == [2, 3, 4]
    assert by[("chi3", 5.1)]["lamH4"] > 0
    assert by[("chi3", 5.1)]["H00"] > by[("chi3", 5.0)]["H00"]
    for name in ("chi3", "chi5", "chi4", "chi8", "chi7", "chi17"):
        assert by[(name, 5.1)]["lamH4"] > 0


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not the cause of μ*" in text or "does not flip" in text
