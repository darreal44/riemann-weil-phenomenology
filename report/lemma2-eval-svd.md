# Eval : hats → ℂ^{zeros}, σ_min² vs λ₀

E_{k n} = Fourier of hat n at γ_k.
σ_min = smallest singular value.
Truncation T_max = c · ω̂, ω̂ = 2π N_B/L.

| L | µ | T_max | m | σ_min² | λ₀ | σ²/λ₀ |
|---|---|---|---|---|---|---|
| χ₅ | 16 | 1 ω̂ | 5 | 0.69 | 1.6×10⁻¹² | 10¹¹ |
| χ₅ | 16 | 2 ω̂ | 14 | 4.5×10⁻¹⁴ | 1.6×10⁻¹² | 0.029 |
| χ₅ | 16 | 4 ω̂ | 35 | 3.4×10⁻¹³ | 1.6×10⁻¹² | 0.21 |
| χ₅ | 16 | all | 231 | 7.0×10⁻¹³ | 1.6×10⁻¹² | **0.44** |
| χ₅ | 38 | all | 231 | 2.2×10⁻²² | 5.3×10⁻²² | **0.42** |
| χ₃ | 16 | all | 206 | 3.4×10⁻¹⁶ | 7.7×10⁻¹⁶ | **0.45** |
| χ₁₃ | 16 | all | 280 | 2.2×10⁻⁵ | 4.8×10⁻⁵ | **0.45** |
| χ₂₉ | 38 | all | 321 | 5.9×10⁻⁶ | 1.3×10⁻⁵ | **0.46** |
| χ₃₁ | 38 | all | 324 | 1.4×10⁻⁴ | 3.1×10⁻⁴ | **0.47** |

At T = ω̂ the matrix is well
conditioned: those zeros are
interpolable. At T = 2 ω̂ the
kernel overfits the truncated
list (σ² < λ₀). With the full
list, σ_min² / λ₀ sits at
**0.42–0.47** on every character.

The missing 2 is the negative
axis (zeros come in ±γ). Weil
prime-side Q is two-sided;
Eval as written is one-sided.

## Statement

Under RH,

\[
\lambda_0(Q)
\;=\;
c\,\sigma_{\min}^2\bigl(\mathrm{Eval}:V_{N_B}\to\mathbb C^{\Gamma_+}\bigr)
\]

with c = 2 + o(1) on these
windows. Lemma 2 is a lower
bound on that singular value
from the geometry of Γ and
the hats.

A bound that only uses
{γ < ω̂} cannot see λ₀. The
nodes that set σ_min are the
zeros *past* the last hat —
the same residual peak as in
`lemma2-F-at-zeros.md`.
