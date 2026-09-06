# 67a1 μ=74: quorum remains complete (journal §113). Prime-side Q. No RH.
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from gl2_curves import ap_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
QUORUM_JSON = os.path.join(ROOT, "report", "gl2-67a1-mu74-quorum.json")


def test_67a1_a2_a5_positive_a41_mute():
    ap = ap_table("67a1", 73)
    assert ap[2] == 2 and ap[5] == 2 and ap[13] == 2
    assert ap[41] == 0 and ap[71] == 0


def test_67a1_mu74_quorum_stays_complete():
    """Preregistration: 2, 5, 13 stay necessary; full Q > 0."""
    if not os.path.exists(QUORUM_JSON):
        pytest.skip("run python code/gl2_quorum_scan.py 67a1 74 80 50")
    data = json.load(open(QUORUM_JSON, encoding="utf-8"))
    assert data["label"] == "67a1" and data["mu"] == 74.0
    by = {r["drop"]: r for r in data["rows"]}
    full = by[None]
    assert full["lam0"] > 0
    assert 10 < full["ell0"] < 25
    for p in (2, 5, 13):
        assert by[p]["lam0"] < 0, (p, by[p]["lam0"])
        assert by[p]["necessary"] is True
    # mute: a_41 = a_71 = 0
    assert by[41]["lam0"] == full["lam0"]
    assert by[71]["lam0"] == full["lam0"]
