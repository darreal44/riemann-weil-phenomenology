# ‖Θ(log 2)‖ ≤ 1 because y ≥ L/2. Schur t2 = |w₂|. Not RH.
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_theta_tail import (  # noqa: E402
    step_is_taken,
    theta_finite_op,
    theta_op_bound,
    y_at_least_half_window,
)
from ql_operator_bound import LOG2, LOG3  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-theta-tail.md")
JSON = os.path.join(ROOT, "report", "ql-theta-tail.json")
NOTE = os.path.join(ROOT, "notes", "ql-theta-tail.md")
SRC = os.path.join(ROOT, "code", "ql_theta_tail.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Galerkin" in text
    assert "Not RH" in text
    assert "χ₅ and χ₃ still δ<0" in text or "chi5" in text.lower()


def test_lemma_y_ge_half_and_op_bound():
    assert y_at_least_half_window() is True
    assert LOG2 >= 0.5 * LOG3
    assert 2.0 >= math.sqrt(3.0)
    assert theta_op_bound() == 1.0
    assert theta_finite_op(2, 40) <= 1.001
    assert theta_finite_op(0, 40) <= 1.001
    assert theta_op_bound(y=0.0) == 2.0


def test_driver_is_not_galerkin():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert "y_at_least_half_window" in src
    assert "theta_op_bound" in src


def test_json_survive_chi5_not_taken():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False
    assert step_is_taken() is False
    assert data["theta_op_bound"] == 1.0
    assert data["theta_finite_tail"] <= 1.001
    assert data["chi8_taken"] is True
    assert data["chi5_taken"] is False
    by = {r["name"]: r for r in data["rows"]}
    assert by["chi5"]["t2_op"] < by["chi5"]["t2_op_old"]
    assert abs(by["chi5"]["t2_op"] / by["chi5"]["t2_op_old"] - 0.5) < 1e-12
    assert by["chi5"]["delta"] < 0
    assert by["chi3"]["delta"] < 0
    assert by["chi8"]["beta_pos"] is True


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not taken" in text
    assert "(∀ L) Q_L ≥ 0" in text or "(∀ L)" in text
    assert "≤ 1" in text or "≤1" in text
