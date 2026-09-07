# μ** of 37a1 drop-83 on (84, 100]. 2-unit grid. No RH.
import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "gl2-37a1-mu-star83.json")
PREREG = os.path.join(ROOT, "report", "prereg-37a1-mu-star83.md")
SRC = os.path.join(ROOT, "code", "gl2_drop83_star.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "drop 83" in text or "drop-83" in text
    assert "Not RH" in text


def test_driver_grid():
    src = open(SRC, encoding="utf-8").read()
    assert "MUS = [86, 88, 90, 92, 94, 96, 98]" in src
    assert "drop=83" in src
    assert "NB, DPS, DEG = 80, 50, 12" in src


def test_mu_star83_is_84_86():
    data = json.load(open(JSON, encoding="utf-8"))
    mus = [r["mu"] for r in data["rows"]]
    assert mus == [86, 88, 90, 92, 94, 96, 98]
    assert data["mu_star83"] == [84, 86]
    by = {r["mu"]: r for r in data["rows"]}
    assert by[86]["drop83_lam0"] < 0
    assert abs(by[86]["drop83_lam0"]) < 1e-9
    vals = [by[m]["drop83_lam0"] for m in mus]
    assert vals == sorted(vals, reverse=True)
    for r in data["rows"]:
        assert r["necessary"] is True


def test_note_does_not_claim_rh():
    text = open(
        os.path.join(ROOT, "notes", "gl2-37a1-mu-star83.md"), encoding="utf-8"
    ).read()
    assert "Not RH" in text
    assert "(84, 86]" in text
