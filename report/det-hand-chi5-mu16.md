# Hand attempt at det H, χ₅ μ=16 — fails

Keep 2,3,4 exact (θ_{f₁} closed
form). Bound the rest n∈{7,8,9,11,13,16}
by |w(n)| and a uniform θ.

## Head 2+3+4, exact enough

    P₁₁(2,3,4) = −0.961
    A₁₁         = −0.987
    gap before rest     0.026

The true rest is −0.025 and
leaves H₁₁ = 9.3×10⁻⁵.
A bound on the rest that is
larger than 0.026 wipes H₁₁.

## Remainder bounds

sum_{n≥7} |w(n)| = 2.95

|θ₁₁| ≤ θ₁₁(log 7) = 0.034
    ⇒ |R₁₁| ≤ 0.102

|θ₁₂| on [log 7, L] ≤ 0.365
    ⇒ |R₁₂| ≤ 1.08

|θ₂₂| on [log 7, L] ≤ 0.83
    ⇒ |R₂₂| ≤ 2.44

Intervals:

    H₁₁ ∈ [−0.128, 0.076]     contains 0
    H₁₂ ∈ [−1.33,  0.83]      contains 0
    H₂₂ ∈ [−2.37,  2.52]      contains 0

det is lost. The crude
max|θ| bound is 40 times the
true |R₁₁| (0.102 vs 0.025)
and 10³ times H₁₁.

Dropping the uniform θ and
using the signed θ₁₁(log n)
gives R₁₁ = −0.026, which
works — but that *is* the
machine table, not a bound.

## Verdict

The remainder n≥5 is too
big for a max-norm estimate
in {f₁,f₂}. The frame is
too loose: e₁ is a good
guess for the well, not
the well. The well is v₀
(‖v₀ − e₁‖ is the φ₁
admixture that makes the
10⁻⁴).

Next certificate: repeat
the 2×2 on span{v₀} after
fixing v₀ from a *smaller*
window (μ=8, cheap) and
checking it stays a
witness at μ=16 — or write
the 2×2 in the measured
{v₀, v₁} and bound there,
where H₁₁ = λ₀ itself.
