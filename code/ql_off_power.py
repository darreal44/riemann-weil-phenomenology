#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Power iteration on a finite block of joint Off = H − w₂ Θ.

H_nm = 1/(2(n+m)) for n≠m, 0 on the diagonal (as in ql_off_s1).
Θ_nm = theta_hat(n, m, log 2, L) on cosine hats.
This is NOT s₁(ℓ²) and NOT Off_far. A block Rayleigh is a
lower bound on the finite-section norm only.

    python code/ql_off_power.py
    python code/ql_off_power.py --N 32 --M 256
"""
from __future__ import annotations

import argparse
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import CHARS, LOG2, LOG3, PI, w2_of  # noqa: E402
from ql_schur_tail import r_frob_bound, theta_hat  # noqa: E402


def s1_upper(N: int, w2: float) -> float:
    return PI / 2.0 + 1.0 / (4.0 * N) + r_frob_bound(N) + abs(w2)


def s1_lower(w2: float) -> float:
    return PI / 2.0 - abs(w2)


def assemble(N: int, M: int, w2: float, L: float) -> np.ndarray:
    idx = np.arange(N, N + M)
    Off = np.zeros((M, M))
    for a, n in enumerate(idx):
        for b, m in enumerate(idx):
            if b < a:
                continue
            h = 0.0 if n == m else 0.5 / (n + m)
            th = theta_hat(int(n), int(m), LOG2, L)
            v = h - w2 * th
            Off[a, b] = Off[b, a] = v
    return Off


def power_iter(Off: np.ndarray, niter: int = 80, seed: int = 0) -> float:
    """Largest |λ| by power iteration on Off and on -Off."""

    def run(A: np.ndarray) -> float:
        rng = np.random.default_rng(seed)
        x = rng.normal(size=A.shape[0])
        x /= np.linalg.norm(x)
        lam = 0.0
        for _ in range(niter):
            y = A @ x
            nrm = np.linalg.norm(y)
            if nrm == 0.0:
                return 0.0
            x = y / nrm
            lam = float(x @ (A @ x))
        return lam

    return max(abs(run(Off)), abs(run(-Off)))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--N", type=int, default=32)
    p.add_argument("--M", type=int, default=256)
    p.add_argument("--L", type=float, default=LOG3)
    args = p.parse_args()
    print(f"N={args.N} M={args.M} L={args.L:.6f}  joint H − w2 Θ  (no R)")
    print(f"{'chi':6} {'w2':>8} {'ess':>7} {'tri':>7} {'pow':>8} {'eigh':>8}")
    for name in ("chi3", "chi5", "chi8"):
        w2 = w2_of(CHARS[name]["d"])
        Off = assemble(args.N, args.M, w2, args.L)
        pw = power_iter(Off)
        ev = np.linalg.eigvalsh(Off)
        eh = float(max(abs(ev[0]), abs(ev[-1])))
        print(
            f"{name:6} {w2:8.4f} {s1_lower(w2):7.3f} "
            f"{s1_upper(args.N, w2):7.3f} {pw:8.4f} {eh:8.4f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
