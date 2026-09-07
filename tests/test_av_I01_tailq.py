# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_compare import g  # noqa: E402
from av_I01_tailq import PARENT_GAP, g_lo, run, tailq_I01, tailq_points  # noqa: E402
from av_I01_switch import true_I01  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")


def test_preregistration_locked():
    text = open(os.path.join(ROOT, "report", "prereg-av-I01-tailq.md"), encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text
    assert "0.002802" in text


def test_m_negative():
    assert all(m < 0.0 for m in tailq_points()["tm_at"])


def test_g_lo_below_g():
    pts = tailq_points()
    for k in range(1, 201):
        y = k / 200.0
        assert g_lo(y, pts) <= g(y) + 1e-8


def test_gap_not_worse_than_chords():
    gap = true_I01() - tailq_I01()[0]
    data = run()
    assert abs(data["gap"] - gap) < 1e-12
    assert gap <= PARENT_GAP + 1e-12
    assert data["verdict"] == "SURVIVE"


def test_note():
    text = open(os.path.join(ROOT, "notes", "av-I01-tailq.md"), encoding="utf-8").read()
    assert "Not RH" in text and "Not Weil" in text
