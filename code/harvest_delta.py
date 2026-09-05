#!/usr/bin/env python3
"""Ramanujan Delta (weight 12, level 1) zeros via PARI.

    python code/harvest_delta.py 80
    python code/harvest_delta.py 320

Writes code/zeros_delta_weyl.pkl. Requires gp.
PARI 2.17: lfunzeros(mfDelta(), T) returns heights t of
zeros 6+it on the critical line of L(Δ,s).
"""
from __future__ import annotations

import os
import pickle
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    tmax = float(sys.argv[1]) if len(sys.argv) > 1 else 80.0
    if not shutil.which("gp"):
        sys.exit("gp not on PATH")
    script = f"""
default(realprecision, 19);
v = lfunzeros(mfDelta(), {tmax});
for(i=1, #v, if(v[i] > 0, print(v[i])));
"""
    proc = subprocess.run(
        ["gp", "-q", "--default", "parisizemax=1G"],
        input=script,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0 or not proc.stdout.strip():
        # older/newer API
        script = f"""
default(realprecision, 19);
F = mfDelta();
mf = mfinit(F);
L = lfunmf(mf, F);
v = lfunzeros(L, {tmax});
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
    dest = os.path.join(HERE, "zeros_delta_weyl.pkl")
    pickle.dump(zeros, open(dest, "wb"))
    print(f"delta n={len(zeros)} T={zeros[-1] if zeros else 0:.2f} -> {dest}")
    if not zeros:
        print("stderr:", proc.stderr[-400:])


if __name__ == "__main__":
    main()
