# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Proved s1(Off_Q): triangle upper, ess lower kills 0.8 and 1.0. Not RH.
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_off_s1 import s1_off_q_lower, s1_off_q_upper  # noqa: E402
from ql_operator_bound import CHARS, PI, w2_of  # noqa: E402
from ql_schur_tail import HILBERT_HANKEL, r_frob_bound  # noqa: E402
from ql_theta_tail import theta_op_bound  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "ql-off-s1.json")
NOTE = os.path.join(ROOT, "notes", "ql-off-s1.md")
SRC = os.path.join(ROOT, "code", "ql_off_s1.py")
NEU = os.path.join(ROOT, "code", "ql_schur_neumann.py")


def test_upper_is_the_old_split():
    w2 = w2_of(CHARS["chi3"]["d"])
    n0 = 32
    split = (
        0.5 * HILBERT_HANKEL
        + 1.0 / (4.0 * n0)
        + r_frob_bound(n0)
        + abs(w2) * theta_op_bound()
    )
    assert abs(s1_off_q_upper(n0, w2) - split) < 1e-15


def test_lower_kills_crans_08_and_10():
    w2 = w2_of(CHARS["chi3"]["d"])
    lo = s1_off_q_lower(w2)
    assert lo > 1.0
    assert abs(lo - (0.5 * PI - abs(w2))) < 1e-12
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["cran_06_below_lower"] is True
    assert data["cran_08_below_lower"] is True
    assert data["cran_10_below_lower"] is True
    assert data["verdict"] == "KILL"
    assert data["step_taken"] is False
    assert data["upper_equals_split"] is True


def test_neumann_uses_s1_upper():
    src = open(NEU, encoding="utf-8").read()
    assert "s1_off_q_upper" in src
    assert "0.5 * HILBERT_HANKEL" not in src


def test_note_does_not_claim_take():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "not a take" in text.lower() or "Not taken" in text
    assert "1.081" in text or "π/2" in text
    assert "false" in text.lower()
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
