#!/usr/bin/env python3
"""T of a zeros list, and Hecke T_p = a_p.

    python code/compute_T.py zeros_11a1_weyl.pkl
    python code/compute_T.py zeros_11a1_weyl.pkl --hecke 11a1 40

T_p on v0 is not implemented: T_p acts on S_k, not on the
cosine window.
"""
from __future__ import annotations

import math
import os
import pickle
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load_zeros(path):
    if not os.path.exists(path):
        path = os.path.join(HERE, path)
    z = sorted(float(x) for x in pickle.load(open(path, "rb")))
    return [t for t in z if t > 1e-12]


def weyl_dirichlet(T, q=1):
    if T <= 0:
        return 0.0
    return (T / math.pi) * math.log(max(q * T / (2 * math.pi), 2.0))


def weyl_gl2(T, N):
    if T <= 0:
        return 0.0
    return (T / math.pi) * math.log(max(T * math.sqrt(N) / (2 * math.pi), 2.0)) - T / math.pi


def primes_upto(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = [False] * len(s[i * i :: i])
    return [i for i, v in enumerate(s) if v]


def hecke_ap(label, cap):
    import shutil, subprocess
    if shutil.which("gp"):
        script = f"""
E = ellinit("{label}");
forprime(p=2, {cap}, print(p, " ", ellap(E, p)));
"""
        proc = subprocess.run(
            ["gp", "-q"], input=script, text=True, capture_output=True
        )
        out = {}
        for line in proc.stdout.splitlines():
            parts = line.split()
            if len(parts) != 2:
                continue
            try:
                out[int(parts[0])] = int(float(parts[1]))
            except ValueError:
                continue
        if out:
            return out
    if label != "11a1":
        raise SystemExit("gp required for this curve")
    sys.path.insert(0, HERE)
    from scan_q_gl2 import AP_11
    return {p: a for p, a in AP_11.items() if p <= cap}


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    path = sys.argv[1]
    z = load_zeros(path)
    T = z[-1] if z else 0.0
    print(f"n={len(z)}  T={T:.6f}  g1={z[0] if z else float('nan'):.6f}")
    name = os.path.basename(path)
    if "a1" in name or "sym2" in name:
        N = 11
        for tok in ("67", "61", "53", "43", "37", "32", "19", "11"):
            if tok in name:
                N = int(tok)
                break
        W = weyl_gl2(T, N)
        tag = f"GL2 N={N}"
    else:
        W = weyl_dirichlet(T, 1)
        tag = "GL1"
    print(f"  Weyl {tag:12s} {W:.1f}  ratio={len(z)/max(W,1):.3f}")
    if "--hecke" in sys.argv:
        i = sys.argv.index("--hecke")
        label = sys.argv[i + 1] if i + 1 < len(sys.argv) else "11a1"
        cap = int(sys.argv[i + 2]) if i + 2 < len(sys.argv) else 40
        ap = hecke_ap(label, cap)
        print(f"T_p = a_p for {label}, p<={cap} ({len(ap)} primes):")
        print(f"  {'p':>5} {'a_p':>6} {'2sqrt(p)':>9} {'a_p/bound':>10}")
        for p in sorted(ap):
            bound = 2 * math.sqrt(p)
            a = ap[p]
            print(f"  {p:5d} {a:6d} {bound:9.3f} {a/bound:10.3f}")


if __name__ == "__main__":
    main()
