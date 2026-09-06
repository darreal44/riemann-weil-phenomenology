"""Raised-cosine lag kernel θ_{f₁} in closed form.

Unit e₁ = (√2, −1, 0)/√3 in the three-hat frame. For y ∈ [0, L],
ω = 2π/L,

    θ_{f₁}(y) = (2/3)(1 − y/L)(2 + cos(ω y)) + (1/π) sin(ω y).

Independent of μ except through t = y/L. Proof: expand
∑_{n,m=0,1} (e₁)_n (e₁)_m th_{nm}(y) using the elementary table
of th (H_2plane_independent.th). Positivity on [0, L] is a
one-variable calculus fact (notes/demonstrations.md).
"""
from __future__ import annotations

import math


def theta_f1(y, L):
    if y <= 0:
        return 2.0
    if y >= L:
        return 0.0
    t = y / L
    th = 2 * math.pi * t
    return (2.0 / 3.0) * (1.0 - t) * (2.0 + math.cos(th)) + math.sin(th) / math.pi


def g_reduced(t):
    """θ_{f₁}(t L) as a function of t ∈ [0, 1], L-free."""
    return theta_f1(t, 1.0)
