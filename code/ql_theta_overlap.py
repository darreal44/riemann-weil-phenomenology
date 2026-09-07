#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Overlap count for the mid-band cap: |θ| vs mass majorant.

Random cosine heads, y=log 2, L=log 5. Not a proof. Not RH.

    python code/ql_theta_overlap.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_schur_tail import theta_hat  # noqa: E402

LOG2 = math.log(2.0)
L5 = math.log(5.0)
SQRT2 = math.sqrt(2.0)
N_HEAD = 16
N_SAMP = 40
N_QUAD = 80


def f_of(v, x, L):
    acc = v[0] / math.sqrt(L)
    s = math.sqrt(2.0 / L)
    for n in range(1, len(v)):
        acc += v[n] * s * math.cos(2.0 * math.pi * n * x / L)
    return acc


def mass(h2, a, b, L):
    if b <= a:
        return 0.0
    xs = np.linspace(a, b, N_QUAD)
    vals = np.array([h2(x) for x in xs])
    return float(np.trapezoid(vals, xs))


def majorant(al, be, m1, m2):
    return (
        2.0 * math.sqrt(max(al, 0.0) * max(be, 0.0))
        + 2.0 * math.sqrt(max(al, 0.0) * max(m2, 0.0))
        + m1
    )


def one(v, y, L):
    v = v / np.linalg.norm(v)
    n1 = len(v)
    Th = np.zeros((n1, n1))
    for i in range(n1):
        for j in range(i, n1):
            Th[i, j] = Th[j, i] = theta_hat(i, j, y, L)
    ray = float(v @ Th @ v)

    def h2(x):
        f = f_of(v, x, L)
        return 2.0 * f * f

    a0, a1 = 0.0, 0.5 * L - y
    c0, c1 = y, 0.5 * L
    # M = [L/2-y, y]; split at midpoint
    mid = 0.5 * ((0.5 * L - y) + y)
    al = mass(h2, a0, a1, L)
    be = mass(h2, c0, c1, L)
    m1 = mass(h2, 0.5 * L - y, mid, L)
    m2 = mass(h2, mid, y, L)
    tot = al + be + m1 + m2
    maj = majorant(al, be, m1, m2)
    return {
        "ray": ray,
        "majorant": maj,
        "mass_sum": tot,
        "ok_maj": abs(ray) <= maj + 1e-6,
        "ok_cap": abs(ray) <= SQRT2 + 1e-6,
    }


def run() -> dict:
    rng = np.random.default_rng(0)
    rows = []
    bad_maj = 0
    bad_cap = 0
    for _ in range(N_SAMP):
        v = rng.normal(size=N_HEAD)
        r = one(v, LOG2, L5)
        rows.append(r)
        if not r["ok_maj"]:
            bad_maj += 1
        if not r["ok_cap"]:
            bad_cap += 1
    return {
        "y": LOG2,
        "L": L5,
        "in_band": (0.25 * L5) <= LOG2 < (0.5 * L5),
        "n_samp": N_SAMP,
        "bad_maj": bad_maj,
        "bad_cap": bad_cap,
        "max_abs_ray": max(abs(r["ray"]) for r in rows),
        "max_maj": max(r["majorant"] for r in rows),
        "mean_mass_sum": sum(r["mass_sum"] for r in rows) / N_SAMP,
        "step_taken": False,
        "verdict": "SURVIVE" if bad_cap == 0 else "KILL",
    }


def main() -> int:
    data = run()
    print(
        f"overlap check y=log2 L=log5 in_band={data['in_band']} "
        f"bad_maj={data['bad_maj']} bad_cap={data['bad_cap']} "
        f"max|ray|={data['max_abs_ray']:.4f}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-theta-overlap.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out} verdict={data['verdict']}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
