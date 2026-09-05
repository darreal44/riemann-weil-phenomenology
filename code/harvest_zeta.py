#!/usr/bin/env python3
"""Riemann zeta zeros via PARI lfunzeros(1, T).

    python code/harvest_zeta.py 320

Writes code/zeros_zeta_weyl.pkl (same shape as the χ lists).
Requires gp on PATH (you already have it).
"""
from __future__ import annotations

import os
import pickle
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    tmax = float(sys.argv[1]) if len(sys.argv) > 1 else 320.0
    if not shutil.which("gp"):
        sys.exit("gp not on PATH")
    script = f"""
default(realprecision, 19);
v = lfunzeros(1, {tmax});
for(i=1, #v, if(v[i] > 0, print(v[i])));
"""
    proc = subprocess.run(
        ["gp", "-q", "--default", "parisizemax=1G"],
        input=script,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        sys.exit(proc.stderr[-800:] or "gp failed")
    zeros = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            x = float(line)
        except ValueError:
            continue
        if x > 1e-12:
            zeros.append(x)
    zeros = sorted(set(zeros))
    dest = os.path.join(HERE, "zeros_zeta_weyl.pkl")
    pickle.dump(zeros, open(dest, "wb"))
    print(f"zeta n={len(zeros)} T={zeros[-1] if zeros else 0:.2f} -> {dest}")


if __name__ == "__main__":
    main()
