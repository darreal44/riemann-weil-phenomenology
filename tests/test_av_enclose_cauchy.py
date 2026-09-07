# Gauss+Cauchy enclose on [0,1] and [1,L]. No trap. Not RH.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-enclose-cauchy-tail.md")
JSON = os.path.join(ROOT, "report", "av-enclose-cauchy-tail.json")
NOTE = os.path.join(ROOT, "notes", "av-enclose-cauchy-tail.md")
SRC = os.path.join(ROOT, "code", "av_enclose_cauchy.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the rewrite" in text or "Locked before" in text
    assert "No trapezoid" in text
    assert "Not RH" in text


def test_driver_has_no_trap():
    src = open(SRC, encoding="utf-8").read()
    assert "gauss3_panels" in src
    assert "gpp_max" not in src
    assert "trap(" not in src


def test_even_and_odd_survive():
    data = json.load(open(JSON, encoding="utf-8"))
    ev, od = data["even"], data["odd"]
    assert ev["inside_window"] is True
    assert ev["Qlo_pos"] is True
    assert ev["R1L"] < ev["R01"]
    assert ev["R1L"] < 2e-5
    assert ev["Qlo"] > 0.005
    assert od["chi3_pos"] is True
    assert od["chi"]["chi3"]["Qlo"] > 0.005
    assert od["R1L"] < od["R01"]


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read()
    assert "Not RH" in text
    assert "SURVIVE" in text
    assert "No trap" in text or "no trap" in text.lower()
