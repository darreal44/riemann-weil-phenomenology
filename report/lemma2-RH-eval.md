# RH check: two-sided Eval vs prime-side Q

E₊ at {γ_k}, E₋ at {−γ_k},
σ±² = σ_min²(E₊ ⊕ E₋).
λ₀ = min of prime-side Q
(same hats, same L).

| L | µ | # ±γ | σ₊² | σ±² | λ₀ | σ±²/λ₀ |
|---|---|---|---|---|---|---|
| χ₅ | 16 | 462 | 7.00×10⁻¹³ | 1.40×10⁻¹² | 1.58×10⁻¹² | **0.884** |
| χ₅ | 38 | 462 | 2.22×10⁻²² | 4.44×10⁻²² | 5.25×10⁻²² | **0.845** |
| χ₃ | 16 | 412 | 3.43×10⁻¹⁶ | 6.86×10⁻¹⁶ | 7.71×10⁻¹⁶ | **0.889** |
| χ₄ | 16 | 440 | 1.26×10⁻¹³ | 2.53×10⁻¹³ | 2.92×10⁻¹³ | **0.867** |
| χ₈ | 16 | 510 | 4.83×10⁻⁹ | 9.65×10⁻⁹ | 1.07×10⁻⁸ | **0.904** |
| χ₁₃ | 16 | 560 | 2.16×10⁻⁵ | 4.32×10⁻⁵ | 4.79×10⁻⁵ | **0.902** |
| χ₂₉ | 38 | 642 | 5.86×10⁻⁶ | 1.17×10⁻⁵ | 1.28×10⁻⁵ | **0.913** |
| χ₃₁ | 38 | 648 | 1.43×10⁻⁴ | 2.85×10⁻⁴ | 3.06×10⁻⁴ | **0.930** |

σ±² = 2 σ₊² to machine
precision (hats real ⇒
F(−γ) = conjugate).

## What this is

Under RH the explicit formula
identifies prime-side Q with
∑_γ |F̂(γ)|² plus the
archimedean term (Γ, trivial
zeros). The table is that
identity on the Galerkin
matrix, with the archimedean
piece and the unharvested
tail (T ≳ 320) left out.

The ratio 0.85–0.93 is the
critical-line zeros' share of
λ₀. The leftover 7–15 % is
Γ + tail, not a failure of
RH on these L-functions
(their zeros are used as
input). It shrinks as the
list of γ grows (χ₃₁ 0.93
with 324 positive zeros,
χ₅-38 0.85 with the same
231 because µ=38 puts more
weight on the tail).

## Bound

\[
0.84\,\lambda_0(Q)
\;\le\;
\sigma_{\min}^2(E_\pm)
\;\le\;
\lambda_0(Q)
\]

on every window here. A
Lemma-2 lower bound on
σ_min(E_±) is a lower bound
on λ₀, with a multiplicative
1.2 that one can absorb in C.
The RH content is already
in the identification
Q ↔ Eval; the inequality
to prove is analytic
(hats versus Γ), not
arithmetic.
