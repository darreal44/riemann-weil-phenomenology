# CST+Gauss is classical Γ on W_L. 10^{-5} is not Weil±. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_arch_weil import step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-arch-weil.md")
JSON = os.path.join(ROOT, "report", "ql-arch-weil.json")
NOTE = os.path.join(ROOT, "notes", "ql-arch-weil.md")
SRC = os.path.join(ROOT, "code", "ql_arch_weil.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "neither Weil-positive nor" in text.replace("\n", " ")
    assert "Kill" in text or "KILL" in text or "**Kill.**" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "arch_digamma" in src
    assert "delta_psi_gamma" in src
    assert "frullani" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_json_writings_agree():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["identified_arch"] is True
    assert data["weil_positive"] is False
    assert data["weil_negative"] is False
    assert data["step_taken"] is False
    assert data["frullani_err"] < 1e-12
    for row in data["weierstrass"]:
        assert row["err"] < 1e-6
    by = {p["name"]: p for p in data["planes"]}
    assert by["chi3"]["max_abs_CST_digamma"] < 1e-12
    assert by["chi5"]["max_abs_CST_digamma"] < 1e-12
    assert by["chi3"]["offdiag_max_abs"] == 0.0
    assert by["chi3"]["lam_CST_pk"] > 0
    assert by["chi3"]["lam_CST_pk"] < 1e-4
    assert by["chi3"]["lam_digamma_pk"] > 0
    assert by["chi3"]["lam_mixed_pk"] < 0
    assert by["chi3"]["ns"] == [2, 3, 4]
    assert by["chi3"]["gap_arch_CA"] > 0.5


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not Weil-positive" in text
    assert "not Weil-negative" in text
    assert "not a disproof" in text
