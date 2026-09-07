# Schur χ₃ at larger h. Neumann S_lo, not β. T infinite. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_schur_chi3_h import HEADS, step_is_taken  # noqa: E402
from ql_schur_chi4_h import HEADS as CHI4_HEADS  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-schur-chi3-h.md")
JSON = os.path.join(ROOT, "report", "ql-schur-chi3-h.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-chi3-h.md")
SRC = os.path.join(ROOT, "code", "ql_schur_chi3_h.py")
NEU = os.path.join(ROOT, "report", "ql-schur-neumann.json")


def _data():
    return json.load(open(JSON, encoding="utf-8"))


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Galerkin" in text
    assert "Not RH" in text
    assert "h = 2, 4, 8, 16, 20, 24" in text or "2, 4, 8, 16, 20, 24" in text
    assert "Neumann" in text


def test_driver_is_not_galerkin_of_WL():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert "HEADS = (2, 4, 8, 16, 20, 24)" in src
    assert "block_norm" in src
    assert HEADS == (2, 4, 8, 16, 20, 24)
    assert HEADS == CHI4_HEADS


def test_json_h_star_and_bounds():
    data = _data()
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False
    assert step_is_taken() is False
    assert data["chi3_taken"] is True
    assert data["h_star"] == [2, 4]
    assert data["first_positive_h"] == 4
    by = {r["h"]: r for r in data["rows"]}
    assert by[2]["s_lo_pos"] is False
    assert by[2]["s_lo"] < 0
    assert by[2]["beta_pos"] is False
    assert by[4]["s_lo_pos"] is True
    assert by[4]["s_lo"] > 0.006
    assert by[24]["s_lo_pos"] is True
    assert by[2]["lamH"] > by[24]["lamH"]
    for r in data["rows"]:
        assert r["beta_pos"] is False
    neu = json.load(open(NEU, encoding="utf-8"))
    chi3 = [r for r in neu["rows"] if r["name"] == "chi3"][0]
    assert abs(by[2]["s_lo"] - chi3["s_lo"]) < 1e-14
    assert abs(by[2]["rho"] - chi3["rho"]) < 1e-14


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "(2, 4]" in text
    assert "(∀ L) Q_L ≥ 0" in text or "(∀ L)" in text
    assert "Not every χ" in text or "not taken" in text
    assert "Neumann" in text
