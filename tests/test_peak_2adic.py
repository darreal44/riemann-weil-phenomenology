# Fmat 2-adic peak at Λ≥16 climbs; not a Dirac. No RH.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from peak_2adic import (  # noqa: E402
    BOMBIERI,
    INVERSE,
    MODULE,
    climbs,
    series,
    through_locked,
)

NOTE = os.path.join(os.path.dirname(__file__), "..", "notes", "2adic-peak-lamge16.md")


def test_lambda16_climbs_through_bombieri():
    s = series(16.0)
    assert len(s) >= 4
    assert climbs(s)
    assert through_locked(s)
    assert s[-1][1] > MODULE


def test_lambda24_and_32_same_gibbs_climb():
    s24 = series(24.0)
    s32 = series(32.0)
    assert climbs(s24) and climbs(s32)
    assert through_locked(s24) and through_locked(s32)
    # past the module twist at the finest 24; 32/160 already past 0.707
    assert s24[-1][1] > MODULE
    assert s32[-1][1] > MODULE
    assert s24[-1][1] < INVERSE
    assert s32[-1][1] < INVERSE


def test_note_does_not_close_the_dirac():
    text = open(NOTE, encoding="utf-8").read()
    assert "not a dirac" in text.lower()
    assert "RH; not this note" in text
    assert abs(BOMBIERI - 0.4901) < 1e-3
