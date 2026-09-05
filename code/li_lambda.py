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


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=8)
    p.add_argument("--zeros", default=os.path.join(HERE, "zeros_zeta_weyl.pkl"))
    args = p.parse_args()
    zs = sorted(float(x) for x in pickle.load(open(args.zeros, "rb")))
    zs = [t for t in zs if t > 1e-12]
    print(f"lambda_1 closed {lambda1_closed():.12f}")
    print(f"zeros {len(zs)} T={zs[-1]:.1f}")
    print(f"{'n':>4} {'lam_zeros':>14}")
    for n in range(1, args.n + 1):
        print(f"{n:4d} {lam_from_zeros(n, zs):14.6f}")
    print("finite list ⇒ underestimate; tail >0 under RH.")


if __name__ == "__main__":
    main()
