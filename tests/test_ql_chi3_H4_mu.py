# χ₃ H₂/H₄ vs μ. μ* in (4.75, 5]. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_chi3_H4_mu import HEADS, MUS, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-chi3-H4-mu.md")
JSON = os.path.join(ROOT, "report", "ql-chi3-H4-mu.json")
NOTE = os.path.join(ROOT, "notes", "ql-chi3-H4-mu.md")
SRC = os.path.join(ROOT, "code", "ql_chi3_H4_mu.py")
MU35 = os.path.join(ROOT, "report", "ql-schur-mu35.json")
MU5 = os.path.join(ROOT, "report", "ql-schur-mu5.json")


def _data():
    return json.load(open(JSON, encoding="utf-8"))


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "μ* ∈ (4.75, 5]" in text or "(4.75, 5]" in text
    assert "No Neumann" in text or "no Neumann" in text.lower()


def test_driver_is_H_only():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "block_norm" not in src
    assert "MUS = (3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0)" in src
    assert HEADS == (2, 4)
    assert MUS[0] == 3.5
    assert MUS[-1] == 5.0


def test_json_mu_star_and_controls():
    data = _data()
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False
    assert step_is_taken() is False
    assert data["mu_star"] == [4.75, 5.0]
    assert data["first_negative_mu"] == 5.0
    by = {(r["mu"], r["h"]): r for r in data["rows"]}
    for mu in MUS:
        assert by[(mu, 2)]["lamH"] > 0
        assert by[(mu, 2)]["primes"] == [2, 3]
    assert by[(4.0, 4)]["lamH"] > 0
    assert by[(4.0, 4)]["log2_ge_half"] is True
    assert by[(4.25, 4)]["log2_ge_half"] is False
    assert by[(4.75, 4)]["lamH"] > 0
    assert by[(5.0, 4)]["lamH"] < 0
    mu35 = json.load(open(MU35, encoding="utf-8"))
    chi3_35 = [r for r in mu35["grids"]["chi3"] if r["h"] == 4][0]
    assert abs(by[(3.5, 4)]["lamH"] - chi3_35["lamH"]) < 1e-14
    mu5 = json.load(open(MU5, encoding="utf-8"))
    chi3_5 = [r for r in mu5["grids"]["chi3"] if r["h"] == 4][0]
    assert abs(by[(5.0, 4)]["lamH"] - chi3_5["lamH"]) < 1e-14


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "(4.75, 5]" in text
    assert "not the crossing" in text
    assert "(∀ L) Q_L ≥ 0" in text or "(∀ L)" in text
