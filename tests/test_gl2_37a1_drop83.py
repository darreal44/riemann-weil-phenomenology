# Isolate 83 on 37a1. Preregistered term-83.md. Prime-side Q. No RH.
import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "gl2-37a1-drop83.json")
PREREG = os.path.join(ROOT, "report", "prereg-37a1-drop83.md")
SRC = os.path.join(ROOT, "code", "gl2_drop83.py")
TERM = os.path.join(ROOT, "report", "term-83.md")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "μ = 82" in text or "μ=82" in text or "82 (83 not in)" in text
    assert "drop 83" in text or "drop-83" in text
    assert "Not RH" in text
    term = open(TERM, encoding="utf-8").read()
    assert "μ=82 vs 84" in term or "82 vs 84" in term


def test_driver_is_drop3_hi_type():
    src = open(SRC, encoding="utf-8").read()
    assert "MUS = [82, 84, 100]" in src
    assert "83" in src and "drop" in src
    assert "ProcessPoolExecutor" in src
    assert "NB, DPS, DEG = 80, 50, 12" in src


def test_isolation_executed():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["label"] == "37a1"
    assert data["NB"] == 80 and data["dps"] == 50
    by = {r["mu"]: r for r in data["rows"]}
    assert set(by) == {82, 84, 100}
    for r in data["rows"]:
        assert r["full_lam0"] > 0
    # 83 not in μ=82: drop-83 = full
    assert by[82]["drop83_lam0"] == by[82]["full_lam0"]
    assert by[82]["drop3_lam0"] > 0
    assert abs(by[82]["drop3_lam0"] - 0.0866) < 0.002
    # arrival: 3 still dispensable, 83 still dispensable
    assert by[84]["drop3_lam0"] > 0
    assert by[84]["drop83_lam0"] > 0
    assert abs(by[84]["drop3_lam0"] - 0.0481) < 0.002
    # cliff window: both necessary; drop-3 matches hi json
    assert by[100]["drop3_lam0"] < 0
    assert by[100]["drop83_lam0"] < 0
    assert abs(by[100]["drop3_lam0"] + 0.4185) < 0.002
    assert abs(by[100]["drop83_lam0"] + 0.0803) < 0.002


def test_note_does_not_claim_rh():
    text = open(os.path.join(ROOT, "notes", "gl2-37a1-drop83.md"), encoding="utf-8").read()
    assert "Not RH" in text or "not RH" in text
    assert "does not isolate the join" in text
    assert "voter at μ=100" in text
