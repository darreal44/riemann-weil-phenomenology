# 37a1 μ=62, retrait de 3. Preregistered journal §116.
# Executed: drop-3 stays positive (KILL). Prime-side Q, not the Gram. No RH.
import json
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from gl2_curves import ap_table  # noqa: E402
from scan_q_gl2 import an_points, assemble_pair  # noqa: E402

os.environ.setdefault("GL2_FIX", "1")

ROOT = os.path.join(os.path.dirname(__file__), "..")
QUORUM_JSON = os.path.join(ROOT, "report", "gl2-37a1-mu62-quorum.json")


def _an(cap):
    return an_points("37a1", cap)


def test_37a1_a3_is_minus_three():
    ap = ap_table("37a1", 40)
    assert ap[3] == -3
    assert ap[37] == -1  # split multiplicative; gp ellap
    assert abs(abs(ap[3]) * math.log(3) / 3 - math.log(3)) < 1e-15


def test_37a1_mu38_three_still_dispensable():
    """Control: at μ=38, ℓ≈9, 3 is still dispensable (journal +0.37)."""
    an = _an(38)
    lam_full, _, lam_drop, _ = assemble_pair(
        "37a1", 38.0, 16, 28, drop=3, an=an, parallel=False
    )
    assert lam_full > 0, lam_full
    assert 0.2 < lam_drop < 0.6, lam_drop  # journal +0.37; NB=16 gives 0.38


def test_37a1_mu62_drop3_preregistration_killed():
    """Journal §116: drop 3 → negative. Executed: λ₀(drop 3) = +0.0929."""
    if not os.path.exists(QUORUM_JSON):
        pytest.skip("run python code/gl2_quorum_scan.py 37a1 62 80 50")
    data = json.load(open(QUORUM_JSON, encoding="utf-8"))
    assert data["label"] == "37a1" and data["mu"] == 62.0
    by = {r["drop"]: r for r in data["rows"]}
    full, d3 = by[None], by[3]
    assert full["lam0"] > 0
    assert 10 < full["ell0"] < 20
    assert d3["lam0"] > 0
    assert d3["necessary"] is False
    # sequential window (NB=80, dps=50) locked 5.258e-7 and +0.0929
    assert abs(full["lam0"] - 5.258e-7) / 5.258e-7 < 0.05
    assert 0.05 < d3["lam0"] < 0.15
    # mute primes: a_17 = a_19 = 0 and 17², 19² > 62
    ap = ap_table("37a1", 20)
    assert ap[17] == 0 and ap[19] == 0
    assert by[17]["lam0"] == full["lam0"]
    assert by[19]["lam0"] == full["lam0"]
    assert by[2]["necessary"] is True
    assert by[5]["necessary"] is True


@pytest.mark.skipif(
    os.environ.get("GL2_SERVER") != "1",
    reason="NB=80 ~200s on 32 cores; GL2_SERVER=1",
)
def test_37a1_mu62_drop3_live_server():
    an = _an(62)
    lam_full, ell_full, lam_drop, _ = assemble_pair(
        "37a1", 62.0, 80, 50, drop=3, an=an
    )
    assert lam_full > 0
    assert 10 < ell_full[0] < 20
    assert lam_drop > 0


if __name__ == "__main__":
    an = _an(62)
    lam_full, ell_full, lam_drop, ell_drop = assemble_pair(
        "37a1", 62.0, 80, 50, drop=3, an=an
    )
    print("full", lam_full, ell_full[:3])
    print("drop3", lam_drop, ell_drop[:3])
    print("KILL" if lam_drop > 0 else "SURVIVE")
