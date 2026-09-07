# Neumann Q_pk μ=5 χ₃. S_lo(2)<0. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_schur_pk_mu5 import HEADS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-schur-pk-mu5.md")
JSON = os.path.join(ROOT, "report", "ql-schur-pk-mu5.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-pk-mu5.md")
SRC = os.path.join(ROOT, "code", "ql_schur_pk_mu5.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Galerkin" in text
    assert "Not RH" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "Q_pk" in src
    assert "block_norm" in src
    assert HEADS == (2, 4, 8, 16, 20, 24)
    assert step_is_taken() is False


def test_json_not_taken_small_h():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["chi3_taken"] is False
    by = {r["h"]: r for r in data["rows"]}
    assert by[2]["s_lo"] < 0
    assert by[4]["s_lo"] < 0


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not take" in text or "eaten" in text
