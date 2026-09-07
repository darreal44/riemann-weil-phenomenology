#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Cutoff error of a truncated Hankel Weyl trial. Not Hartman.

H_nm = ½/(n+m) on [N,M), including the diagonal (Hilbert object).
Trial x_n = n^{-1/2} and n^{-1/2} cos(τ log n) (Mellin, Hankel).
R(M) = ⟨Hx,x⟩, e_R = π/2 − R, e_σ = π/2 − ‖H‖₂.
Fit e_σ ~ a / log(M/N) + b. No GL CSV. No infinite Weyl sequence.

    python code/ql_hankel_weyl_cut.py

Named in report/minorant-weyl-error.md ([32,80) only).
Not a take. Not RH.
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

PI = math.pi
HALF_PI = 0.5 * PI
N0 = 32
MS = (80, 128, 192, 256, 384, 512, 1024, 2048)
TAUS = (0.0, 0.5, 1.0, 2.0)


def hankel(n0: int, n1: int) -> np.ndarray:
    ns = np.arange(n0, n1, dtype=float)
    return 0.5 / (ns[:, None] + ns[None, :])


def trial(n0: int, n1: int, tau: float) -> np.ndarray:
    ns = np.arange(n0, n1, dtype=float)
    x = ns ** -0.5
    if tau != 0.0:
        x = x * np.cos(tau * np.log(ns))
    nrm = np.linalg.norm(x)
    return x / nrm


def row_of(n0: int, n1: int) -> dict:
    H = hankel(n0, n1)
    sig = float(np.linalg.norm(H, 2))
    best = None
    trials = []
    for tau in TAUS:
        x = trial(n0, n1, tau)
        R = float(x @ (H @ x))
        rec = {
            "tau": tau,
            "R": R,
            "e_R": HALF_PI - R,
            "Hx": float(np.linalg.norm(H @ x)),
        }
        trials.append(rec)
        if best is None or rec["R"] > best["R"]:
            best = rec
    return {
        "n0": n0,
        "n1": n1,
        "dim": n1 - n0,
        "sigma": sig,
        "e_sigma": HALF_PI - sig,
        "inv_log": 1.0 / math.log(n1 / n0),
        "best_tau": best["tau"],
        "R": best["R"],
        "e_R": best["e_R"],
        "Hx": best["Hx"],
        "trials": trials,
    }


def fit_inv_log(rows: list[dict], key: str) -> dict:
    """e ~ a / log(M/N) + b, least squares on all rows."""
    x = np.array([r["inv_log"] for r in rows])
    y = np.array([r[key] for r in rows])
    A = np.column_stack([x, np.ones_like(x)])
    coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ coef
    resid = y - pred
    ss_res = float(np.sum(resid ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return {
        "a": float(coef[0]),
        "b": float(coef[1]),
        "r2": r2,
        "key": key,
    }


def main() -> int:
    rows = []
    for m in MS:
        r = row_of(N0, m)
        rows.append(r)
        print(
            f"[{N0},{m}) dim={r['dim']:4d}  "
            f"σ={r['sigma']:.4f}  eσ={r['e_sigma']:.4f}  "
            f"R={r['R']:.4f}  eR={r['e_R']:.4f}  "
            f"τ*={r['best_tau']}  1/log={r['inv_log']:.4f}",
            flush=True,
        )
    fit_s = fit_inv_log(rows, "e_sigma")
    fit_r = fit_inv_log(rows, "e_R")
    print(
        f"fit eσ = {fit_s['a']:.3f}/log(M/N) + {fit_s['b']:.3f}  "
        f"R²={fit_s['r2']:.3f}",
        flush=True,
    )
    print(
        f"fit eR = {fit_r['a']:.3f}/log(M/N) + {fit_r['b']:.3f}  "
        f"R²={fit_r['r2']:.3f}  (b→0 would be Hartman; not claimed)",
        flush=True,
    )
    data = {
        "step_taken": False,
        "verdict": "KILL",
        "why": (
            "Truncated Weyl trial measures cutoff error e_H(M), "
            "not s1_ess. Fit is not Hartman. No GL CSV."
        ),
        "n0": N0,
        "half_pi": HALF_PI,
        "rows": rows,
        "fit_e_sigma": fit_s,
        "fit_e_R": fit_r,
        "e_sigma_512": next(r["e_sigma"] for r in rows if r["n1"] == 512),
        "e_sigma_2048": next(r["e_sigma"] for r in rows if r["n1"] == 2048),
        "R_2048": next(r["R"] for r in rows if r["n1"] == 2048),
        "sigma_2048": next(r["sigma"] for r in rows if r["n1"] == 2048),
    }
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-hankel-weyl-cut.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}  verdict={data['verdict']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
