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


def test_lfunc_zeros_conjugate_and_holomorphic():
    from lmfdb_encode import (
        load_lfunc_cmf,
        load_lfunc_dirichlet,
        load_lfunc_maass,
        load_mf_newforms,
    )

    maass = load_lfunc_maass()
    gl3 = [r for r in maass if r["type"] == "MaassGL3"]
    gl2 = [r for r in maass if r["type"] == "MaassGL2"]
    assert len(gl3) == 1554
    assert gl3[0]["zeros"].size >= 1
    assert any(r.get("conjugate") for r in gl3)
    # rigor GL2 zeros are not in lfunc_lfunctions
    assert len(gl2) <= 2
    assert all(r["zeros"].size == 0 for r in gl2) or len(gl2) == 0

    dL = load_lfunc_dirichlet()
    assert len(dL) >= 3
    by_url = {r["url"]: r for r in dL}
    chi52 = by_url["Character/Dirichlet/5/2"]
    assert chi52["conjugate"] == "dirichlet_L_5.3"
    assert chi52["zeros"].size >= 100
    chi53 = by_url["Character/Dirichlet/5/3"]
    assert chi53["conjugate"] == "dirichlet_L_5.2"
    chi54 = by_url["Character/Dirichlet/5/4"]
    assert chi54["self_dual"] is True

    mf = load_mf_newforms()
    by_mf = {r["label"]: r for r in mf}
    assert by_mf["11.2.a.a"]["level"] == 11
    assert by_mf["11.2.a.a"]["weight"] == 2
    assert by_mf["1.12.a.a"]["weight"] == 12
    assert by_mf["11.2.a.a"]["is_self_dual"] is True

    cmf = load_lfunc_cmf()
    by_cmf = {r["url"]: r for r in cmf}
    rec = by_cmf["ModularForm/GL2/Q/holomorphic/11/2/a/a"]
    assert rec["zeros"].size >= 1
    assert rec["label"].startswith("2-11-")
