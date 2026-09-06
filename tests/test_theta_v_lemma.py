# Locked numbers of lemma Theta_v.
# Usage: python3 -m pytest tests/test_theta_v_lemma.py -q
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
os.environ["RETURN_S"] = "1"

from scan_s import assemble
import numpy as np


def _v_of(S):
    N = S.rows
    M = np.array([[float(S[i, j]) for j in range(N)] for i in range(N)], float)
    ev, U = np.linalg.eigh(M)
    v = U[:, 0]
    if v[0] < 0:
        v = -v
    p2 = v * v
    return ev[0], v, 1.0 / float(np.sum(p2 * p2))


def test_chi5_mu16_two_mode():
    lam, ell, dt, S = assemble("chi5", 16.0, 8, 22)
    assert 26.5 < ell[0] < 28.0
    ev, v, ne = _v_of(S)
    assert 2.05 < ne < 2.20
    assert abs(v[0] / v[1]) > 1.0


def test_chi3_mu16_third_mode_on():
    lam, ell, dt, S = assemble("chi3", 16.0, 8, 22)
    assert 33.5 < ell[0] < 36.0
    ev, v, ne = _v_of(S)
    assert ne > 2.20
    assert abs(v[2]) > 0.15


def test_onb_form_factor_synthetic():
    # v0/|v1| = 2^{-1/2} exp(pi^2 / nll) at nll=48.47 (zeta mu=11)
    nll = 48.47
    pred = (1 / math.sqrt(2)) * math.exp(math.pi ** 2 / nll)
    assert abs(pred - 0.8668) < 0.002


def test_reduce_two_hat_smaller_than_full():
    lam, ell, dt, S = assemble("chi5", 16.0, 8, 22)
    ev2, v2, ne2 = _v_of(S)  # full
    M = np.array([[float(S[i, j]) for j in range(2)] for i in range(2)], float)
    ev, U = np.linalg.eigh(M)
    assert ev[0] > lam
    assert ev[0] > 1e-6
