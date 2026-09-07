# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Truncated Hankel Weyl trial: cutoff error, not Hartman. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_hankel_weyl_cut import HALF_PI, N0, hankel, row_of  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "ql-hankel-weyl-cut.json")
NOTE = os.path.join(ROOT, "notes", "ql-hankel-weyl-cut.md")
SRC = os.path.join(ROOT, "code", "ql_hankel_weyl_cut.py")
REM = os.path.join(ROOT, "notes", "remaining-before-rh.md")


def _data():
    return json.load(open(JSON, encoding="utf-8"))


def test_not_a_take():
    data = _data()
    assert data["verdict"] == "KILL"
    assert data["step_taken"] is False
    assert data["n0"] == 32
    assert abs(data["half_pi"] - HALF_PI) < 1e-15


def test_tau_star_is_always_zero():
    data = _data()
    for r in data["rows"]:
        assert r["best_tau"] == 0.0
        t0 = next(t for t in r["trials"] if t["tau"] == 0.0)
        for t in r["trials"]:
            assert t["R"] <= t0["R"] + 1e-12


def test_matches_origin_window_and_grows():
    by = {r["n1"]: r for r in _data()["rows"]}
    assert abs(by[80]["sigma"] - 0.2275) < 0.001
    assert abs(by[80]["Hx"] - 0.2275) < 0.001
    assert by[512]["sigma"] > 0.60
    assert by[2048]["sigma"] > by[512]["sigma"]
    assert 0.70 < by[2048]["e_sigma"] < 0.80
    assert abs(by[2048]["sigma"] - 0.8181) < 0.001
    for r in by.values():
        assert r["R"] > 0.95 * r["sigma"]
        assert abs(r["e_sigma"] - (HALF_PI - r["sigma"])) < 1e-12


def test_fit_is_not_hartman():
    fs = _data()["fit_e_sigma"]
    fr = _data()["fit_e_R"]
    assert fs["a"] > 0.5
    assert fs["b"] > 0.5
    assert abs(fs["b"] - 0.707) < 0.01
    assert fs["r2"] > 0.85
    assert fr["b"] > 0.5
    assert fr["r2"] > 0.85


def test_recompute_small_window_and_diagonal():
    H = hankel(32, 34)
    assert abs(H[0, 0] - 0.5 / (32 + 32)) < 1e-15
    r = row_of(N0, 80)
    stored = next(x for x in _data()["rows"] if x["n1"] == 80)
    assert abs(r["sigma"] - stored["sigma"]) < 1e-10
    assert abs(r["R"] - stored["R"]) < 1e-10
    assert r["best_tau"] == 0.0
    assert r["dim"] == 48


def test_driver_and_note():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert ".csv" not in src
    assert "lmfdb" not in src.lower()
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "not a take" in text.lower() or "Not taken" in text
    assert "Hartman" in text
    assert "0.707" in text
    assert "1.081" in text
    assert "s₁≤0.8" in text or "s1<=0.8" in text or "license" in text.lower()
    assert "GL" in text
    rem = open(REM, encoding="utf-8").read()
    assert "## 8i." in rem
    assert "ql_hankel_weyl_cut" in rem
    assert "0.818" in rem or "0.753" in rem
    assert "Not RH" in rem.split("## 8i.")[1].split("## 9.")[0]
