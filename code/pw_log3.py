#!/usr/bin/env python3
"""Paley–Wiener class of type log 3, versus Galerkin V_N.

W_L is even L² on a window of length L = log 3. Cosine hats V_N
are nested with dense union in W_L. The (log 2, log 3] step is
c_L^* = inf_{W_L} Q_L / ||f||² ≥ 0, not Q > 0 on one V_N.

    python code/pw_log3.py
"""
from __future__ import annotations

import concurrent.futures
import math
import multiprocessing
import os
import sys

LOG2 = math.log(2)
LOG3 = math.log(3)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def galerkin_takes_the_class() -> bool:
    """A PSD certificate on V_N does not take W_L. Courant: the other way."""
    return False


def step_is_taken() -> bool:
    """c_L^* ≥ 0 on W_{log 3} is open. Not RH (one L)."""
    return False


def nested_courant(lams: list[float]) -> bool:
    """λ_min(V_N) is nonincreasing in N, up to a relative 3% for quadrature."""
    if len(lams) < 2:
        return True
    for a, b in zip(lams, lams[1:]):
        if b > a * 1.03 + 1e-18:
            return False
    return True


def _chi_job(payload):
    name, mu, NB, dps = payload
    from scan_s import assemble

    lam, ell, dt = assemble(name, mu, NB, dps)
    return ("chi", name, NB, float(lam), float(ell[0]), dt)


def _zeta_job(payload):
    mu, NB, dps = payload
    from spectro_zeta import run
    import mpmath as mp

    lam, ell = run(mp.mpf(mu), NB, dps, 12, K=2)
    return ("zeta", "zeta", NB, float(lam), float(ell[0]), 0.0)


def ladder(workers: int | None = None) -> list[dict]:
    """Prime-side λ_min at μ=3, several N, χ₅ / χ₄ / ζ. Parallel."""
    jobs_chi = []
    for name in ("chi5", "chi4", "chi3"):
        for NB, dps in ((8, 28), (16, 30), (24, 32), (32, 35)):
            jobs_chi.append((name, 3.0, NB, dps))
    jobs_z = [(3.0, 8, 28), (3.0, 16, 30), (3.0, 24, 32)]
    ncpu = os.cpu_count() or 4
    njob = len(jobs_chi) + len(jobs_z)
    workers = max(1, min(int(workers or njob), ncpu, njob))
    rows = []
    ctx = multiprocessing.get_context("spawn")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=ctx
    ) as pool:
        futs = [pool.submit(_chi_job, j) for j in jobs_chi]
        futs += [pool.submit(_zeta_job, j) for j in jobs_z]
        for fut in concurrent.futures.as_completed(futs):
            kind, name, NB, lam, ell0, dt = fut.result()
            rows.append(
                {
                    "kind": kind,
                    "name": name,
                    "NB": NB,
                    "N": NB + 1,
                    "lam0": lam,
                    "ell0": ell0,
                    "dt": dt,
                }
            )
            print(
                f"  {name:5s} N={NB+1:2d}  lam0={lam:.6e}  ell={ell0:.3f}",
                flush=True,
            )
    rows.sort(key=lambda r: (r["name"], r["NB"]))
    return rows


def main() -> None:
    print(f"L = log 3 = {LOG3:.6f}; interior prime 2; class step taken: {step_is_taken()}")
    print(f"Galerkin takes the class: {galerkin_takes_the_class()}")
    rows = ladder()
    by = {}
    for r in rows:
        by.setdefault(r["name"], []).append(r)
    for name, rs in by.items():
        lams = [r["lam0"] for r in rs]
        print(f"{name}: lam0 = {[f'{x:.4e}' for x in lams]}  nested={nested_courant(lams)}")
        print(f"         all positive: {all(x > 0 for x in lams)}")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
