# drop-89 and drop-97 at 37a1 μ=100. Optional isolation. No RH.
import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "gl2-37a1-drop89-97.json")
PREREG = os.path.join(ROOT, "report", "prereg-37a1-drop89-97.md")
SRC = os.path.join(ROOT, "code", "gl2_drop89_97.py")
TERM = os.path.join(ROOT, "report", "term-89-97.md")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "drop 89" in text and "drop 97" in text
    assert "Not RH" in text
    term = open(TERM, encoding="utf-8").read()
    assert "drop-{89,97}" in term or "89,97" in term


def test_driver_two_jobs():
    src = open(SRC, encoding="utf-8").read()
    assert "DROPS = (89, 97)" in src
    assert "MU, NB, DPS, DEG = 100, 80, 50, 12" in src
    assert "ProcessPoolExecutor" in src


def test_both_dispensable():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["label"] == "37a1" and data["mu"] == 100
    by = {r["drop"]: r for r in data["rows"]}
    assert set(by) == {89, 97}
    assert by[89]["lam0"] > 0 and by[89]["necessary"] is False
    assert by[97]["lam0"] > 0 and by[97]["necessary"] is False
    assert abs(by[89]["lam0"] - 7.11e-10) / 7.11e-10 < 0.05
    assert abs(by[97]["lam0"] - 3.06e-10) / 3.06e-10 < 0.05
    # 97 almost full (2.76e-10); 89 shallows but stays PSD
    assert by[97]["ell0"] > 21
    assert 20 < by[89]["ell0"] < 22


def test_note_does_not_claim_rh():
    text = open(os.path.join(ROOT, "notes", "gl2-37a1-drop89-97.md"), encoding="utf-8").read()
    assert "Not RH" in text or "not RH" in text
    assert "SURVIVE" in text
    assert "no 89+97 piece" in text or "not" in text.lower()
