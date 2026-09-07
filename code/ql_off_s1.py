#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Proved s₁(Off_Q) on the tail. Replaces the Hankel+Θ split.

Off = H + R − w₂ Θ_off on ℓ²(n≥N), H_nm = ½/(n+m) (n≠m).

    ‖H‖ ≤ π/2          Hilbert 1894 / Hartman (tail ess = π/2)
    ‖R‖_F ≤ r_frob(N)  IPP remainder
    ‖Θ‖ ≤ 1            y = log 2 ≥ L/2
    1/(4N)             Hankel diagonal not in Off

Upper (operator norm):

    s1_off_q_upper(N,w₂) = π/2 + 1/(4N) + r_frob(N) + |w₂|

Lower (essential norm):

    s1_off_q_lower(w₂) = π/2 − |w₂|

because ‖A+B‖_ess ≥ ‖A‖_ess − ‖B‖. So s₁≤0.8 and s₁≤1.0
are false. Named in report/drop-half-pi.md. Not a take.

    python code/ql_off_s1.py

Not RH. One L.
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import CHARS, PI, w2_of  # noqa: E402
from ql_schur_tail import HILBERT_HANKEL, r_frob_bound  # noqa: E402
from ql_theta_tail import theta_op_bound  # noqa: E402

HALF_PI = 0.5 * PI


def s1_off_q_upper(n0: int, w2: float) -> float:
    """Proved ‖Off_Q‖ on ℓ²(n≥n0). Same number as the old Off_far split."""
    return (
        0.5 * HILBERT_HANKEL
        + 1.0 / (4.0 * n0)
        + r_frob_bound(n0)
        + abs(w2) * theta_op_bound()
    )


def s1_off_q_lower(w2: float) -> float:
    """Proved ‖Off_Q‖_ess ≥ π/2 − |w₂|‖Θ‖."""
    return 0.5 * HILBERT_HANKEL - abs(w2) * theta_op_bound()


def main() -> int:
    w2 = w2_of(CHARS["chi3"]["d"])
    n0 = 32
    up = s1_off_q_upper(n0, w2)
    lo = s1_off_q_lower(w2)
    split = (
        0.5 * HILBERT_HANKEL
        + 1.0 / (4.0 * n0)
        + r_frob_bound(n0)
        + abs(w2) * theta_op_bound()
    )
    print(
        f"χ₃ w2={w2:.3f}  N={n0}  "
        f"s1_upper={up:.4f}  s1_lower={lo:.4f}  "
        f"split={split:.4f}  ½π={HALF_PI:.4f}",
        flush=True,
    )
    flip_need = up - HALF_PI
    print(
        f"s1≤0.6 dead: 0.6 < lower={lo:.3f}  "
        f"s1≤0.8 false  s1≤1.0 false  (drop-half-pi.md)",
        flush=True,
    )
    print(
        f"S_lo flip needs Off_far≲{flip_need:.3f} < lower={lo:.3f}  "
        f"no proved s1 can flip χ₃",
        flush=True,
    )
    data = {
        "step_taken": False,
        "verdict": "KILL",
        "why": (
            "The proved s1(Off_Q) is the triangle π/2+|w2|; "
            "the ess lower π/2-|w2| kills 0.8 and 1.0. ½π stays."
        ),
        "w2": w2,
        "n0": n0,
        "s1_upper": up,
        "s1_lower": lo,
        "split": split,
        "half_pi": HALF_PI,
        "cran_06": 0.6,
        "cran_08": 0.8,
        "cran_10": 1.0,
        "cran_06_below_lower": 0.6 < lo,
        "cran_08_below_lower": 0.8 < lo,
        "cran_10_below_lower": 1.0 < lo,
        "upper_equals_split": abs(up - split) < 1e-15,
        "flip_need": up - HALF_PI,
        "flip_below_lower": (up - HALF_PI) < lo,
    }
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-off-s1.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}  verdict={data['verdict']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
