# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# ρ_far crosses 1 on (5, 7]. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_rhofar_mu import MUS, N_NEAR, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-rhofar-mu.md")
JSON = os.path.join(ROOT, "report", "ql-rhofar-mu.json")
NOTE = os.path.join(ROOT, "notes", "ql-rhofar-mu.md")
SRC = os.path.join(ROOT, "code", "ql_rhofar_mu.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "t_atoms" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "far_pieces" in src
    assert "row_at" not in src
    assert "Copyright" in src
    assert N_NEAR == 32
    assert MUS[0] == 5.0 and MUS[-1] == 7.0
    assert step_is_taken() is False


def test_json_crosses():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["rho_far_crosses"] is True
    by = {r["mu"]: r for r in data["rows"]}
    assert by[5.0]["rho_far"] < 1.0
    assert by[7.0]["rho_far"] > 1.0
    assert by[7.0]["t_atoms"] > by[5.0]["t_atoms"]
    assert by[5.0]["ns"] == [2, 3, 4]
    assert by[7.0]["ns"] == [2, 3, 4, 5]
    assert by[5.5]["rho_far"] < 1.0
    assert by[6.0]["rho_far"] > 1.0


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "Not a take" in text
    assert "LICENSE.md" in text
