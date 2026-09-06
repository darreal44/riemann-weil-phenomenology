#!/usr/bin/env python3
"""Remainder ball for the odd integrand on [1, L], G3 treated as in the even case.

    python3 code/av_enclose_odd_ball.py
"""
from __future__ import annotations
import math
from scan_s import CHARS, chi_tab
from av_gauss import theta_v, GAUSS_NODES, GAUSS_WEIGHTS, L16
from av_enclose import trap
from av_odd_app import termwise_M

GAMMA = 0.5772156649015329


def w_odd(y):
    return 2.0 * math.exp(-1.5 * y) / (1.0 - math.exp(-2.0 * y))


def a_odd(y):
    return 0.5 * w_odd(y) * (2.0 * math.exp(-0.5 * y) - theta_v(y))


def app_fd(y, h=1e-4):
    return (a_odd(y + h) - 2.0 * a_odd(y) + a_odd(y - h)) / h / h


def max_app(A, B, n=200):
    h = (B - A) / n
    return max(abs(app_fd(A + i * h)) for i in range(1, n))


def cst(q):
    return math.log(q / math.pi) - GAMMA - math.log(1.0 - 1.0 / 256.0)


def p_of(name):
    cf = CHARS[name]
    tab = chi_tab(cf["d"], cf["q"])
    acc = 0.0
    for n in range(2, 17):
        y2, p = n, None
        for qq in (2, 3, 5, 7, 11, 13):
            if y2 % qq == 0:
                p = qq
                while y2 % qq == 0:
                    y2 //= qq
                break
        if not (p and y2 == 1):
            continue
        chi = tab[n % cf["q"]]
        if chi == 0:
            continue
        acc += chi * math.log(p) / math.sqrt(n) * theta_v(math.log(n))
    return acc


def main():
    g3 = sum(w * a_odd(x) for w, x in zip(GAUSS_WEIGHTS, GAUSS_NODES))
    t1, _ = trap(a_odd, 1.0, 1.59, 8)
    t2, _ = trap(a_odd, 1.59, L16, 8)
    M1 = max_app(1.0, 1.59)
    M2 = max_app(1.59, L16)
    h1, h2 = 0.59 / 8, (L16 - 1.59) / 8
    e1 = 8.0 * (h1 ** 3) / 12.0 * M1
    e2 = 8.0 * (h2 ** 3) / 12.0 * M2
    Ilo = g3 + t1 + t2 - e1 - e2
    Ihi = g3 + t1 + t2 + e1 + e2
    print(f"G3 odd       {g3:.9f}")
    print(f"trap[1,1.59] {t1:.9f} +/- {e1:.9f}  M={M1:.4f}")
    print(f"trap[1.59,L] {t2:.9f} +/- {e2:.9f}  M={M2:.4f}")
    print(f"I odd        [{Ilo:.6f}, {Ihi:.6f}]")
    ok = True
    print(f"{'name':<8} {'Qlo':>10} {'Qhi':>10}")
    for name in ("chi3", "chi4", "chi7"):
        c, p = cst(CHARS[name]["q"]), p_of(name)
        Qlo, Qhi = c + Ilo - p, c + Ihi - p
        print(f"{name:<8} {Qlo:10.5f} {Qhi:10.5f}")
        ok = ok and Qlo > 0

    MT1 = termwise_M(1.0, 0.7190, 0.6138, 1.4006)
    MT2 = termwise_M(1.59, 0.7222, 0.2764, 0.6516)
    et1 = 8.0 * (h1 ** 3) / 12.0 * MT1
    et2 = 8.0 * (h2 ** 3) / 12.0 * MT2
    print(f"termwise M    {MT1:.4f} {MT2:.4f}  err={et1+et2:.6f}")
    print(f"chi3 termwise Q [{cst(CHARS['chi3']['q'])+g3+t1+t2-et1-et2-p_of('chi3'):.5f}, {cst(CHARS['chi3']['q'])+g3+t1+t2+et1+et2-p_of('chi3'):.5f}]")
    print("tight odds Qlo>0", ok)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
