# S_lo identified Q_pk takes W_log5 at h=16. Not Weil+. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_slo_identified import step_is_taken  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-slo-identified.md")
JSON = os.path.join(ROOT, "report", "ql-slo-identified.json")
NOTE = os.path.join(ROOT, "notes", "ql-slo-identified.md")
SRC = os.path.join(ROOT, "code", "ql_slo_identified.py")
OLD = os.path.join(ROOT, "report", "ql-schur-pk-mu5.json")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not RH" in text
    assert "gap" in text.lower() or "dead" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "run_pk" in src or "ql_schur_pk_mu5" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_json_take_not_weil():
    data = json.load(open(JSON, encoding="utf-8"))
    assert data["verdict"] == "SURVIVE"
    assert data["identified_arch"] is True
    assert data["w_log5_take"] is True
    assert data["weil_positive"] is False
    assert data["weil_negative"] is False
    by = {r["h"]: r for r in data["rows"]}
    assert by[2]["s_lo"] < 0
    assert by[4]["s_lo"] < 0
    assert by[16]["s_lo"] > 0
    assert by[24]["s_lo"] > 0
    old = json.load(open(OLD, encoding="utf-8"))
    old_by = {r["h"]: r for r in old["rows"]}
    assert abs(by[16]["s_lo"] - old_by[16]["s_lo"]) < 1e-15


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "not Weil-positive" in text
    assert "take" in text
