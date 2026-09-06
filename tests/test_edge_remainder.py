# Edge remainder R = ell − (−2 ln|ψ(0)|) is O(1) on a cheap window. Not the lemma.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from scan_s import assemble  # noqa: E402
from schur_head import mp_to_numpy  # noqa: E402
from edge_from_S import from_Q  # noqa: E402


def test_chi13_mu16_edge_carries_the_depth():
    os.environ["RETURN_S"] = "1"
    try:
        out = assemble("chi13", 16.0, 12, 28)
    finally:
        os.environ.pop("RETURN_S", None)
    rec = from_Q(mp_to_numpy(out[3]), 16.0)
    assert rec["lam0"] > 0
    assert rec["ell"] > 4
    ratio = rec["edge"] / rec["ell"]
    assert 0.70 < ratio < 1.15, rec
    assert abs(rec["R"]) < 6.0, rec
