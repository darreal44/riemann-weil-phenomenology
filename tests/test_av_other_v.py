# Other v at χ₅ μ=150. Pencil of v-impact.md. No RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "av-other-v-mu150.json")
PREREG = os.path.join(ROOT, "report", "prereg-av-other-v-mu150.md")
NOTE = os.path.join(ROOT, "notes", "av-other-v-mu150.md")
PENCIL = {"rat", "5-4-1", "4-3-0", "1-1-0", "3-2-1"}


def _block(mu):
    data = json.load(open(JSON, encoding="utf-8"))
    return next(b for b in data["blocks"] if abs(b["mu"] - mu) < 1e-9)


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Q≤0" in text or "Q<=0" in text
    assert "Not RH" in text
    assert "Not a sixth slope" in text or "not a sixth slope" in text


def test_mu16_reproduces_v_impact():
    by = {r["name"]: r for r in _block(16)["rows"]}
    assert abs(by["rat"]["Q"] - 0.0055) < 0.0002
    assert abs(by["5-4-1"]["Q"] - 0.0014) < 0.0002
    assert abs(by["4-3-0"]["Q"] - 0.00054) < 0.0002
    assert abs(by["1-1-0"]["Q"] - 0.0095) < 0.0003
    assert abs(by["3-2-1"]["Q"] - 0.019) < 0.0005
    assert _block(16)["overlap_rat_vmin"] > 0.99


def test_pencil_survives_mu150():
    b = _block(150)
    assert b["lam_min"] > 0
    assert b["overlap_rat_vmin"] > 0.99
    by = {r["name"]: r for r in b["rows"]}
    for name in PENCIL:
        assert by[name]["Q"] > 0, name
        assert by[name]["pencil"] is True
    assert abs(by["rat"]["Q"] - 0.0041) < 0.0002
    # A-P23 through 0 is this v, not the plane
    assert by["rat"]["A_minus_P23"] < 0
    assert by["5-4-1"]["A_minus_P23"] > 0
    assert by["e0"]["Q"] > 0 and by["e1"]["Q"] > 0 and by["e2"]["Q"] > 0


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "SURVIVE" in text
    assert "Not RH" in text or "not RH" in text
    assert "not (∀ μ)" in text or "Not (∀ μ)" in text
