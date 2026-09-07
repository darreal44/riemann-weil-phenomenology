# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_compare import g  # noqa: E402
from av_I01_chord import (  # noqa: E402
    PARENT_GAP,
    chord_I01,
    chord_points,
    g_lo,
    run,
    step_is_taken,
)
from av_I01_switch import true_I01  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-I01-chord.md")
NOTE = os.path.join(ROOT, "notes", "av-I01-chord.md")
SRC = os.path.join(ROOT, "code", "av_I01_chord.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text
    assert "Not RH" in text
    assert "0.00315" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "g_lo" in src and "cnodes" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_chords_start_at_yinf():
    pts = chord_points()
    assert abs(pts["cnodes"][0] - pts["yinf"]) < 1e-12
    assert abs(pts["cnodes"][-1] - 1.0) < 1e-12


def test_g_lo_lies_below_shipped_g():
    pts = chord_points()
    for k in range(1, 201):
        y = k / 200.0
        assert g_lo(y, pts) <= g(y) + 1e-8, (y, g_lo(y, pts), g(y))


def test_gap_tighter_than_parent():
    pts = chord_points()
    i_true = true_I01()
    i_lo, _ = chord_I01(pts)
    gap = i_true - i_lo
    data = run()
    assert abs(data["gap"] - gap) < 1e-12
    assert gap < PARENT_GAP
    assert data["gpp_negative_tail"] is True
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False


def test_note_does_not_claim_weil_or_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "Not Weil" in text or "not Weil" in text
    assert "SURVIVE" in text
    assert "LICENSE.md" in text
