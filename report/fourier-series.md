# Fourier series of the window

## The basis

scan_s / music_zeros expand even functions on the Weil window
[-L/2, L/2], L = log μ, as

    f(x) = a0 / √L  +  Σ_{n≥1} a_n √(2/L) cos(2π n x / L).

The frequencies are ω_n = 2π n / L. Nyquist in the dual is
ν = 2π / L = ω_1: one cosine per Nyquist cell of PW_{L/2}.
The hat of the n-th bar at a zero γ is the formula `chat_f`
in music_zeros.py — a Dirichlet kernel, not an independent
mystery.

This *is* the Fourier series of the window. Q and the Gram
are the Gram matrix of those hats at Γ (prime side vs zero
side).

## v0 as a series

The dumped modes have N_eff ≈ 1.7 and k̄ ≈ 0.5: v0 is
essentially a0 plus a1. Higher harmonics of the *same*
series are the O(1) eigenvectors (k̄ = 6–22), the
“vibrations” of `fluctuations-excitations.md`. The Fourier
series of the singlet is a slow cosine. The node in the
charged pair is a node of that cosine in the dual variable γ.

## PW as Fourier transforms

F ∈ PW_τ means F = hat f with f ∈ L²[-τ, τ]. Here τ = L/2,
so the Weil window *is* the support of f. Completeness of
{cos ω_n} on that window is ordinary Fourier series on an
interval. Sampling of F at Γ is then the question whether
the values F(γ) determine f, i.e. whether Γ samples PW_τ —
Landau / Beurling / DS, already written.

## What Fourier series does not add

A new density. A new mass at p=2. A new C(χ). It names the
basis we already diagonalize. The only number it contributes
is the identification ω_1 = ν, which we have used since the
first scan_s.
