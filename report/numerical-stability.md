# Numerical stability — χ₂₉ hat Gram, float64

## Condition

| μ | λ₀ | κ(Q) | κ(H) | κ(T) |
|---|---|---|---|---|
| 11 | 0.298 | 25 | 12 | 2.9 |
| 22 | 4.1e-3 | 1.8e3 | 99 | 4.0 |
| 38 | 7.9e-6 | 9.6e5 | 3.1e3 | 7.3 |

κ(T) stays O(1). The blow-up is λ₀
falling, not T becoming singular.
At μ=38 float64 still has ~10 digits
on λ₀ (eps·κ ~ 2e-10 relative).

## Cholesky residual

‖Q − LLᵀ‖_F / ‖Q‖_F = 1.0–1.4 × 10⁻¹⁶
at every μ, including 38. Factorisation
is stable. No pivot breakdown: min
L_ii = L22 = 0.071 ≫ √eps.

Eigen residual ‖Qv−λv‖ = 1.7×10⁻¹⁵
at μ=38.

## What actually moves λ₀

Not rounding. The T-cutoff of the
zero list:

| μ | T=80 | T=160 | T=320 | (160−320)/320 |
|---|---|---|---|---|
| 11 | 0.285 | 0.294 | 0.298 | 1.4 % |
| 22 | 3.7e-3 | 4.0e-3 | 4.1e-3 | 3.2 % |
| 38 | 5.5e-6 | 7.1e-6 | 7.9e-6 | 9.4 % |

At μ=38 the missing zeros past 320
are a 10 % systematic, a million
times the rounding error. N>24
changes λ₀ by <1 %.

float64 is enough through μ=38.
The next error to kill is T₀, not
dps.
