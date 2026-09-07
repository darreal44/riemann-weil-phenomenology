# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₃ Neumann take dies on (5, 7]. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_schur_chi3_mu57 import HEADS, MUS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-schur-chi3-mu57.md")
JSON = os.path.join(ROOT, "report", "ql-schur-chi3-mu57.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-chi3-mu57.md")
SRC = os.path.join(ROOT, "code", "ql_schur_chi3_mu57.py")
OLD = os.path.join(ROOT, "report", "ql-H16-mu.json")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "5.5" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "row_at" in src
    assert "ql_neumann_pk" in src
    assert "Copyright" in src
    assert "from scan_s import assemble" not in src
    assert HEADS == (16, 24)
    assert MUS[0] == 5.0 and MUS[-1] == 7.0
    assert step_is_taken() is False


def test_json_take_dies():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["take_dies"] is True
    assert data["take_mu_h16"] == [5.0]
    assert data["weil_positive"] is False
    by = {(r["mu"], r["h"]): r for r in data["rows"]}
    assert by[(5.0, 16)]["s_lo_pos"] is True
    assert by[(7.0, 16)]["s_lo_pos"] is False
    assert by[(5.5, 16)]["s_lo_pos"] is False
    old = json.load(open(OLD, encoding="utf-8"))
    old_by = {r["mu"]: r for r in old["rows"]}
    assert abs(by[(5.0, 16)]["lamH"] - old_by[5.0]["lamH"]) < 1e-12
    assert abs(by[(7.0, 16)]["lamH"] - old_by[7.0]["lamH"]) < 1e-12


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "single-L" in text or "dies" in text
    assert "LICENSE.md" in text
