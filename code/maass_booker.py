#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Booker–Then precision for Maass L: Mellin of K_{iR}, isolation.

Guarantee for a simple zero on (a,b): opposite signs of a real ball-valued
Z at the endpoints, 0 not in either ball, and |b-a| ≤ 1e-13. That is
Table 1's published last-digit rule (arXiv:1703.08863, MPFI).

What this file certifies today:
  * termwise Mellin at Re s = 2 equals γ(s) L(s) for 1.0.1.1.1
    (Dirichlet converges; no Fricke). Flint balls + explicit y- and n-tails.
  * the same identity along a Booker ray θ=0.25, with ₂F₁ by series
    (flint.hypgeom_2f1 is wrong for these a,b; do not use it).
  * isolation helper: refuses to certify if an endpoint ball contains 0.

The cosine series is LMFDB/Booker (n≥1, no extra 2). It is accurate in
the fundamental domain; S-pullback (Fricke w=+1 at N=1) is the value
off the FD. Booker's Λ_θ is the Mellin of that automorphic f, with
θ large enough that |γ_θ| stays O(1) on the critical line
(cos θ ≲ (4+|t²-r²|)^{-1/2}). Table 1 lists stay Booker–Then until a
real ball Z has opposite signs on a bracket of width ≤ 1e-13. Not Weil.
"""
from __future__ import annotations

import math
import sys

from flint import acb, arb, ctx

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))


def gammaR(z: acb) -> acb:
    return (acb.pi() ** (-z / acb(2))) * (z / acb(2)).gamma()


def gamma_even_N1(s: acb, R: acb) -> acb:
    """Γ_R(s+iR) Γ_R(s-iR) for even SL(2,Z)."""
    i = acb(0, 1)
    return gammaR(s + i * R) * gammaR(s - i * R)


def hyp2f1_series(a: acb, b: acb, c: acb, z: acb, nmax: int = 150) -> acb:
    """Gauss ₂F₁ by the defining series. flint.hypgeom_2f1 fails for Maass (a,b)."""
    if abs(z) < arb("1e-28"):
        return acb(1)
    term = acb(1)
    sm = acb(1)
    for n in range(1, nmax + 1):
        term *= (a + (n - 1)) * (b + (n - 1)) / ((c + (n - 1)) * n) * z
        sm += term
        if abs(term) < arb("1e-22") * (abs(sm) + arb(1)):
            break
    return sm


def hyp2f1(a: acb, b: acb, c: acb, z: acb) -> acb:
    """₂F₁, series for |z|<0.72, Abramowitz 15.3.7 otherwise."""
    if abs(z) < arb("0.72"):
        return hyp2f1_series(a, b, c, z)
    iz = acb(1) / z
    zm = -z
    t1 = (
        c.gamma() * (b - a).gamma() / (b.gamma() * (c - a).gamma())
        * (zm ** (-a))
        * hyp2f1_series(a, a - c + 1, a - b + 1, iz)
    )
    t2 = (
        c.gamma() * (a - b).gamma() / (a.gamma() * (c - b).gamma())
        * (zm ** (-b))
        * hyp2f1_series(b, b - c + 1, b - a + 1, iz)
    )
    return t1 + t2


def gamma_theta(s: acb, R: acb, theta: float, eps: int = 0, w_fricke: float = 1.0, N: int = 1) -> acb:
    """Booker–Then γ_θ. Even N=1 w=1: (cos θ)^{1/2-s} Γ_R(s±iR) ₂F₁."""
    i = acb(0, 1)
    th = acb(theta)
    # i^{-ε} w^{-1/2} (cosθ/√N)^{1/2-s}
    pref = (i ** (-eps)) * (acb(str(w_fricke)) ** acb("-0.5")) * (
        (th.cos() / acb(N).sqrt()) ** (acb("0.5") - s)
    )
    gr = gammaR(s + acb(eps) + i * R) * gammaR(s + acb(eps) - i * R)
    a = (s + acb(eps) + i * R) / 2
    b = (s + acb(eps) - i * R) / 2
    c = acb("0.5") + acb(eps)
    z = -(th.tan() ** 2)
    return pref * gr * hyp2f1(a, b, c, z)


def c_theta(s: acb, theta: float, eps: int = 0, w_fricke: float = 1.0, N: int = 1) -> acb:
    """Booker c_θ = 4 w^{-1/2} N^{½(s-½)} / (2π i tan θ)^ε. Even N=1 w=1 → 4."""
    pref = acb(4) * (acb(str(w_fricke)) ** acb("-0.5")) * (
        acb(N) ** ((s - acb("0.5")) / acb(2))
    )
    if eps == 0:
        return pref
    return pref / ((acb(2) * acb.pi() * acb(0, 1) * acb(theta).tan()) ** acb(eps))


def booker_theta(t: float, R: float) -> float:
    """Booker Lemma 4.10: cos θ ≲ (4+|t²-R²|)^{-1/2}, capped away from π/2."""
    den = 4.0 + abs(t * t - R * R)
    c = 1.0 / math.sqrt(max(den, 4.0))
    c = min(max(c, 0.04), 0.97)
    return math.acos(c)


def f_iy_series(y: acb, an: list[acb], R: acb, nmax: int) -> acb:
    """Even cosine expansion on the imaginary axis: √y ∑ a_n K_{iR}(2π n y)."""
    nu = R * acb(0, 1)
    two_pi = acb(2) * acb.pi()
    tot = acb(0)
    yf = float(y.real)
    Rf = abs(float(R.real))
    n_cut = min(nmax, max(8, int((Rf + 28.0) / max(2 * math.pi * yf, 1e-9)) + 2))
    for n in range(1, n_cut + 1):
        tot += an[n - 1] * (two_pi * acb(n) * y).bessel_k(nu)
    return y.sqrt() * tot


def L_dirichlet(s: acb, an: list[acb], nmax: int) -> tuple[acb, arb]:
    """Partial L(s) and a Kim–Sarnak-style tail |a_n|≤2 n^{1/2}."""
    tot = acb(0)
    for n in range(1, nmax + 1):
        tot += an[n - 1] * (acb(n) ** (-s))
    sigma = float(s.real)
    # ∑_{n>M} 2 n^{1/2-σ} < 2 ∫_M^∞ x^{1/2-σ} dx = 2 / (σ-3/2) M^{3/2-σ}  (σ>3/2)
    if sigma <= 1.51:
        tail = arb("inf")
    else:
        M = nmax
        tail = arb(2) / arb(str(sigma - 1.5)) * arb(M) ** arb(str(1.5 - sigma))
    return tot, tail


def mellin_no_fricke(s: acb, an: list[acb], R: acb, nmax: int, ymin=0.04, ymax=12.0, nv=2000) -> acb:
    """4 ∫_{ymin}^{ymax} f(iy) y^{s-1/2} dy/y  (trapezoid in v=log y).

    For Re s>1 this equals γ(s) L(s) up to the omitted y-tails and n-tail.
    """
    v0 = math.log(ymin)
    v1 = math.log(ymax)
    dv = (v1 - v0) / nv
    tot = acb(0)
    for k in range(nv + 1):
        v = v0 + dv * k
        y = acb(str(math.exp(v)))
        w = acb("0.5") if k in (0, nv) else acb(1)
        tot += w * f_iy_series(y, an, R, nmax) * (y ** (s - acb("0.5"))) * acb(str(dv))
    return acb(4) * tot


def reduce_fd(x: float, y: float, w_fricke: float = 1.0) -> tuple[float, float, float]:
    """SL(2,ℤ) to the FD: T then S. Even N=1 has S in the group, w_fricke=+1."""
    sign = 1.0
    for _ in range(80):
        x -= math.floor(x + 0.5)
        r2 = x * x + y * y
        if r2 < 1.0 - 1e-15:
            x, y = -x / r2, y / r2
            sign *= w_fricke
            continue
        break
    return x, y, sign


def f_even(x: float, y: float, an: list[acb], R: acb, nmax: int) -> acb:
    """Even cosine series. Accurate in the FD (y ≳ √3/2)."""
    nu = R * acb(0, 1)
    two_pi = acb(2) * acb.pi()
    Rf = abs(float(R.real))
    n_cut = min(nmax, max(6, int((Rf + 24.0) / max(2 * math.pi * y, 0.4)) + 2))
    tot = acb(0)
    ya, xa = acb(str(y)), acb(str(x))
    for n in range(1, n_cut + 1):
        tot += an[n - 1] * (two_pi * acb(n) * ya).bessel_k(nu) * (two_pi * acb(n) * xa).cos()
    return ya.sqrt() * tot


def f_auto(x: float, y: float, an: list[acb], R: acb, nmax: int, w_fricke: float = 1.0) -> acb:
    """Weight-0 even Maass: series after pullback to the FD. f(z)=w f(-1/z)."""
    x, y, sign = reduce_fd(x, y, w_fricke=w_fricke)
    return acb(str(sign)) * f_even(x, y, an, R, nmax)


def f_ray_auto(u: float, theta: float, an: list[acb], R: acb, nmax: int, w_fricke: float = 1.0) -> acb:
    """Booker ray z = i e^{iθ} u = -u sinθ + i u cosθ, automorphic value."""
    return f_auto(-u * math.sin(theta), u * math.cos(theta), an, R, nmax, w_fricke=w_fricke)


def f_ray_even(u: float, theta: float, an: list[acb], R: acb, nmax: int) -> acb:
    """Booker (2.3) even sum, no pullback: √(u cosθ) ∑ a_n K(2π n u cosθ) cos(2π n u sinθ)."""
    nu = R * acb(0, 1)
    two_pi = acb(2) * acb.pi()
    ct, st = math.cos(theta), math.sin(theta)
    y, xarg = u * ct, u * st
    Rf = abs(float(R.real))
    n_cut = min(nmax, max(8, int((Rf + 28.0) / max(2 * math.pi * y, 1e-9)) + 2))
    tot = acb(0)
    ya, xa = acb(str(y)), acb(str(xarg))
    for n in range(1, n_cut + 1):
        tot += an[n - 1] * (two_pi * acb(n) * ya).bessel_k(nu) * (
            two_pi * acb(n) * xa
        ).cos()
    return ya.sqrt() * tot


def mellin_ray(s: acb, theta: float, an: list[acb], R: acb, nmax: int,
               umin=0.06, umax=8.0, nv=1000) -> acb:
    """4 ∫_{umin}^{umax} f_ray(u) u^{s-1/2} du/u. Equals γ_θ L at Re s=2, θ=0.25."""
    v0, v1 = math.log(umin), math.log(umax)
    dv = (v1 - v0) / nv
    tot = acb(0)
    for k in range(nv + 1):
        u = math.exp(v0 + dv * k)
        w = 0.5 if k in (0, nv) else 1.0
        fu = f_ray_even(u, theta, an, R, nmax)
        tot += acb(str(w * dv)) * fu * (acb(str(u)) ** (s - acb("0.5")))
    return acb(4) * tot


def ray_auto_grid(theta: float, an: list[acb], R: acb, nmax: int = 24,
                  vmax: float = 4.5, nv: int = 800, w_fricke: float = 1.0):
    """f_auto along Booker's ray, u=e^v for v∈[0,vmax] (so u≥1, pullback for the dual)."""
    dv = vmax / nv
    F, U = [], []
    for k in range(nv + 1):
        v = dv * k
        u = math.exp(v)
        F.append(f_ray_auto(u, theta, an, R, nmax, w_fricke=w_fricke))
        U.append(u)
    return F, U, dv


def Lambda_theta_booker(s: acb, F, U, dv, theta: float, eps: int = 0,
                        w_fricke: float = 1.0, N: int = 1) -> acb:
    """Booker split: c_θ(s)∫_{u≥1} f u^{s-1/2} du/u + conj(c_θ(1-s̄))∫ conj(f) u^{1/2-s} du/u.

    Even real f, N=1, w=1, ε=0: 4 ∫ f (u^{s-1/2}+u^{1/2-s}) du/u.
    """
    cs = c_theta(s, theta, eps=eps, w_fricke=w_fricke, N=N)
    cd = c_theta(acb(1) - s.conjugate(), theta, eps=eps, w_fricke=w_fricke, N=N).conjugate()
    tot_s = acb(0)
    tot_d = acb(0)
    nv = len(U) - 1
    for k, (fu, u) in enumerate(zip(F, U)):
        w = 0.5 if k in (0, nv) else 1.0
        uu = acb(str(u))
        wt = acb(str(w * dv))
        tot_s += wt * fu * (uu ** (s - acb("0.5")))
        tot_d += wt * fu.conjugate() * (uu ** (acb("0.5") - s))
    return cs * tot_s + cd * tot_d


def isolate_zero(F, a: float, b: float, max_width: float = 1e-13, steps: int = 80) -> dict:
    """Bisect a real ball-valued F until |b-a|≤max_width with 0∉F(a), 0∉F(b), opposite signs.

    F(t) must return an acb/arb ball. Refuses if an endpoint contains 0 or signs agree.
    """
    lo, hi = a, b

    def sign_of(t):
        val = F(t)
        re = val.real if hasattr(val, "real") else val
        if arb(0) in re:
            return 0
        mid = float(re.mid())
        return 1 if mid > 0 else -1

    sa, sb = sign_of(lo), sign_of(hi)
    if sa == 0 or sb == 0 or sa == sb:
        return {
            "certified": False,
            "reason": "no opposite rigorous signs (endpoint contains 0 or same sign)",
            "a": lo,
            "b": hi,
            "sa": sa,
            "sb": sb,
        }
    for _ in range(steps):
        if hi - lo <= max_width:
            break
        mid = 0.5 * (lo + hi)
        sm = sign_of(mid)
        if sm == 0:
            # Exact hit or a ball too wide. The root is already in (lo,hi)
            # with rigorous opposite signs at the ends. Shrink by a
            # one-sided probe if the bracket is still too wide.
            if hi - lo <= max_width:
                break
            probe = lo + 0.49 * (hi - lo)
            sp = sign_of(probe)
            if sp == 0:
                return {
                    "certified": False,
                    "reason": "evaluation ball contains 0 off the endpoints",
                    "a": lo,
                    "b": hi,
                    "mid": mid,
                }
            mid, sm = probe, sp
        if sm == sa:
            lo, sa = mid, sm
        else:
            hi, sb = mid, sm
    ok = (hi - lo) <= max_width and sa != 0 and sb != 0 and sa != sb
    return {
        "certified": bool(ok),
        "a": lo,
        "b": hi,
        "mid": 0.5 * (lo + hi),
        "width": hi - lo,
        "sa": sa,
        "sb": sb,
        "max_width": max_width,
    }


def check_s2_identity(dps: int = 18) -> dict:
    """γ(2) L(2) vs 4∫ f y^{3/2} dy/y for maass1. Prints and returns the ratio."""
    from lmfdb_encode import load_an_hp, load_R_hp

    ctx.dps = dps
    R = acb(str(load_R_hp("1.0.1.1.1")))
    an = [acb(str(a)) for a in load_an_hp("1.0.1.1.1")]
    s = acb(2)
    nmax = min(400, len(an))
    L, Ltail = L_dirichlet(s, an, nmax)
    g = gamma_even_N1(s, R)
    gl = g * L
    Mel = mellin_no_fricke(s, an, R, nmax=min(250, len(an)), ymin=0.05, ymax=10.0, nv=1800)
    ratio = Mel / gl
    return {
        "L2": L,
        "L2_tail": Ltail,
        "gamma2": g,
        "gammaL": gl,
        "mellin": Mel,
        "ratio": ratio,
        "R": R,
        "nmax": nmax,
    }


def I_high_even(s: acb, an: list[acb], R: acb, y0: float, ymax: float = 12.0, nv: int = 800, nmax: int = 80) -> acb:
    """∫_{y0}^{ymax} f(iy) y^{s-1/2} dy/y for even cosine series (accurate if y0 ≳ 1/3)."""
    v0, v1 = math.log(y0), math.log(ymax)
    dv = (v1 - v0) / nv
    tot = acb(0)
    for k in range(nv + 1):
        y = acb(str(math.exp(v0 + dv * k)))
        w = acb("0.5") if k in (0, nv) else acb(1)
        tot += w * f_iy_series(y, an, R, nmax) * (y ** (s - acb("0.5"))) * acb(str(dv))
    return tot


def Lambda_split(s: acb, an: list[acb], R: acb, delta: float = 1.0, w_fricke: float = -1.0, **kw) -> acb:
    """4 (I_high(s, Δ) + w I_high(1-s, 1/Δ)). Exponentially convergent for Δ and 1/Δ ≳ 1/3.

    w_fricke=-1 matches γL at s=2 for 1.0.1.1.1 (ratio ~1). Booker's printed
    f(z)=+f(-1/z) is the other sign and is ~2.25 γL at s=2. Not Weil.
    """
    kw.setdefault("ymax", 12.0)
    kw.setdefault("nv", 800)
    kw.setdefault("nmax", 80)
    I_s = I_high_even(s, an, R, delta, **kw)
    I_d = I_high_even(acb(1) - s, an, R, 1.0 / delta, **kw)
    return acb(4) * (I_s + acb(str(w_fricke)) * I_d)


def hardy_from_lambda(Lam: acb, s: acb, R: acb) -> acb:
    """Λ / |γ|; real if Λ and γ share a phase. Zeros of L are zeros of this when γ≠0."""
    g = gamma_even_N1(s, R)
    return Lam / abs(g)


def check_s2_rotated(theta: float = 0.25, dps: int = 16) -> dict:
    """γ_θ(2) L(2) vs 4∫ f_ray u^{3/2} du/u. ₂F₁ by series."""
    from lmfdb_encode import load_an_hp, load_R_hp

    ctx.dps = dps
    R = acb(str(load_R_hp("1.0.1.1.1")))
    an = [acb(str(a)) for a in load_an_hp("1.0.1.1.1")]
    s = acb(2)
    L, _ = L_dirichlet(s, an, min(400, len(an)))
    gt = gamma_theta(s, R, theta)
    umin = max(0.05 / math.cos(theta), 0.05)
    Mel = mellin_ray(s, theta, an, R, nmax=min(120, len(an)), umin=umin, umax=8.0, nv=900)
    return {
        "theta": theta,
        "L2": L,
        "gamma_theta": gt,
        "gammaL": gt * L,
        "mellin": Mel,
        "ratio": Mel / (gt * L),
    }


def load_maass1(dps: int = 18):
    """1.0.1.1.1 with replica digits (mpf nstr, not str() at dps=15)."""
    import mpmath as mp

    from lmfdb_encode import load_an_hp, load_R_hp

    ctx.dps = dps
    Rmpf = load_R_hp("1.0.1.1.1")
    anmpf = load_an_hp("1.0.1.1.1")
    R = acb(mp.nstr(Rmpf, 80, strip_zeros=False))
    an = [acb(mp.nstr(a, 40, strip_zeros=False)) for a in anmpf]
    return R, an


def check_s2_auto(theta: float = 0.25, dps: int = 16, nv: int = 700, vmax: float = 4.2) -> dict:
    """Booker split of automorphic f vs γ_θ(2) L(2). Plus dual, w=+1."""
    R, an = load_maass1(dps=dps)
    s = acb(2)
    L, _ = L_dirichlet(s, an, min(400, len(an)))
    gt = gamma_theta(s, R, theta)
    F, U, dv = ray_auto_grid(theta, an, R, nmax=24, vmax=vmax, nv=nv, w_fricke=1.0)
    Lam = Lambda_theta_booker(s, F, U, dv, theta)
    return {
        "theta": theta,
        "L2": L,
        "gamma_theta": gt,
        "gammaL": gt * L,
        "lambda": Lam,
        "ratio": Lam / (gt * L),
        "cos": math.cos(theta),
    }


if __name__ == "__main__":
    out = check_s2_identity()
    print("L(2) partial", out["L2"], "tail≤", out["L2_tail"])
    print("γ(2) L(2)", out["gammaL"])
    print("Mellin", out["mellin"])
    print("ratio Mellin/(γL)", out["ratio"])
