#!/usr/bin/env python3
"""Load Maass a_n from Zenodo 15490636 (not the zeros).

    python code/harvest_maass_zenodo.py --download
    python code/harvest_maass_zenodo.py --file MaassForms.txt --level 1 --nforms 3

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


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--download", action="store_true")
    p.add_argument("--file", default="MaassForms.txt")
    p.add_argument("--level", type=int, default=1)
    p.add_argument("--nforms", type=int, default=3)
    args = p.parse_args()
    path = args.file
    if not os.path.isabs(path):
        cand = os.path.join(HERE, path)
        path = cand if os.path.exists(cand) else path
    if args.download and not os.path.exists(path):
        download(path)
    if not os.path.exists(path):
        sys.exit(f"missing {path} — run with --download (~335MB)")
    kept = 0
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            rec = parse_line(line)
            if rec is None:
                continue
            if rec["N"] != args.level:
                continue
            slug = rec["label"].replace("/", "_").replace(" ", "_")
            dest = os.path.join(HERE, f"maass_an_{slug}.json")
            json.dump(rec, open(dest, "w"), indent=0)
            print(
                f"{rec['label']} N={rec['N']} R={rec['R']:.4f} "
                f"n_an={len(rec['a_n'])} a2={rec['a_n'][1] if len(rec['a_n'])>1 else '?'} -> {dest}"
            )
            kept += 1
            if kept >= args.nforms:
                break
    if kept == 0:
        sys.exit("no forms at that level — check separator/format")


if __name__ == "__main__":
    main()
