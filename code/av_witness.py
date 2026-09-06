"""Rational witness v = (4, −3, 1)/√26 at χ₅ μ=16.

Origin left A(v) as a machine integral, remaining work [0, 1]
(`report/A-v-tail.md`). This module:

- reuses the elementary lag table (H2_arb.th);
- splits A(v) = CST + ½ I_{[0,1]} + ½ I_{[1,L]};
- encloses each piece in Arb balls.

    python code/av_witness.py
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from H2_arb import Arch_pair, P_pair, theta_vec, _arb  # noqa: E402


def v_rat(arb):
    s = arb(26).sqrt()
    return [arb(4) / s, -arb(3) / s, arb(1) / s]


def cst_chi5(arb, L):
    euler = arb("0.577215664901532860606512090082402431042159335939")
    return (arb(5) / arb.pi()).log() - euler - (1 - (-2 * L).exp()).log()


def integrand(v, L, s0, arb):
    F = arb(2)

    def g(y, _):
        K = 2 * ((-2 * s0 * y).exp()) / (1 - (-2 * y).exp())
        EC = (-(2 - 2 * s0) * y).exp()
        return K * (F * EC - theta_vec(v, v, y, L, arb))

    return g


def certify(dps=50):
    arb, acb, ctx = _arb()
    ctx.dps = dps
    v = v_rat(arb)
    L = arb(16).log()
    s0 = arb(1) / 4
    CST = cst_chi5(arb, L)
    g = integrand(v, L, s0, arb)
    eps = arb("1e-20")
    one = arb(1)
    I01 = acb.integral(g, eps, one).real
    I1L = acb.integral(g, one, L).real
    A_from_split = CST + I01 / 2 + I1L / 2
    A = Arch_pair(v, v, L, 5, s0, arb, acb)
    P = P_pair(v, v, 16, 5, 5, arb)
    Q = A - P
    return {
        "CST": CST,
        "I01": I01,
        "I1L": I1L,
        "A_split": A_from_split,
        "A": A,
        "P": P,
        "Q": Q,
        "L": L,
    }


if __name__ == "__main__":
    r = certify()
    for k in ("CST", "I01", "I1L", "A_split", "A", "P", "Q"):
        print(k, r[k])
