#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Isolate Maass γ from enclosed Booker Λ_θ. Does not overwrite Table 1 txt.

    python code/maass_booker_zeros.py --forms maass1
    python code/maass_booker_zeros.py --forms all --T 115

Writes code/zeros_{name}_enclosed.txt and report/maass-booker-zeros.json.
Booker–Then zeros_maass{1..5}.txt stay the Table 1 source. Not Weil.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from maass_table1 import ALIAS, TABLE1  # noqa: E402
import maass_booker as mb  # noqa: E402


def _json_zero(rec: dict) -> dict:
    out = {}
    for k, v in rec.items():
        if hasattr(v, "mid"):
            out[k] = float(v.mid())
        else:
            out[k] = v
    return out


def write_txt(path: str, lab: str, eps: int, rows: list[dict]) -> int:
    lines = [
        f"# L-zeros of enclosed Booker Λ_θ for {lab}, ε={eps}.",
        "# |Lambda/gamma|<0.05 at the midpoint (gamma-dips dropped).",
        "# |b-a|≤1e-13 when isolate_zero certified; else located mid.",
        "# Does not replace zeros_maass*.txt. Not Weil.",
    ]
    n = 0
    for rec in rows:
        if not rec.get("is_L_zero"):
            continue
        if rec.get("mid") is None:
            continue
        lines.append(f"{rec['mid']:.14f}")
        n += 1
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return n


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--forms", default="all", help="maass1 or all")
    p.add_argument("--T", type=float, default=115.0)
    p.add_argument("--tmin", type=float, default=0.4)
    p.add_argument("--dt", type=float, default=0.1)
    p.add_argument("--theta", type=float, default=1.0)
    args = p.parse_args()
    names = list(ALIAS) if args.forms.strip() == "all" else [args.forms.strip()]
    t0 = time.time()
    blob = {
        "T": args.T,
        "theta": args.theta,
        "dt": args.dt,
        "forms": [],
        "not": "Weil; does not replace zeros_maass*.txt",
    }
    report_dir = os.path.join(ROOT, "report")
    os.makedirs(report_dir, exist_ok=True)
    for name in names:
        lab = ALIAS.get(name, name)
        out = mb.harvest_form(
            lab, T=args.T, tmin=args.tmin, dt=args.dt, theta=args.theta
        )
        n = write_txt(
            os.path.join(HERE, f"zeros_{name}_enclosed.txt")
            if name in ALIAS
            else os.path.join(HERE, f"zeros_{lab}_enclosed.txt"),
            out["label"],
            out["eps"],
            out["zeros"],
        )
        g1 = TABLE1.get(name, {}).get("g1")
        first = next((r for r in out["zeros"] if r.get("certified")), None)
        match = None
        if first is not None and g1 is not None:
            match = abs(first["mid"] - g1) < 0.01
        blob["forms"].append(
            {
                "name": name,
                "label": out["label"],
                "eps": out["eps"],
                "n_certified": out["n_certified"],
                "n_brackets": out["n_brackets"],
                "nv": out["nv"],
                "g1_table1": g1,
                "g1_ours": first["mid"] if first else None,
                "g1_match": match,
                "zeros": [_json_zero(r) for r in out["zeros"]],
            }
        )
        print(f"wrote {n} certified γ for {name}", flush=True)
    blob["elapsed"] = time.time() - t0
    json_path = os.path.join(report_dir, "maass-booker-zeros.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(blob, f, indent=2)
        f.write("\n")
    print(f"report {json_path} elapsed {blob['elapsed']:.1f}s", flush=True)


if __name__ == "__main__":
    main()
