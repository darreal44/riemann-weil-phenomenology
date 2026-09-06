"""Exact split of the cosine-hat Fourier transform.

    hat ψ(γ) = 2 ψ(0) sin(γ L / 2) / γ  +  r(γ)

with ψ(0) = L^{−1/2}(v₀ + √2 ∑_{n≥1} v_n) and

    r(γ) = 2√2 sin(γ L/2) L^{−1/2} ∑_{n≥1} v_n ω_n² / (γ (γ² − ω_n²)),

ω_n = 2π n / L. Identity of finite trigonometric polynomials;
no RH, no zeros. The edge heuristic drops r.
"""
from __future__ import annotations

import math


def omega(n, L):
    return 2.0 * math.pi * n / L


def hat_n(n, g, L):
    s = math.sin(g * L / 2.0)
    sL = math.sqrt(L)
    if n == 0:
        return 2.0 * s / (g * sL)
    om = omega(n, L)
    return math.sqrt(2.0 / L) * s * 2.0 * g / (g * g - om * om)


def psi0(v, L):
    return (v[0] + math.sqrt(2.0) * sum(v[1:])) / math.sqrt(L)


def hat_psi(v, g, L):
    return sum(v[n] * hat_n(n, g, L) for n in range(len(v)))


def remainder_r(v, g, L):
    s = math.sin(g * L / 2.0)
    acc = 0.0
    for n in range(1, len(v)):
        om2 = omega(n, L) ** 2
        acc += v[n] * om2 / (g * (g * g - om2))
    return 2.0 * math.sqrt(2.0) * s / math.sqrt(L) * acc


def jump_term(v, g, L):
    return 2.0 * psi0(v, L) * math.sin(g * L / 2.0) / g
