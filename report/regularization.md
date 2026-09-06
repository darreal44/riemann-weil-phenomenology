# Regularisation of Q — χ₂₉ Gram

The well *is* the small eigenvalue.
Most regularisers replace it.

## Tikhonov Q + ε I

| μ | λ₀ | ε=10⁻⁸ | ε=10⁻⁶ | ε=10⁻⁴ | ε=10⁻² |
|---|---|---|---|---|---|
| 22 | 4.1e-3 | 4.1e-3 | 4.1e-3 | 4.2e-3 | 1.4e-2 |
| 38 | 7.9e-6 | 7.9e-6 | 8.9e-6 | 1.1e-4 | 1.0e-2 |

Rule: if ε ≪ λ₀ the well is untouched;
if ε ≳ λ₀ then λ₀(Q+εI) ≈ ε. At μ=38
even 10⁻⁶ already shifts by 13 %.

## Diagonal loading Q + ε diag(Q)

Worse: diag(Q) is O(1), so ε=10⁻⁴
already triples λ₀ at μ=38
(7.9e-6 → 2.4e-5).

## Spectral cutoff

Drop eigenvalues below τ and rebuild.
At μ=38, τ=10⁻⁴ removes the well
(rank lost = 1) and the new λ₀ is
roundoff. The signal *is* that mode.

## Ridge on H only

Q[:3,:3] += ε I. At μ=38, ε=10⁻³
gives λ₀ ≈ 10⁻³ = ε. Same as
Tikhonov on the 3-hat plane, where
the well lives.

## What to use

Nothing, through μ=38: κ=10⁶ is
comfortable in float64, Cholesky
residual is 1 ulp.

If μ grows until λ₀ < 10⁻¹², use
a higher-dps eigen solve on the
3×3 Schur Δ, not a regulariser
on Q. Regularising Q hides the
quantity we measure.
