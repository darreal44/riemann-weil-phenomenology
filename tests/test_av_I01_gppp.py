# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# I_{[0,1]} cubic Taylor, |g'''| by lag amplitudes. Miss 1.40. Not Weil.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_gppp import (  # noqa: E402
    K_hand,
    cubic_lo,
    run,
    step_is_taken,
    th_ppp_amp,
)
from av_I01_compare import g, g_p, g_pp  # noqa: E402
from av_I01_switch import WINDOW  # noqa: E402
from av_gpp import g_ppp, th_ppp  # noqa: E402
from av_gauss import L16  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "av-I01-gppp.json")
NOTE = os.path.join(ROOT, "notes", "av-I01-gppp.md")
SRC = os.path.join(ROOT, "code", "av_I01_gppp.py")
PREREG = os.path.join(ROOT, "report", "prereg-av-I01-gppp.md")
REM = os.path.join(ROOT, "notes", "remaining-before-rh.md")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text
    assert "Not RH" in text
    assert "K :=" in text or "|g'''|" in text


def test_amp_covers_th_ppp():
    for n in range(3):
        for m in range(3):
            amp = th_ppp_amp(n, m)
            for y in (0.0, 0.2, 0.5, 1.0, L16 / 2):
                assert abs(th_ppp(n, m, y)) <= amp + 1e-9


def test_K_covers_gppp_and_cubic_below_g():
    caps = K_hand()
    K = caps["K"]
    gp0, gpp0 = g_p(0.0), g_pp(0.0)
    for i in range(21):
        y = i / 20.0
        assert abs(g_ppp(y)) <= K + 1e-9
        if y > 0:
            assert cubic_lo(y, gp0, gpp0, K) <= g(y) + 1e-8


def test_run_misses_window():
    data = json.load(open(JSON, encoding="utf-8"))
    live = run()
    assert data["verdict"] == "KILL"
    assert data["step_taken"] is False
    assert step_is_taken() is False
    assert data["gap"] > 1.0
    assert data["Q_lo"] < 0.0
    assert data["closes_window"] is False
    assert data["K_covers_sample"] is True
    assert abs(live["I_lo"] - data["I_lo"]) < 1e-6
    assert data["gap"] > WINDOW


def test_driver_and_note():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "Not Weil" in text
    assert "1.40" in text or "1.403" in text
    assert "KILL" in text
    rem = open(REM, encoding="utf-8").read()
    assert "gppp" in rem or "g'''" in rem or "cubic Taylor" in rem
