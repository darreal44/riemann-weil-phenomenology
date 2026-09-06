# A vs P alignment against μ

2-plane {e₁,e₂}. cos = |⟨v_min(P), v_min(A)⟩|.

## χ₅ (thin)

| μ | eig P | eig A | cos | ‖H‖_F | λ_min(H) |
|---|---|---|---|---|---|
| 8 | −0.92, 0.63 | −0.79, 1.27 | 0.987 | 0.77 | 8.5×10⁻⁵ |
| 11 | −1.02, 0.95 | −0.98, 1.12 | 0.999 | 0.21 | 2.5×10⁻⁵ |
| 16 | −1.18, 0.97 | −1.18, 0.98 | 1.000 | 0.0039 | 3.2×10⁻⁶ |
| 22 | −1.33, 0.86 | −1.33, 0.87 | 1.000 | 0.012 | 6.9×10⁻⁷ |
| 30 | −1.47, 0.76 | −1.47, 0.77 | 1.000 | 0.010 | 8.7×10⁻⁷ |

From μ=16 the negative axes
coincide. P and A deepen
together (λ_min ~ −log μ).
H stays a 10⁻³ residual;
λ_min(H) drops like a slow
power of μ, not a well.

## χ₁₃ (wide desert)

| μ | eig P | eig A | cos | ‖H‖_F | λ_min(H) |
|---|---|---|---|---|---|
| 8 | −0.28, 1.00 | 0.16, 2.22 | 0.95 | 1.49 | 0.19 |
| 11 | −0.27, 0.57 | −0.03, 2.08 | 0.90 | 1.74 | 0.016 |
| 16 | −0.42, −0.23 | −0.23, 1.93 | **0.03** | 2.35 | 0.0021 |
| 22 | −1.10, −0.26 | −0.38, 1.82 | 0.44 | 2.80 | 0.0013 |
| 30 | −1.52, −0.25 | −0.51, 1.72 | 0.55 | 2.98 | 1.5×10⁻⁴ |

P becomes negative-definite
around μ=16 and its axis
leaves A's. ‖H‖ is O(1) and
grows. The 2-plane is easy
here; the well of Q is not
this H (N_eff leaves the
plane).

## Reading

The hard window is the one
where spec P = spec A + o(1)
and the axes lock. Then
det H is the area of two
almost-parallel residuals
and every extra prime can
flip it. That is χ₅ at
μ≥16, not χ₁₃.
