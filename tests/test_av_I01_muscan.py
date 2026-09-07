# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_muscan import run  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")


def test_prereg():
    text = open(os.path.join(ROOT, "report", "prereg-av-I01-muscan.md"), encoding="utf-8").read()
    assert "Locked before the run" in text


def test_mu16_and_shape_change():
    rows = run()["rows"]
    assert 0.002 < rows["16"]["gap"] < 0.004
    assert rows["5"]["gap"] > rows["16"]["gap"]
    assert rows["32"]["ok"] is False


def test_note():
    text = open(os.path.join(ROOT, "notes", "av-I01-muscan.md"), encoding="utf-8").read()
    assert "Not RH" in text and "Not Weil" in text
