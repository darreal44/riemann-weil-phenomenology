#!/usr/bin/env python3
"""Useful extra L-functions (gp). Not a third copy of 11a1.

    python code/harvest_associated.py --list
    python code/harvest_associated.py delta_chi5 80
    python code/harvest_associated.py --all 80
    python code/harvest_associated.py --all 320

Each target is one PARI constructor + lfunzeros.
Failures print stderr and skip. Writes zeros_{name}_weyl.pkl.
"""
from __future__ import annotations

import argparse
import os
import pickle
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# name -> (gp snippet that binds L, note)
# Snippets must leave L defined.
TARGETS = {
    "delta_chi5": (
        'F=mfDelta(); G=mftwist(F,5); mf=mfinit(G); L=lfunmf(mf,G);',
        "L(Delta ⊗ χ5), weight 12, conductor 25",
    ),
    "delta_chi4": (
        'F=mfDelta(); G=mftwist(F,-4); mf=mfinit(G); L=lfunmf(mf,G);',
        "L(Delta ⊗ χ_{-4})",
    ),
    "11a1_chi5": (
        'E=ellinit("11a1"); L0=lfuncreate(E); L=lfuntwist(L0,5);',
        "L(E11 ⊗ χ5) — fallback constructors below if lfuntwist missing",
    ),
    "sym2_11a1": (
        'E=ellinit("11a1"); L0=lfuncreate(E); L=lfunsympow(L0,2);',
        "L(sym^2 E11), degree 3",
    ),
    "sym2_delta": (
        'F=mfDelta(); mf=mfinit(F); L0=lfunmf(mf,F); L=lfunsympow(L0,2);',
        "L(sym^2 Delta), degree 3",
    ),
}

FALLBACKS = {
    "11a1_chi5": [
        'E=ellinit("11a1"); L=lfuncreate([E,5]);',
        'chi=lfuncreate(5); E=ellinit("11a1"); L=lfunmul(lfuncreate(E),chi);',
    ],
    "delta_chi5": [
        'L=lfuncreate(mftwist(mfDelta(),5));',
        'L=lfunzeros; /* placeholder never used */',
    ],
}


def run_gp(body: str, tmax: float) -> tuple[list[float], str]:
    script = f"""
default(realprecision, 19);
{body}
v = lfunzeros(L, {tmax});
for(i=1, #v, if(v[i] > 0, print(v[i])));
"""
    proc = subprocess.run(
        ["gp", "-q", "--default", "parisizemax=1G"],
        input=script, text=True, capture_output=True,
    )
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
    return sorted(set(zeros)), (proc.stderr or proc.stdout)[-500:]


def harvest(name: str, tmax: float) -> None:
    if name not in TARGETS:
        sys.exit(f"unknown {name}, have {sorted(TARGETS)}")
    body, note = TARGETS[name]
    print(f"== {name} == {note}", flush=True)
    zeros, err = run_gp(body, tmax)
    if not zeros:
        for fb in FALLBACKS.get(name, []):
            if "placeholder" in fb:
                continue
            print(f"  fallback…", flush=True)
            zeros, err = run_gp(fb, tmax)
            if zeros:
                break
    if not zeros:
        print(f"  FAIL {name}\n  {err}")
        return
    dest = os.path.join(HERE, f"zeros_{name}_weyl.pkl")
    pickle.dump(zeros, open(dest, "wb"))
    print(f"  n={len(zeros)} T={zeros[-1]:.2f} g1={zeros[0]:.3f} -> {dest}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("name", nargs="?")
    p.add_argument("tmax", nargs="?", type=float, default=80.0)
    p.add_argument("--all", action="store_true")
    p.add_argument("--list", action="store_true")
    args = p.parse_args()
    if args.list:
        for k, (_, note) in TARGETS.items():
            print(f"{k:16s} {note}")
        return
    if not shutil.which("gp"):
        sys.exit("gp not on PATH")
    names = list(TARGETS) if args.all else ([args.name] if args.name else None)
    if not names:
        p.print_help()
        sys.exit(2)
    for n in names:
        harvest(n, args.tmax)


if __name__ == "__main__":
    main()
