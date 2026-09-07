#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Multiprocess grid for scan_q_maass.assemble.

One job = one (name, mu). mpmath inside the job stays serial.
Not a faster single assemble.

    python code/scan_q_maass_mp.py
    python code/scan_q_maass_mp.py maass1,maass3 22,38 36 40 --workers 4

Windows: spawn. Use --workers 8 on the Threadripper.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import multiprocessing
import os
import sys
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan_q_maass import ALIAS, assemble  # noqa: E402


def _job(payload):
    name, mu, NB, dps = payload
    os.environ["OMP_NUM_THREADS"] = "1"
    lam0, ell, dt = assemble(name, float(mu), int(NB), int(dps))
    return {
        "name": name,
        "mu": float(mu),
        "NB": int(NB),
        "dps": int(dps),
        "lam0": float(lam0),
        "ell0": float(ell[0]) if ell else None,
        "seconds": float(dt),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("names", nargs="?", default="maass1")
    p.add_argument("mus", nargs="?", default="22,38")
    p.add_argument("NB", nargs="?", type=int, default=36)
    p.add_argument("dps", nargs="?", type=int, default=40)
    p.add_argument("--workers", type=int, default=0)
    args = p.parse_args()
    names = [x.strip() for x in args.names.split(",") if x.strip()]
    mus = [float(x) for x in args.mus.split(",") if x.strip()]
    ncpu = args.workers or min(len(names) * len(mus), os.cpu_count() or 4)
    jobs = [(n, m, args.NB, args.dps) for n in names for m in mus]
    print(
        f"jobs={len(jobs)} workers={ncpu} NB={args.NB} dps={args.dps} names={names} mus={mus}",
        flush=True,
    )
    t0 = time.time()
    rows = []
    ctx = multiprocessing.get_context("spawn")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=ncpu, mp_context=ctx
    ) as pool:
        futs = [pool.submit(_job, j) for j in jobs]
        for fut in concurrent.futures.as_completed(futs):
            rec = fut.result()
            rows.append(rec)
            print(
                f"  {rec['name']} mu={rec['mu']:.0f} lam0={rec['lam0']:.4e} "
                f"ell0={rec['ell0']} {rec['seconds']:.0f}s",
                flush=True,
            )
    rows.sort(key=lambda r: (r["name"], r["mu"]))
    dest = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "report",
        "scan-q-maass-mp.json",
    )
    payload = {
        "names": names,
        "mus": mus,
        "NB": args.NB,
        "dps": args.dps,
        "workers": ncpu,
        "rows": rows,
        "seconds": round(time.time() - t0, 3),
    }
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"wrote {dest}  wall={payload['seconds']}s", flush=True)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
