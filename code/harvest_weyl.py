#!/usr/bin/env python3
"""Weyl-complete zero harvest by sign change of the completed L.

Sign changes of completed Lambda. One-sided Weyl counter (gamma>0).

    python3 code/harvest_weyl.py chi5 320
    python3 code/harvest_weyl.py chi29 200

Resumes from code/zeros_{name}_weyl.pkl. Prints have/expected as it goes.
"""
from __future__ import annotations

import os
import pickle
import sys
import time

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kronecker import chi_tab  # noqa: E402

CHARS = {
    "chi3": dict(q=3, d=-3, a=1),
    "chi4": dict(q=4, d=-4, a=1),
    "chi5": dict(q=5, d=5, a=0),
    "chi7": dict(q=7, d=-7, a=1),
    "chi8": dict(q=8, d=8, a=0),
    "chi11": dict(q=11, d=-11, a=1),
    "chi12": dict(q=12, d=12, a=0),
    "chi13": dict(q=13, d=13, a=0),
    "chi15": dict(q=15, d=-15, a=1),
    "chi17": dict(q=17, d=17, a=0),
    "chi19": dict(q=19, d=-19, a=1),
    "chi21": dict(q=21, d=21, a=0),
    "chi23": dict(q=23, d=-23, a=1),
    "chi24e": dict(q=24, d=24, a=0),
    "chi24o": dict(q=24, d=-24, a=1),
    "chi29": dict(q=29, d=29, a=0),
}


def Lchi(s, q, tab):
    return q ** (-s) * mp.fsum(
        tab[r] * mp.zeta(s, mp.mpf(r) / q) for r in range(1, q) if tab[r]
    )


def Lam(t, q, tab, a):
    s = mp.mpf("0.5") + 1j * t
    return mp.re(
        (mp.mpf(q) / mp.pi) ** ((s + a) / 2)
        * mp.gamma((s + a) / 2)
        * Lchi(s, q, tab)
    )


def expected_N(T, q):
    if T <= 1:
        return 0.0
    # one-sided count (gamma > 0 only), matching the lists; the two-sided formula (T/pi)... reads 0.50 on a complete harvest
    return (T / (2 * mp.pi)) * mp.log(q * T / (2 * mp.pi * mp.e))


def path(name):
    return os.path.join(HERE, f"zeros_{name}_weyl.pkl")


def main():
    name = sys.argv[1]
    tmax = float(sys.argv[2]) if len(sys.argv) > 2 else 320.0
    step = float(sys.argv[3]) if len(sys.argv) > 3 else 0.04
    cf = CHARS[name]
    q, a = cf["q"], cf["a"]
    tab = chi_tab(cf["d"], q)
    mp.mp.dps = 22
    fn = path(name)
    Z = []
    t0_wall = time.time()
    if os.path.exists(fn):
        Z = sorted(float(x) for x in pickle.load(open(fn, "rb")))
    t = mp.mpf(Z[-1] + step) if Z else mp.mpf("0.01")
    prev = Lam(t, q, tab, a)
    print(
        f"{name}: resume t={float(t):.2f} n={len(Z)} -> {tmax} step={step}",
        flush=True,
    )
    n_last = len(Z)
    while t < tmax:
        t2 = t + step
        cur = Lam(t2, q, tab, a)
        if prev * cur < 0:
            z = float(
                mp.findroot(lambda x: Lam(x, q, tab, a), (t, t2), solver="bisect")
            )
            Z.append(z)
            pickle.dump(sorted(Z), open(fn, "wb"))
        prev, t = cur, t2
        if len(Z) >= n_last + 10 or float(t2) >= tmax:
            T = float(Z[-1]) if Z else float(t2)
            exp = float(expected_N(T, q))
            ratio = (len(Z) / exp) if exp else 0
            print(
                f"  n={len(Z)} t={float(t2):.1f} last={Z[-1] if Z else 0:.2f} "
                f"Weyl={ratio:.2f} {time.time()-t0_wall:.0f}s",
                flush=True,
            )
            n_last = len(Z)
    print(
        f"DONE {name} n={len(Z)} g1={Z[0] if Z else None} "
        f"gmax={Z[-1] if Z else 0:.1f}",
        flush=True,
    )


if __name__ == "__main__":
    main()
