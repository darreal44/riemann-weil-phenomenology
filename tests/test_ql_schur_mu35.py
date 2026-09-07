# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Schur μ=3.5, primes {2,3}. Neumann. T infinite. Not RH.
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from kronecker import kronecker  # noqa: E402
from log2_log3_step import interior_primes  # noqa: E402
from ql_operator_bound import LOG2, s0_of, w2_of  # noqa: E402
from ql_schur_mu35 import (  # noqa: E402
    HEADS,
    L,
    MU,
    Q_window,
    step_is_taken,
)
from ql_schur_tail import Q_nm  # noqa: E402
from ql_theta_tail import theta_op_bound  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-schur-mu35.md")
JSON = os.path.join(ROOT, "report", "ql-schur-mu35.json")
NOTE = os.path.join(ROOT, "notes", "ql-schur-mu35.md")
SRC = os.path.join(ROOT, "code", "ql_schur_mu35.py")


def _data():
    return json.load(open(JSON, encoding="utf-8"))


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Galerkin" in text
    assert "Not RH" in text
    assert "{2,3}" in text or "2,3" in text


def test_driver_is_not_galerkin_and_primes():
    src = open(SRC, encoding="utf-8").read()
    assert "from scan_s import assemble" not in src
    assert "ProcessPool" not in src
    assert "Q_window" in src
    assert HEADS == (2, 4, 8, 16, 20, 24)
    assert MU == 3.5
    assert interior_primes(3.0) == [2]
    assert interior_primes(3.5) == [2, 3]
    assert LOG2 >= 0.5 * L
    assert theta_op_bound(LOG2, L) == 1.0
    assert kronecker(-3, 3) == 0


def test_mu3_Q_window_matches_qnm():
    a = Q_window(0, 0, 3, s0_of(1), -3, math.log(3.0), 3.0)
    b = Q_nm(0, 0, 3, s0_of(1), w2_of(-3), math.log(3.0))
    assert abs(a - b) < 1e-14


def test_json_signs():
    data = _data()
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False
    assert step_is_taken() is False
    assert data["mu3_matches_qnm"] is True
    assert data["primes"] == [2, 3]
    g = data["grids"]
    by3 = {r["h"]: r for r in g["chi3"]}
    by5 = {r["h"]: r for r in g["chi5"]}
    by4 = {r["h"]: r for r in g["chi4"]}
    assert by3[2]["s_lo"] < 0
    assert by3[4]["s_lo"] > 0
    assert by3[8]["s_lo"] > 0.001
    assert by5[2]["s_lo"] < 0
    assert by5[4]["s_lo"] > 0.005
    assert by4[2]["s_lo"] < 0
    assert by4[4]["s_lo"] > 0.01
    snap = {r["name"]: r for r in data["snaps"]}
    assert snap["chi8"]["s_lo"] > 0.1
    assert snap["chi7"]["s_lo"] > 0.05
    assert snap["chi17"]["s_lo"] > 0.4


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "only prime 2 on (log 3, log 4)" in text
    assert "**false**" in text
    assert "(∀ L) Q_L ≥ 0" in text or "(∀ L)" in text
