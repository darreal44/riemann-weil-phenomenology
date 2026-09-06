# kappa_block2 probe. Smoke locked in the journal. Not RH. Not Thm 4.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from kappa_block2 import LADDER, probe  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
JOURNAL = os.path.join(ROOT, "notes", "journal-kappa-block2.md")
JSON = os.path.join(ROOT, "report", "kappa-block2-ladder.json")
SRC = os.path.join(ROOT, "code", "kappa_block2.py")


def test_journal_locked_before_server():
    text = open(JOURNAL, encoding="utf-8").read()
    assert "Locked before the server" in text
    assert "κ → 4" in text and "κ → 8" in text
    assert "Kill if" in text
    assert "Not RH" in text
    assert "cpu=400" in text and "cpu=200" in text
    assert "--ladder" in text or "kappa_block2.py --ladder" in open(
        os.path.join(ROOT, "code", "kappa_block2.py"), encoding="utf-8"
    ).read()


def test_ladder_points_match_journal():
    assert LADDER == [(8, 40), (16, 80), (16, 160), (16, 400), (24, 200)]
    src = open(SRC, encoding="utf-8").read()
    assert "--ladder" in src
    assert "ProcessPoolExecutor" in src


def test_sandbox_smoke_toward_four():
    r2 = probe(2, 16)
    r4 = probe(4, 40)
    assert abs(r2["mass"] - 0.590) < 0.01
    assert abs(r2["kappa"] - 1.67) < 0.05
    assert abs(r4["mass"] - 1.109) < 0.01
    assert abs(r4["kappa"] - 3.14) < 0.05
    assert r4["kappa"] > r2["kappa"]


def test_ladder_executed_kill():
    data = json.load(open(JSON, encoding="utf-8"))
    rows = data["rows"]
    assert [(int(r["Lam"]), int(r["cpu"])) for r in rows] == list(LADDER)
    by = {(int(r["Lam"]), int(r["cpu"])): r for r in rows}
    k160 = by[(16, 160)]["kappa"]
    k400 = by[(16, 400)]["kappa"]
    wander = abs(k400 - k160)
    assert wander < 0.15
    assert abs(k400 - 5.984) < 0.02
    assert abs(k400 - 4.0) > 0.2
    assert abs(k400 - 8.0) > 0.2
    assert abs(by[(8, 40)]["kappa"] - 4.284) < 0.02
    assert abs(by[(24, 200)]["kappa"] - 7.260) < 0.02


def test_note_does_not_claim_thm4():
    text = open(os.path.join(ROOT, "notes", "kappa-block2.md"), encoding="utf-8").read()
    assert "Not RH" in text
    assert "Not Thm 4" in text or "not a shell freeze" in text
    assert "KILL" in text
