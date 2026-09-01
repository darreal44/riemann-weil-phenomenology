# Cheap identities used by the (0,0) audit. No Q assembly.
import math
import mpmath as mp


def test_hat0_square_matches_4_over_L():
    L = math.log(11.0)
    g = 14.134725141734693
    hat = 2 * math.sin(g * L / 2) / (g * math.sqrt(L))
    two_hat2 = 2 * hat * hat
    pref = (4 / L) * (1 - math.cos(g * L)) / (g * g)
    assert abs(two_hat2 / pref - 1) < 1e-12


def test_pole_closed_form_mu11():
    mp.mp.dps = 30
    L = mp.log(11)
    cf = 32 * mp.sinh(L / 4) ** 2 / L
    num = mp.quad(lambda y: 2 * (L - y) / L * (mp.e ** (y / 2) + mp.e ** (-y / 2)), [0, L])
    assert abs(cf - num) < mp.mpf('1e-18')


def test_C_formula_mu9_within_15pct():
    C9 = 0.1036
    pred = math.log(3) / (4 * 3)
    assert abs(C9 / pred - 1) < 0.15
