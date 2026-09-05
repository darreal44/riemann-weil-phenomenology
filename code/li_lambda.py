#!/usr/bin/env python3
"""Li coefficients λ_n from zeros + λ_1 closed form.

    python code/li_lambda.py
    python code/li_lambda.py --n 12 --zeros code/zeros_zeta_weyl.pkl

λ_n ≥ 0 ∀n ⇔ RH. A finite prefix is not a proof.
"""
from __future__ import annotations

import argparse
import math
import os
import pickle

HERE = os.path.dirname(os.path.abspath(__file__))


def lambda1_closed():
    g = 0.5772156649015328606
    return 1.0 + 0.5 * g - 0.5 * math.log(4 * math.pi)


def lam_from_zeros(n, zs):
    s = 0.0
    for t in zs:
        rho = 0.5 + 1j * t
        s += (1 - (1 - 1 / rho) ** n).real * 2
    return s


def weyl_rho(t):
    u = t / (2 * math.pi)
    if u <= 1:
        return 0.0
    return math.log(u) / math.pi


def lam_tail(n, T, T2=5000, nq=80):
    from numpy.polynomial.legendre import leggauss
    xs, ws = leggauss(nq)
    t = 0.5 * (T2 - T) * xs + 0.5 * (T2 + T)
    w = 0.5 * (T2 - T) * ws
    s = 0.0
    for ti, wi in zip(t, w):
        r = 0.5 + 1j * float(ti)
        s += 2 * ((1 - (1 - 1 / r) ** n).real) * weyl_rho(float(ti)) * float(wi)
    return s


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=8)
    p.add_argument("--zeros", default=os.path.join(HERE, "zeros_zeta_weyl.pkl"))
    args = p.parse_args()
    zs = sorted(float(x) for x in pickle.load(open(args.zeros, "rb")))
    zs = [t for t in zs if t > 1e-12]
    closed = lambda1_closed()
    T = zs[-1]
    z1 = lam_from_zeros(1, zs)
    t1 = lam_tail(1, T)
    scale = (closed - z1) / t1 if t1 else 1.0
    print(f"lambda_1 closed {closed:.12f}")
    print(f"zeros {len(zs)} T={T:.1f}  raw tail scale for lam1={scale:.3f}")
    print(f"{'n':>4} {'zeros':>10} {'tail':>10} {'raw':>10} {'scaled':>10}")
    for n in range(1, args.n + 1):
        a = lam_from_zeros(n, zs)
        b = lam_tail(n, T)
        print(f"{n:4d} {a:10.5f} {b:10.5f} {a+b:10.5f} {a+scale*b:10.5f}")
    print("scaled tail is fixed on λ1; still a finite check, not RH.")


if __name__ == "__main__":
    main()
