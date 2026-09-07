# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Table 1 aliases, LMFDB pkl, not lexicographic 1.0.1.10.1. Not Weil.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from lmfdb_encode import by_label_gl2, load_gl2, load_gl3  # noqa: E402
from maass_table1 import ALIAS, NOT_TABLE1, TABLE1  # noqa: E402
from scan_gl2 import zeros  # noqa: E402
from scan_q_maass import load_form  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
JSON = os.path.join(ROOT, "report", "maass-table1-pair.json")
NOTE = os.path.join(ROOT, "notes", "maass-table1-pair.md")
REM = os.path.join(ROOT, "notes", "remaining-before-rh.md")
SRC_Q = os.path.join(ROOT, "code", "scan_q_maass.py")
HZ = os.path.join(ROOT, "code", "harvest_maass_zenodo.py")


def test_pkl_catalog_has_table1_and_lexicographic():
    rows = load_gl2()
    assert len(rows) == 35416
    by = by_label_gl2()
    assert abs(by["1.0.1.1.1"]["R"] - 9.533695) < 1e-5
    assert abs(by["1.0.1.2.1"]["R"] - 12.173) < 0.01
    assert by["1.0.1.10.1"]["R"] > 19.0
    assert by["1.0.1.100.1"]["R"] > 40.0
    g3 = load_gl3()
    assert len(g3) == 1532
    assert g3[0]["z1"] > 0.0


def test_alias_is_table1():
    assert ALIAS["maass2"] == "1.0.1.2.1"
    assert ALIAS["maass3"] == "1.0.1.3.1"
    assert "1.0.1.10.1" in NOT_TABLE1
    rec = load_form("maass3")
    assert rec["slug"] == "1.0.1.3.1"
    assert rec["symmetry"] == 0
    assert 13.5 < rec["R"] < 14.0


def test_gram_accepts_lmfdb_table1_label():
    z = zeros("1.0.1.2.1")
    assert abs(float(z[0]) - 5.1055) < 0.01
    z_short = zeros("1.2")
    assert abs(float(z_short[0]) - float(z[0])) < 1e-15
    z1 = zeros("maass1")
    assert abs(float(z1[0]) - 17.0249) < 0.01


def test_pair_json_and_note():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["paired"] is True
    assert data["step_taken"] is False
    assert data["verdict"] == "KILL"
    by = {r["name"]: r for r in data["rows"]}
    assert by["maass2"]["label"] == "1.0.1.2.1"
    assert by["maass3"]["even"] is False
    assert by["maass1"]["Q00"] > 1.0
    text = open(NOTE, encoding="utf-8").read()
    assert "Not Weil" in text
    assert "1.0.1.10.1" in text
    rem = open(REM, encoding="utf-8").read()
    assert "1.0.1.2.1" in rem
    src = open(SRC_Q, encoding="utf-8").read()
    assert "symmetry" in src and "> 0" in src
    hz = open(HZ, encoding="utf-8").read()
    assert "--labels" in hz
    assert "from scan_s import assemble" not in src
