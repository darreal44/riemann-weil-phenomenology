# A lower bound for λ_min(H)

H is 2×2, SPD iff tr H > 0 and det H > 0.
Then

    λ_min(H) = 2 det / (tr + √(tr² − 4 det))
             ≥ det / tr.

On the four windows below the two
sides agree to one part in 10³:
λ_max ≈ tr (the well is one deep
direction). So det/tr is not a
lossy bound. It *is* λ_min.

## µ = 16

| χ | det H | tr H | det/tr | λ_min | ratio |
|---|---|---|---|---|---|
| χ₅ | 1.26×10⁻⁸ | 3.95×10⁻³ | 3.20×10⁻⁶ | 3.21×10⁻⁶ | 1.001 |
| χ₃ | 5.67×10⁻¹⁰ | 8.98×10⁻³ | 6.31×10⁻⁸ | 6.31×10⁻⁸ | 1.000 |
| χ₈ | 1.99×10⁻⁴ | 1.15 | 1.73×10⁻⁴ | 1.73×10⁻⁴ | 1.000 |
| χ₁₃ | 4.89×10⁻³ | 2.36 | 2.08×10⁻³ | 2.08×10⁻³ | 1.001 |

tr H > 0 is cheap: it is H₂₂ plus a
10⁻⁴, and H₂₂ is 10⁻³ to 2 with no
tight cancel.

The inequality that remains is
**det H > 0**.

## Why a norm bound dies

Split H = A − P (Arch minus primes).
On χ₅:

    A₁₁ = −0.9869    P₁₁ = −0.9870
    A₁₂ = +0.6196    P₁₂ = +0.6201
    A₂₂ = +0.7811    P₂₂ = +0.7772

A is *not* positive on e₁. λ_min(A)
= −1.18. ‖P‖_F = 1.53.
λ_min(A) − ‖P‖_F = −2.7 < 0.
Any bound that treats A and P as
two operators without their
alignment gives the wrong sign.

The content is the alignment:
A and P agree on span{e₁} to
10⁻⁴, and differ on e₂ by 4×10⁻³.
That difference is H, and it is
positive because the mismatch on
e₂ is larger than the residual
on e₁ times the condition.

## What a proof has to say

    det(A − P) > 0,

with A the Laplace series and P
the nine or so prime-power
samples of Θ. Equivalent form,
since A ≈ P on e₁:

    (A₂₂ − P₂₂)(A₁₁ − P₁₁) > (A₁₂ − P₁₂)²

Left side is (4×10⁻³)·(9×10⁻⁵) on χ₅;
right side is (5×10⁻⁴)² = 3×10⁻⁷;
left is 4×10⁻⁷. Margin of 30 %.
Not a 10¹⁴ miracle — a 30 %
inequality between three residuals
of size 10⁻⁴ to 10⁻³.

No closed minorant yet. The
reduction is: positivity of a
2×2 of residuals, each residual
an explicit finite sum.
