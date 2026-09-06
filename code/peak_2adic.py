#!/usr/bin/env python3
"""Fmat 2-adic peak at λ=2 from campaign_2adic_large.jsonl.

The grid is a window of width ~Λ^{-2}, not a Dirac.
mass_at_two('inverse') = √2 is the Thm 4 target this
climb heads toward. Bombieri and module twist are
different Haar.

    python code/peak_2adic.py
"""
from __future__ import annotations

import json
import math
import os

SQRT2 = math.sqrt(2)
BOMBIERI = math.log(2) / SQRT2
MODULE = 1.0 / SQRT2
INVERSE = SQRT2


def load_rows(path=None):
    if path is None:
        path = os.path.join(
            os.path.dirname(__file__), "..", "report", "campaign_2adic_large.jsonl"
        )
    rows = []
    for line in open(path, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            if "w2" in r:
                rows.append(r)
    return rows


def series(Lam: float, rows=None):
    """(cpu, w2) for one Λ, sorted by cpu."""
    if rows is None:
        rows = load_rows()
    s = sorted(
        [(int(r["cpu"]), float(r["w2"])) for r in rows if float(r["Lam"]) == float(Lam)]
    )
    return s


def climbs(seq) -> bool:
    if len(seq) < 2:
        return False
    w = [x[1] for x in seq]
    return all(w[i] < w[i + 1] for i in range(len(w) - 1))


def through_locked(seq) -> bool:
    """Walks through Bombieri 0.490; may or may not pass 0.707."""
    w = [x[1] for x in seq]
    return w[0] < BOMBIERI < w[-1]


def resolution(Lam: float, cpu: int) -> float:
    """h / (Λ^{-2}) = Λ²/cpu. Smaller is finer relative to peak width."""
    return float(Lam) ** 2 / float(cpu)


def main() -> None:
    rows = load_rows()
    print(f"{'Λ':>4} {'cpu':>5} {'h':>8} {'Λ²/cpu':>8} {'w2':>8}")
    print(f"Bombieri {BOMBIERI:.4f}  module {MODULE:.4f}  inverse {INVERSE:.4f}")
    for Lam in (16.0, 24.0, 32.0):
        seq = series(Lam, rows)
        for cpu, w in seq:
            print(
                f"{Lam:4.0f} {cpu:5d} {1/cpu:8.4f} {resolution(Lam, cpu):8.2f} {w:8.3f}"
            )
        if seq:
            print(
                f"  climb={climbs(seq)}  through Bombieri={through_locked(seq)}"
            )


if __name__ == "__main__":
    main()
