# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""SVD of Hilbert–Hankel sections stays below π and grows with N."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_hankel_aak import spectrum  # noqa: E402

PI = math.pi


def test_sigma_max_below_pi():
    r = spectrum(2, 64)
    assert r["s0"] < PI
    assert r["s0"] > 1.0


def test_section_grows_toward_pi():
    a = spectrum(2, 32)["s0"]
    b = spectrum(2, 128)["s0"]
    assert b > a
    assert b < PI


def test_larger_head_smaller_sigma():
    lo = spectrum(2, 64)["s0"]
    hi = spectrum(24, 64)["s0"]
    assert hi < lo
