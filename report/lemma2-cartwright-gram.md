# Cartwright product and PW-Gram on Λ_L

τ = L/2. Λ_L = zeros below the last
hat. λ_k = k π/τ : sine zeros of
PW_τ.

## Product R(z) = Π (z−γ)/(z−λ) · (λ/γ)

| L | µ | m | ell | −log\|R(i)\| | −log\|s_τ(i)\| |
|---|---|---|---|---|---|
| χ₅ | 16 | 5 | 27.2 | 0.11 | 0.63 |
| χ₃ | 80 | 10 | 111 | 0.31 | 1.49 |
| χ₁₃ | 16 | 7 | 10.0 | 0.06 | 0.63 |

The finite Blaschke is O(1). It
does not contain ell.

## Gram of reproducing kernels on Λ_L

G_{jk} = sin(τ(γ_j−γ_k)) / (π (γ_j−γ_k)).

| L | µ | m | −log det G | λ_min(G) | −ln λ_min | /ell |
|---|---|---|---|---|---|---|
| χ₅ 16 | 5 | 4.4 | 0.21 | 1.55 | 0.06 |
| χ₃ 80 | 10 | 3.8 | 0.48 | 0.72 | 0.007 |
| χ₁₃ 16 | 7 | 7.2 | 0.07 | 2.60 | 0.26 |
| χ₃₁ 38 | 12 | 9.6 | 0.04 | 3.15 | 0.39 |

Λ_L is a *sampling* set for PW_τ
(λ_min = O(1)). Interpolation in
the whole Paley–Wiener space is
cheap. The exponential in ell is
not there.

## Where the exponential lives

Q is not the min of ∑ |F(γ)|² over
PW_τ. It is the min over the
**hat subspace** of dimension
N_B+1 ≪ dim of the band-limited
functions that could vanish on
Λ_L.

N_B+1 > m, so a kernel exists.
How small ∑ |F(γ)|² can be is the
smallest singular value of the
evaluation map

    hats  →  ℂ^m,   φ ↦ (F̂(γ))_{γ∈Λ_L}.

That map *is* Q (restricted to
those zeros, which carry the
mass). Lemma 2 stated for PW_τ
is a different, easier inequality
and is numerically O(1). The
measured depth is a fact about
the hat Galerkin, not about
Beurling on PW_τ.

## Restated target

Bound σ_min(Eval : V_{N_B} → ℂ^{Λ_L})
from the geometry of Λ_L and the
hats. That is a finite matrix.
The desert enters because the
first rows (small γ) of Eval are
almost linearly dependent in the
low hats — the same edge story
as ψ(0).
