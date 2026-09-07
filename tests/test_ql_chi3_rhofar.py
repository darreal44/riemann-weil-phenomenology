# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# χ₃ ρ_far: larger N_NEAR / 3-layer. T infinite. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_chi3_rhofar import (  # noqa: E402
    GRIDS,
    HEAD,
    RHO_NEED,
    THREE,
    step_is_taken,
)

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-chi3-rhofar.md")
JSON = os.path.join(ROOT, "report", "ql-chi3-rhofar.json")
NOTE = os.path.join(ROOT, "notes", "ql-chi3-rhofar.md")
SRC = os.path.join(ROOT, "code", "ql_chi3_rhofar.py")
NEU = os.path.join(ROOT, "report", "ql-schur-neumann.json")


def _data():
    return json.load(open(JSON, encoding="utf-8"))


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Galerkin" in text
    assert "Not RH" in text
    assert "N_NEAR=24,32,40,48,64,80" in text
    assert "3-layer" in text


def test_driver_is_not_galerkin_of_WL():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert "GRIDS = ((24, 40), (32, 40), (40, 56), (48, 64), (64, 80), (80, 96))" in src
    assert "THREE = (24, 48, 64)" in src
    assert "HILBERT" in src
    assert HEAD == 2
    assert GRIDS[0] == (24, 40)
    assert GRIDS[-1] == (80, 96)
    assert THREE == (24, 48, 64)
    assert abs(RHO_NEED - 0.41) < 1e-15


def test_json_chi3_not_taken_and_n32_matches_61():
    data = _data()
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False
    assert step_is_taken() is False
    assert data["chi3_taken"] is False
    by = {r["n_near"]: r for r in data["rows"]}
    assert set(by) == {24, 32, 40, 48, 64, 80}
    for r in data["rows"]:
        assert r["s_lo"] < 0
        assert r["rho"] > RHO_NEED
        assert r["rho_hankel"] > RHO_NEED
        assert r["s_lo_pos"] is False
    assert by[80]["rho_far"] >= RHO_NEED
    assert by[80]["rho_near"] > by[24]["rho_near"]
    assert abs(by[32]["s_diag"] - 0.00756) < 5e-4
    neu = json.load(open(NEU, encoding="utf-8"))
    chi3 = [r for r in neu["rows"] if r["name"] == "chi3"][0]
    assert abs(by[32]["rho"] - chi3["rho"]) < 1e-14
    assert abs(by[32]["s_lo"] - chi3["s_lo"]) < 1e-14
    assert abs(by[32]["s_diag"] - chi3["s_diag"]) < 1e-14
    three = data["three_layer"]
    assert three["rho"] > RHO_NEED
    assert three["s_lo"] < 0
    assert three["s_lo_pos"] is False


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not taken" in text or "Not every χ" in text
    assert "(∀ L) Q_L ≥ 0" in text or "(∀ L)" in text
    assert "Hilbert" in text
    assert "χ₃" in text or "chi3" in text.lower()
