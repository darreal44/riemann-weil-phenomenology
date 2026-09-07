#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""True Off = Hankel − w₂ Θ. Lag split. Not Nehari. Not a take.

S_k identifies A_arch as ½/(n+m). For χ₃, w₂<0 so
Off = H + |w₂|Θ on the off-diagonal (same sign).

Each Hankel lag k has weights 1/(2(2n+k))∈ℓ², hence
HS / compact. Finite near-band H^{(K)} has

    ‖H^{(K)}‖₂ ≤ √((K−1)/(8(N−1)))   on ℓ²(n≥N).

Θ lags do not die in n (B₁). A window [N,N+L) never
sees H_ess=π/2 (Hartman lives across dyadic scales).
Long unions [32,M) with A_arch replaced by ½/(n+m)
(identified) test whether Off stays ~0.5 while H
climbs, or tracks H toward π/2.

    python code/ql_off_tail.py

Not RH. One L (χ₃, μ=3).
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_operator_bound import (  # noqa: E402
    CHARS,
    D2,
    LOG2,
    LOG3,
    N_GAUSS,
    N_PANELS,
    PI,
    _gauss_nodes,
    s0_of,
    w2_of,
)
from ql_schur_neumann import (  # noqa: E402
    HEAD,
    M_C,
    N_NEAR,
    Q,
    block_norm,
)
from ql_schur_tail import theta_hat  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
HALF_PI = 0.5 * PI
ALPHA = LOG2 / LOG3


def _nodes(s0: float):
    ys: list[float] = []
    ws: list[float] = []
    d2: list[float] = []
    h = LOG3 / N_PANELS
    for p in range(N_PANELS):
        y, w = _gauss_nodes(p * h, (p + 1) * h)
        ys.extend(y)
        ws.extend(w)
        d2.extend(D2(yi, s0) for yi in y)
    return (
        np.array(ys, float),
        np.array(ws, float),
        np.array(d2, float),
    )


def arch_off(n: int, m: int, ys, ws, d2) -> float:
    """−½ ∫ D₂ θ_nm on the Gauss mesh. Off-diagonal (F0=0)."""
    acc = 0.0
    for y, w, d in zip(ys, ws, d2):
        acc += w * d * theta_hat(n, m, float(y))
    return -0.5 * acc


def hankel_near_hs_bound(n0: int, k_max: int) -> float:
    """‖H^{(k_max)}‖₂ ≤ HS on ℓ²(n≥n0), lags 1..k_max.

    ‖‖_HS² ≤ (k_max)/8 · ∑_{n≥n0} n^{-2} ≤ k_max / (8(n0−1)).
    """
    if k_max < 1 or n0 <= 1:
        return 0.0
    return math.sqrt(k_max / (8.0 * (n0 - 1)))


def section_norms(
    n0: int, n1: int, w2: float, ys, ws, d2, k_split: int = 8
) -> dict:
    dim = n1 - n0
    off = np.zeros((dim, dim))
    arch = np.zeros((dim, dim))
    th = np.zeros((dim, dim))
    hank = np.zeros((dim, dim))
    b1 = np.zeros((dim, dim))
    near = np.zeros((dim, dim))
    far = np.zeros((dim, dim))
    hank_near = np.zeros((dim, dim))
    hank_far = np.zeros((dim, dim))
    for i, n in enumerate(range(n0, n1)):
        for m in range(n, n1):
            jj = m - n0
            a = 0.0 if n == m else arch_off(n, m, ys, ws, d2)
            t = 0.0 if n == m else theta_hat(n, m, LOG2)
            q = a - w2 * t
            arch[i, jj] = a
            arch[jj, i] = a
            th[i, jj] = t
            th[jj, i] = t
            k = m - n
            if n != m:
                h = 0.5 / (n + m)
                hank[i, jj] = h
                hank[jj, i] = h
                off[i, jj] = q
                off[jj, i] = q
                if k < k_split:
                    near[i, jj] = q
                    near[jj, i] = q
                    hank_near[i, jj] = h
                    hank_near[jj, i] = h
                else:
                    far[i, jj] = q
                    far[jj, i] = q
                    hank_far[i, jj] = h
                    hank_far[jj, i] = h
            if m == n + 1:
                b1[i, jj] = q
                b1[jj, i] = q
    hs_cap = hankel_near_hs_bound(n0, k_split - 1)
    return {
        "n0": n0,
        "n1": n1,
        "dim": dim,
        "k_split": k_split,
        "off": float(np.linalg.norm(off, 2)),
        "arch": float(np.linalg.norm(arch, 2)),
        "hankel": float(np.linalg.norm(hank, 2)),
        "theta": float(np.linalg.norm(th, 2)),
        "B1": float(np.linalg.norm(b1, 2)),
        "off_near": float(np.linalg.norm(near, 2)),
        "off_far": float(np.linalg.norm(far, 2)),
        "hank_near": float(np.linalg.norm(hank_near, 2)),
        "hank_far": float(np.linalg.norm(hank_far, 2)),
        "hank_near_hs_cap": hs_cap,
        "w2": float(w2),
        "half_pi": HALF_PI,
    }


def section_fast(n0: int, n1: int, w2: float, k_split: int = 8) -> dict:
    """Off = ½/(n+m) − w₂ Θ(log 2), closed form. n0≥1.

    S_k identifies A_arch as Hankel; skip Gauss.
    """
    if n0 < 1:
        raise ValueError("section_fast needs n0≥1")
    ns = np.arange(n0, n1, dtype=float)
    dim = n1 - n0
    n = ns[:, None]
    m = ns[None, :]
    diff = m - n
    nz = diff != 0
    hank = np.divide(0.5, n + m, out=np.zeros((dim, dim)), where=nz)
    s = np.sin((2.0 * PI / LOG3) * ns * LOG2)
    num = n * s[:, None] - m * s[None, :]
    den = PI * (m * m - n * n)
    th = np.divide(2.0 * num, den, out=np.zeros((dim, dim)), where=nz)
    off = hank - w2 * th
    kabs = np.abs(diff)
    near = np.where((kabs > 0) & (kabs < k_split), off, 0.0)
    far = np.where(kabs >= k_split, off, 0.0)
    hank_near = np.where((kabs > 0) & (kabs < k_split), hank, 0.0)
    hank_far = np.where(kabs >= k_split, hank, 0.0)
    b1 = np.where(kabs == 1, off, 0.0)
    hs_cap = hankel_near_hs_bound(n0, k_split - 1)
    return {
        "n0": n0,
        "n1": n1,
        "dim": dim,
        "k_split": k_split,
        "method": "hankel-id",
        "off": float(np.linalg.norm(off, 2)),
        "arch": float(np.linalg.norm(hank, 2)),
        "hankel": float(np.linalg.norm(hank, 2)),
        "theta": float(np.linalg.norm(th, 2)),
        "B1": float(np.linalg.norm(b1, 2)),
        "off_near": float(np.linalg.norm(near, 2)),
        "off_far": float(np.linalg.norm(far, 2)),
        "hank_near": float(np.linalg.norm(hank_near, 2)),
        "hank_far": float(np.linalg.norm(hank_far, 2)),
        "hank_near_hs_cap": hs_cap,
        "w2": float(w2),
        "half_pi": HALF_PI,
        "rev_tri": float(
            abs(np.linalg.norm(hank, 2) - abs(w2) * np.linalg.norm(th, 2))
        ),
        "tri": float(np.linalg.norm(hank, 2) + abs(w2) * np.linalg.norm(th, 2)),
    }


def b1_caps() -> dict:
    """Closed 2/π vs the quasi-periodic cap 2|sin(π α)|/π."""
    crude = 2.0 / PI
    sharp = 2.0 * abs(math.sin(PI * ALPHA)) / PI
    w2 = abs(w2_of(CHARS["chi3"]["d"]))
    return {
        "alpha": ALPHA,
        "theta_cap_2_over_pi": crude,
        "theta_cap_sin": sharp,
        "B1_thm": 4.0 * w2 / PI,
        "B1_sin": 2.0 * w2 * sharp,
        "w2": w2,
    }


def slo_with_off_far(off_far: float) -> dict:
    """Recompute χ₃ S_lo with a trial Off_far. Not a certified take."""
    dim = N_NEAR - HEAD
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(HEAD, N_NEAR)):
        for j, m in enumerate(range(HEAD, N_NEAR)):
            T[i, j] = Q("chi3", n, m)
    d = np.diag(T)
    A = (T - np.diag(d)) * np.outer(1.0 / np.sqrt(d), 1.0 / np.sqrt(d))
    rho_n = float(np.linalg.norm(A, 2))
    qmin_far = min(Q("chi3", n, n) for n in range(N_NEAR, M_C))
    rho_far = off_far / qmin_far
    b2 = 0.0
    w2 = w2_of(CHARS["chi3"]["d"])
    for n in range(HEAD, N_NEAR):
        qnn = Q("chi3", n, n)
        for m in range(N_NEAR, M_C):
            b2 += Q("chi3", n, m) ** 2 / (qnn * Q("chi3", m, m))
        b2 += 0.25 / max(n + M_C - 1, 1) / (qnn * qmin_far)
        if abs(w2) > 0.0:
            b2 += (2.0 * abs(w2) / PI) ** 2 / max(M_C - n - 1, 1) / (
                qnn * qmin_far
            )
    rho_b = math.sqrt(b2)
    rho = block_norm(rho_n, rho_b, rho_far)
    H = np.array(
        [[Q("chi3", i, j) for j in range(HEAD)] for i in range(HEAD)], float
    )
    C = np.array(
        [[Q("chi3", i, m) for m in range(HEAD, N_NEAR)] for i in range(HEAD)],
        float,
    )
    cdc = C @ np.diag(1.0 / d) @ C.T
    cfar = np.zeros((HEAD, HEAD))
    for k in range(N_NEAR, M_C):
        ck = np.array([Q("chi3", i, k) for i in range(HEAD)])
        cfar += np.outer(ck, ck) / Q("chi3", k, k)
    s_diag = float(np.linalg.eigvalsh(H - cdc)[0])
    s_lo = float(np.linalg.eigvalsh(H - (cdc + cfar) / (1.0 - rho))[0])
    return {
        "off_far": off_far,
        "rho_near": rho_n,
        "rho_B": rho_b,
        "rho_far": rho_far,
        "rho": rho,
        "s_diag": s_diag,
        "s_lo": s_lo,
        "qmin_far": qmin_far,
    }


def hankel_id_samples(ys, ws, d2) -> list[dict]:
    """A_arch ≈ ½/(n+m) on a few far pairs (S_k ⇒ Hankel)."""
    out = []
    for n, m in ((2, 39), (32, 33), (32, 47)):
        a = arch_off(n, m, ys, ws, d2)
        h = 0.5 / (n + m)
        out.append(
            {
                "n": n,
                "m": m,
                "arch": a,
                "hankel": h,
                "ratio": a / h,
            }
        )
    return out


def main() -> int:
    cf = CHARS["chi3"]
    s0 = s0_of(cf["a"])
    w2 = w2_of(cf["d"])
    ys, ws, d2 = _nodes(s0)
    caps = b1_caps()
    samples = hankel_id_samples(ys, ws, d2)
    chk = section_norms(32, 48, w2, ys, ws, d2)
    chk_f = section_fast(32, 48, w2)
    print(
        f"cross [32,48) Gauss Off={chk['off']:.6f}  "
        f"fast={chk_f['off']:.6f}  d={abs(chk['off']-chk_f['off']):.2e}",
        flush=True,
    )
    rows = []
    dyadic = []
    longu = []
    for n0, n1 in ((32, 48), (32, 64), (32, 80), (32, 96)):
        r = section_fast(n0, n1, w2)
        rows.append(r)
        print(
            f"[{r['n0']},{r['n1']}) dim={r['dim']}  "
            f"‖Off‖={r['off']:.3f}  ‖H‖={r['hankel']:.3f}  "
            f"‖Θ‖={r['theta']:.3f}  ‖B1‖={r['B1']:.3f}  "
            f"near8={r['off_near']:.3f} far8={r['off_far']:.3f}  "
            f"Hnear={r['hank_near']:.3f}≤{r['hank_near_hs_cap']:.3f}",
            flush=True,
        )
    for n0, n1 in (
        (32, 64),
        (64, 128),
        (96, 160),
        (128, 256),
        (256, 512),
    ):
        r = section_fast(n0, n1, w2)
        dyadic.append(r)
        print(
            f"dyadic [{r['n0']},{r['n1']})  "
            f"‖Off‖={r['off']:.3f}  ‖H‖={r['hankel']:.3f}  "
            f"‖Θ‖={r['theta']:.3f}  ‖B1‖={r['B1']:.3f}",
            flush=True,
        )
    union = None
    for n1 in (128, 192, 256, 384, 512):
        r = section_fast(32, n1, w2)
        longu.append(r)
        print(
            f"union [32,{n1}) dim={r['dim']}  "
            f"‖Off‖={r['off']:.3f}  ‖H‖={r['hankel']:.3f}  "
            f"‖Θ‖={r['theta']:.3f}  tri={r['tri']:.3f}  "
            f"rev={r['rev_tri']:.3f}",
            flush=True,
        )
        if n1 == 128:
            union = r
    print(
        f"w2={w2:.3f} (<0 ⇒ Off=H+|w2|Θ)  "
        f"B1 thm={caps['B1_thm']:.3f}  sin-cap={caps['B1_sin']:.3f}  "
        f"θ 2/π={caps['theta_cap_2_over_pi']:.3f}  "
        f"θ sin={caps['theta_cap_sin']:.3f}",
        flush=True,
    )
    for s in samples:
        print(
            f"  A({s['n']},{s['m']})={s['arch']:.6f}  "
            f"½/(n+m)={s['hankel']:.6f}  ratio={s['ratio']:.6f}",
            flush=True,
        )
    trial = slo_with_off_far(rows[-1]["off"])
    trial_u = slo_with_off_far(union["off"])
    trial_long = slo_with_off_far(longu[-1]["off"])
    print(
        f"trial Off_far={trial['off_far']:.3f}  ρ={trial['rho']:.3f}  "
        f"Slo={trial['s_lo']:+.4f}  (section substitute, not a take)",
        flush=True,
    )
    print(
        f"trial union128 Off_far={trial_u['off_far']:.3f}  ρ={trial_u['rho']:.3f}  "
        f"Slo={trial_u['s_lo']:+.4f}",
        flush=True,
    )
    print(
        f"trial union{longu[-1]['n1']} Off_far={trial_long['off_far']:.3f}  "
        f"ρ={trial_long['rho']:.3f}  Slo={trial_long['s_lo']:+.4f}",
        flush=True,
    )
    data = {
        "step_taken": False,
        "verdict": "KILL",
        "why": (
            "S_k identifies A_arch as Hankel ½/(n+m); "
            "w2<0 so Off=H+|w2|Θ; long unions [32,M) are "
            "truncated tails, not s1(Q_tail) on ℓ²(n≥32)"
        ),
        "w2_sign": "negative",
        "caps": caps,
        "hankel_id": samples,
        "cross_check": {
            "gauss_off": chk["off"],
            "fast_off": chk_f["off"],
            "abs_diff": abs(chk["off"] - chk_f["off"]),
        },
        "sections": rows,
        "dyadic": dyadic,
        "union": union,
        "long": longu,
        "trial_slo": trial,
        "trial_slo_union": trial_u,
        "trial_slo_long": trial_long,
        "half_pi": HALF_PI,
        "hankel_near_hs": {
            "n0": 32,
            "k_max": 7,
            "cap": hankel_near_hs_bound(32, 7),
        },
    }
    out = os.path.join(ROOT, "report", "ql-off-tail.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
