#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""I_{[0,1]} cubic Taylor with a proved |g'''| cap from lag amplitudes.

g = 2 e^{−3y/2} − θ_v. |g'''| ≤ K from |trig|≤1 on the six elementary
lags, no mesh of g. Then

    g(y) ≥ g'(0) y + g''(0) y²/2 − (K/6) y³   on [0,1].

a_lo = ½ w g_lo. Not a mesh. Not Weil. Not RH.

    python code/av_I01_gppp.py
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_I01_compare import a_from_g, g, g_p, g_pp, gauss_on  # noqa: E402
from av_I01_switch import I1L_LO, WINDOW, true_I01  # noqa: E402
from av_enclose import CST, p_of_v  # noqa: E402
from av_gauss import L16, V  # noqa: E402
from av_gpp import g_ppp, th_ppp  # noqa: E402

PI = math.pi
SQRT2 = math.sqrt(2.0)


def omega(k: int, L: float = L16) -> float:
    return 2.0 * PI * k / L


def th_ppp_amp(n: int, m: int, L: float = L16) -> float:
    """Uniform bound |∂_yyy θ_nm| from |sin|,|cos| ≤ 1."""
    if n > m:
        n, m = m, n
    if n == 0 and m == 0:
        return 0.0
    if n == 0:
        j = m
        w = omega(j, L)
        return 2.0 * (w ** 3) / (SQRT2 * PI * j)
    if n == m:
        w = omega(n, L)
        # 2 * (3 w²/L + w³ + w³/(2π n)), u ≤ 1
        return 2.0 * (3.0 * w * w / L + w ** 3 + (w ** 3) / (2.0 * PI * n))
    wn, wm = omega(n, L), omega(m, L)
    return (
        2.0
        * (n * (wn ** 3) + m * (wm ** 3))
        / (PI * (m * m - n * n))
    )


def K_hand(L: float = L16, v=V) -> dict:
    """K ≥ |g'''| on [0,∞): 6.75 + ∑ |v_n v_m| Amp(θ_nm''')."""
    amps = {}
    cap_theta = 0.0
    for n in range(3):
        for m in range(3):
            amp = th_ppp_amp(n, m, L)
            amps[f"{n}{m}"] = amp
            cap_theta += abs(v[n] * v[m]) * amp
    # |−6.75 e^{−3y/2} − θ'''| ≤ 6.75 + |θ'''|
    K = 6.75 + cap_theta
    return {
        "K": K,
        "cap_theta": cap_theta,
        "amps": amps,
        "exp_cap": 6.75,
    }


def cubic_lo(y: float, gp0: float, gpp0: float, K: float) -> float:
    if y <= 0.0:
        return 0.0
    return gp0 * y + 0.5 * gpp0 * y * y - (K / 6.0) * y ** 3


def run() -> dict:
    caps = K_hand()
    K = caps["K"]
    gp0 = g_p(0.0)
    gpp0 = g_pp(0.0)
    # sanity: measured |g'''| on [0,1] must sit under K
    ys = [i / 40.0 for i in range(41)]
    gppp_vals = [g_ppp(y) for y in ys]
    meas_abs = max(abs(t) for t in gppp_vals)
    under = meas_abs <= K + 1e-9

    def alo(y: float) -> float:
        return a_from_g(max(y, 1e-15), cubic_lo(y, gp0, gpp0, K))

    i_lo = gauss_on(alo, 1e-15, 1.0, 48)
    i_true = true_I01()
    gap = i_true - i_lo
    p = p_of_v()
    q_lo = CST + i_lo + I1L_LO - p
    # legal lower bound? cubic ≤ g on a sample
    sample_ok = all(
        cubic_lo(y, gp0, gpp0, K) <= g(y) + 1e-9 for y in ys if y > 0
    )
    closes = gap < WINDOW and gap > 0.0
    return {
        "K": K,
        "cap_theta": caps["cap_theta"],
        "amps": caps["amps"],
        "g_prime_0": gp0,
        "g_pp_0": gpp0,
        "meas_abs_gppp": meas_abs,
        "K_covers_sample": under,
        "cubic_below_g_sample": sample_ok,
        "I_true": i_true,
        "I_lo": i_lo,
        "gap": gap,
        "CST": CST,
        "P": p,
        "I1L_lo": I1L_LO,
        "Q_lo": q_lo,
        "window": WINDOW,
        "closes_window": closes,
        "step_taken": False,
        "verdict": "KILL",
        "why": (
            "Elementary |g'''| cap is a true inequality and is too crude "
            "for the ±0.003 A-window. Not a mesh. Not Weil."
        ),
    }


def step_is_taken() -> bool:
    return False


def main() -> int:
    print("I_{[0,1]} cubic Taylor, |g'''| by lag amplitudes; not Weil, not RH", flush=True)
    data = run()
    print(
        f"  K={data['K']:.4f}  |g'''|_meas={data['meas_abs_gppp']:.4f}  "
        f"covers={data['K_covers_sample']}",
        flush=True,
    )
    print(
        f"  I_true={data['I_true']:+.6f}  I_lo={data['I_lo']:+.6f}  "
        f"gap={data['gap']:+.6f}",
        flush=True,
    )
    print(
        f"  Q_lo={data['Q_lo']:+.6f}  closes={data['closes_window']}  "
        f"verdict={data['verdict']}",
        flush=True,
    )
    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "report",
        "av-I01-gppp.json",
    )
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
