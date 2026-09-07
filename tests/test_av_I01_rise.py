# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# I_{[0,1]} mesh on convex rise. Gap from shipped a and a_lo. Not Weil.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_compare import g, gauss_on  # noqa: E402
from av_I01_mesh import N_MESH  # noqa: E402
from av_I01_rise import (  # noqa: E402
    WINDOW,
    a_lo,
    g_lo,
    rise_I01,
    rise_points,
    run,
    step_is_taken,
)
from av_I01_switch import true_I01  # noqa: E402
from av_gauss import a_integrand  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-I01-rise.md")
NOTE = os.path.join(ROOT, "notes", "av-I01-rise.md")
SRC = os.path.join(ROOT, "code", "av_I01_rise.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text
    assert "Not RH" in text
    assert "y_inf" in text or "y_min" in text
    assert "0.0053" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "g_lo" in src and "a_lo" in src
    assert "rnodes" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_rise_drops_the_floor():
    pts = rise_points()
    assert pts["ymin"] < pts["rnodes"][0] + 1e-12
    assert abs(pts["rnodes"][0] - pts["ymin"]) < 1e-12
    assert abs(pts["rnodes"][-1] - pts["yinf"]) < 1e-12
    # Mid-rise is a parabola, not the floor gmin.
    ymid = 0.5 * (pts["ymin"] + pts["yinf"])
    assert g_lo(ymid, pts) > pts["gmin"] + 1e-6
    assert abs(g_lo(1.0, pts) - pts["g1"]) < 1e-12


def test_g_lo_lies_below_shipped_g():
    pts = rise_points()
    ys = [k / 200.0 for k in range(1, 201)]
    for y in ys:
        assert g_lo(y, pts) <= g(y) + 1e-8, (y, g_lo(y, pts), g(y))


def test_gap_from_shipped_comparison_and_integrand():
    pts = rise_points()
    i_true = true_I01()
    i_lo, _pieces = rise_I01(pts)
    i_true_again = gauss_on(lambda y: a_integrand(max(y, 1e-15)), 1e-15, 1.0)
    assert abs(i_true - i_true_again) < 1e-12
    i_lo_again = gauss_on(lambda y: a_lo(max(y, 1e-15), pts), 1e-15, pts["ymin"])
    span = pts["yinf"] - pts["ymin"]
    h = span / N_MESH
    for i in range(N_MESH):
        i_lo_again += gauss_on(
            lambda y: a_lo(y, pts), pts["ymin"] + i * h, pts["ymin"] + (i + 1) * h
        )
    i_lo_again += gauss_on(lambda y: a_lo(y, pts), pts["yinf"], 1.0)
    assert abs(i_lo - i_lo_again) < 5e-4
    gap = i_true - i_lo
    data = run()
    assert abs(data["I_true"] - i_true) < 1e-12
    assert abs(data["I_lo"] - i_lo) < 1e-12
    assert abs(data["gap"] - gap) < 1e-12
    assert data["closes_window"] is (gap < WINDOW)
    assert data["gppp_negative"] is True
    assert gap < 0.0053
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False


def test_note_does_not_claim_weil_or_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "Not Weil" in text or "not Weil" in text
    assert "SURVIVE" in text
    assert "still open" in text
    assert "LICENSE.md" in text
    assert "(∀ L)" in text or "covering" in text.lower()
