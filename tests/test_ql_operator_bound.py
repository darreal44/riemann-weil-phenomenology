# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Bochner multiplier of Q̂_L on W_log3. Not Galerkin. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_operator_bound import (  # noqa: E402
    Q_cosine,
    m_Q,
    s0_of,
    step_is_taken,
    w2_of,
)
from kronecker import kronecker  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-operator-bound.md")
JSON = os.path.join(ROOT, "report", "ql-operator-bound.json")
NOTE = os.path.join(ROOT, "notes", "ql-operator-bound.md")
SRC = os.path.join(ROOT, "code", "ql_operator_bound.py")
OP = os.path.join(ROOT, "report", "operator-bound-WL.md")


def _rows():
    return json.load(open(JSON, encoding="utf-8"))


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Galerkin" in text
    assert "Not RH" in text
    assert "α_line < 0" in text or "alpha_line < 0" in text


def test_driver_is_not_galerkin():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert "eigsy" not in src
    assert "C_A_lo" in src
    assert "m_Q" in src


def test_step_is_not_taken():
    assert step_is_taken() is False
    data = _rows()
    assert data["step_taken"] is False
    assert data["bochner_takes_class"] is False
    assert data["cosine_kills_class"] is False
    assert data["verdict"] == "SURVIVE"


def test_alpha_line_negative_all_four():
    data = _rows()
    by = {r["name"]: r for r in data["rows"]}
    assert set(by) == {"chi5", "chi8", "chi4", "chi3"}
    for name, r in by.items():
        assert r["alpha_line"] < 0, name
        assert r["alpha_line_neg"] is True
        assert r["cosine_pos"] is True
        assert r["Q_cos_min"] > 0
        assert r["S00_match"] is True
        assert r["S11_match"] is True
    assert by["chi5"]["alpha_line"] < -0.40
    assert by["chi8"]["alpha_line"] < -0.90
    assert by["chi4"]["alpha_line"] < -0.50
    assert by["chi3"]["alpha_line"] < -0.20
    assert by["chi5"]["t_inf"] == 0.0
    assert by["chi3"]["mQ_pi_log2"] < 0.0
    assert by["chi3"]["mQ_pi_log2"] + by["chi3"]["tail_pi_log2"] < 0.0


def test_cstar_infinite_when_chi2_minus():
    by = {r["name"]: r for r in _rows()["rows"]}
    assert by["chi5"]["A_const"] < 0
    assert by["chi3"]["A_const"] < 0
    assert by["chi5"]["cstar_finite"] is False
    assert by["chi3"]["cstar_finite"] is False
    assert by["chi8"]["A_const"] > 0
    assert by["chi4"]["A_const"] > 0


def test_shipped_mQ_reproduces_chi5_alpha():
    r = m_Q(0.0, 5, 0.25, w2_of(5))
    assert r["mQ"] < -0.20
    assert 2.0 * r["mQ"] < -0.40
    assert r["C_A_lo_tail"] < 1e-12
    assert kronecker(5, 2) == -1


def test_shipped_Q_const_matches_scan_s_diagonal():
    import math

    q0 = Q_cosine(0.0, 5, s0_of(0), w2_of(5))
    data = _rows()
    chi5 = [r for r in data["rows"] if r["name"] == "chi5"][0]
    assert abs(q0["Q"] - chi5["Q_const"]) < 1e-10
    assert abs(q0["Q"] - chi5["S00_ref"]) < 1e-8
    qhat = Q_cosine(2.0 * math.pi / math.log(3.0), 5, 0.25, w2_of(5))
    assert abs(qhat["Q"] - chi5["S11_ref"]) < 1e-8


def test_note_does_not_claim_the_class():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not taken" in text
    assert "Not Galerkin" in text
    assert "(∀ L) Q_L ≥ 0" in text
    op = open(OP, encoding="utf-8").read()
    assert "None of those estimates is in the repo" not in op
    assert "ql-operator-bound" in op
