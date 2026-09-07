# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# I_{[0,1]} three-tangent envelope. Gap from shipped a and a_lo. Not Weil.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_compare import g, gauss_on  # noqa: E402
from av_I01_envelope import (  # noqa: E402
    WINDOW,
    a_lo,
    envelope_I01,
    envelope_points,
    g_lo,
    run,
    step_is_taken,
)
from av_I01_switch import true_I01  # noqa: E402
from av_gauss import a_integrand  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-I01-envelope.md")
NOTE = os.path.join(ROOT, "notes", "av-I01-envelope.md")
SRC = os.path.join(ROOT, "code", "av_I01_envelope.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text
    assert "Not RH" in text
    assert "y_meet" in text
    assert "0.088" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "g_lo" in src and "a_lo" in src
    assert "ymeet" in src or "y_meet" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_envelope_is_not_the_switch():
    pts = envelope_points()
    assert pts["ymin"] < pts["ymeet"] < pts["yinf"]
    # On (y_meet, y_inf) the switch keeps the floor; the envelope uses tinf.
    ymid = 0.5 * (pts["ymeet"] + pts["yinf"])
    tinf = pts["ginf"] + pts["gpinf"] * (ymid - pts["yinf"])
    assert abs(g_lo(ymid, pts) - tinf) < 1e-12
    assert g_lo(ymid, pts) > pts["gmin"] + 1e-9
    assert abs(g_lo(pts["ymeet"], pts) - pts["gmin"]) < 1e-9
    assert abs(g_lo(pts["ysw"], pts) - pts["gmin"]) < 1e-9
    assert abs(g_lo(0.05, pts) - pts["gp0"] * 0.05) < 1e-12
    assert abs(g_lo(1.0, pts) - pts["g1"]) < 1e-12


def test_g_lo_lies_below_shipped_g():
    pts = envelope_points()
    ys = [k / 200.0 for k in range(1, 201)]
    for y in ys:
        assert g_lo(y, pts) <= g(y) + 1e-9, (y, g_lo(y, pts), g(y))


def test_gap_from_shipped_comparison_and_integrand():
    pts = envelope_points()
    i_true = true_I01()
    i1, i2, i3, i4, i_lo = envelope_I01(pts)
    i_true_again = gauss_on(lambda y: a_integrand(max(y, 1e-15)), 1e-15, 1.0)
    i1b = gauss_on(lambda y: a_lo(max(y, 1e-15), pts), 1e-15, pts["ysw"])
    i2b = gauss_on(lambda y: a_lo(y, pts), pts["ysw"], pts["ymeet"])
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
    assert 0.02 < gap < 0.08
    assert gap >= WINDOW
    assert gap < 0.088
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
