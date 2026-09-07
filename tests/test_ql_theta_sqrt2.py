# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# ‖Θ‖ ≤ √2 on [L/4, L/2). Not RH.
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_theta_sqrt2 import SQRT2, step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-theta-sqrt2.md")
JSON = os.path.join(ROOT, "report", "ql-theta-sqrt2.json")
NOTE = os.path.join(ROOT, "notes", "ql-theta-sqrt2.md")
SRC = os.path.join(ROOT, "code", "ql_theta_sqrt2.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "√2" in text or "sqrt" in text.lower()


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "in_sqrt2_band" in src
    assert "theta_op_cap" in src
    assert "mass_majorant" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_json_lemma_and_slo():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["lemma_holds"] is True
    assert data["in_band"] is True
    assert data["mass_majorant_ok"] is True
    assert data["t_atoms_sqrt2"] < data["t_atoms_cap2"]
    for row in data["theta_norms"]:
        assert row["op"] <= SQRT2 + 1e-9
    assert data["theta_norms"][-1]["op"] > 1.41
    by = {r["h"]: r for r in data["rows"]}
    assert by[16]["s_lo"] > 0
    assert by[24]["s_lo"] > 0
    assert by[8]["s_lo"] < 0
    assert by[16]["s_lo"] >= data["s_lo16_cap2"] - 1e-15


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "do not take" in text.replace("\n", " ")
    assert "√2" in text
