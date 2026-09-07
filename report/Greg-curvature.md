# Curvature of G_reg = D₂ − 1/y

Numerical second derivative (finite differences 10⁻⁵):

         s₀=1/4              s₀=3/4
    y    G       G''         G       G''
    0.05 +0.498  −0.124      −0.502  +0.125
    0.20 +0.489  −0.121      −0.506  +0.123
    0.50 +0.464  −0.103      −0.506  +0.110
    1.00 +0.403  −0.057      −0.484  +0.070

Even cell: G_reg>0 and *concave* (G''<0). Odd cell: G_reg<0 and *convex*
(G''>0). The slogan “G_reg convex” is false as a uniform statement. It
holds for s₀=3/4 (χ₃, χ₇) and fails for s₀=1/4 (χ₄, χ₅, χ₈, χ₁₇).

Near 0 both |G''| ≈1/8. The sign tracks 1−2s₀ (the prefactor of the sinh
writing).

This is not g'' of #82 (that g includes −θ_v and a specific Bose weight
2e^{−3y/2}). A tangent under-estimator of G_reg is legal only on the odd
cells. On the even cells one wants a chord (concave).
