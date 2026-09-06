#!/usr/bin/env python3
"""Leibniz a_odd'' and termwise M on [1, L].

    a = 1/2 w g,  w = 2 e^{-3y/2}/(1-e^{-2y}),  g = 2 e^{-y/2}-θ_v
    g'' = (1/2) e^{-y/2} − θ_v''
"""
from __future__ import annotations
import math
from av_gauss import theta_v, L16
from av_gpp import theta_v_pp


def w_odd(y):
    return 2.0 * math.exp(-1.5 * y) / (1.0 - math.exp(-2.0 * y))


def w_odd_p(y):
    e = math.exp(-2.0 * y)
    return w_odd(y) * (-1.5 - 2.0 * e / (1.0 - e))


def w_odd_pp(y):
    e = math.exp(-2.0 * y)
    al = 2.0 * math.exp(-1.5 * y)
    be = 1.0 / (1.0 - e)
    ap = -1.5 * al
    app = 2.25 * al
    bp = -2.0 * e / (1.0 - e) ** 2
    bpp = 4.0 * e / (1.0 - e) ** 2 + 8.0 * e ** 2 / (1.0 - e) ** 3
    return app * be + 2.0 * ap * bp + al * bpp


def g_odd(y):
    return 2.0 * math.exp(-0.5 * y) - theta_v(y)


def g_odd_pp(y):
    return 0.5 * math.exp(-0.5 * y) - theta_v_pp(y)


def termwise_M(A, g_max, gp_max, gpp_max):
    return 0.5 * (
        abs(w_odd_pp(A)) * g_max
        + 2.0 * abs(w_odd_p(A)) * gp_max
        + w_odd(A) * gpp_max
    )
