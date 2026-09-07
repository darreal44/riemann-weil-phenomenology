# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# CST 4-plane vs 2 m_Q(ω_n). Signs disagree. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_arch_4plane import step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-arch-4plane.md")
JSON = os.path.join(ROOT, "report", "ql-arch-4plane.json")
NOTE = os.path.join(ROOT, "notes", "ql-arch-4plane.md")
SRC = os.path.join(ROOT, "code", "ql_arch_4plane.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "Hybrid λ_min(H₄)<0" in text or "hybrid" in text.lower()


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "m_arch" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_json_signs_disagree():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["identified"] is False
    assert data["signs_agree"] is False
    assert data["lam_CST_pk"] > 0
    assert data["lam_hybrid_pk"] < 0
    assert data["gaps"][0] < -0.5


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "disagree" in text
