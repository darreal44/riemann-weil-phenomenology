# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Booker Mellin identity at s=2, sine automorphy, isolation helper."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))

from flint import acb, arb, ctx

import maass_booker as mb
from lmfdb_encode import load_an_hp, load_R_hp, load_zeros, load_zeros_hp


def test_form_eps_zenodo_encoding():
    """Zenodo: 0=even (cosine), 1=odd (sine). 1.0.1.1.1 is odd; 1.0.1.3.1 even."""
    assert mb.form_eps("1.0.1.1.1") == 1
    assert mb.form_eps("maass1") == 1
    assert mb.form_eps("1.0.1.3.1") == 0


def test_s2_mellin_matches_gamma_L():
    """c_θ ∫ f_ray u^{3/2} du/u = γ_θ(2) L(2) for 1.0.1.1.1, ε=1, θ=0.25."""
    out = mb.check_s2_identity(dps=16)
    assert out["eps"] == 1
    err = abs(out["ratio"] - 1)
    assert float(err.real.mid()) < 2e-3, out["ratio"]


def test_s2_rotated_mellin_matches_gamma_theta_L():
    """Same identity, explicit θ=0.25."""
    out = mb.check_s2_rotated(theta=0.25, dps=16, eps=1)
    err = abs(out["ratio"] - 1)
    assert float(err.real.mid()) < 3e-3, out["ratio"]


def test_isolate_refuses_without_sign_change():
    def F(t):
        return acb(t) * acb(t) + acb(1)

    rec = mb.isolate_zero(F, 1.0, 2.0, max_width=1e-13)
    assert rec["certified"] is False


def test_isolate_certifies_a_simple_real_root():
    def F(t):
        return acb(str(t)) - acb("1.5")

    rec = mb.isolate_zero(F, 1.0, 2.0, max_width=1e-13)
    assert rec["certified"] is True
    assert rec["width"] <= 1e-13
    assert abs(rec["mid"] - 1.5) < 1e-13


def test_s2_split_minus_near_gamma_L():
    """Even-axis unbalanced split, w=-1, Δ=1: ~even-γ L at s=2. Not automorphic Λ."""
    ctx.dps = 16
    R = acb(str(load_R_hp("1.0.1.1.1")))
    an = [acb(str(a)) for a in load_an_hp("1.0.1.1.1")]
    s = acb(2)
    L, _ = mb.L_dirichlet(s, an, 400)
    g = mb.gamma_even_N1(s, R)
    Lam = mb.Lambda_split(s, an, R, delta=1.0, w_fricke=-1.0, ymax=10.0, nv=600, nmax=40)
    err = abs(Lam / (g * L) - 1)
    assert float(err.real.mid()) < 0.02, Lam / (g * L)


def test_table1_digits_are_booker_then_not_ours():
    """Guarantee for Table 1 γ is Booker–Then's MPFI list, already on disk."""
    z = load_zeros("maass1")
    hp = load_zeros_hp("maass1")
    assert abs(float(z[0]) - 17.0249420759926) < 1e-12
    assert str(hp[0]).startswith("17.0249420759926")


def test_sine_series_is_automorphic():
    """Raw sine series of 1.0.1.1.1 equals itself at S(z). Cosine does not."""
    ctx.dps = 16
    R = acb(str(load_R_hp("1.0.1.1.1")))
    an = [acb(str(a)) for a in load_an_hp("1.0.1.1.1")]
    x, y = 0.2, 1.1
    n2 = x * x + y * y
    xi, yi = -x / n2, y / n2
    s1 = mb.f_odd(x, y, an, R, 24)
    s2 = mb.f_odd(xi, yi, an, R, 24)
    err = abs(s1 / s2 - 1)
    assert float(err.real.mid()) < 1e-6, s1 / s2
    c1 = mb.f_even(x, y, an, R, 24)
    c2 = mb.f_even(xi, yi, an, R, 24)
    errc = abs(c1 / c2 - 1)
    assert float(errc.real.mid()) > 0.1, c1 / c2


def test_auto_involution_and_fd_series():
    """S-pullback is an involution; in the FD it is the sine series."""
    ctx.dps = 16
    R = acb(str(load_R_hp("1.0.1.1.1")))
    an = [acb(str(a)) for a in load_an_hp("1.0.1.1.1")]
    x, y = 0.2, 1.1
    f1 = mb.f_auto(x, y, an, R, 24, eps=1)
    n2 = x * x + y * y
    f2 = mb.f_auto(-x / n2, y / n2, an, R, 24, eps=1)
    err = abs(f1 / f2 - 1)
    assert float(err.real.mid()) < 1e-6, f1 / f2
    fs = mb.f_odd(0.1, 1.2, an, R, 24)
    fa = mb.f_auto(0.1, 1.2, an, R, 24, eps=1)
    err2 = abs(fa / fs - 1)
    assert float(err2.real.mid()) < 1e-6, fa / fs


def test_s2_auto_split_matches_gamma_theta_L():
    """Booker split of automorphic sine f equals γ_θ L at s=2 (odd, θ=0.25)."""
    out = mb.check_s2_auto(theta=0.25, dps=16, nv=500, vmax=3.8, eps=1)
    err = abs(out["ratio"] - 1)
    assert float(err.real.mid()) < 0.05, out["ratio"]


def test_isolate_maass1_g1_table1():
    """Enclosed odd Λ_θ changes sign on a ≤1e-13 bracket around Table 1 γ₁."""
    rec = mb.isolate_maass1_g1()
    assert rec["certified"] is True, rec
    assert rec["width"] <= 1e-13
    assert rec["sa"] != rec["sb"] and rec["sa"] != 0 and rec["sb"] != 0
    assert abs(rec["mid"] - rec["g1_table1"]) < 1e-13
    rem = rec["remainder_rad"]
    assert float(rem.mid()) < 1e-20, rem


def test_harvest_maass1_first_two_match_table1():
    """Enclosed harvest finds Table 1 γ1 and γ2 of maass1, |b-a|≤1e-13."""
    from lmfdb_encode import load_zeros

    z = load_zeros("maass1")
    out = mb.harvest_form("maass1", T=20.0, tmin=16.0, dt=0.15, theta=1.0)
    ok = [r for r in out["zeros"] if r.get("certified")]
    assert len(ok) >= 2, out["n_certified"]
    assert abs(ok[0]["mid"] - float(z[0])) < 1e-12
    assert abs(ok[1]["mid"] - float(z[1])) < 1e-12
    assert ok[0]["width"] <= 1e-13 and ok[1]["width"] <= 1e-13


def test_enclosed_g1_matches_table1():
    """Harvested enclosed lists start at Booker–Then γ₁ (L-zeros, not gamma-dips)."""
    from lmfdb_encode import load_zeros

    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code")
    for name in ("maass1", "maass2", "maass3", "maass4", "maass5"):
        path = os.path.join(root, f"zeros_{name}_enclosed.txt")
        assert os.path.exists(path), path
        mids = [
            float(ln)
            for ln in open(path, encoding="utf-8")
            if ln.strip() and ln.strip()[0].isdigit()
        ]
        z = load_zeros(name)
        assert abs(mids[0] - float(z[0])) < 1e-10, (name, mids[0], float(z[0]))


def test_remainder_tails_are_below_last_digit():
    """n-tail in the FD and u-tail at vmax=4.5, θ=1 are far below 10^{-13}."""
    from flint import acb

    ntail = mb.series_n_tail(math.sqrt(3.0) / 2.0, 19)
    assert float(ntail.mid()) < 1e-40
    utail = mb.u_tail_integrand(4.5, 1.0)
    assert float(utail.mid()) < 1e-100
    x = acb("6.0")
    k0 = x.bessel_k(acb(0)).real
    bnd = (acb.pi() / (acb(2) * x)).sqrt().real * (-x.real).exp()
    assert float((bnd - k0).mid()) > 0.0
