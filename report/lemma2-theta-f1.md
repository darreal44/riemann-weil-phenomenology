# Pairing kernel of the raised cosine

Unit vector e₁ = (√2, −1, 0)/√3.
Lag kernel of f₁ against itself, L = log μ,
ω = 2π/L:

    θ_{f₁}(y)
    = (2/3)(1 − y/L) [ 2 + cos(ω y) ]
      + (1/π) sin(ω y)     for y ∈ [0, L]
    = 0                     at y = L.

Elementary, positive, decreasing
on (0, L) for L = log 16:

| p^k | y | θ_{f₁}(y) |
|---|---|---|
| 2 | 0.693 | 1.318 |
| 3 | 1.099 | 0.678 |
| 4 | 1.386 | 0.333 |
| 5 | 1.609 | 0.160 |
| 7 | 1.946 | 0.034 |
| 8 | 2.079 | 0.015 |
| ≥9 | | < 0.007 |

## Prime-side form on this one vector

    Q(f₁,f₁) = Arch(f₁) − Σ_{n≤μ} χ(n) Λ(n) n^{-1/2} θ_{f₁}(log n).

Nine terms at μ = 16. The weights
Λ(n)/√n are (log 2)/√2 ≈ 0.490,
(log 3)/√3 ≈ 0.634, (log 2)/2 = 0.347,
… and χ only flips signs.

On χ₅ (χ(2)=χ(3)=−1) the first two
terms are *plus* 0.490·1.318 + 0.634·0.678
= 0.646 + 0.430 = 1.076, matching
the earlier table of Primes|ker to
the digit. Arch(f₁) sits at −1.18
on the same window; the difference
after the whole sum is 10^{-3} on
this single direction, 10^{-6} after
the 2-plane is optimised.

## A bound that does not work

θ ≥ 0, so dropping all but {2,3,4}
gives Q from above or below according
to the signs of χ, with an error
O(Σ_{n≥5} Λ(n) n^{-1/2} θ(log n))
≤ 0.03 on μ=16. That error is 10⁴
times λ_min(H|ker). A truncation of
the Euler product cannot see 10^{-6}.

The cancellation is Arch against the
*whole* short sum, in both
directions of the 2-plane at once.
Any proof has to keep the
archimedean integral and the two
modes together.

## What is closed

θ_{f₁} is closed. θ_{f₂} is the same
recipe with hats {0,1,2}. The 2×2
matrix of lag kernels is a 2×2 of
elementary functions of y. Arch is
the only piece still written as a
quadrature (Gamma / Sonin kernel
in `scan_s`). That quadrature, on
a two-mode bump, is the remaining
analytic object.
