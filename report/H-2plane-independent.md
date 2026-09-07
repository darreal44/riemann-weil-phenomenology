# The 2×2 without hats

`code/H_2plane_independent.py` builds
H_{ij}=Arch(eᵢ,eⱼ)−P(eᵢ,eⱼ) from the
same regular integrand and the same
elementary θ_{nm} as H₁₁, now on
the pair {e₁,e₂}.

µ=16 versus `cert_2plane` (Q₃
projected):

| χ | H₁₁ | H₁₂ | H₂₂ | det | eigmin |
|---|---|---|---|---|---|
| χ₅ | 9.315×10⁻⁵ | −5.886×10⁻⁴ | 3.855×10⁻³ | 1.265×10⁻⁸ | 3.205×10⁻⁶ |
| χ₃ | 2.179×10⁻⁴ | −1.381×10⁻³ | 8.758×10⁻³ | 5.666×10⁻¹⁰ | 6.313×10⁻⁸ |
| χ₈ | 1.707×10⁻³ | −4.189×10⁻² | 1.144 | 1.988×10⁻⁴ | 1.735×10⁻⁴ |

Same digits as the hat projection.
Two engines, one 2×2, no zeros.

What this closes: the matrix H
is a finite explicit formula.
What it does not: a reason that
det>0 other than evaluating it.
`tests/test_H_2plane_independent.py`.
