#!/usr/bin/env python3
"""Linearised mass of block(2) on the archimedean compression.

    Fmat <- block(2) only
    A    <- P F_infty P
    tau  <- lambda^{-1/2} (cross terms)
    m    <- int_{window at 2} tau d*lambda

Preregistered: if m freezes, kappa = m * 2 * sqrt(2);
kappa=4 -> module 1/sqrt(2); kappa=8 -> inverse sqrt(2).
Not RH.

    python code/kappa_block2.py 4 32          # sandbox smoke
    python code/kappa_block2.py 16 80         # server
    python code/kappa_block2.py 16 160
    python code/kappa_block2.py 16 400
"""
from __future__ import annotations

import math
import os
import sys
import time

import numpy as np
from scipy.special import sici


def Si(x):
    return sici(x)[0]


def block(ein, eout, s):
    a, b = ein[:-1], ein[1:]
    c, d = eout[:-1], eout[1:]
    dc = (d - c)[:, None]
    k = 2 * np.pi * s

    def G(x):
        xa = k * x[:, None] * a[None, :]
        xb = k * x[:, None] * b[None, :]
        return (Si(xb) - Si(xa)) / (np.pi * s)

    return (G(d) - G(c)) / dc


def probe(Lam: float, cpu: int, half: float = 0.12) -> dict:
    t0 = time.time()
    lams = np.concatenate(
        [
            np.linspace(1.50, 1.80, 31),
            np.linspace(1.81, 2.20, 81),
            np.linspace(2.21, 2.60, 31),
        ]
    )
    R = Lam * float(lams.max()) * 1.02
    N_in = int(Lam * cpu)
    hc = Lam / N_in
    ein = np.linspace(0.0, Lam, N_in + 1)
    N_out = int(np.ceil(R / hc))
    eout = np.linspace(0.0, N_out * hc, N_out + 1)
    Finf = block(ein, eout, 1.0)
    B2 = block(ein, eout, 2.0)
    A = 0.5 * (Finf[:N_in, :N_in] + Finf[:N_in, :N_in].T)
    # linear cross: W = B2 @ A + Finf @ (P B2 P)
    PB2P = 0.5 * (B2[:N_in, :N_in] + B2[:N_in, :N_in].T)
    # Delta F carries +1/2 B2; cross terms with that factor.
    W = 0.5 * (B2.dot(A) + Finf.dot(PB2P))
    xin = 0.5 * (ein[:-1] + ein[1:])
    tau = np.empty(len(lams))
    for k, lam in enumerate(lams):
        idx = np.clip(np.floor(xin / lam / hc).astype(int), 0, N_out - 1)
        tau[k] = lam ** -0.5 * np.sum(W[idx, np.arange(N_in)])
    m = np.abs(lams - 2.0) < half * 2.0
    mass = float(np.trapezoid(tau[m] / lams[m], lams[m]))
    kappa = mass * 2.0 * math.sqrt(2.0)
    return {
        "Lam": Lam,
        "cpu": cpu,
        "N_in": N_in,
        "N_out": N_out,
        "sec": round(time.time() - t0, 2),
        "mass": mass,
        "kappa": kappa,
        "target4": abs(kappa - 4.0),
        "target8": abs(kappa - 8.0),
    }


def main() -> None:
    Lam = float(sys.argv[1]) if len(sys.argv) > 1 else 4.0
    cpu = int(sys.argv[2]) if len(sys.argv) > 2 else 32
    row = probe(Lam, cpu)
    print(
        f"Lam={row['Lam']} cpu={row['cpu']}  "
        f"N={row['N_in']}x{row['N_out']}  "
        f"m={row['mass']:+.4f}  kappa={row['kappa']:+.3f}  "
        f"|k-4|={row['target4']:.3f} |k-8|={row['target8']:.3f}  "
        f"{row['sec']}s",
        flush=True,
    )


if __name__ == "__main__":
    main()
