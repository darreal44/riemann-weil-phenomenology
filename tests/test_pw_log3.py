# Paley–Wiener of type log 3: Galerkin is not the class. No RH.
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from log2_log3_step import interior_primes, step_is_taken as mech_step  # noqa: E402
from pw_log3 import (  # noqa: E402
    galerkin_takes_the_class,
    nested_courant,
    step_is_taken,
)
from scan_s import assemble  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
LADDER = os.path.join(ROOT, "report", "pw-log3-ladder.json")
NOTE = os.path.join(ROOT, "notes", "pw-log3.md")


def test_galerkin_does_not_take_the_class():
    assert galerkin_takes_the_class() is False
    assert step_is_taken() is False
    assert mech_step() is False
    assert interior_primes(3.0) == [2]


def test_note_does_not_claim_the_step():
    text = open(NOTE, encoding="utf-8").read()
    assert "not taken" in text
    assert "Galerkin is the wrong direction" in text
    assert "RH; not this note" in text
    assert "the step is taken" not in text.lower()


def test_locked_ladder_is_nested_and_positive():
    data = json.load(open(LADDER, encoding="utf-8"))
    assert data["step_taken"] is False
    assert data["galerkin_takes_class"] is False
    by = {}
    for r in data["rows"]:
        by.setdefault(r["name"], []).append(r["lam0"])
    for name, lams in by.items():
        assert all(x > 0 for x in lams), (name, lams)
        assert nested_courant(lams), (name, lams)
    # zeta N=9 matches sampling-floor 1.026e-7
    z9 = [r["lam0"] for r in data["rows"] if r["name"] == "zeta" and r["N"] == 9][0]
    assert abs(z9 / 1.026e-7 - 1) < 0.01


def test_chi5_mu3_two_sizes_nested_live():
    lam8, ell8, _ = assemble("chi5", 3.0, 8, 28)
    lam16, ell16, _ = assemble("chi5", 3.0, 16, 30)
    assert lam8 > 0 and lam16 > 0
    assert lam16 <= lam8 * 1.03
    assert abs(lam8 - 0.04416) < 0.001
