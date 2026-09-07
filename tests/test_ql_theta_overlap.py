# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_theta_overlap import run  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")


def test_prereg():
    text = open(os.path.join(ROOT, "report", "prereg-ql-theta-overlap.md"), encoding="utf-8").read()
    assert "Locked before the run" in text


def test_sample_respects_cap():
    data = run()
    assert data["in_band"]
    assert data["bad_cap"] == 0
    assert data["verdict"] == "SURVIVE"
    assert abs(data["mean_mass_sum"] - 1.0) < 1e-3


def test_note():
    text = open(os.path.join(ROOT, "notes", "ql-theta-overlap.md"), encoding="utf-8").read()
    assert "Not RH" in text
