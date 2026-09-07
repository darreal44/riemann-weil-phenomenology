# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# I_{[0,1]} tangent/floor switch. Gap from shipped a and a_lo. Not RH.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_compare import g, gauss_on  # noqa: E402
from av_I01_switch import (  # noqa: E402
    WINDOW,
    a_lo,
    critical_points,
    g_lo,
    run,
    step_is_taken,
    switch_I01,
    true_I01,
)
from av_gauss import a_integrand  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-I01-switch.md")
NOTE = os.path.join(ROOT, "notes", "av-I01-switch.md")
SRC = os.path.join(ROOT, "code", "av_I01_switch.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "y_sw" in text
    assert "parent 3-piece" in text or "y_min" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "g_lo" in src and "a_lo" in src
    assert "ysw" in src or "y_sw" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_switch_is_not_parent_tangent_until_ymin():
    pts = critical_points()
    assert pts["ysw"] < pts["ymin"] < pts["yinf"] < 1.0
    assert abs(pts["ysw"] - pts["gmin"] / pts["gp0"]) < 1e-12
    # On (y_sw, y_min) the parent keeps the tangent; the switch uses the floor.
    ymid = 0.5 * (pts["ysw"] + pts["ymin"])
    assert abs(g_lo(ymid, pts) - pts["gmin"]) < 1e-12
    assert g_lo(ymid, pts) > pts["gp0"] * ymid + 1e-9
    assert abs(g_lo(pts["ysw"], pts) - pts["gmin"]) < 1e-9
    assert abs(g_lo(0.05, pts) - pts["gp0"] * 0.05) < 1e-12
    assert abs(g_lo(1.0, pts) - pts["g1"]) < 1e-12


def test_g_lo_lies_below_shipped_g():
    pts = critical_points()
    ys = [k / 200.0 for k in range(1, 201)]
    for y in ys:
        assert g_lo(y, pts) <= g(y) + 1e-9, (y, g_lo(y, pts), g(y))


def test_gap_from_shipped_comparison_and_integrand():
    pts = critical_points()
    i_true = true_I01()
    i1, i2, i3, i_lo = switch_I01(pts)
    # Same shipped a, recomputed, not a hardcoded −0.70065 oracle.
    i_true_again = gauss_on(lambda y: a_integrand(max(y, 1e-15)), 1e-15, 1.0)
    # a_lo jumps at y_inf; integrate the three pieces, not one panel.
    i1b = gauss_on(lambda y: a_lo(max(y, 1e-15), pts), 1e-15, pts["ysw"])
    i2b = gauss_on(lambda y: a_lo(y, pts), pts["ysw"], pts["yinf"])
    i3b = gauss_on(lambda y: a_lo(y, pts), pts["yinf"], 1.0)
    assert abs(i_true - i_true_again) < 1e-12
    assert abs(i1 - i1b) < 1e-12
    assert abs(i2 - i2b) < 1e-12
    assert abs(i3 - i3b) < 1e-12
    gap = i_true - i_lo
    data = run()
    assert abs(data["I_true"] - i_true) < 1e-12
    assert abs(data["I_lo"] - i_lo) < 1e-12
    assert abs(data["gap"] - gap) < 1e-12
    assert data["closes_window"] is (gap < WINDOW)
    assert data["closes_window"] is False
    assert 0.05 < gap < 0.15
    assert gap >= WINDOW
    assert gap < 0.20
    assert data["Q_lo"] < 0.0
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "still open" in text
    assert "LICENSE.md" in text
    assert "covering" in text.lower() or "(∀ L)" in text or "(forall L)" in text.lower()
