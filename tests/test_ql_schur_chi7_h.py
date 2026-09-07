# Schur χ₇, χ(2)=+1 cell. Neumann S_lo at h=2. T infinite. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from kronecker import kronecker  # noqa: E402
from ql_schur_chi4_h import HEADS as CHI4_HEADS  # noqa: E402
from ql_schur_chi7_h import (  # noqa: E402
    CHI2,
    HEADS,
    W2,
    step_is_taken,
)

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-schur-chi7-h.md")
JSON = os.path.join(ROOT, "report", "ql-schur-chi7-h.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-chi7-h.md")
SRC = os.path.join(ROOT, "code", "ql_schur_chi7_h.py")


def _data():
    return json.load(open(JSON, encoding="utf-8"))


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Galerkin" in text
    assert "Not RH" in text
    assert "χ(2)=+1" in text or "chi(2)=+1" in text.lower()
    assert "S_lo(2)>0" in text


def test_driver_is_not_galerkin_of_WL():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert "HEADS = (2, 4, 8, 16, 20, 24)" in src
    assert "block_norm" in src
    assert HEADS == (2, 4, 8, 16, 20, 24)
    assert HEADS == CHI4_HEADS
    assert CHI2 == 1
    assert kronecker(-7, 2) == 1
    assert W2 > 0.0


def test_json_chi7_taken_at_h2():
    data = _data()
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False
    assert step_is_taken() is False
    assert data["chi7_taken"] is True
    assert data["chi2"] == 1
    assert data["w2"] > 0.0
    assert data["first_positive_h"] == 2
    by = {r["h"]: r for r in data["rows"]}
    assert by[2]["s_lo_pos"] is True
    assert by[2]["s_lo"] > 0.25
    assert by[2]["beta_pos"] is False
    assert by[4]["beta_pos"] is True
    assert by[4]["beta"] > 0
    assert by[24]["s_lo_pos"] is True
    assert by[2]["lamH"] > 0.3
    assert by[2]["lamH"] > by[24]["lamH"]


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "Not every χ" in text or "not taken" in text
    assert "(∀ L) Q_L ≥ 0" in text or "(∀ L)" in text
    assert "χ(2)=+1" in text or "chi(2)" in text.lower()
