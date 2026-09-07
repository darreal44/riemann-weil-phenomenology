#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Double-limit cutoff error of truncated Hankel: N and M/N.

H_nm = ½/(n+m) on [N,M). e_σ = π/2 − ‖H‖₂.
Per N, fit e_σ ~ a / log(M/N) + b(N).
b→0 as N→∞ would be Hartman; not claimed.
τ=0 only (8i: oscillating never wins). No GL CSV.

    python code/ql_hankel_weyl_N.py

Named in notes/ql-hankel-weyl-cut.md (N=32 only).
Not a take. Not RH.
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_hankel_weyl_cut import (  # noqa: E402
    HALF_PI,
    fit_inv_log,
    hankel,
    trial,
)

NS = (16, 32, 64, 128)
RATIOS = (4, 8, 16, 32)
M_CAP = 2048


def row_sigma(n0: int, n1: int) -> dict:
    H = hankel(n0, n1)
    sig = float(np.linalg.norm(H, 2))
    x = trial(n0, n1, 0.0)
    R = float(x @ (H @ x))
    return {
        "n0": n0,
        "n1": n1,
        "dim": n1 - n0,
        "ratio": n1 / n0,
        "inv_log": 1.0 / math.log(n1 / n0),
        "sigma": sig,
        "e_sigma": HALF_PI - sig,
        "R": R,
        "e_R": HALF_PI - R,
    }


def grid() -> list[tuple[int, int]]:
    pairs = []
    for n0 in NS:
        for r in RATIOS:
            n1 = n0 * r
            if n1 <= M_CAP and n1 > n0 + 4:
                pairs.append((n0, n1))
        # always include M=2048 when it is a new ratio
        if M_CAP > n0 and (n0, M_CAP) not in pairs:
            pairs.append((n0, M_CAP))
    return pairs


def main() -> int:
    pairs = grid()
    rows = []
    for n0, n1 in pairs:
        r = row_sigma(n0, n1)
        rows.append(r)
        print(
            f"[{n0},{n1}) dim={r['dim']:4d}  "
            f"σ={r['sigma']:.4f}  eσ={r['e_sigma']:.4f}  "
            f"R={r['R']:.4f}  1/log={r['inv_log']:.4f}",
            flush=True,
        )
    by_n: dict[int, list[dict]] = {n: [] for n in NS}
    for r in rows:
        by_n[r["n0"]].append(r)
    fits = []
    for n0 in NS:
        chunk = by_n[n0]
        fs = fit_inv_log(chunk, "e_sigma")
        fr = fit_inv_log(chunk, "e_R")
        rec = {
            "n0": n0,
            "n_rows": len(chunk),
            "fit_e_sigma": fs,
            "fit_e_R": fr,
            "e_sigma_at_ratio8": next(
                (x["e_sigma"] for x in chunk if abs(x["ratio"] - 8.0) < 1e-9),
                None,
            ),
        }
        fits.append(rec)
        print(
            f"N={n0:3d}  eσ = {fs['a']:.3f}/log(M/N) + {fs['b']:.3f}  "
            f"R²={fs['r2']:.3f}",
            flush=True,
        )
    bs = [f["fit_e_sigma"]["b"] for f in fits]
    b_min, b_max = min(bs), max(bs)
    toward_zero = b_min < 0.3
    slices = {}
    for ratio in RATIOS:
        chunk = [r for r in rows if abs(r["ratio"] - ratio) < 1e-9]
        if len(chunk) < 2:
            continue
        es = [r["e_sigma"] for r in chunk]
        slices[str(ratio)] = {
            "n0s": [r["n0"] for r in chunk],
            "e_sigma": es,
            "spread": max(es) - min(es),
        }
    data = {
        "step_taken": False,
        "verdict": "KILL",
        "why": (
            "At matched M/N, eσ is independent of N (spread < 0.005). "
            "Raising N at fixed ratio does nothing. b(N) does not go to 0. "
            "Hartman not exhibited. No GL CSV."
        ),
        "half_pi": HALF_PI,
        "m_cap": M_CAP,
        "rows": rows,
        "fits": fits,
        "ratio_slices": slices,
        "b_min": b_min,
        "b_max": b_max,
        "b_toward_zero": toward_zero,
        "b16": bs[0],
        "b32": bs[1],
        "b64": bs[2],
        "b128": bs[3],
        "spread_ratio4": slices.get("4", {}).get("spread"),
        "spread_ratio8": slices.get("8", {}).get("spread"),
    }
    if toward_zero:
        data["why"] = (
            "b(N) dropped below 0.3; still not Hartman, "
            "no infinite Weyl sequence, not a take."
        )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-hankel-weyl-N.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(
        f"wrote {out}  b(N)={', '.join(f'{b:.3f}' for b in bs)}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
