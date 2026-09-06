# Arb enclosure of det(A−P) on the 2-plane. Verification, not a hand bound.
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

flint = pytest.importorskip("flint")
from H2_arb import H2_arb  # noqa: E402
from H_2plane_independent import H2  # noqa: E402


def test_chi5_mu16_arb_det_excludes_zero():
    r = H2_arb("chi5", 16, 40)
    det = r["det"]
    mid = float(det.mid())
    rad = float(det.rad())
    assert mid > 0, det
    assert rad < mid, (mid, rad, det)
    _, det_mp, _, _ = H2("chi5", 16, 28)
    assert abs(mid / float(det_mp) - 1) < 0.05, (mid, float(det_mp))
