#!/usr/bin/env python3
"""Prime-side Q with all n=p^k, 1<n<μ. Weil Λ(n)χ(n)n^{-1/2}.

At μ=3 this is Q_nm (only n=2). At μ=5, n=4=2² enters.
Not the archimedean identification. Not RH.

    python code/ql_q_pk.py
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kronecker import kronecker  # noqa: E402
from log2_log3_step import interior_primes  # noqa: E402
from ql_operator_bound import LOG3, s0_of, w2_of  # noqa: E402
from ql_schur_mu35 import Q_window  # noqa: E402
from ql_schur_tail import Q_nm, theta_hat  # noqa: E402

Q3, D3, A3 = 3, -3, 1
S0 = s0_of(A3)


def lambda_von_mangoldt(n: int) -> float:
    """Λ(n)=log p if n=p^k, else 0."""
    if n < 2:
        return 0.0
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            return math.log(p) if x == 1 else 0.0
        p = 3 if p == 2 else p + 2
    return math.log(n)


def interior_ns(mu: float) -> list[int]:
    """n with 1<n<μ and Λ(n)≠0 (primes and prime powers)."""
    hi = math.floor(float(mu) - 1e-15)
    return [n for n in range(2, int(hi) + 1) if lambda_von_mangoldt(n) > 0.0]


def wn(d: int, n: int) -> float:
    """χ(n) Λ(n) n^{-1/2}."""
    lam = lambda_von_mangoldt(n)
    if lam == 0.0:
        return 0.0
    return kronecker(d, n) * lam / math.sqrt(n)


def Q_pk(
    n: int, m: int, q: int, s0: float, d: int, L: float, mu: float
) -> float:
    """Arch minus every interior prime power. μ=3 recovers Q_nm."""
    acc = Q_nm(n, m, q, s0, 0.0, L)
    for k in interior_ns(mu):
        acc -= wn(d, k) * theta_hat(n, m, math.log(k), L)
    return acc


def step_is_taken() -> bool:
    return False


def run() -> dict:
    ns3 = interior_ns(3.0)
    ns35 = interior_ns(3.5)
    ns5 = interior_ns(5.0)
    qnm = Q_nm(0, 0, Q3, S0, w2_of(D3), LOG3)
    pk3 = Q_pk(0, 0, Q3, S0, D3, LOG3, 3.0)
    win35 = Q_window(0, 0, Q3, S0, D3, math.log(3.5), 3.5)
    pk35 = Q_pk(0, 0, Q3, S0, D3, math.log(3.5), 3.5)
    L5 = math.log(5.0)
    win5 = Q_window(0, 0, Q3, S0, D3, L5, 5.0)
    pk5 = Q_pk(0, 0, Q3, S0, D3, L5, 5.0)
    dH00 = pk5 - win5
    pred_ok = (
        ns3 == [2]
        and ns35 == [2, 3]
        and ns5 == [2, 3, 4]
        and abs(pk3 - qnm) < 1e-14
        and abs(pk35 - win35) < 1e-14
        and dH00 < -0.05
        and interior_primes(5.0) == [2, 3]
    )
    return {
        "ns3": ns3,
        "ns35": ns35,
        "ns5": ns5,
        "w4": wn(D3, 4),
        "mu3_matches_qnm": abs(pk3 - qnm) < 1e-14,
        "mu35_matches_window": abs(pk35 - win35) < 1e-14,
        "H00_shift_mu5": dH00,
        "step_taken": step_is_taken(),
        "verdict": "SURVIVE" if pred_ok else "KILL",
    }


def main() -> int:
    print("Q_pk: primes and p^k; μ=3 = Q_nm; n=4 at μ=5", flush=True)
    data = run()
    print(
        f"  ns3={data['ns3']} ns35={data['ns35']} ns5={data['ns5']}",
        flush=True,
    )
    print(
        f"  w4={data['w4']:.6f}  dH00(μ=5)={data['H00_shift_mu5']:+.6f}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-q-pk.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
