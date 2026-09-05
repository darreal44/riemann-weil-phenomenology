#!/usr/bin/env python3
"""Sato-Tate histogram for a Cremona curve.

    python code/sato_tate.py 11a1 2000

Needs gp. Prints an ASCII histogram and, if matplotlib is
installed, report/sato_tate_11a1.png.
"""
from __future__ import annotations

import math
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def ellap(label: str, cap: int) -> list[tuple[int, int]]:
    if not shutil.which("gp"):
        sys.exit("gp not on PATH")
    script = f'E=ellinit("{label}"); forprime(p=2,{cap}, print(p," ",ellap(E,p)));'
    proc = subprocess.run(["gp", "-q"], input=script, text=True, capture_output=True)
    out = []
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) != 2:
            continue
        try:
            out.append((int(parts[0]), int(float(parts[1]))))
        except ValueError:
            continue
    return out


def angles(pairs):
    th = []
    skipped = 0
    for p, a in pairs:
        if p == 0:
            continue
        x = a / (2 * math.sqrt(p))
        if x < -1 or x > 1:
            skipped += 1
            x = max(-1, min(1, x))
        th.append(math.acos(x))
    return th, skipped


def ascii_hist(th, bins=12):
    lo, hi = 0.0, math.pi
    w = (hi - lo) / bins
    counts = [0] * bins
    for t in th:
        i = min(int((t - lo) / w), bins - 1)
        counts[i] += 1
    n = len(th) or 1
    print(f"theta in [0,pi], {len(th)} primes")
    print("  theta     ST dens   count  bar")
    for i, c in enumerate(counts):
        mid = lo + (i + 0.5) * w
        st = (2 / math.pi) * math.sin(mid) ** 2
        bar = "#" * int(40 * c / max(counts))
        print(f"  {mid:5.2f}    {st:6.3f}   {c:5d}  {bar}")


def maybe_png(label, cap, th):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print("matplotlib missing — ASCII only")
        return
    xs = np.linspace(0, math.pi, 200)
    st = (2 / math.pi) * np.sin(xs) ** 2
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(th, bins=16, density=True, color="#3d5a80", alpha=0.75, label="empirical")
    ax.plot(xs, st, color="#e07a5f", lw=2, label=r"(2/\pi) sin^2 \theta")
    ax.set_xlabel(r"$\theta=\arccos(a_p/(2\sqrt{p}))$")
    ax.set_ylabel("density")
    ax.set_title(f"Sato-Tate {label}, p≤{cap}, n={len(th)}")
    ax.legend()
    dest = os.path.join(ROOT, "report", f"sato_tate_{label}_{cap}.png")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    fig.tight_layout()
    fig.savefig(dest, dpi=120)
    print(f"wrote {dest}")


def main():
    label = sys.argv[1] if len(sys.argv) > 1 else "11a1"
    cap = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    pairs = ellap(label, cap)
    # drop p | N for the ST measure (additive reduction still has a_p)
    th, skipped = angles(pairs)
    mean = sum(math.cos(t) for t in th) / len(th)
    print(f"{label} p≤{cap}: {len(th)} angles, mean cosθ={mean:.3f}, clip={skipped}")
    ascii_hist(th)
    maybe_png(label, cap, th)


if __name__ == "__main__":
    main()
