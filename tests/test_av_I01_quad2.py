# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# I_{[0,1]} two-piece quadratic. Gap from shipped a and a_lo. Not Weil.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_compare import g, gauss_on  # noqa: E402
from av_I01_quad import gppp_negative_on_well  # noqa: E402
from av_I01_quad2 import (  # noqa: E402
    WINDOW,
    a_lo,
    g_lo,
    q1_of,
    q2_of,
    run,
    split_I01,
    split_points,
    step_is_taken,
)
from av_I01_switch import true_I01  # noqa: E402
from av_gauss import a_integrand  # noqa: E402
from av_gpp import g_pp  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-I01-quad2.md")
NOTE = os.path.join(ROOT, "notes", "av-I01-quad2.md")
SRC = os.path.join(ROOT, "code", "av_I01_quad2.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text
    assert "Not RH" in text
    assert "y_h" in text and "y_q" in text
    assert "0.047" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "g_lo" in src and "a_lo" in src
    assert "yh" in src or "y_h" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_split_is_not_single_m_quadratic():
    pts = split_points()
    assert abs(pts["yh"] - 0.5 * pts["ymin"]) < 1e-12
    assert pts["yh"] < pts["yq"] < pts["ymin"]
    assert pts["m1"] > pts["m2"] > 0.0
    assert abs(pts["m1"] - g_pp(pts["yh"])) < 1e-12
    assert abs(pts["m2"] - g_pp(pts["ymin"])) < 1e-12
    assert gppp_negative_on_well(pts) is True
    ymid = 0.5 * pts["yh"]
    assert abs(g_lo(ymid, pts) - q1_of(ymid, pts)) < 1e-12
    # First piece uses m1 > m2, so q1 sits above the single-m quadratic.
    single = pts["gp0"] * ymid + 0.5 * pts["m2"] * ymid * ymid
    assert g_lo(ymid, pts) > single + 1e-9
    y2 = 0.5 * (pts["yh"] + pts["yq"])
    assert abs(g_lo(y2, pts) - q2_of(y2, pts)) < 1e-12
    assert abs(g_lo(pts["yq"], pts) - pts["gmin"]) < 1e-8
    assert abs(g_lo(1.0, pts) - pts["g1"]) < 1e-12


def test_g_lo_lies_below_shipped_g():
    pts = split_points()
    ys = [k / 200.0 for k in range(1, 201)]
    for y in ys:
        assert g_lo(y, pts) <= g(y) + 1e-9, (y, g_lo(y, pts), g(y))


def test_gap_from_shipped_comparison_and_integrand():
    pts = split_points()
    i_true = true_I01()
    i1, i2, i3, i4, i5, i_lo = split_I01(pts)
    i_true_again = gauss_on(lambda y: a_integrand(max(y, 1e-15)), 1e-15, 1.0)
    i1b = gauss_on(lambda y: a_lo(max(y, 1e-15), pts), 1e-15, pts["yh"])
    i2b = gauss_on(lambda y: a_lo(y, pts), pts["yh"], pts["yq"])
    i3b = gauss_on(lambda y: a_lo(y, pts), pts["yq"], pts["ymeet"])
    i4b = gauss_on(lambda y: a_lo(y, pts), pts["ymeet"], pts["yinf"])
    i5b = gauss_on(lambda y: a_lo(y, pts), pts["yinf"], 1.0)
    assert abs(i_true - i_true_again) < 1e-12
    assert abs(i1 - i1b) < 1e-12
    assert abs(i2 - i2b) < 1e-12
    assert abs(i3 - i3b) < 1e-12
    assert abs(i4 - i4b) < 1e-12
    assert abs(i5 - i5b) < 1e-12
    gap = i_true - i_lo
    data = run()
    assert abs(data["I_true"] - i_true) < 1e-12
    assert abs(data["I_lo"] - i_lo) < 1e-12
    assert abs(data["gap"] - gap) < 1e-12
    assert data["closes_window"] is False
    assert data["gppp_negative"] is True
    assert 0.01 < gap < 0.047
    assert gap >= WINDOW
    assert data["Q_lo"] < 0.0
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
