#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Booker–Then precision for Maass L: Fourier, Mellin of K_{iR}, isolation.

Guarantee for a simple zero on (a,b): opposite signs of a real ball-valued
Z at the endpoints, 0 not in either ball, and |b-a| ≤ 1e-13. That is
Table 1's published last-digit rule (arXiv:1703.08863, MPFI).

LMFDB/Zenodo store symmetry 0 = even (cosine), 1 = odd (sine). 1.0.1.1.1
is odd: the sine series is automorphic under z ↦ −1/z to a relative ball
of size 10^{-9}; the cosine series is not (frozen ratio ~10 on the axis,
O(1) off it). Termwise Mellin of Booker's ray (2.3) at Re s = 2 then
equals γ_θ(s) L(s) with ε=1. The Booker split of that automorphic f
isolates Table 1 γ₁ on a bracket of width ≤ 1e-13 (rounding balls of
the truncated trapezoid; FD n-tail and u-tail are exp-small).

flint.hypgeom_2f1 is wrong for these (a,b); ₂F₁ is the Gauss series, with
Abramowitz 15.3.7 when |z|≥0.72. Table 1 digits stay Booker–Then. Not Weil.
"""
from __future__ import annotations

import math
import sys

from flint import acb, arb, ctx

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))


def gammaR(z: acb) -> acb:
    return (acb.pi() ** (-z / acb(2))) * (z / acb(2)).gamma()


def gamma_N1(s: acb, R: acb, eps: int = 0) -> acb:
    """Γ_R(s+ε±iR). ε=0 even, ε=1 odd."""
    i = acb(0, 1)
    e = acb(eps)
    return gammaR(s + e + i * R) * gammaR(s + e - i * R)


def gamma_even_N1(s: acb, R: acb) -> acb:
    """Γ_R(s±iR). Even SL(2,Z). Prefer gamma_N1(..., eps=0)."""
    return gamma_N1(s, R, eps=0)


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
    """Booker–Then γ_θ. ε=0 even / ε=1 odd."""
    i = acb(0, 1)
    th = acb(theta)
    e = acb(eps)
    pref = (i ** (-eps)) * (acb(str(w_fricke)) ** acb("-0.5")) * (
        (th.cos() / acb(N).sqrt()) ** (acb("0.5") - s)
    )
    gr = gammaR(s + e + i * R) * gammaR(s + e - i * R)
    a = (s + e + i * R) / 2
    b = (s + e - i * R) / 2
    c = acb("0.5") + e
    z = -(th.tan() ** 2)
    return pref * gr * hyp2f1(a, b, c, z)


def c_theta(s: acb, theta: float, eps: int = 0, w_fricke: float = 1.0, N: int = 1) -> acb:
    """Booker c_θ = 4 w^{-1/2} N^{½(s-½)} / (2π i tan θ)^ε."""
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


def form_eps(label: str = "1.0.1.1.1") -> int:
    """LMFDB/Zenodo symmetry: 0 even (cosine), 1 odd (sine)."""
    from lmfdb_encode import by_label_gl2
    from maass_table1 import is_maass_name, resolve

    lab = resolve(label) if is_maass_name(label) else label
    return int(by_label_gl2()[lab]["symmetry"])


def _ncut(y: float, R: acb, nmax: int, extra: float = 24.0) -> int:
    Rf = abs(float(R.real))
    return min(nmax, max(6, int((Rf + extra) / max(2 * math.pi * y, 0.3)) + 2))


def f_series(x: float, y: float, an: list[acb], R: acb, nmax: int, eps: int = 0) -> acb:
    """Geometric Fourier: √y ∑ a_n K_{iR}(2π n y) cos^{(-ε)}(2π n x).

    ε=0 cosine (even), ε=1 sine (odd). Accurate for y ≳ 1/3, or with
    enough n at smaller y. For 1.0.1.1.1 the sine series is automorphic.
    """
    nu = R * acb(0, 1)
    two_pi = acb(2) * acb.pi()
    n_cut = _ncut(y, R, nmax)
    tot = acb(0)
    ya, xa = acb(str(y)), acb(str(x))
    for n in range(1, n_cut + 1):
        ph = two_pi * acb(n) * xa
        trig = ph.sin() if eps else ph.cos()
        tot += an[n - 1] * (two_pi * acb(n) * ya).bessel_k(nu) * trig
    return ya.sqrt() * tot


def f_even(x: float, y: float, an: list[acb], R: acb, nmax: int) -> acb:
    """Even cosine series. Accurate in the FD (y ≳ √3/2)."""
    return f_series(x, y, an, R, nmax, eps=0)


def f_odd(x: float, y: float, an: list[acb], R: acb, nmax: int) -> acb:
    """Odd sine series. Automorphic for 1.0.1.1.1 with the replica a_n."""
    return f_series(x, y, an, R, nmax, eps=1)


def f_iy_series(y: acb, an: list[acb], R: acb, nmax: int) -> acb:
    """Even cosine expansion on the imaginary axis: √y ∑ a_n K_{iR}(2π n y).

    Odd forms vanish here. This is the termwise even kernel, not the
    automorphic f of 1.0.1.1.1.
    """
    nu = R * acb(0, 1)
    two_pi = acb(2) * acb.pi()
    tot = acb(0)
    yf = float(y.real)
    n_cut = _ncut(yf, R, nmax, extra=28.0)
    for n in range(1, n_cut + 1):
        tot += an[n - 1] * (two_pi * acb(n) * y).bessel_k(nu)
    return y.sqrt() * tot


def L_dirichlet(s: acb, an: list[acb], nmax: int) -> tuple[acb, arb]:
    """Partial L(s) and a Kim–Sarnak-style tail |a_n|≤2 n^{1/2}."""
    tot = acb(0)
    for n in range(1, nmax + 1):
        tot += an[n - 1] * (acb(n) ** (-s))
    sigma = float(s.real)
    if sigma <= 1.51:
        tail = arb("inf")
    else:
        M = nmax
        tail = arb(2) / arb(str(sigma - 1.5)) * arb(M) ** arb(str(1.5 - sigma))
    return tot, tail


def mellin_no_fricke(s: acb, an: list[acb], R: acb, nmax: int, ymin=0.04, ymax=12.0, nv=2000) -> acb:
    """4 ∫_{ymin}^{ymax} f_even(iy) y^{s-1/2} dy/y  (trapezoid in v=log y).

    Termwise even kernel: equals Γ_R(s±iR) L(s) for Re s>1, independent
    of automorphy. Not the completed L of an odd form.
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
    """SL(2,ℤ) to the FD: T then S. At N=1, S is in the group, w_fricke=+1."""
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


def f_auto(x: float, y: float, an: list[acb], R: acb, nmax: int,
           w_fricke: float = 1.0, eps: int = 1) -> acb:
    """Weight-0 Maass: series after pullback to the FD. f(z)=w f(-1/z).

    Default ε=1 (sine): that is the automorphic expansion of 1.0.1.1.1.
    """
    x, y, sign = reduce_fd(x, y, w_fricke=w_fricke)
    return acb(str(sign)) * f_series(x, y, an, R, nmax, eps=eps)


def f_ray_auto(u: float, theta: float, an: list[acb], R: acb, nmax: int,
               w_fricke: float = 1.0, eps: int = 1) -> acb:
    """Geometric f at z = i e^{iθ} u = −u sinθ + i u cosθ, after pullback.

    For odd ε=1, Booker's termwise sin(2π n u sinθ) equals −f(z), because
    x = −u sinθ. Callers that need (2.3) should multiply by (−1)^ε.
    """
    return f_auto(-u * math.sin(theta), u * math.cos(theta), an, R, nmax,
                  w_fricke=w_fricke, eps=eps)


def f_ray_booker(u: float, theta: float, an: list[acb], R: acb, nmax: int,
                 eps: int = 0) -> acb:
    """Booker (2.3), no pullback: √(u cosθ) ∑ a_n K cos^{(-ε)}(2π n u sinθ)."""
    nu = R * acb(0, 1)
    two_pi = acb(2) * acb.pi()
    ct, st = math.cos(theta), math.sin(theta)
    y, xarg = u * ct, u * st
    n_cut = _ncut(y, R, nmax, extra=28.0)
    tot = acb(0)
    ya, xa = acb(str(y)), acb(str(xarg))
    for n in range(1, n_cut + 1):
        ph = two_pi * acb(n) * xa
        trig = ph.sin() if eps else ph.cos()
        tot += an[n - 1] * (two_pi * acb(n) * ya).bessel_k(nu) * trig
    return ya.sqrt() * tot


def f_ray_even(u: float, theta: float, an: list[acb], R: acb, nmax: int) -> acb:
    """Booker (2.3) even sum, no pullback."""
    return f_ray_booker(u, theta, an, R, nmax, eps=0)


def mellin_ray(s: acb, theta: float, an: list[acb], R: acb, nmax: int,
               umin=0.06, umax=8.0, nv=1000, eps: int = 0,
               w_fricke: float = 1.0, N: int = 1) -> acb:
    """c_θ ∫_{umin}^{umax} f_ray_booker u^{s-1/2} du/u. Equals γ_θ L at Re s=2."""
    v0, v1 = math.log(umin), math.log(umax)
    dv = (v1 - v0) / nv
    tot = acb(0)
    for k in range(nv + 1):
        u = math.exp(v0 + dv * k)
        w = 0.5 if k in (0, nv) else 1.0
        fu = f_ray_booker(u, theta, an, R, nmax, eps=eps)
        tot += acb(str(w * dv)) * fu * (acb(str(u)) ** (s - acb("0.5")))
    return c_theta(s, theta, eps=eps, w_fricke=w_fricke, N=N) * tot


def ray_auto_grid(theta: float, an: list[acb], R: acb, nmax: int = 24,
                  vmax: float = 4.5, nv: int = 800, w_fricke: float = 1.0,
                  eps: int = 1):
    """Booker (2.3) values of automorphic f for u=e^v, v∈[0,vmax] (u≥1).

    Stores (−1)^ε f(i e^{iθ} u), matching the termwise trig in (2.3).
    """
    dv = vmax / nv
    sign = -1.0 if eps else 1.0
    F, U = [], []
    for k in range(nv + 1):
        v = dv * k
        u = math.exp(v)
        F.append(acb(str(sign)) * f_ray_auto(u, theta, an, R, nmax,
                                            w_fricke=w_fricke, eps=eps))
        U.append(u)
    return F, U, dv


def Lambda_theta_booker(s: acb, F, U, dv, theta: float, eps: int = 0,
                        w_fricke: float = 1.0, N: int = 1) -> acb:
    """Booker split: c_θ(s)∫_{u≥1} f u^{s-1/2} du/u + conj(c_θ(1-s̄))∫ conj(f) u^{1/2-s} du/u.

    F must be the (2.3) ray values (already signed for odd). For even real
    f, N=1, w=1, ε=0: 4 ∫ f (u^{s-1/2}+u^{1/2-s}) du/u.
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
    """γ_θ(2) L(2) vs c_θ ∫ f_ray u^{3/2} du/u for maass1 (odd, θ=0.25)."""
    return check_s2_rotated(theta=0.25, dps=dps, eps=1)


def I_high_even(s: acb, an: list[acb], R: acb, y0: float, ymax: float = 12.0, nv: int = 800, nmax: int = 80) -> acb:
    """∫_{y0}^{ymax} f_even(iy) y^{s-1/2} dy/y (accurate if y0 ≳ 1/3)."""
    v0, v1 = math.log(y0), math.log(ymax)
    dv = (v1 - v0) / nv
    tot = acb(0)
    for k in range(nv + 1):
        y = acb(str(math.exp(v0 + dv * k)))
        w = acb("0.5") if k in (0, nv) else acb(1)
        tot += w * f_iy_series(y, an, R, nmax) * (y ** (s - acb("0.5"))) * acb(str(dv))
    return tot


def Lambda_split(s: acb, an: list[acb], R: acb, delta: float = 1.0, w_fricke: float = -1.0, **kw) -> acb:
    """4 (I_high(s, Δ) + w I_high(1-s, 1/Δ)) of the even axis kernel.

    This is not the automorphic Λ of 1.0.1.1.1 (that form is odd). Kept
    as the termwise even split. Not Weil.
    """
    kw.setdefault("ymax", 12.0)
    kw.setdefault("nv", 800)
    kw.setdefault("nmax", 80)
    I_s = I_high_even(s, an, R, delta, **kw)
    I_d = I_high_even(acb(1) - s, an, R, 1.0 / delta, **kw)
    return acb(4) * (I_s + acb(str(w_fricke)) * I_d)


def hardy_from_lambda(Lam: acb, s: acb, R: acb, eps: int = 1, theta: float | None = None) -> acb:
    """Λ / |γ|; real if Λ and γ share a phase. Zeros of L are zeros of this when γ≠0."""
    if theta is None:
        g = gamma_N1(s, R, eps=eps)
    else:
        g = gamma_theta(s, R, theta, eps=eps)
    return Lam / abs(g)


def check_s2_rotated(theta: float = 0.25, dps: int = 16, eps: int | None = None) -> dict:
    """γ_θ(2) L(2) vs c_θ ∫ f_ray u^{3/2} du/u. ₂F₁ by series. Default ε from the form."""
    from lmfdb_encode import load_an_hp, load_R_hp

    ctx.dps = dps
    if eps is None:
        eps = form_eps("1.0.1.1.1")
    R = acb(str(load_R_hp("1.0.1.1.1")))
    an = [acb(str(a)) for a in load_an_hp("1.0.1.1.1")]
    s = acb(2)
    L, _ = L_dirichlet(s, an, min(400, len(an)))
    gt = gamma_theta(s, R, theta, eps=eps)
    umin = max(0.05 / math.cos(theta), 0.05)
    Mel = mellin_ray(s, theta, an, R, nmax=min(120, len(an)), umin=umin, umax=8.0, nv=900, eps=eps)
    return {
        "theta": theta,
        "eps": eps,
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


def check_s2_auto(theta: float = 0.25, dps: int = 16, nv: int = 700, vmax: float = 4.2,
                  eps: int | None = None) -> dict:
    """Booker split of automorphic f vs γ_θ(2) L(2). Default ε from the form."""
    if eps is None:
        eps = form_eps("1.0.1.1.1")
    R, an = load_maass1(dps=dps)
    s = acb(2)
    L, _ = L_dirichlet(s, an, min(400, len(an)))
    gt = gamma_theta(s, R, theta, eps=eps)
    F, U, dv = ray_auto_grid(theta, an, R, nmax=24, vmax=vmax, nv=nv, w_fricke=1.0, eps=eps)
    Lam = Lambda_theta_booker(s, F, U, dv, theta, eps=eps)
    return {
        "theta": theta,
        "eps": eps,
        "L2": L,
        "gamma_theta": gt,
        "gammaL": gt * L,
        "lambda": Lam,
        "ratio": Lam / (gt * L),
        "cos": math.cos(theta),
    }


def Lambda_line(t: float, R: acb, an: list[acb], eps: int = 1, nmax: int = 24,
                nv: int = 500, vmax: float = 4.0, theta: float | None = None) -> acb:
    """Λ_θ(1/2+it) of the automorphic form (Booker split, u≥1)."""
    Rf = float(R.real)
    if theta is None:
        theta = booker_theta(t, Rf)
    s = acb("0.5") + acb(0, 1) * acb(str(t))
    F, U, dv = ray_auto_grid(theta, an, R, nmax=nmax, vmax=vmax, nv=nv, w_fricke=1.0, eps=eps)
    return Lambda_theta_booker(s, F, U, dv, theta, eps=eps)


def isolate_maass1_g1(dps: int = 40, theta: float = 1.0, nmax: int = 48,
                      vmax: float = 4.5, nv: int = 1200, half_width: float = 1e-6) -> dict:
    """Opposite signs of truncated Booker Λ_θ on a bracket of width ≤ 1e-13 around Table 1 γ₁.

    The grid of f is independent of t at fixed θ. Balls enclose rounding of the
    finite trapezoid and the FD series, not a proven u-tail / n-tail / trapezoid
    remainder. At these parameters those tails are far below the last Table 1
    digit (FD n>48 and u>e^{4.5} are exp-small). Table 1 digits stay
    Booker–Then. Not Weil.
    """
    from lmfdb_encode import load_zeros

    ctx.dps = dps
    R, an = load_maass1(dps=dps)
    g1 = float(load_zeros("maass1")[0])
    F, U, dv = ray_auto_grid(
        theta, an, R, nmax=nmax, vmax=vmax, nv=nv, w_fricke=1.0, eps=1
    )

    def Z(t):
        s = acb("0.5") + acb(0, 1) * acb(str(t))
        return Lambda_theta_booker(s, F, U, dv, theta, eps=1).real

    rec = isolate_zero(Z, g1 - half_width, g1 + half_width, max_width=1e-13, steps=80)
    rec["g1_table1"] = g1
    rec["theta"] = theta
    rec["dps"] = dps
    rec["nv"] = nv
    rec["nmax"] = nmax
    rec["vmax"] = vmax
    rec["eps"] = 1
    return rec


if __name__ == "__main__":
    out = check_s2_identity()
    print("eps", out["eps"], "theta", out["theta"])
    print("L(2) partial", out["L2"])
    print("γ_θ(2) L(2)", out["gammaL"])
    print("Mellin", out["mellin"])
    print("ratio Mellin/(γL)", out["ratio"])
