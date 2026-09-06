# A−P23 vs P_rest at μ=150. One point, not a slope. No RH.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_split23 import split_AP  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
NOTE = os.path.join(ROOT, "notes", "av-mu150.md")
PREREG = os.path.join(ROOT, "report", "prereg-av-mu150.md")


def test_split_matches_mu16_table():
    r = split_AP(16.0, dps=30)
    assert abs(r["A_minus_P23"] - 0.075) < 0.002
    assert abs(r["Prest"] - 0.070) < 0.002
    assert abs(r["Q"] - 0.0055) < 0.001
    assert r["crossed"] is False


def test_mu150_A_minus_P23_does_not_cross_Prest():
    r = split_AP(150.0, dps=40)
    assert r["Q"] > 0
    assert 0.003 < r["Q"] < 0.009
    assert r["A_minus_P23"] < 0  # naive zero-crossing of A-P23 happened
    assert r["Prest"] < 0  # Prest went with it
    assert r["crossed"] is False  # A-P23 still above Prest
    assert r["A_minus_P23"] > r["Prest"]


def test_note_is_one_point_not_a_slope():
    text = open(NOTE, encoding="utf-8").read()
    prereg = open(PREREG, encoding="utf-8").read()
    assert "Not a sixth slope" in prereg or "not a sixth slope" in prereg.lower()
    assert "not taken" in text.lower() or "open" in text
    assert "RH; not this note" in text
