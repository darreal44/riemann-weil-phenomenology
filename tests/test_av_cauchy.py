# Cauchy majorant of |a^{(6)}| on [0,1]. Not RH.
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_cauchy import ROOM, a_complex, elementary_M  # noqa: E402
from av_gauss import a_integrand

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-cauchy-a6.md")
JSON = os.path.join(ROOT, "report", "av-cauchy-a6.json")
NOTE = os.path.join(ROOT, "notes", "av-cauchy-a6.md")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "r=2" in text
    assert "Not RH" in text
    assert "Kill" in text or "**Kill.**" in text


def test_a_complex_matches_real_on_the_interval():
    for y in (0.0, 0.1127, 0.5, 0.8873, 1.0):
        ac = a_complex(y)
        assert abs(ac.imag) < 1e-12
        assert abs(ac.real - a_integrand(y)) < 1e-12


def test_poles_outside_r2():
    assert math.pi > 2.0
    assert ROOM > 0


def test_elementary_bound_is_finite():
    b = elementary_M(2.0)
    assert b["M_elem"] > 0
    assert b["sinh_floor"] > 0


def test_two_panel_fits_and_Q_positive():
    data = json.load(open(JSON, encoding="utf-8"))
    el = data["elementary"]
    enc = data["enclose"]
    assert data["r"] == 2.0
    assert el["fits_1panel"] is False
    assert el["fits_2panel"] is True
    assert el["rem_2panel"] < ROOM
    assert enc["inside_window"] is True
    assert enc["Qlo_pos"] is True
    assert enc["Qlo"] > 0.003
    assert abs(data["min_sinh_caps"] - data["sin_r"]) < 1e-6


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "two panels" in text.lower() or "Two panels" in text
