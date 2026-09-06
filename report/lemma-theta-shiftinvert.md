# Shift-invert Lanczos, σ=0

Apply Lanczos to Q⁻¹, not to Q.
One factorization, then matvecs
v ↦ Q⁻¹ v. Ritz values θ of Q⁻¹
become λ = 1/θ.

Guess: (1, −1, 0, …). µ=16, NB=8.

| L | m | 1/θ_max | λ₀ | rel |
|---|---|---|---|---|
| χ₅ | 1 | 1.64×10⁻¹² | 1.58×10⁻¹² | 3 % |
| χ₅ | 2 | 1.58×10⁻¹² | | 10⁻⁴ |
| χ₅ | 3 | same | | λ₁ also in |
| χ₁₃ | 1 | 5.81×10⁻⁵ | 4.79×10⁻⁵ | 21 % |
| χ₁₃ | 2 | 4.79×10⁻⁵ | | 10⁻¹⁰ |
| χ₁₃ | 3 | same | | λ₁ = 0.202 |
| χ₃ | 1–4 | ~8×10⁻¹⁶ | 9.7×10⁻¹⁶ | 18 % |

m=1 is inverse iteration. m=2 is
already the floor for χ₅ and χ₁₃.
m=3 picks up λ₁.

χ₃ is the condition-number wall:
κ₂ ~ 10¹⁵, float64 Q⁻¹ is a 20 % lie.
Shift-invert does not invent digits.
Do it in mpmath, same as `eigsy`.

## Shifts other than 0

σ in the bulk (σ ~ 1) finds Haar
modes. σ ≈ λ₁ isolates the first
rung and misses λ₀. The lemma wants
σ=0. Always.

At dim 512: factor Q once
(sparse-direct or preconditioned),
run shift-invert Lanczos for 3–5
steps, stop. That is the 2-adic
job. At dim 9 it is a slower
`eigsy`.
