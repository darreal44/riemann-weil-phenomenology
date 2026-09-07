# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# I_{[0,1]} quadratic support near 0. Gap from shipped a and a_lo. Not Weil.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_compare import g, gauss_on  # noqa: E402
from av_I01_quad import (  # noqa: E402
    WINDOW,
    a_lo,
    g_lo,
    gppp_negative_on_well,
    q_of,
    quad_I01,
    quad_points,
    run,
    step_is_taken,
)
from av_I01_switch import true_I01  # noqa: E402
from av_gauss import a_integrand  # noqa: E402
from av_gpp import g_pp  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-I01-quad.md")
NOTE = os.path.join(ROOT, "notes", "av-I01-quad.md")
SRC = os.path.join(ROOT, "code", "av_I01_quad.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text
    assert "Not RH" in text
    assert "y_q" in text
    assert "0.068" in text
    assert "g''" in text or "g''(0)" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "g_lo" in src and "a_lo" in src
    assert "yq" in src or "y_q" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_quadratic_is_not_the_envelope_t0():
    pts = quad_points()
    assert pts["ysw"] < pts["yq"] < pts["ymin"]
    assert abs(pts["m"] - g_pp(pts["ymin"])) < 1e-12
    assert gppp_negative_on_well(pts) is True
    # On (0, y_q) the envelope used t0; this comparison uses q > t0.
    ymid = 0.5 * pts["yq"]
    assert abs(g_lo(ymid, pts) - q_of(ymid, pts)) < 1e-12
    assert g_lo(ymid, pts) > pts["gp0"] * ymid + 1e-9
    assert abs(g_lo(pts["yq"], pts) - pts["gmin"]) < 1e-9
    assert abs(g_lo(1.0, pts) - pts["g1"]) < 1e-12


def test_g_lo_lies_below_shipped_g():
    pts = quad_points()
    ys = [k / 200.0 for k in range(1, 201)]
    for y in ys:
        assert g_lo(y, pts) <= g(y) + 1e-9, (y, g_lo(y, pts), g(y))


def test_gap_from_shipped_comparison_and_integrand():
    pts = quad_points()
    i_true = true_I01()
    i1, i2, i3, i4, i_lo = quad_I01(pts)
    i_true_again = gauss_on(lambda y: a_integrand(max(y, 1e-15)), 1e-15, 1.0)
    i1b = gauss_on(lambda y: a_lo(max(y, 1e-15), pts), 1e-15, pts["yq"])
    i2b = gauss_on(lambda y: a_lo(y, pts), pts["yq"], pts["ymeet"])
    i3b = gauss_on(lambda y: a_lo(y, pts), pts["ymeet"], pts["yinf"])
    i4b = gauss_on(lambda y: a_lo(y, pts), pts["yinf"], 1.0)
    assert abs(i_true - i_true_again) < 1e-12
    assert abs(i1 - i1b) < 1e-12
    assert abs(i2 - i2b) < 1e-12
    assert abs(i3 - i3b) < 1e-12
    assert abs(i4 - i4b) < 1e-12
    gap = i_true - i_lo
    data = run()
    assert abs(data["I_true"] - i_true) < 1e-12
    assert abs(data["I_lo"] - i_lo) < 1e-12
    assert abs(data["gap"] - gap) < 1e-12
    assert data["closes_window"] is (gap < WINDOW)
    assert data["closes_window"] is False
    assert data["gppp_negative"] is True
    assert 0.02 < gap < 0.068
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
