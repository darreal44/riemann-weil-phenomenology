"""Arb enclosure of the raised-cosine 2-plane H = A − P.

Same finite explicit formula as H_2plane_independent.H2 (no zeros).
python-flint required. A ball that excludes 0 is a verification that
det(A−P)>0 on that window, not a hand estimate that keeps every n.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kronecker import chi_tab  # noqa: E402

CHARS = {
    "chi5": (5, 5, 0),
    "chi3": (-3, 3, 1),
    "chi4": (-4, 4, 1),
    "chi8": (8, 8, 0),
    "chi13": (13, 13, 0),
}


def _arb():
    from flint import arb, acb, ctx

    return arb, acb, ctx


def th(n, m, y, L, arb):
    def om(k):
        return 2 * arb.pi() * k / L

    if n == 0 and m == 0:
        return 2 * (L - y) / L
    if n == 0 or m == 0:
        j = max(n, m)
        return -2 * (om(j) * y).sin() / (arb(2).sqrt() * arb.pi() * j)
    if n == m:
        return 2 * ((L - y) * (om(n) * y).cos() / L - (om(n) * y).sin() / (2 * arb.pi() * n))
    return 2 * (n * (om(n) * y).sin() - m * (om(m) * y).sin()) / (arb.pi() * (m * m - n * n))


def frame(arb):
    s3, s15 = arb(3).sqrt(), arb(15).sqrt()
    e1 = [arb(2).sqrt() / s3, -arb(1) / s3, arb(0)]
    e2 = [-arb(2).sqrt() / s15, -arb(2) / s15, arb(3) / s15]
    return e1, e2


def theta_vec(e, f, y, L, arb):
    acc = arb(0)
    for n in range(3):
        for m in range(3):
            acc += e[n] * f[m] * th(n, m, y, L, arb)
    return acc


def F0_vec(e, f, arb):
    acc = arb(0)
    for n in range(3):
        for m in range(3):
            if n == m:
                acc += e[n] * f[m] * arb(2)
    return acc


def Arch_pair(e, f, L, q, s0, arb, acb):
    F = F0_vec(e, f, arb)
    euler = arb("0.577215664901532860606512090082402431042159335939")
    CST = (arb(q) / arb.pi()).log() - euler - (1 - (-2 * L).exp()).log()
    eps = arb("1e-20")

    def g(y, _):
        K = 2 * ((-2 * s0 * y).exp()) / (1 - (-2 * y).exp())
        EC = (-(2 - 2 * s0) * y).exp()
        return K * (F * EC - theta_vec(e, f, y, L, arb))

    I = acb.integral(g, eps, L).real
    return F / 2 * CST + I / 2


def P_pair(e, f, mu, d, q, arb):
    L = arb(mu).log()
    tab = chi_tab(d, q)
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    acc = arb(0)
    for n in range(2, int(mu) + 1):
        y2, p = n, None
        for qq in small:
            if y2 % qq == 0:
                p = qq
                while y2 % qq == 0:
                    y2 //= qq
                break
        if not (p and y2 == 1 and tab[n % q] != 0):
            continue
        w = arb(tab[n % q]) * arb(p).log() / arb(n).sqrt()
        acc += w * theta_vec(e, f, arb(n).log(), L, arb)
    return acc


def H2_arb(name, mu=16, dps=40):
    arb, acb, ctx = _arb()
    ctx.dps = dps
    d, q, a = CHARS[name]
    L = arb(mu).log()
    s0 = arb(1) / 4 + arb(a) / 2
    e1, e2 = frame(arb)
    entries = {}
    for i, ei in enumerate((e1, e2)):
        for j, ej in enumerate((e1, e2)):
            A = Arch_pair(ei, ej, L, q, s0, arb, acb)
            P = P_pair(ei, ej, mu, d, q, arb)
            entries[(i, j)] = A - P
    H11, H12, H22 = entries[(0, 0)], entries[(0, 1)], entries[(1, 1)]
    det = H11 * H22 - H12 * H12
    tr = H11 + H22
    return {
        "H11": H11,
        "H12": H12,
        "H22": H22,
        "det": det,
        "tr": tr,
        "lmin_bound": det / tr,
    }


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "chi5"
    r = H2_arb(name)
    print(name, "det", r["det"], "lmin", r["lmin_bound"])
