#!/usr/bin/env python3
"""chi5 at mu>=50 and a new conductor (chi17) for the geometric law.

Two independent tracks, both CPU (mpmath). Do not use the GPU.

  1) harvest zeros of L(s,chi) by |L|^2 minima on the critical line
  2) measure lambda_min(Q) at a list of windows (scan_s.assemble)
  3) compare two-point slopes to geom_law.s_pred

Usage (repo root):

    python3 code/campaign_geom_chars.py harvest --char chi5 --tmax 320
    python3 code/campaign_geom_chars.py harvest --char chi17 --tmax 320
    python3 code/campaign_geom_chars.py slope  --char chi5  --windows 30,40,50,62,74
    python3 code/campaign_geom_chars.py slope  --char chi17 --windows 11,22,30,50
    python3 code/campaign_geom_chars.py table  --char chi5 --char chi17

JSONL: report/campaign_geom_chars.jsonl
"""
from __future__ import annotations

import argparse
import json
import os
import pickle
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from geom_law import F, s_pred  # noqa: E402
from kronecker import chi_tab  # noqa: E402
from scan_s import CHARS, assemble  # noqa: E402

OUT = ROOT / "report" / "campaign_geom_chars.jsonl"

# New conductor: primitive even Kronecker (./17). Not in the §67 set.
CHARS.setdefault("chi17", dict(q=17, d=17, a=0))

# Depth-adequate (N, dps) guesses. Raise N if lam0 is still diving.
WINDOWS = {
    11: (32, 45),
    22: (36, 50),
    30: (40, 55),
    40: (44, 55),
    50: (48, 60),
    62: (52, 65),
    74: (56, 70),
}


def zeros_path(name: str) -> Path:
    for p in (HERE / f"zeros_{name}_150.pkl", HERE / f"zeros_{name}.pkl"):
        if p.exists():
            return p
    return HERE / f"zeros_{name}.pkl"


def load_zeros(name: str) -> list:
    p = zeros_path(name)
    if not p.exists():
        return []
    z = pickle.load(open(p, "rb"))
    return sorted(float(x) for x in z)


def save_zeros(name: str, zeros: list) -> None:
    p = zeros_path(name)
    pickle.dump(sorted(set(float(x) for x in zeros)), open(p, "wb"))


def a2_factory(name: str):
    cf = CHARS[name]
    q, tab = cf["q"], chi_tab(cf["d"], cf["q"])

    def a2(t):
        s = mp.mpf("0.5") + 1j * mp.mpf(t)
        v = q ** (-s) * mp.fsum(
            tab[r] * mp.zeta(s, mp.mpf(r) / q) for r in range(1, q) if tab[r]
        )
        return float(mp.re(v) ** 2 + mp.im(v) ** 2)

    return a2


def harvest(name: str, tmax: float, budget: float, h: float = 0.35) -> None:
    mp.mp.dps = 15
    a2 = a2_factory(name)
    Z = load_zeros(name)
    t0 = time.time()
    if not Z:
        t, p2, p1 = 0.4, a2(0.4), a2(0.4 + h)
        t = 0.4 + h
    else:
        t = Z[-1] + h
        p2, p1 = a2(t - 2 * h), a2(t - h)
    print(f"{name}: harvest from {t:.2f} to {tmax} ({len(Z)} zeros)", flush=True)
    phi = (5**0.5 - 1) / 2
    while t < tmax and time.time() - t0 < budget:
        c = a2(t + h)
        if p1 < p2 and p1 < c:
            a, b = t - h, t + h
            for _ in range(26):
                c1, c2 = b - phi * (b - a), a + phi * (b - a)
                if a2(c1) < a2(c2):
                    b = c2
                else:
                    a = c1
            zm = (a + b) / 2
            if a2(zm) < 1e-5:
                Z.append(zm)
                save_zeros(name, Z)
                if len(Z) % 10 == 0:
                    print(f"  {len(Z)} zeros, last {Z[-1]:.2f}", flush=True)
        p2, p1 = p1, c
        t += h
    print(
        f"  -> {len(Z)} zeros max={max(Z) if Z else 0:.1f} "
        f"{'DONE' if t >= tmax else 'partial'} [{time.time()-t0:.0f}s]",
        flush=True,
    )


def append(row: dict) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("a") as f:
        f.write(json.dumps(row) + "\n")
        f.flush()


def slope(name: str, mus: list) -> None:
    rows = []
    for mu in mus:
        NB, dps = WINDOWS.get(int(mu), (48, 60))
        lam0, ell, dt = assemble(name, float(mu), NB, dps)
        rec = {
            "kind": "slope",
            "char": name,
            "mu": float(mu),
            "N": NB + 1,
            "dps": dps,
            "lam0": lam0,
            "ell0": ell[0],
            "sec": dt,
        }
        append(rec)
        rows.append(rec)
        print(rec, flush=True)
    z = load_zeros(name)
    for i in range(len(rows) - 1):
        a, b = rows[i], rows[i + 1]
        s_hat = (b["ell0"] - a["ell0"]) / (b["mu"] - a["mu"])
        pred = s_pred(a["mu"], b["mu"], z) if len(z) >= 2 else None
        out = {
            "kind": "pair",
            "char": name,
            "mu1": a["mu"],
            "mu2": b["mu"],
            "s_hat": s_hat,
            "s_pred": pred,
            "ratio": (None if pred in (None, 0) else s_hat / pred),
            "nzeros": len(z),
        }
        append(out)
        print(out, flush=True)


def table(names: list) -> None:
    for name in names:
        z = load_zeros(name)
        print(f"\n{name} nzeros={len(z)} g1={z[0] if z else None}")
        if len(z) < 2:
            continue
        for m1, m2 in ((11, 22), (22, 50), (30, 50), (50, 62), (62, 74)):
            print(
                f"  s_pred {m1}-{m2} = {s_pred(m1, m2, z):.3f}  "
                f"F({m1})={F(m1,z):.2f} F({m2})={F(m2,z):.2f}"
            )


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=("harvest", "slope", "table"))
    p.add_argument("--char", action="append", default=[])
    p.add_argument("--tmax", type=float, default=320.0)
    p.add_argument("--budget", type=float, default=20000.0)
    p.add_argument("--windows", type=str, default="50,62,74")
    args = p.parse_args()
    names = args.char or ["chi5"]
    if args.cmd == "harvest":
        for n in names:
            harvest(n, args.tmax, args.budget)
    elif args.cmd == "slope":
        mus = [float(x) for x in args.windows.split(",") if x]
        for n in names:
            slope(n, mus)
    else:
        table(names)


if __name__ == "__main__":
    main()
