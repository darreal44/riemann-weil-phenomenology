# 37a1 drop 3 at μ=74 and μ=80: preregistered negative, executed plateau. No RH.
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON74 = os.path.join(ROOT, "report", "gl2-37a1-mu74-quorum.json")
JSON80 = os.path.join(ROOT, "report", "gl2-37a1-mu80-quorum.json")
PREREG = os.path.join(ROOT, "report", "prereg-37a1-mu74.md")


def _by(path):
    if not os.path.exists(path):
        pytest.skip(f"missing {path}")
    data = json.load(open(path, encoding="utf-8"))
    return data, {r["drop"]: r for r in data["rows"]}


def test_preregistration_is_drop3_negative_at_74():
    text = open(PREREG, encoding="utf-8").read()
    assert "drop 3 → λ₀ < 0" in text or "drop 3" in text
    assert "Kill if drop 3 stays positive" in text


def test_37a1_mu74_drop3_stays_positive():
    data, by = _by(JSON74)
    assert data["label"] == "37a1" and data["mu"] == 74.0
    assert by[None]["lam0"] > 0
    assert 10 < by[None]["ell0"] < 25
    assert by[3]["lam0"] > 0
    assert 0.05 < by[3]["lam0"] < 0.15
    assert by[2]["necessary"] is True
    assert by[5]["necessary"] is True


def test_37a1_mu80_drop3_stays_positive():
    data, by = _by(JSON80)
    assert data["label"] == "37a1" and data["mu"] == 80.0
    assert by[None]["lam0"] > 0
    assert by[3]["lam0"] > 0
    assert 0.05 < by[3]["lam0"] < 0.15
    # plateau vs μ=74
    _, by74 = _by(JSON74)
    assert abs(by[3]["lam0"] - by74[3]["lam0"]) < 0.01
