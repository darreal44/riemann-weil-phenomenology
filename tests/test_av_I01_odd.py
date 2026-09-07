# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# g_lo at s0=3/4. Not a chi5-only well. Not Weil.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_compare import gauss_on  # noqa: E402
from av_I01_odd import (  # noqa: E402
    a_true,
    g,
    gp,
    gpp,
    run,
    scan_inf,
    scan_min,
    step_is_taken,
)
from av_odd_app import g_odd, w_odd  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-I01-odd.md")
NOTE = os.path.join(ROOT, "notes", "av-I01-odd.md")
SRC = os.path.join(ROOT, "code", "av_I01_odd.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "s₀=3/4" in text or "s0=3/4" in text or "3/4" in text
    assert "Not Weil" in text
    assert "artefact" in text.lower() or "artifact" in text.lower()


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "g_odd" in src and "w_odd" in src
    assert "s0" in src or "3/4" in src or "0.75" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_odd_g_is_shipped_bose_not_even():
    assert abs(g(0.5) - g_odd(0.5)) < 1e-15
    # Even Bose is e^{-3y/2}; odd is e^{-y/2}.
    assert abs(g(0.5) - (2.0 * __import__("math").exp(-0.5 * 0.5) - __import__(
        "av_gauss", fromlist=["theta_v"]
    ).theta_v(0.5))) < 1e-12
    assert w_odd(0.5) != 2.0 * __import__("math").exp(-0.5 * 0.5) / (
        1.0 - __import__("math").exp(-1.0)
    )


def test_well_verdict_from_shipped_g():
    ymin, gmin = scan_min()
    yinf = scan_inf()
    well = (
        yinf is not None
        and yinf > ymin
        and ymin < 0.9
        and gpp(0.0) > 0.0
        and gp(0.0) < 0.0
    )
    data = run()
    assert data["ok"] is well
    assert data["artefact"] is (not well)
    if well:
        assert data["verdict"] == "SURVIVE"
        assert data["glo_below_g"] is True
        i_true = gauss_on(a_true, 1e-12, 1.0)
        assert abs(data["I_true"] - i_true) < 1e-12
        assert gmin < 0.0
    else:
        assert data["verdict"] == "KILL"


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "Not Weil" in text or "not Weil" in text
    assert "LICENSE.md" in text
    assert "s0" in text.lower() or "3/4" in text or "odd" in text.lower()
