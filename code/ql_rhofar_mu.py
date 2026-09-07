#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""ρ_far autopsy, χ₃, μ on (5, 7]. N_NEAR=32. No S_lo.

Identified Q_pk, cap √2. Not a take. Not RH.

    python code/ql_rhofar_mu.py
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_neumann_pk import clear_cache, far_pieces  # noqa: E402
from ql_operator_bound import LOG2  # noqa: E402
from ql_q_pk import interior_ns  # noqa: E402
from ql_theta_sqrt2 import in_sqrt2_band  # noqa: E402

MUS = (5.0, 5.5, 6.0, 6.5, 7.0)
N_NEAR = 32


def step_is_taken() -> bool:
    return False


def run() -> dict:
    clear_cache()
    rows = []
    for mu in MUS:
        far = far_pieces("chi3", mu, N_NEAR)
        far["mu"] = mu
        far["L"] = math.log(mu)
        far["ns"] = interior_ns(mu)
        far["log2_in_band"] = in_sqrt2_band(LOG2, far["L"])
        far["rho_far_ge1"] = bool(far["rho_far"] >= 1.0)
        rows.append(far)
    by = {r["mu"]: r for r in rows}
    pred_ok = (
        by[5.0]["ns"] == [2, 3, 4]
        and by[7.0]["ns"] == [2, 3, 4, 5]
        and by[7.0]["t_atoms"] > by[5.0]["t_atoms"]
        and by[5.0]["rho_far"] < 1.0
        and by[7.0]["rho_far"] > 1.0
    )
    return {
        "name": "chi3",
        "n_near": N_NEAR,
        "mus": list(MUS),
        "rho_far_crosses": by[5.0]["rho_far"] < 1.0 < by[7.0]["rho_far"],
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
    }


def main() -> int:
    print(
        "ρ_far autopsy χ₃ (5,7] N_NEAR=32; not a take; not RH",
        flush=True,
    )
    data = run()
    print(
        "mu    ns           t_atoms  qmin_far  hilbert  ρ_far",
        flush=True,
    )
    for r in data["rows"]:
        print(
            f"{r['mu']:.1f}  {str(r['ns']):12s}  {r['t_atoms']:.4f}  "
            f"{r['qmin_far']:.4f}  {r['hilbert']:.4f}  {r['rho_far']:.3f}",
            flush=True,
        )
    print(
        f"crosses={data['rho_far_crosses']}  verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-rhofar-mu.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
