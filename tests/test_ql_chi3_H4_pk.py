# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₃ H₄ with p^k stays positive through μ=5. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_chi3_H4_pk import HEADS, MUS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-chi3-H4-pk.md")
JSON = os.path.join(ROOT, "report", "ql-chi3-H4-pk.json")
NOTE = os.path.join(ROOT, "notes", "ql-chi3-H4-pk.md")
SRC = os.path.join(ROOT, "code", "ql_chi3_H4_pk.py")
H4MU = os.path.join(ROOT, "report", "ql-chi3-H4-mu.json")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "H₄(5)>0" in text or "H4(5)>0" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "Q_pk" in src
    assert "block_norm" not in src
    assert HEADS == (2, 4)
    assert MUS[-1] == 5.0
    assert step_is_taken() is False


def test_json_rescue():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["h4_positive_on_grid"] is True
    assert data["mu_star"] is None
    by = {(r["mu"], r["h"]): r for r in data["rows"]}
    assert by[(5.0, 4)]["lamH"] > 0
    assert by[(5.0, 4)]["ns"] == [2, 3, 4]
    assert by[(4.0, 4)]["ns"] == [2, 3]
    old = json.load(open(H4MU, encoding="utf-8"))
    old35 = [r for r in old["rows"] if r["mu"] == 3.5 and r["h"] == 4][0]
    assert abs(by[(3.5, 4)]["lamH"] - old35["lamH"]) < 1e-14
    old5 = [r for r in old["rows"] if r["mu"] == 5.0 and r["h"] == 4][0]
    assert old5["lamH"] < 0
    assert by[(5.0, 4)]["lamH"] > 0


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "rescue" in text
    assert "(∀ L)" in text or "Not (∀ L)" in text
