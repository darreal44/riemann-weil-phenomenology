# Schur χ₁₇, even χ(2)=+1. Both bounds at h=2. T infinite. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from kronecker import kronecker  # noqa: E402
from ql_schur_chi17_h import (  # noqa: E402
    CHI2,
    HEADS,
    S0,
    W2,
    step_is_taken,
)
from ql_schur_chi4_h import HEADS as CHI4_HEADS  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-schur-chi17-h.md")
JSON = os.path.join(ROOT, "report", "ql-schur-chi17-h.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-chi17-h.md")
SRC = os.path.join(ROOT, "code", "ql_schur_chi17_h.py")


def _data():
    return json.load(open(JSON, encoding="utf-8"))


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Galerkin" in text
    assert "Not RH" in text
    assert "S_lo(2)>0" in text
    assert "β(2)>0" in text or "beta(2)>0" in text.lower()


def test_driver_is_not_galerkin_of_WL():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert "HEADS = (2, 4, 8, 16, 20, 24)" in src
    assert HEADS == CHI4_HEADS
    assert CHI2 == 1
    assert kronecker(17, 2) == 1
    assert W2 > 0.0
    assert abs(S0 - 0.25) < 1e-15


def test_json_chi17_taken_at_h2_both_bounds():
    data = _data()
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False
    assert step_is_taken() is False
    assert data["chi17_taken"] is True
    assert data["chi2"] == 1
    assert data["first_positive_h"] == 2
    by = {r["h"]: r for r in data["rows"]}
    assert by[2]["s_lo_pos"] is True
    assert by[2]["s_lo"] > 0.6
    assert by[2]["beta_pos"] is True
    assert by[2]["beta"] > 0.3
    assert by[2]["lamH"] > 0.6
    assert by[2]["lamH"] > by[24]["lamH"]


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "Not every χ" in text or "not taken" in text
    assert "(∀ L) Q_L ≥ 0" in text or "(∀ L)" in text
    assert "six cells" in text or "(s₀, χ(2))" in text
