# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# LMFDB pkl vs Zenodo JSON: same label ⇒ same N, R, symmetry, Fricke.
import glob
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from lmfdb_encode import by_label_gl2  # noqa: E402
from maass_table1 import parse_label, resolve  # noqa: E402

CODE = os.path.join(os.path.dirname(__file__), "..", "code")


def test_label_encoding_level_weight_conrey():
    p = parse_label("1.0.1.2.1")
    assert p["level"] == 1 and p["weight"] == 0
    assert p["character"] == "1.1"
    assert p["m"] == 2 and p["d"] == 1
    assert p["short"] == "1.2"
    assert p["degree"] == 2
    p2 = parse_label("2.0.1.1.1")
    assert p2["level"] == 2 and p2["character"] == "2.1"
    assert p2["short"] == "2.1"
    assert resolve("1.2") == "1.0.1.2.1"
    assert resolve("2.1") == "2.0.1.1.1"
    assert resolve("1.0.1.1") == "1.0.1.1.1"
    assert resolve("maass2") == "1.0.1.2.1"


def test_pkl_character_matches_conrey_N_dot_a():
    by = by_label_gl2()
    assert by["1.0.1.2.1"]["character"] == "1.1"
    assert by["1.0.1.2.1"]["degree"] == 2
    assert by["1.0.1.2.1"]["weight"] == 0
    assert by["2.0.1.1.1"]["character"] == "2.1"
    assert by["2.0.1.1.1"]["N"] == 2
    assert by["11.0.1.1.1"]["character"] == "11.1"


def test_every_zenodo_json_matches_lmfdb_pkl():
    by = by_label_gl2()
    paths = sorted(glob.glob(os.path.join(CODE, "maass_an_*.json")))
    assert len(paths) >= 8
    for path in paths:
        rec = json.load(open(path, encoding="utf-8"))
        lab = rec["label"]
        assert lab in by, lab
        cat = by[lab]
        parsed = parse_label(lab)
        assert cat["N"] == rec["N"] == parsed["level"]
        assert abs(cat["R"] - rec["R"]) < 1e-6
        assert cat["symmetry"] == rec["symmetry"]
        assert cat["fricke"] == rec["fricke"]
        assert cat["character"] == parsed["character"]
        assert cat["degree"] == 2
        assert cat["weight"] == parsed["weight"]


def test_an_all_levels_and_zenodo_a2():
    from lmfdb_encode import load_an, load_dirichlet

    an = load_an()
    assert len(an) == 35416
    rec = json.load(open(os.path.join(CODE, "maass_an_1.0.1.1.1.json"), encoding="utf-8"))
    assert abs(float(an["1.0.1.1.1"][1]) - rec["a_n"][1]) < 1e-5
    assert "105.0.1.1.1" in an
    assert len(an["105.0.1.1.1"]) == 1000
    chi = load_dirichlet()
    assert len(chi) >= 20000
    five = next(r for r in chi if r["label"] == "5.b")
    assert five["is_primitive"] and five["modulus"] == 5
