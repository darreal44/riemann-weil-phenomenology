#!/usr/bin/env python3
"""Other v at χ₅ μ=150. Pencil from v-impact.md, plus v_min.

Assemble A, P23, Prest once per μ (3×3), then every v is a sandwich.
Two μ in parallel.

    python code/av_other_v.py
"""
from __future__ import annotations

import concurrent.futures
import json
import multiprocessing
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_split23 import assemble_AP  # noqa: E402

# Locked table of v-impact.md (μ=16). Pencil first, then off-pencil hats.
VECTORS = [
    ("rat", (4.0, -3.0, 1.0)),
    ("5-4-1", (5.0, -4.0, 1.0)),
    ("4-3-0", (4.0, -3.0, 0.0)),
    ("1-1-0", (1.0, -1.0, 0.0)),
    ("3-2-1", (3.0, -2.0, 1.0)),
    ("e0", (1.0, 0.0, 0.0)),
    ("e1", (0.0, 1.0, 0.0)),
    ("e2", (0.0, 0.0, 1.0)),
]
PENCIL = {"rat", "5-4-1", "4-3-0", "1-1-0", "3-2-1"}
MUS = (16.0, 150.0)


def _unit(raw) -> np.ndarray:
    v = np.asarray(raw, dtype=float)
    return v / np.linalg.norm(v)


def eval_mu(mu: float, dps: int = 40) -> dict:
    t0 = time.time()
    A, P23, Prest = assemble_AP(mu, dps=dps)
    H = A - P23 - Prest
    evals, evecs = np.linalg.eigh(H)
    vmin = evecs[:, 0]
    vrat = _unit(VECTORS[0][1])
    if float(vmin @ vrat) < 0:
        vmin = -vmin
    rows = []
    for name, raw in VECTORS:
        v = _unit(raw)
        Av = float(v @ A @ v)
        p23 = float(v @ P23 @ v)
        prest = float(v @ Prest @ v)
        Q = Av - p23 - prest
        a = [float(v @ evecs[:, k]) for k in range(3)]
        if a[0] < 0:
            a = [-x for x in a]
        rows.append(
            {
                "name": name,
                "pencil": name in PENCIL,
                "v": [float(x) for x in v],
                "A": Av,
                "P23": p23,
                "Prest": prest,
                "A_minus_P23": Av - p23,
                "Q": Q,
                "overlap_vmin": abs(float(v @ vmin)),
                "alpha": a,
            }
        )
    lam0 = float(evals[0])
    Qmin = float(vmin @ H @ vmin)
    return {
        "mu": float(mu),
        "seconds": round(time.time() - t0, 2),
        "lam_min": lam0,
        "evals": [float(x) for x in evals],
        "evecs": [[float(x) for x in evecs[:, k]] for k in range(3)],
        "vmin": [float(x) for x in vmin],
        "Q_vmin": Qmin,
        "overlap_rat_vmin": abs(float(vrat @ vmin)),
        "rows": rows,
    }


def _job(mu: float) -> dict:
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    return eval_mu(float(mu))


def main() -> None:
    workers = min(len(MUS), os.cpu_count() or 2)
    print(
        f"mus={list(MUS)}  nv={len(VECTORS)}  workers={workers}  "
        "estimate wall ~30s (one 3x3 assemble at mu=150, NB=3)",
        flush=True,
    )
    t0 = time.time()
    ctx = multiprocessing.get_context("spawn")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=ctx
    ) as pool:
        futs = [pool.submit(_job, mu) for mu in MUS]
        by_mu = {}
        for fut in concurrent.futures.as_completed(futs):
            block = fut.result()
            by_mu[block["mu"]] = block
            print(
                f"  mu={block['mu']:.0f}  lam_min={block['lam_min']:.3e}  "
                f"Q(vmin)={block['Q_vmin']:.4f}  "
                f"ov(rat,vmin)={block['overlap_rat_vmin']:.3f}  "
                f"{block['seconds']}s",
                flush=True,
            )
            for r in block["rows"]:
                tag = "penc" if r["pencil"] else "hat "
                print(
                    f"    {r['name']:6s} {tag}  Q={r['Q']: .5f}  "
                    f"A-P23={r['A_minus_P23']: .4f}  Prest={r['Prest']: .4f}",
                    flush=True,
                )
    dest = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "report",
        "av-other-v-mu150.json",
    )
    payload = {
        "seconds": round(time.time() - t0, 1),
        "blocks": [by_mu[mu] for mu in MUS],
    }
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    b150 = by_mu[150.0]
    pencil_neg = [
        r["name"] for r in b150["rows"] if r["pencil"] and r["Q"] <= 0
    ]
    psd = b150["lam_min"] > 0
    print(f"wrote {dest}", flush=True)
    if pencil_neg or not psd:
        print(
            "KILL",
            f"pencil_neg={pencil_neg or 'none'}",
            f"lam_min={b150['lam_min']:.3e}",
            flush=True,
        )
    else:
        print(
            "SURVIVE",
            f"lam_min={b150['lam_min']:.3e}",
            f"ov={b150['overlap_rat_vmin']:.3f}",
            flush=True,
        )


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
