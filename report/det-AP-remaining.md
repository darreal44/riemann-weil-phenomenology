# The remaining inequality: det(A − P) > 0

On the 2-plane, Lemma 2 at three
hats is positivity of a 2×2

    H = A − P,

A the 10-term Laplace series of
the archimedean kernel against
{f₁,f₂}, P the finite prime-power
sum

    P_{ij} = Σ_{n≤µ} χ(n) Λ(n) n^{-1/2} θ_{ij}(log n).

θ_{f₁} is elementary
(`lemma2-theta-f1.md`). No zeros
enter. The inequality is
unconditional and finite.

## Size

χ₅ µ=16, unit frame:

    H₁₁ = 9.3×10⁻⁵,   H₁₂ = −5.9×10⁻⁴,   H₂₂ = 3.9×10⁻³
    det H = 1.5×10⁻⁸,   λ_min = det/tr = 3.2×10⁻⁶.

A and P are both O(1) and agree
to 10⁻³ on the f₁-direction,
to 10⁻⁶ on λ_min. The determinant
is the area of two residuals of
size 10⁻³, almost parallel.

## Why CS and Weyl miss it

Weyl: tr H > 0 is H₁₁+H₂₂ ≈ H₂₂ > 0,
true and cheap, does not give the
sign of λ_min.

Gershgorin: H₁₁ ≥ |H₁₂| fails
(9×10⁻⁵ ≱ 6×10⁻⁴).

Cauchy–Schwarz on the pair
(Arch, Primes) gives
|A−P| ≤ ‖A‖+‖P‖, the wrong
direction.

The only cheap bound that sees
the sign is

    λ_min ≥ det H / tr H,

and det H is the thing to prove.

## What a hand estimate can use

1. θ_{f₁}(y) > 0 and decreasing
   on (0,L) at L=log 16. Prime
   2 then 3 carry most of P(f₁):
   χ₅(2)=χ₅(3)=−1, so those two
   terms *add*, 0.49·1.32 + 0.63·0.68
   = 1.08 against Arch(f₁) ≈ 0.98
   in the scalar table (signs of
   Arch depend on the constant
   term). The remainder n=4..16
   is O(10⁻¹) and must be kept;
   dropping it flips nothing on
   χ₅ but does on thinner deserts.

2. The Laplace tail of A after
   ten terms is O(e^{-2L}) = 1/256
   at µ=16, smaller than the
   target 10⁻⁶ once summed, not
   the bottleneck.

3. The pairing is truncated Weil
   on two explicit functions of
   type 4π/L. A positivity
   certificate in the style of
   the µ=3 Arb 5×5 (flint, already
   in the repo) would close the
   2×2 at µ=16 to a ball. That
   is a verification, not a
   reason.

## What it would not close

det H > 0 is λ_min(H) > 0, depth
~13 nats on χ₅, ~20 on χ₃ µ=80.
The Schur identity of
`HT-is-eigenvector.md` then
says λ₀ is a different number.
A complete Lemma 2 (window) still
needs a reason that a tail exists
with Qv ≈ 0, which is Weil on the
whole hat space — circular if
the goal is λ₀>0, useful if the
goal is only H>0 on the plane.

The honest target of a hand proof
on the 2-plane is therefore
narrower than STATUS: positivity
of truncated Weil on {f₁,f₂},
unconditional, no claim on λ₀.
