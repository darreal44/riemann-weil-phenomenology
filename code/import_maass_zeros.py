#!/usr/bin/env python3
"""Load Maass γ from a text file (one float per line, or LMFDB paste).

    python code/import_maass_zeros.py 11.0.1.1.1 zeros.txt
    python code/scan_gl2.py 11.0.1.1.1 22 36 50

LMFDB API is 500. Page:
  https://www.lmfdb.org/ModularForm/GL2/Q/Maass/
Search N=11, R≈2.033, download positive zeros.
"""
from __future__ import annotations

import os
import pickle
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def parse(path: str) -> list[float]:
    raw = open(path, encoding="utf-8", errors="ignore").read()
    nums = re.findall(r"[-+]?\d+\.\d+(?:[eE][-+]?\d+)?", raw)
    z = sorted(float(x) for x in nums if float(x) > 1e-12)
    return z


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit("usage: import_maass_zeros.py LABEL FILE")
    label, src = sys.argv[1], sys.argv[2]
    z = parse(src)
    if not z:
        sys.exit("no floats in " + src)
    dest = os.path.join(HERE, f"zeros_{label}_weyl.pkl")
    pickle.dump(z, open(dest, "wb"))
    print(f"{label} n={len(z)} g1={z[0]:.4f} T={z[-1]:.2f} -> {dest}")


if __name__ == "__main__":
    main()
