# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Schur μ=5, six-character quorum. χ₃ H_4<0. T infinite. Not RH.
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from log2_log3_step import interior_primes  # noqa: E402
from ql_operator_bound import LOG2  # noqa: E402
from ql_schur_mu5 import HEADS, L, MU, step_is_taken  # noqa: E402
from ql_theta_tail import theta_op_bound  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-schur-mu5.md")
JSON = os.path.join(ROOT, "report", "ql-schur-mu5.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-mu5.md")
SRC = os.path.join(ROOT, "code", "ql_schur_mu5.py")


def _data():
    return json.load(open(JSON, encoding="utf-8"))


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Galerkin" in text
    assert "Not RH" in text
    assert "λ_min(H_4)<0" in text or "lamH" in text.lower()


def test_driver_window():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert MU == 5.0
    assert HEADS == (2, 4, 8, 16, 20, 24)
    assert interior_primes(5.0) == [2, 3]
    assert LOG2 < 0.5 * L
    assert theta_op_bound(LOG2, L) == 2.0
    assert theta_op_bound(math.log(3.0), L) == 1.0


def test_json_quorum_signs():
    data = _data()
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False
    assert step_is_taken() is False
    assert data["theta_op_log2"] == 2.0
    g = data["grids"]
    assert set(g) == {"chi3", "chi5", "chi4", "chi8", "chi7", "chi17"}
    by = {name: {r["h"]: r for r in rows} for name, rows in g.items()}
    assert by["chi3"][4]["lamH"] < 0
    assert by["chi3"][4]["s_exact"] < 0
    assert by["chi3"][4]["s_lo"] < 0
    assert by["chi5"][2]["s_lo"] < 0
    assert by["chi5"][8]["s_lo"] > 0
    assert by["chi4"][4]["s_lo"] < 0
    assert by["chi4"][8]["s_lo"] > 0
    assert by["chi8"][2]["s_lo"] > 0
    assert by["chi7"][2]["s_lo"] > 0
    assert by["chi17"][2]["s_lo"] > 0.2


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "Not a disproof of RH" in text or "do not identify" in text
    assert "SURVIVE" in text
    assert "(∀ L) Q_L ≥ 0" in text or "(∀ L)" in text
