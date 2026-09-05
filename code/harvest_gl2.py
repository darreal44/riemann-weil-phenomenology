#!/usr/bin/env python3
"""GL(2) zero harvest via PARI/GP (elliptic curves = weight-2 newforms).

Requires `gp` on PATH. Install:

    # Debian / Ubuntu
    sudo apt install pari-gp
    # Fedora
    sudo dnf install pari
    # conda
    conda install -c conda-forge pari
    # Windows: https://pari.math.u-bordeaux.fr/download.html
              add gp.exe to PATH

    python3 code/harvest_gl2.py 11a1 80
    python3 code/harvest_gl2.py --all 80 --workers 4

Writes code/zeros_{name}_weyl.pkl (same shape as Dirichlet harvests).
One process per curve. Slices inside one L-function stay in GP.
"""
from __future__ import annotations

import argparse
import os
import pickle
import shutil
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))

# Cremona labels: weight-2 newforms / elliptic curves over Q.
CURVES = {
    "11a1": 11,
    "19a1": 19,
    "32a1": 32,
    "37a1": 37,
    "43a1": 43,
    "53a1": 53,
    "61a1": 61,
    "67a1": 67,
}


def path_for(name: str) -> str:
    return os.path.join(HERE, f"zeros_{name}_weyl.pkl")


def expected_N(T: float, Ncond: int) -> float:
    """One-sided Weyl for a degree-2 L of conductor N, critical line."""
    import math
    if T <= 0:
        return 0.0
    # two Gamma factors: N(T) ~ (T/π) log(√N · T / 2π)
    return (T / math.pi) * math.log(max(T * (Ncond ** 0.5) / (2 * math.pi), 2.0))


def run_gp(label: str, tmax: float) -> list[float]:
    if not shutil.which("gp"):
        raise SystemExit(
            "gp not found. Install PARI/GP (see code/harvest_gl2.py header)."
        )
    # default(realprecision, 19) ~ 18 digits, enough for T~320 zeros.
    script = f"""
default(realprecision, 19);
E = ellinit("{label}");
v = lfunzeros(E, {tmax});
for(i=1, #v, print(v[i]));
"""
    proc = subprocess.run(
        ["gp", "-q", "--default", "parisizemax=1G"],
        input=script,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr[-800:] or proc.stdout[-800:])
    out = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            x = float(line)
        except ValueError:
            continue
        if x > 1e-12:
            out.append(x)
    return sorted(set(out))


def harvest_one(name: str, tmax: float) -> dict:
    zeros = run_gp(name, tmax)
    dest = path_for(name)
    if os.path.exists(dest):
        old = [float(x) for x in pickle.load(open(dest, "rb"))]
        zeros = sorted(set(old + zeros))
    pickle.dump(zeros, open(dest, "wb"))
    nexp = expected_N(tmax, CURVES[name])
    return {
        "name": name,
        "n": len(zeros),
        "T": zeros[-1] if zeros else 0.0,
        "expected": nexp,
        "ratio": (len(zeros) / nexp) if nexp else 0.0,
        "path": dest,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("name", nargs="?", help="Cremona label, e.g. 11a1")
    p.add_argument("tmax", nargs="?", type=float, default=80.0)
    p.add_argument("--all", action="store_true")
    p.add_argument("--workers", type=int, default=1)
    args = p.parse_args()
    if args.all:
        jobs = list(CURVES)
    elif args.name:
        if args.name not in CURVES:
            sys.exit(f"unknown curve {args.name}, have {sorted(CURVES)}")
        jobs = [args.name]
    else:
        p.print_help()
        sys.exit(2)
    print(f"gp = {shutil.which('gp') or 'MISSING'}")
    if args.workers == 1 or len(jobs) == 1:
        for n in jobs:
            r = harvest_one(n, args.tmax)
            print(
                f"{r['name']} n={r['n']} T={r['T']:.2f} "
                f"Weyl~{r['expected']:.1f} ratio={r['ratio']:.2f}"
            )
        return
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(harvest_one, n, args.tmax): n for n in jobs}
        for fut in as_completed(futs):
            r = fut.result()
            print(
                f"{r['name']} n={r['n']} T={r['T']:.2f} "
                f"Weyl~{r['expected']:.1f} ratio={r['ratio']:.2f}"
            )


if __name__ == "__main__":
    main()
