# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Q_pk: p^k on the prime side. μ=3 = Q_nm. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_q_pk import interior_ns, step_is_taken, wn  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-q-pk.md")
JSON = os.path.join(ROOT, "report", "ql-q-pk.json")
NOTE = os.path.join(ROOT, "notes", "ql-q-pk.md")
SRC = os.path.join(ROOT, "code", "ql_q_pk.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "n=4=2²" in text or "2²" in text


def test_interior_ns_and_w4():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert interior_ns(3.0) == [2]
    assert interior_ns(3.5) == [2, 3]
    assert interior_ns(5.0) == [2, 3, 4]
    assert abs(wn(-3, 4) - 0.34657359027997264) < 1e-12
    assert step_is_taken() is False


def test_json():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["mu3_matches_qnm"] is True
    assert data["mu35_matches_window"] is True
    assert data["H00_shift_mu5"] < -0.09
    assert data["ns5"] == [2, 3, 4]


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "−0.096" in text or "-0.096" in text
