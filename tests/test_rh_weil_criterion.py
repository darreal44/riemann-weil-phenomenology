# The shipped RH note states Clay's claim and does not close it.
import os

NOTE = os.path.join(os.path.dirname(__file__), "..", "notes", "rh-weil-criterion.md")
FREEZE = os.path.join(os.path.dirname(__file__), "..", "report", "FREEZE.md")


def _note():
    return open(NOTE, encoding="utf-8").read()


def test_artifact_exists():
    assert os.path.isfile(NOTE)


def test_states_clay_conclusion():
    t = _note()
    assert "Re(s) = 1/2" in t or "Re(s)=1/2" in t
    assert "negative even integer" in t


def test_covering_step_is_all_L():
    t = _note()
    assert "(∀ L > 0)(Q_L ≥ 0)" in t or "(∀ L) Q_L ≥ 0" in t
    assert "no off-line zero" in t


def test_does_not_claim_a_proof():
    t = _note().lower()
    assert "does **not** prove" in _note() or "does not prove rh" in t
    assert "missing lemma" in t or "not proved" in t


def test_does_not_relabel_finite_window_as_rh():
    t = " ".join(_note().split())
    assert "certified window" in t and "force RH" in t
    freeze = open(FREEZE, encoding="utf-8").read()
    assert "not a proof of RH" in freeze


def test_weil_equivalence_is_global():
    t = _note()
    assert "W(h) ≥ 0" in t
    assert "admissible" in t
