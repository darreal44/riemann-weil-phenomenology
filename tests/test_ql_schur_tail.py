# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Schur tail of Q̂_L on W_log3, h=2. Not Galerkin of W_L. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_schur_tail import (  # noqa: E402
    HEAD,
    HILBERT_HANKEL,
    Q_nm,
    step_is_taken,
)
from ql_operator_bound import s0_of, w2_of  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-schur-tail.md")
JSON = os.path.join(ROOT, "report", "ql-schur-tail.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-tail.md")
SRC = os.path.join(ROOT, "code", "ql_schur_tail.py")


def _data():
    return json.load(open(JSON, encoding="utf-8"))


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Galerkin" in text
    assert "Not RH" in text
    assert "β > 0 on χ₈" in text or "beta > 0 on chi8" in text.lower()


def test_driver_is_not_galerkin_of_WL():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert "HEAD = 2" in src
    assert "HILBERT" in src
    assert "Hilbert 1894" in src
    assert abs(HILBERT_HANKEL - 3.1415926535) < 1e-8
    assert HEAD == 2


def test_step_not_taken_globally():
    assert step_is_taken() is False
    data = _data()
    assert data["step_taken"] is False
    assert data["verdict"] == "SURVIVE"
    assert data["chi8_taken"] is True
    assert data["head"] == 2


def test_beta_signs():
    by = {r["name"]: r for r in _data()["rows"]}
    assert set(by) == {"chi5", "chi8", "chi4", "chi3"}
    assert by["chi8"]["beta_pos"] is True
    assert by["chi8"]["beta"] > 0.05
    assert by["chi8"]["delta"] > 0.8
    assert by["chi5"]["beta_pos"] is False
    assert by["chi5"]["delta"] < 0
    assert by["chi3"]["beta_pos"] is False
    assert by["chi3"]["delta"] < 0
    assert by["chi4"]["beta_pos"] is False
    for r in by.values():
        assert r["S00_match"] is True
        assert r["S11_match"] is True
        assert r["qmin_at"] == 2


def test_shipped_Q00_matches_scan_s():
    q00 = Q_nm(0, 0, 8, s0_of(0), w2_of(8))
    chi8 = [r for r in _data()["rows"] if r["name"] == "chi8"][0]
    assert abs(q00 - chi8["H00"]) < 1e-10
    assert abs(q00 - chi8["H00"]) < 1e-8


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not taken" in text
    assert "(∀ L) Q_L ≥ 0" in text or "(∀ L)" in text
    assert "χ₈" in text or "chi8" in text.lower()
    assert "Hilbert 1894" in text
