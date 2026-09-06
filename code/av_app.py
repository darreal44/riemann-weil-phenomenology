#!/usr/bin/env python3
"""a = (1/2) w g and a'' by Leibniz.

    w = 2 e^{-y/2} / (1 - e^{-2y})
    a'' = (1/2) (w'' g + 2 w' g' + w g'')
"""
from __future__ import annotations
import math
from av_gauss import theta_v, L16
from av_gpp import g_pp


def w(y):
    return 2.0 * math.exp(-0.5 * y) / (1.0 - math.exp(-2.0 * y))


def w_p(y):
    e = math.exp(-2.0 * y)
    return w(y) * (-0.5 - 2.0 * e / (1.0 - e))


def w_pp(y):
    e = math.exp(-2.0 * y)
    al = 2.0 * math.exp(-0.5 * y)
    be = 1.0 / (1.0 - e)
    ap = -0.5 * al
    app = 0.25 * al
    bp = -2.0 * e / (1.0 - e) ** 2
    bpp = 4.0 * e / (1.0 - e) ** 2 + 8.0 * e ** 2 / (1.0 - e) ** 3
    return app * be + 2.0 * ap * bp + al * bpp


def g(y):
    return 2.0 * math.exp(-1.5 * y) - theta_v(y)


def a_pp(y, gp):
    return 0.5 * (w_pp(y) * g(y) + 2.0 * w_p(y) * gp + w(y) * g_pp(y))
