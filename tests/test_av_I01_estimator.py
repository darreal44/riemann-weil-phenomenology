# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_estimator import run  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")


def test_prereg():
    text = open(os.path.join(ROOT, "report", "prereg-av-I01-estimator.md"), encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text


def test_score_matches_gap():
    data = run()
    assert abs(data["sum_score"] - data["gap"]) < 1e-6
    assert data["sum_cap_int"] > 0.0
    assert data["sum_cap_int"] < data["gap"] + 1e-6
    assert data["step_taken"] is False


def test_note():
    text = open(os.path.join(ROOT, "notes", "av-I01-estimator.md"), encoding="utf-8").read()
    assert "Not RH" in text and "Not Weil" in text
