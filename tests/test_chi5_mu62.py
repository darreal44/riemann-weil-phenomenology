# Live assembly at mu=62 (chi5). ~25s. For the server after harvest, or alone.
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "code"))

from scan_s import assemble

# Locked 5 September 2026, N=53, dps=65.
ELL62 = 126.72
LAM62 = 9.29e-56


def test_chi5_mu62_positive_and_depth():
    lam0, ell, dt = assemble("chi5", 62.0, 52, 65)
    assert lam0 > 0
    assert abs(ell[0] - ELL62) < 1.0
    assert abs(ell[0] / 62.0 - ELL62 / 62.0) < 0.03
