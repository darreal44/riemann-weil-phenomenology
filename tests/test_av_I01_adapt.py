# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# I_{[0,1]} leftover-driven adaptive mesh. Gap from shipped a and a_lo. Not Weil.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_adapt import (  # noqa: E402
    N_EXTRA,
    PARENT_GAP,
    adapt_I01,
    adapt_points,
    g_lo,
    leftover,
    run,
    step_is_taken,
)
from av_I01_compare import g, gauss_on  # noqa: E402
from av_I01_switch import WINDOW, true_I01  # noqa: E402
from av_gauss import a_integrand  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-I01-adapt.md")
NOTE = os.path.join(ROOT, "notes", "av-I01-adapt.md")
SRC = os.path.join(ROOT, "code", "av_I01_adapt.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text
    assert "Not RH" in text
    assert "leftover" in text
    assert "Kronrod" in text
    assert "0.002793" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "leftover" in src and "g_lo" in src and "a_lo" in src
    assert "Kronrod" in src or "kronrod" in src.lower() or "not Kronrod" in open(
        PREREG, encoding="utf-8"
    ).read()
    assert "from scan_s import assemble" not in src
    assert "Kronrod" in src
    assert step_is_taken() is False


def test_splits_are_leftover_driven_not_uniform():
    pts = adapt_points()
    assert pts["n_extra"] == N_EXTRA
    assert len(pts["anodes"]) == 9 + N_EXTRA
    hs = [
        pts["anodes"][i + 1] - pts["anodes"][i]
        for i in range(len(pts["anodes"]) - 1)
    ]
    assert max(hs) > min(hs) + 1e-9
    # First extra cut hits a high-leftover parent slab, not a Kronrod panel of a.
    first = pts["splits"][0]
    assert first["leftover"] > 1.0
    assert abs(leftover(first["lo"], first["hi"]) - first["leftover"]) < 1e-12


def test_g_lo_lies_below_shipped_g():
    pts = adapt_points()
    for k in range(1, 201):
        y = k / 200.0
        assert g_lo(y, pts) <= g(y) + 1e-8, (y, g_lo(y, pts), g(y))


def test_gap_from_shipped_comparison_and_integrand():
    pts = adapt_points()
    i_true = true_I01()
    i_lo, _pieces = adapt_I01(pts)
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
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False


def test_note_does_not_claim_weil_or_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "Not Weil" in text or "not Weil" in text
    assert "SURVIVE" in text
    assert "LICENSE.md" in text
    assert "(∀ L)" in text or "covering" in text.lower()
