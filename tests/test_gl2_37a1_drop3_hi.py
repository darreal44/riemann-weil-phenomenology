# 37a1 drop 3 at μ=100..250. Preregistered plateau O(0.1); executed 16/16 NEG.
# Prime-side Q. No RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "gl2-37a1-drop3-hi.json")
JSON74 = os.path.join(ROOT, "report", "gl2-37a1-mu74-quorum.json")
CONTROL = os.path.join(ROOT, "report", "gl2-37a1-drop3-control.json")
PREREG = os.path.join(ROOT, "report", "prereg-37a1-drop3-hi.md")
NOTE = os.path.join(ROOT, "notes", "gl2-37a1-drop3-hi.md")
SRC = os.path.join(ROOT, "code", "gl2_drop3_hi.py")


def _hi():
    return json.load(open(JSON, encoding="utf-8"))


def test_preregistration_locked_before_run():
    text = open(PREREG, encoding="utf-8").read()
    assert "μ = 100, 110, …, 250" in text or "μ = 100, 110" in text
    assert "O(0.1)" in text
    assert "drop-3 λ₀ < 0" in text
    assert "Not RH" in text or "Not the Gram" in text


def test_driver_uses_32_jobs_and_spawn():
    src = open(SRC, encoding="utf-8").read()
    assert "range(100, 260, 10)" in src
    assert "ProcessPoolExecutor" in src
    assert 'get_context("spawn")' in src
    assert "(mu, 3," in src
    assert "prime_power_prime" in open(
        os.path.join(ROOT, "code", "scan_q_gl2.py"), encoding="utf-8"
    ).read()


def test_old_mu74_missed_71_and_73():
    """Historical assembly: ppts capped at 67, so drop-71 = full."""
    data = json.load(open(JSON74, encoding="utf-8"))
    by = {r["drop"]: r for r in data["rows"]}
    assert by[71]["lam0"] == by[None]["lam0"]
    assert by[73]["lam0"] == by[None]["lam0"]
    assert by[3]["lam0"] > 0


def test_grid_executed_kill_joined():
    data = _hi()
    assert data["label"] == "37a1"
    assert data["NB"] == 80 and data["dps"] == 50
    mus = [r["mu"] for r in data["rows"]]
    assert mus == list(range(100, 260, 10))
    for r in data["rows"]:
        assert r["full_lam0"] > 0
        assert r["full_ell"] > 20
        assert r["drop3_lam0"] < 0
        assert r["necessary"] is True
    # locked endpoints
    r0, r1 = data["rows"][0], data["rows"][-1]
    assert abs(r0["drop3_lam0"] + 0.4185) < 0.01
    assert abs(r1["drop3_lam0"] + 1.016) < 0.02
    assert 21 < r0["full_ell"] < 23
    assert 43 < r1["full_ell"] < 45
    # well deepens
    ells = [r["full_ell"] for r in data["rows"]]
    assert ells == sorted(ells)


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text or "not RH" in text
    assert "KILL" in text
    assert "16/16" in text
    assert "(∀ L) Q_L ≥ 0" in text or "Q_L" in text


def test_control_74_80_plateau_survives_ppts_fix():
    data = json.load(open(CONTROL, encoding="utf-8"))
    by = {r["mu"]: r for r in data["rows"]}
    assert set(by) == {74, 80}
    for mu, r in by.items():
        assert r["full_lam0"] > 0
        assert r["drop3_lam0"] > 0
        assert r["necessary"] is False
        assert 0.05 < r["drop3_lam0"] < 0.15
    assert abs(by[74]["drop3_lam0"] - 0.09019) < 0.002
    assert abs(by[80]["drop3_lam0"] - 0.08902) < 0.002
    # 71 votes in the full form (old μ=80 json missed it)
    assert by[80]["full_ell"] > 18
