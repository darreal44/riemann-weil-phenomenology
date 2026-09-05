# Gram tail vs Li tail

Same remainder: ∑_{γ>T} K(γ) ≈ ∫_T^∞ K(t) ρ_Weyl(t) dt
with K>0 and K(t) ∼ 1/t².

| | Gram χ₂₉ μ=11 | Li ζ λ₁ |
|---|---|---|
| Kernel K | 2\|hat(t)\|² on v₀ | 2 Re(1/ρ) = 1/(t²+¼) |
| Target | Q λ₀ = 0.303 | closed λ₁ = 0.023096 |
| List | T=69 (ω≈63) / T=320 | T=319 (150 zeros) |
| Without tail | 0.281 (−7.3 %) | 0.02064 (−10.6 %) |
| Discrete T=320 | 0.298 (−1.6 %) | — |
| Raw Weyl | 0.312 (+3 %) | 0.02507 (+8.5 %) |
| Scale s | 0.60–0.70 | 0.554 |
| After scale | 0.303 | 0.02310 |
| Sign | stays + | stays + |

## Why the scales are close

Both codes put a factor 2 in front of a
one-sided list (ΦᵀΦ×2, or ±γ). Smooth
Weyl has no pair correlation, so raw ρ
is a bit fat. s≈0.55–0.65 absorbs both.

## Why the raw deficits differ

Gram at T=69 is cut *inside* the hats
(ω≈63): 7 % missing, then T=320 already
1.6 %. Li λ₁ has no band cutoff; 10 % is
the whole t>319 piece of 1/(t²+¼).

At the same T≈320 the Gram leftover is
smaller because hats decay faster than
1/t² once t≫ω (sinc envelope).

## Common conclusion

The tail is a positive, computable
remainder of the explicit formula.
It aligns G with Q and λ₁ with its
closed form. It does not produce a
negative eigenvalue and is not RH.
