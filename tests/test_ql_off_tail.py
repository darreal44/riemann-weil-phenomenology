# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Off tail: S_k is Hankel; sections saturate; not a take. Not RH.
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_off_tail import ALPHA, HALF_PI, b1_caps, hankel_near_hs_bound  # noqa: E402
from ql_operator_bound import LOG2, LOG3, PI, w2_of, CHARS  # noqa: E402


ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "ql-off-tail.json")
NOTE = os.path.join(ROOT, "notes", "ql-off-tail.md")
SRC = os.path.join(ROOT, "code", "ql_off_tail.py")


def test_not_a_take():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "KILL"
    assert data["step_taken"] is False
    assert data["trial_slo"]["s_lo"] > 0.0
    assert data["trial_slo"]["s_lo"] < 0.01


def test_sk_is_hankel_not_one_over_kn():
    data = json.load(open(JSON, encoding="utf-8"))
    for s in data["hankel_id"]:
        assert abs(s["ratio"] - 1.0) < 1e-4
    src = open(SRC, encoding="utf-8").read()
    assert "½/(n+m)" in src or "1/2(n+m)" in src or "0.5 / (n + m)" in src
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src


def test_off_saturates_hankel_climbs():
    data = json.load(open(JSON, encoding="utf-8"))
    by = {r["dim"]: r for r in data["sections"]}
    assert abs(by[16]["off"] - 0.445) < 0.01
    assert by[64]["off"] < 0.55
    assert by[64]["off"] < HALF_PI / 2.0
    assert by[64]["hankel"] > by[16]["hankel"] + 0.1
    assert abs(by[16]["arch"] - by[16]["hankel"]) < 1e-6
    assert by[64]["B1"] < 0.45


def test_b1_sin_cap_beats_2_over_pi_not_045():
    caps = b1_caps()
    assert abs(ALPHA - LOG2 / LOG3) < 1e-15
    assert caps["theta_cap_sin"] < caps["theta_cap_2_over_pi"]
    assert abs(caps["theta_cap_sin"] - 2.0 * abs(math.sin(PI * ALPHA)) / PI) < 1e-12
    assert caps["B1_sin"] < caps["B1_thm"]
    assert caps["B1_sin"] > 0.45


def test_w2_negative_same_sign():
    assert w2_of(CHARS["chi3"]["d"]) < 0.0


def test_hankel_near_is_hs():
    cap = hankel_near_hs_bound(32, 7)
    assert 0.16 < cap < 0.17
    data = json.load(open(JSON, encoding="utf-8"))
    for r in data["sections"]:
        assert r["hank_near"] <= r["hank_near_hs_cap"] + 1e-12
        assert r["hank_near"] < 0.12


def test_dyadic_off_uniform_union_not_hartman():
    data = json.load(open(JSON, encoding="utf-8"))
    offs = [r["off"] for r in data["dyadic"]]
    assert len(offs) == 5
    assert max(offs) - min(offs) < 0.02
    assert all(0.40 < x < 0.55 for x in offs)
    u = data["union"]
    assert u["off"] < 0.60
    assert u["hankel"] > data["dyadic"][0]["hankel"]
    assert u["off"] < HALF_PI / 2.0


def test_long_tail_off_climbs_past_cran():
    data = json.load(open(JSON, encoding="utf-8"))
    longu = data["long"]
    by = {r["n1"]: r for r in longu}
    assert by[128]["off"] < 0.55
    assert by[256]["off"] > 0.60
    assert by[512]["off"] > by[256]["off"]
    assert by[512]["hankel"] > by[128]["hankel"]
    assert by[512]["theta"] < 1.0
    assert data["cross_check"]["abs_diff"] < 1e-6
    assert data["trial_slo_long"]["s_lo"] < 0.01
    assert data["verdict"] == "KILL"


def test_note_does_not_claim_rh_or_take():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "take" in text.lower()
    assert "Hankel" in text
    assert "cancelled" in text or "cancels" in text
    assert "0.719" in text or "0.72" in text
    assert "256" in text
    assert "Nehari" in text
    assert "not a theorem" in text.lower() or "Not taken" in text or "Not\ntaken" in text
