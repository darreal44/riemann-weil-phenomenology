# The factor 2 is a 30 % deficit on v₀, not Poisson

Fourier coefficients of the bulk Gaussian
exp(−a (t−L/2)²) with a L² = −ln λ₀,

    ĉ_n = (−1)^n exp(−π² n² / (a L²)),     α = 0.204 at µ=11.

| n | ĉ_n (scaled to v₁) | v_n |
|---|---|---|
| 0 | 0.851 | **0.598** |
| 1 | −0.694 | −0.694 |
| 2 | 0.377 | 0.378 |
| 3 | −0.136 | −0.130 |
| 4 | 0.033 | 0.025 |

n ≥ 1 is the Gaussian series. v₀ is short by a
factor 0.70 (v₀/|v₁| = 0.86 vs ĉ₀/ĉ₁ = 1.23).

A pure Gaussian Fourier vector, same ℓ², has
−ln|ψ(0)| ≈ 2, i.e. the *one-tail* value a L²/4 ≈ 12
never appears: the period-L cosine sum of a
Gaussian does **not** evaluate to the spatial tail
(Poisson stays O(10⁻¹)). Putting the true v₀
back is what drives ψ(0) from 10⁻¹ down to 10⁻¹⁰.

That deficit is the tower axis. v_towers ≈ e₀,
⟨v_arch, v_towers⟩ ≈ 0, and the 2×2 mix
lowers v₀ by thirty percent. The “factor 2”
in −ln|ψ(0)| ≈ (−ln λ₀)/2 versus the Gaussian
tail a L²/4 is this mix, not an extra Slepian
identity.

The 4-mode wall = Gaussian rungs n=1,2,3
+ a constant mode suppressed by the primes.
Compute the 30 % from the 2×2 pairings
(report/lemma-theta-2x2.md) and the edge
law follows.
