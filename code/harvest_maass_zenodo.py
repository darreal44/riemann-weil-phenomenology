#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Load Maass a_n from Zenodo 15490636 (not the zeros).

    python code/harvest_maass_zenodo.py --download
    python code/harvest_maass_zenodo.py --file MaassForms.txt --level 1 --nforms 3
    python code/harvest_maass_zenodo.py --file MaassForms.txt --labels 1.0.1.2.1,1.0.1.3.1,1.0.1.4.1,1.0.1.5.1

Lexicographic file order is 1.0.1.1.1, 1.0.1.10.1, 1.0.1.100.1, …
not Booker–Then Table 1 (R-order: 1.0.1.1.1 … 1.0.1.5.1).
Use --labels for Table 1. Do not alias maass2 to 1.0.1.10.1.

File format (no header), fields separated by ':':
  label : N : R : symmetry : Fricke : [a1, a2, ..., a1000]

Writes code/maass_an_<label>.json with R, N, a_n.
These coefficients feed a future Q (Γ_R(s±iR)), not scan_gl2.
Zeros still come from LMFDB positive_zeros / harvest_maass.py.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ZENODO = "https://zenodo.org/records/15490636/files/MaassForms.txt?download=1"


def download(dest: str) -> None:
    print(f"GET {ZENODO}", flush=True)
    urllib.request.urlretrieve(ZENODO, dest)
    print(f"wrote {dest} ({os.path.getsize(dest)/1e6:.1f} MB)")


def parse_line(line: str):
    parts = line.rstrip("\n").split(":")
    if len(parts) < 6:
        return None
    label, N, R, sym, fricke = parts[0], parts[1], parts[2], parts[3], parts[4]
    coeffs_s = ":".join(parts[5:])
    try:
        coeffs = ast.literal_eval(coeffs_s)
    except (ValueError, SyntaxError):
        return None
    return {
        "label": label,
        "N": int(float(N)),
        "R": float(R),
        "symmetry": int(float(sym)),
        "fricke": int(float(fricke)),
        "a_n": [float(x) for x in coeffs],
    }


def resolve_file(name: str) -> str:
    if os.path.isabs(name) and os.path.exists(name):
        return name
    for cand in (
        os.path.join(HERE, name),
        os.path.join(os.path.dirname(HERE), name),
        name,
    ):
        if os.path.exists(cand):
            return cand
    return name


def write_json(rec: dict) -> str:
    slug = rec["label"].replace("/", "_").replace(" ", "_")
    dest = os.path.join(HERE, f"maass_an_{slug}.json")
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=0)
        f.write("\n")
    print(
        f"{rec['label']} N={rec['N']} R={rec['R']:.4f} "
        f"n_an={len(rec['a_n'])} a2={rec['a_n'][1] if len(rec['a_n'])>1 else '?'} -> {dest}",
        flush=True,
    )
    return dest


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--download", action="store_true")
    p.add_argument("--file", default="MaassForms.txt")
    p.add_argument("--level", type=int, default=1)
    p.add_argument("--nforms", type=int, default=3)
    p.add_argument(
        "--labels",
        default="",
        help="comma-separated LMFDB labels (Table 1: 1.0.1.2.1,…,1.0.1.5.1)",
    )
    args = p.parse_args()
    path = resolve_file(args.file)
    if args.download and not os.path.exists(path):
        download(path)
    if not os.path.exists(path):
        sys.exit(f"missing {path} — run with --download (~335MB)")
    want = [s.strip() for s in args.labels.split(",") if s.strip()]
    found: set[str] = set()
    kept = 0
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            # label is the first colon field; skip the 1000-float parse if unneeded
            head = line.split(":", 1)[0].strip()
            if want:
                if head not in want or head in found:
                    continue
                rec = parse_line(line)
                if rec is None:
                    continue
                write_json(rec)
                found.add(head)
                if found == set(want):
                    break
                continue
            rec = parse_line(line)
            if rec is None or rec["N"] != args.level:
                continue
            write_json(rec)
            kept += 1
            if kept >= args.nforms:
                break
    if want:
        missing = [lab for lab in want if lab not in found]
        if missing:
            sys.exit("missing labels: " + ",".join(missing))
        return
    if kept == 0:
        sys.exit("no forms at that level — check separator/format")


if __name__ == "__main__":
    main()
