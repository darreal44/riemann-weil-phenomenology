#!/usr/bin/env python3
"""Parallel Weyl harvest. One process per t-slice.

    python3 code/harvest_weyl_mp.py chi29 200 16

Third arg = workers (default 16). Writes zeros_{name}_weyl.pkl.
Safe to run after the serial script: existing zeros are kept.
"""
from __future__ import annotations

import os
import pickle
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from harvest_weyl import CHARS, Lam, expected_N, path  # noqa: E402
from kronecker import chi_tab  # noqa: E402
import mpmath as mp


def scan_slice(args):
    name, t_lo, t_hi, step = args
    cf = CHARS[name]
    q, a = cf["q"], cf["a"]
    tab = chi_tab(cf["d"], q)
    mp.mp.dps = 18
    t = mp.mpf(t_lo)
    prev = Lam(t, q, tab, a)
    found = []
    while t < t_hi:
        t2 = t + step
        cur = Lam(t2, q, tab, a)
        if prev * cur < 0:
            z = float(
                mp.findroot(lambda x: Lam(x, q, tab, a), (t, t2), solver="bisect")
            )
            found.append(z)
        prev, t = cur, t2
    return found


def main():
    name = sys.argv[1]
    tmax = float(sys.argv[2]) if len(sys.argv) > 2 else 200.0
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 16
    step = 0.04
    fn = path(name)
    Z = []
    if os.path.exists(fn):
        Z = sorted(float(x) for x in pickle.load(open(fn, "rb")))
    t_start = (Z[-1] + step) if Z else 0.01
    if t_start >= tmax:
        print(f"{name}: already to {Z[-1]:.1f}")
        return
    width = (tmax - t_start) / workers
    overlap = 2 * step
    slices = []
    for i in range(workers):
        lo = t_start + i * width
        hi = t_start + (i + 1) * width
        if i:
            lo -= overlap
        slices.append((name, max(t_start, lo), hi, step))
    print(
        f"{name}: {workers} workers, t={t_start:.2f}->{tmax}, have {len(Z)}",
        flush=True,
    )
    t0 = time.time()
    found = []
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(scan_slice, sl) for sl in slices]
        for i, fut in enumerate(as_completed(futs), 1):
            chunk = fut.result()
            found.extend(chunk)
            print(f"  slice done {i}/{workers} +{len(chunk)} {time.time()-t0:.0f}s", flush=True)
    Z = sorted(set(Z + found))
    pickle.dump(Z, open(fn, "wb"))
    T = Z[-1] if Z else 0
    q = CHARS[name]["q"]
    exp = float(expected_N(T, q)) if T else 0
    ratio = len(Z) / exp if exp else 0
    print(f"DONE n={len(Z)} gmax={T:.1f} Weyl={ratio:.2f} {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
