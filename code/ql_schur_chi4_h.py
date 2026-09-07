#!/usr/bin/env python3
"""Schur tail for χ₄ at larger h. w₂=0. T infinite.

Grid h=2,4,8,16,20,24. Off_T = Hankel π/2 + HS rem (#58).
C = Gauss to M=40 plus Hankel tail 1/(2(i+j))², not the
R-inflated #58 tail. Not Galerkin of W_L. Not RH.

    python code/ql_schur_chi4_h.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import CHARS, PI, s0_of, w2_of  # noqa: E402
from ql_schur_tail import (  # noqa: E402
    HILBERT_HANKEL,
    Q_nm,
    r_frob_bound,
)

HEADS = (2, 4, 8, 16, 20, 24)
M_C = 40
N_DIAG = 40
NAME = "chi4"

_cache: dict[tuple[int, int], float] = {}


def Q(n: int, m: int, q: int, s0: float, w2: float) -> float:
    key = (min(n, m), max(n, m))
    if key not in _cache:
        _cache[key] = Q_nm(n, m, q, s0, w2)
    return _cache[key]


def hankel_c_tail_sq(i: int, m0: int) -> float:
    """∑_{j≥m0} [1/(2(i+j))]² (i≥1). i=0: |Q_0j| ≤ 1.8/(√2 π j)."""
    if i == 0:
        a = 1.8 / (math.sqrt(2.0) * PI)
        return (a * a) / max(m0 - 1, 1)
    return 0.25 / max(m0 + i - 1, 1)


def row_at_h(h: int, q: int, s0: float, w2: float) -> dict:
    H = np.zeros((h, h))
    qmax_nm = 0.0
    for i in range(h):
        for j in range(i, h):
            v = Q(i, j, q, s0, w2)
            H[i, j] = v
            H[j, i] = v
            if i != j and i >= 1:
                qmax_nm = max(qmax_nm, abs(v) * (i + j))
    lamH = float(np.linalg.eigvalsh(H)[0])
    diags = [Q(n, n, q, s0, w2) for n in range(h, N_DIAG)]
    qmin = min(diags)
    qmin_at = h + int(np.argmin(np.array(diags)))
    c_ex = 0.0
    for i in range(h):
        for j in range(h, M_C):
            v = Q(i, j, q, s0, w2)
            c_ex += v * v
            if i >= 1:
                qmax_nm = max(qmax_nm, abs(v) * (i + j))
    c_tail = sum(hankel_c_tail_sq(i, M_C) for i in range(h))
    c_frob = math.sqrt(c_ex + c_tail)
    rf = r_frob_bound(h)
    hankel = 0.5 * HILBERT_HANKEL + 1.0 / (4.0 * h)
    delta = qmin - (hankel + rf)
    beta = lamH - (c_frob * c_frob) / delta if delta > 0.0 else None
    return {
        "h": h,
        "lamH": lamH,
        "qmin": qmin,
        "qmin_at": qmin_at,
        "c_exact_sq": c_ex,
        "c_tail_sq": c_tail,
        "c_frob": c_frob,
        "hankel_op": hankel,
        "r_frob": rf,
        "delta": delta,
        "beta": beta,
        "beta_pos": bool(beta is not None and beta > 0.0),
        "qmax_times_sum": qmax_nm,
    }


def step_is_taken() -> bool:
    return False


def run() -> dict:
    cf = CHARS[NAME]
    q, s0, w2 = cf["q"], s0_of(cf["a"]), w2_of(cf["d"])
    assert w2 == 0.0
    _cache.clear()
    rows = [row_at_h(h, q, s0, w2) for h in HEADS]
    by = {r["h"]: r for r in rows}
    pos = [r["h"] for r in rows if r["beta_pos"]]
    h_star = [16, 20] if (not by[16]["beta_pos"] and by[20]["beta_pos"]) else None
    pred_ok = (
        (not by[2]["beta_pos"])
        and (not by[16]["beta_pos"])
        and by[20]["beta_pos"]
        and by[24]["beta_pos"]
        and all(r["qmax_times_sum"] <= 0.5000001 for r in rows)
    )
    return {
        "name": NAME,
        "heads": list(HEADS),
        "M_C": M_C,
        "step_taken": step_is_taken(),
        "chi4_taken": bool(pos),
        "h_star": h_star,
        "first_positive_h": pos[0] if pos else None,
        "verdict": "SURVIVE" if pred_ok else "KILL",
        "rows": rows,
        "cache_size": len(_cache),
    }


def main() -> int:
    print(
        "χ₄ Schur; h=2,4,8,16,20,24; Hankel C tail; T infinite; not Galerkin",
        flush=True,
    )
    data = run()
    for r in data["rows"]:
        b = f"{r['beta']:+.4f}" if r["beta"] is not None else "−∞"
        print(
            f"  h={r['h']:2d}  lamH={r['lamH']:.5f}  qmin={r['qmin']:.3f}  "
            f"δ={r['delta']:+.3f}  ‖C‖F={r['c_frob']:.3f}  β={b}  "
            f"|Q|(n+m)≤{r['qmax_times_sum']:.6f}",
            flush=True,
        )
    print(
        f"chi4_taken={data['chi4_taken']}  h*={data['h_star']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "ql-schur-chi4-h.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0 if data["verdict"] == "SURVIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
