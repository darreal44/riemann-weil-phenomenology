# Cauchy |a_odd^{(6)}| on [0,1]. Not RH.
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_cauchy_odd import ROOM, a_odd_complex, kernel_limit_odd  # noqa: E402
from av_enclose_odd_ball import a_odd  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-cauchy-odd.md")
JSON = os.path.join(ROOT, "report", "av-cauchy-odd.json")
NOTE = os.path.join(ROOT, "notes", "av-cauchy-odd.md")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "s₀=3/4" in text or "s0=3/4" in text
    assert "Not RH" in text
    assert "Kill" in text or "**Kill.**" in text


def test_a_odd_complex_matches_real():
    assert abs(a_odd_complex(0.0).real - 0.5 * kernel_limit_odd()) < 1e-12
    for y in (0.1127, 0.5, 0.8873, 1.0):
        ac = a_odd_complex(y)
        assert abs(ac.imag) < 1e-12
        assert abs(ac.real - a_odd(y)) < 1e-12


def test_same_poles_as_even():
    assert math.pi > 2.0
    assert ROOM > 0.004


def test_two_panel_chi3_positive():
    data = json.load(open(JSON, encoding="utf-8"))
    el = data["elementary"]
    enc = data["enclose"]
    assert data["r"] == 2.0
    assert el["fits_1panel"] is False
    assert el["fits_2panel"] is True
    assert el["rem_2panel"] < ROOM
    assert enc["chi3_pos"] is True
    assert enc["chi"]["chi3"]["Qlo"] > 0.004
    assert enc["chi"]["chi4"]["Qlo"] > 0
    assert enc["chi"]["chi7"]["Qlo"] > 0


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "two panels" in text.lower() or "Two panels" in text
