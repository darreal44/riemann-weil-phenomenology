# Closed form of θ_{f₁} and positivity on [0, L]. Calculus, no zeros.
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from theta_f1 import theta_f1, g_reduced  # noqa: E402
from H_2plane_independent import frame, theta_vec  # noqa: E402
import mpmath as mp  # noqa: E402


def test_closed_form_matches_theta_vec():
    L = float(mp.log(16))
    e1, _ = frame()
    for t in (0.1, 0.25, 0.5, 0.7, 0.85, 0.95):
        y = t * L
        closed = theta_f1(y, L)
        vec = float(theta_vec(e1, e1, mp.mpf(y), mp.mpf(L)))
        assert abs(closed / vec - 1) < 1e-10, (t, closed, vec)


def test_g_nonnegative_on_unit_interval():
    # Analytic on [0, 1 − √3/(2π)]; grid on the compact remainder.
    t_star = 1.0 - math.sqrt(3.0) / (2.0 * math.pi)
    for i in range(401):
        t = t_star * i / 400
        a = (4.0 / 3.0) * (1.0 - t)
        b2 = (4.0 / 9.0) * (1.0 - t) ** 2 + 1.0 / math.pi**2
        assert a * a + 1e-15 >= b2
        assert g_reduced(t) >= -1e-12
    gmin = min(g_reduced(0.724 + 0.276 * i / 2000) for i in range(2001))
    assert gmin >= -1e-12
    assert abs(g_reduced(1.0)) < 1e-12
    assert g_reduced(0.0) > 1.9


def test_theta_f1_positive_at_prime_lags_mu16():
    L = math.log(16.0)
    prev = theta_f1(1e-9, L)
    for n in (2, 3, 4, 5, 7, 8, 11, 13):
        val = theta_f1(math.log(n), L)
        assert val > 0, (n, val)
        assert val < prev + 1e-12, (n, val, prev)
        prev = val
