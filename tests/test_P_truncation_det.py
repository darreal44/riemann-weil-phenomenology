# Truncating P flips det(A−P). A hand bound that drops n>8 proves the wrong matrix.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from H_2plane_independent import H2  # noqa: E402


def test_chi5_mu16_cutoff_11_indefinite_13_spd():
    _, det11, ev11, _ = H2("chi5", 16, 24, nmax=11)
    _, det13, ev13, _ = H2("chi5", 16, 24, nmax=13)
    assert float(det11) < 0, det11
    assert float(min(ev11)) < 0, ev11
    assert float(det13) > 0, det13
    assert float(min(ev13)) > 0, ev13


def test_chi3_mu16_cutoff_8_not_enough():
    _, det8, _, _ = H2("chi3", 16, 24, nmax=8)
    _, det_full, _, _ = H2("chi3", 16, 24)
    assert float(det8) < 0, det8
    assert float(det_full) > 0, det_full
