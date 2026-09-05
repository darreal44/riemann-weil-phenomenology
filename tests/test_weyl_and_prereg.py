# Locks the claims that would silently rot: half-density cache,
# frozen geometric coefficients, chi29 pre-reg, 2-adic taper overshoot.
import math
import os
import pickle
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "code"))

from geom_law import A, B, s_pred  # noqa: E402


def _zeros(name):
    p = os.path.join(ROOT, "code", name)
    return sorted(float(x) for x in pickle.load(open(p, "rb")))


def test_geom_coefficients_frozen():
    assert A == 1.69
    assert B == 0.82


def test_chi5_150_is_half_weyl():
    z = _zeros("zeros_chi5_150.pkl")
    T = z[-1]
    q = 5
    expected = (T / math.pi) * math.log(q * T / (2 * math.pi * math.e))
    ratio = len(z) / expected
    assert 80 < len(z) < 100
    assert 0.45 < ratio < 0.55


def test_chi29_prereg_s_pred_locked():
    z = _zeros("zeros_chi29.pkl")
    pred = s_pred(11, 22, z)
    assert abs(pred - 0.436) < 0.005


def test_chi29_measured_against_lock():
    s_hat = 0.390
    s_pred_lock = 0.436
    ratio = s_hat / s_pred_lock
    assert 0.85 < ratio < 0.95


def test_taper_still_overshoots_at_cpu160():
    # PR 13, Hann 20%, Lambda=16
    w_hard_160 = 0.594
    w_tap_160 = 0.529
    expected = math.log(2) / math.sqrt(2)
    assert w_hard_160 > expected
    assert w_tap_160 > expected
    assert w_tap_160 < w_hard_160


def test_completed_L_changes_sign_at_chi5_gamma1():
    mp = pytest.importorskip("mpmath")
    from harvest_weyl import CHARS, Lam
    from kronecker import chi_tab

    cf = CHARS["chi5"]
    tab = chi_tab(cf["d"], cf["q"])
    mp.mp.dps = 15
    g1 = 6.648453344727715
    left = Lam(mp.mpf(g1 - 0.02), cf["q"], tab, cf["a"])
    right = Lam(mp.mpf(g1 + 0.02), cf["q"], tab, cf["a"])
    assert float(left * right) < 0
