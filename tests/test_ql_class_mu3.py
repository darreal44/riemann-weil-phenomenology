# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# W_log3 Neumann beyond six cells. Not (forall chi). Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_class_mu3 import MORE, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-class-mu3.md")
JSON = os.path.join(ROOT, "report", "ql-class-mu3.json")
NOTE = os.path.join(ROOT, "notes", "ql-class-mu3.md")
SRC = os.path.join(ROOT, "code", "ql_class_mu3.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text or "Not RH" in text
    assert "six" in text.lower() or "W_log3" in text or "log 3" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "MORE" in src and "row_at" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False
    assert len(MORE) == 13
    assert "chi5" not in MORE and "chi17" not in MORE


def test_json_quorum():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["n_chi"] == 13
    assert data["n_take"] == len(data["taken"])
    assert data["step_taken"] is False
    if data["n_take"] == 13:
        assert data["verdict"] == "SURVIVE"
    else:
        assert data["verdict"] == "KILL"
        dead = [n for n, hs in data["taken"].items() if not hs]
        assert dead


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "Not Weil" in text or "not Weil" in text
    assert "(∀" in text or "forall" in text.lower() or "every χ" in text or "every chi" in text.lower()
    assert "LICENSE.md" in text
