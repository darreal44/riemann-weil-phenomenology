# Spectral gap of Q

χ₅. Gap = λ₁/λ₀ = exp(Δℓ),
Δℓ = ℓ₀ − ℓ₁.

## Versus μ, N=8

| μ | λ₀ | λ₁ | λ₁/λ₀ | Δℓ | ℓ₂−ℓ₁ |
|---|---|---|---|---|---|
| 8 | 9.6×10⁻⁷ | 2.7×10⁻² | 2.8×10⁴ | 10.3 | 3.7 |
| 11 | 1.7×10⁻⁹ | 3.4×10⁻⁴ | 2.0×10⁵ | 12.2 | 7.1 |
| 16 | 1.6×10⁻¹² | 2.8×10⁻⁷ | 1.8×10⁵ | 12.1 | 9.9 |
| 22 | 1.1×10⁻¹⁴ | 2.6×10⁻⁹ | 2.4×10⁵ | 12.4 | 9.5 |

Δℓ locks at 12 nats past μ=11.
Both floors drop together;
their *ratio* is constant.
That is the even/odd pair
(`Q-excited-spectrum.md`),
not a closing gap.

ℓ₂−ℓ₁ grows (3.7 → 9.5):
the third level peels off
the pair. N_eff stays ~2.

## Versus N, μ=16

| N | λ₁/λ₀ | Δℓ |
|---|---|---|
| 4 | 1.8×10⁴ | 9.8 |
| 6 | 4.3×10⁴ | 10.7 |
| 8 | 1.8×10⁵ | 12.1 |
| 10 | 2.8×10⁵ | 12.5 |
| 12 | 7.0×10⁵ | 13.5 |

More hats deepen both
floors and *widen* the
ratio. The isolated
eigenvalue becomes more
isolated.

## Why the shape converges fast

A rank-one projector onto
an isolated eigenvalue
has error O((λ₀/λ₁)^{r})
in a residual of size
matching the tail hats.
λ₀/λ₁ ~ 10⁻⁵ already at
N=8, so 1−⟨v_N,v_{N+2}⟩
~ 10⁻⁵–10⁻⁶
(`v0-rate.md`) is the
gap talking.

The gap does not need to
be proved to use v₀ as a
witness. It explains why
N=8 freezes the direction
while λ₀ itself is still
moving by decades.
