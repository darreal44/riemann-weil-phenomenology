# Schur χ₄ at larger h. T infinite. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_schur_chi4_h import HEADS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-schur-chi4-h.md")
JSON = os.path.join(ROOT, "report", "ql-schur-chi4-h.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-chi4-h.md")
SRC = os.path.join(ROOT, "code", "ql_schur_chi4_h.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Galerkin" in text
    assert "Not RH" in text
    assert "h = 2, 4, 8, 16, 20, 24" in text or "2, 4, 8, 16, 20, 24" in text


def test_driver_is_not_galerkin_of_WL():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert "HEADS = (2, 4, 8, 16, 20, 24)" in src
    assert "hankel_c_tail" in src
    assert HEADS == (2, 4, 8, 16, 20, 24)


def test_json_h_star_and_signs():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False
    assert step_is_taken() is False
    assert data["chi4_taken"] is True
    assert data["h_star"] == [16, 20]
    assert data["first_positive_h"] == 20
    by = {r["h"]: r for r in data["rows"]}
    assert by[2]["beta_pos"] is False
    assert by[16]["beta_pos"] is False
    assert by[16]["beta"] < 0
    assert by[20]["beta_pos"] is True
    assert by[20]["beta"] > 0
    assert by[24]["beta_pos"] is True
    for r in data["rows"]:
        assert r["qmax_times_sum"] <= 0.500001


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "(16, 20]" in text
    assert "(∀ L) Q_L ≥ 0" in text or "(∀ L)" in text
    assert "χ(2)=−1" in text or "chi(2)" in text.lower()
