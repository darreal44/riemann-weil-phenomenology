#!/usr/bin/env python3
"""Arithmetic enclosure of A(v) for v=(4,-3,1)/sqrt(26), chi5 mu=16.

No flint. CST + 3-point Gauss on [0,1] + 8+8 trapezoid on [1,L]
with Leibniz endpoint majorants of |a''|.

    python3 code/av_enclose.py
"""
from __future__ import annotations
import math
from av_gauss import L16, a_integrand, gauss3_unit
from av_app import w, w_p, w_pp, g
from av_gpp import g_pp


WINDOW = (-0.8303, -0.8244)
CST = math.log(5.0 / math.pi) - 0.5772156649015329 - math.log(1.0 - 1.0 / 256.0)


def trap(f, A, B, n):
    h = (B - A) / n
    xs = [A + i * h for i in range(n + 1)]
    s = 0.5 * f(xs[0]) + 0.5 * f(xs[-1]) + sum(f(x) for x in xs[1:-1])
    return s * h, xs


def termwise_M(A, B, gpp_max, gp_max, g_max):
    # envelopes of w(*) at the left end (w decreasing, |w'| decreasing)
    W = w(A)
    Wp = abs(w_p(A))
    Wpp = abs(w_pp(A))
    return 0.5 * (Wpp * g_max + 2.0 * Wp * gp_max + W * gpp_max)


def main():
    g3 = gauss3_unit(a_integrand)
    t1, xs1 = trap(a_integrand, 1.0, 1.59, 8)
    t2, xs2 = trap(a_integrand, 1.59, L16, 8)
    # endpoint-style M from app-endpoints.md
    M1 = termwise_M(1.0, 1.59, gpp_max=0.707, gp_max=0.5510, g_max=0.2229)
    M2 = termwise_M(1.59, L16, gpp_max=0.552, gp_max=0.2398, g_max=0.0564)
    h1 = 0.59 / 8
    h2 = (L16 - 1.59) / 8
    e1 = 8.0 * (h1 ** 3) / 12.0 * M1
    e2 = 8.0 * (h2 ** 3) / 12.0 * M2
    Ilo = t1 + t2 - e1 - e2
    Ihi = t1 + t2 + e1 + e2
    Alo, Ahi = CST + g3 + Ilo, CST + g3 + Ihi
    print(f"CST          {CST:.9f}")
    print(f"G3 [0,1]     {g3:.9f}")
    print(f"trap[1,1.59] {t1:.9f}  +/- {e1:.9f}  M={M1:.4f}")
    print(f"trap[1.59,L] {t2:.9f}  +/- {e2:.9f}  M={M2:.4f}")
    print(f"I[1,L]       [{Ilo:.6f}, {Ihi:.6f}]")
    print(f"A(v)         [{Alo:.6f}, {Ahi:.6f}]")
    print(f"window       [{WINDOW[0]}, {WINDOW[1]}]")
    print(f"inside window {Alo >= WINDOW[0] and Ahi <= WINDOW[1]}")
    P = p_of_v()
    print(f"P(v)         {P:.9f}")
    print(f"Q(v)         [{Alo-P:.6f}, {Ahi-P:.6f}]")
    print(f"Q lower>0    {Alo-P > 0}")
    return 0 if (Alo >= WINDOW[0] and Ahi <= WINDOW[1] and Alo-P > 0) else 1


def p_of_v():
    from av_gauss import theta_v
    import math
    acc = 0.0
    for n, p, chi in (
        (2, 2, -1), (3, 3, -1), (4, 2, 1), (7, 7, -1), (8, 2, -1),
        (9, 3, 1), (11, 11, 1), (13, 13, -1), (16, 2, 1),
    ):
        acc += chi * math.log(p) / math.sqrt(n) * theta_v(math.log(n))
    return acc


if __name__ == "__main__":
    raise SystemExit(main())
