# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# I_{[0,1]} uniform N=8 rate test. Gap from shipped a and a_lo. Not Weil.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_compare import g, gauss_on  # noqa: E402
from av_I01_n8 import (  # noqa: E402
    N8,
    PARENT_CAP,
    PARENT_GAP,
    g_lo,
    n8_I01,
    n8_points,
    run,
    step_is_taken,
)
from av_I01_switch import WINDOW, true_I01  # noqa: E402
from av_gauss import a_integrand  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-I01-n8.md")
NOTE = os.path.join(ROOT, "notes", "av-I01-n8.md")
SRC = os.path.join(ROOT, "code", "av_I01_n8.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text
    assert "Not RH" in text
    assert "N=8" in text
    assert "0.00279" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "g_lo" in src and "a_lo" in src
    assert "N8" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_mesh_is_uniform_n8_not_adaptive():
    pts = n8_points()
    assert pts["n8"] == N8
    assert len(pts["wnodes"]) == N8 + 1
    assert len(pts["r8"]) == N8 + 1
    assert abs(pts["wnodes"][-1] - pts["ymin"]) < 1e-12
    assert abs(pts["r8"][0] - pts["ymin"]) < 1e-12
    assert abs(pts["r8"][-1] - pts["yinf"]) < 1e-12
    hw = [pts["wnodes"][i + 1] - pts["wnodes"][i] for i in range(N8)]
    assert max(hw) - min(hw) < 1e-12


def test_g_lo_lies_below_shipped_g():
    pts = n8_points()
    for k in range(1, 201):
        y = k / 200.0
        assert g_lo(y, pts) <= g(y) + 1e-8, (y, g_lo(y, pts), g(y))


def test_gap_from_shipped_comparison_and_integrand():
    pts = n8_points()
    i_true = true_I01()
    i_lo, _pieces = n8_I01(pts)
    i_true_again = gauss_on(lambda y: a_integrand(max(y, 1e-15)), 1e-15, 1.0)
    assert abs(i_true - i_true_again) < 1e-12
    gap = i_true - i_lo
    data = run()
    assert abs(data["I_true"] - i_true) < 1e-12
    assert abs(data["I_lo"] - i_lo) < 1e-12
    assert abs(data["gap"] - gap) < 1e-12
    assert data["closes_window"] is (gap < WINDOW)
    assert data["gppp_negative"] is True
    assert gap < PARENT_GAP
    assert data["cap_ratio"] <= 0.5 + 1e-12
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False
    assert pts["cap"] < PARENT_CAP


def test_note_does_not_claim_weil_or_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "Not Weil" in text or "not Weil" in text
    assert "SURVIVE" in text
    assert "LICENSE.md" in text
    assert "(∀ L)" in text or "covering" in text.lower()
