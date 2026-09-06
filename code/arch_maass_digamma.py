#!/usr/bin/env python3
"""Maass archimedean term from digamma, compared to the recycled panel.

    python code/arch_maass_digamma.py

W(t) = Re ½ ψ(¼ + i(t±R)/2) − log π
Q_nm = ∫_0^∞ W(t) 2 φ_n(t) φ_m(t) dt/π  −  ∑ Λ_f(n) n^{-1/2} θ_nm(log n)
"""
from __future__ import annotations

import json
import math
import os
import pickle

import numpy as np
from scipy.special import digamma

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    rec = json.load(open(os.path.join(HERE, "maass_an_1.0.1.1.1.json")))
    R = float(rec["R"])
    an = {i + 1: float(a) for i, a in enumerate(rec["a_n"])}
    z = np.array(sorted(float(x) for x in pickle.load(open(os.path.join(HERE, "zeros_maass1_weyl.pkl"), "rb"))))
    z = z[z > 1e-12]
    mu, NB = 6.0, 8
    L = math.log(mu)
    om = np.array([2 * math.pi * n / L for n in range(NB + 1)])
    s = np.sin(z * L / 2)
    phi0 = 2 * s / (z * math.sqrt(L))
    G00 = float(2 * phi0 @ phi0)

    def phi(t):
        v = np.empty(NB + 1)
        if abs(t) < 1e-12:
            v[0] = math.sqrt(L)
            v[1:] = 0
            return v
        s = math.sin(t * L / 2)
        v[0] = 2 * s / (t * math.sqrt(L))
        v[1:] = math.sqrt(2 / L) * s * 2 * t / (t * t - om[1:] ** 2)
        return v

    def W(t):
        a = 0.25 + 1j * (t + R) / 2
        b = 0.25 + 1j * (t - R) / 2
        return (0.5 * digamma(a) + 0.5 * digamma(b)).real - math.log(math.pi)

    ts = np.linspace(0.0, 80.0, 2500)
    dt = ts[1] - ts[0]
    A = np.zeros((NB + 1, NB + 1))
    for t in ts:
        v = phi(t)
        A += W(t) * np.outer(v, v)
    A *= 2 * dt / math.pi

    def th(n, m, y):
        if n == 0 and m == 0:
            return 2 * (L - y) / L
        if n == 0 or m == 0:
            j = max(n, m)
            return -2 * math.sin(om[j] * y) / (math.sqrt(2) * math.pi * j)
        if n == m:
            return 2 * ((L - y) * math.cos(om[n] * y) / L - math.sin(om[n] * y) / (2 * math.pi * n))
        return 2 * (n * math.sin(om[n] * y) - m * math.sin(om[m] * y)) / (math.pi * (m * m - n * n))

    cap = int(math.exp(L) + 1e-9)
    P = np.zeros_like(A)
    for n, a in an.items():
        if n < 2 or n > cap:
            continue
        p = None
        for q in range(2, int(n**0.5) + 1):
            if n % q == 0:
                p = q
                break
        if p is None:
            p = n
        m = n
        while m % p == 0:
            m //= p
        if m != 1:
            continue
        y = math.log(n)
        w = a * math.log(p) / math.sqrt(n)
        for i in range(NB + 1):
            for j in range(i, NB + 1):
                P[i, j] += w * th(i, j, y)
                if i != j:
                    P[j, i] = P[i, j]
    Q = A - P
    ev = np.linalg.eigvalsh(Q)
    print(f"maass1 mu={mu} R={R:.4f}")
    print(f"G00={G00:.4f} A00={A[0,0]:.4f} P00={P[0,0]:.4f} Q00={Q[0,0]:.4f}")
    print(f"lam0={ev[0]:.4f}  ell0={-math.log(abs(ev[0])):.2f}")
    print(f"A already indefinite: {np.linalg.eigvalsh(A)[0]:.3f}")


if __name__ == "__main__":
    main()
