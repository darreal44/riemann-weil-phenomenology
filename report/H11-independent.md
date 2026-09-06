# H₁₁ without the 3×3

Second engine for the (1,1) entry
on unit e₁. Arch is the regular
integrand

    ½ ∫_0^L K(y) (2 e^{-(2-2s₀)y} − θ_{f₁}(y)) dy
    + CST,

K(y) = 2 e^{-2 s₀ y}/(1−e^{-2y}),
θ_{f₁} elementary. P is the finite
prime-power sum against the same
θ. No hat matrix, no zeros.

A naive Laplace series that splits
2 e^{-(2-2s₀)y} from θ diverges
(harmonic). The combination is
O(y) at the origin and integrable.

µ=16, dps=40, versus `cert_2plane`
(projection of Q₃):

| χ | Arch | P | H₁₁ | rel. to 2-plane |
|---|---|---|---|---|
| χ₅ | −0.98695 | −0.98704 | 9.315×10⁻⁵ | 4×10⁻⁷ |
| χ₃ | −0.62477 | −0.62498 | 2.179×10⁻⁴ | 5×10⁻⁷ |
| χ₄ | −0.33708 | −0.33826 | 1.179×10⁻³ | 3×10⁻⁶ |
| χ₈ | −0.51695 | −0.51865 | 1.707×10⁻³ | 2×10⁻⁶ |
| χ₁₃ | −0.03144 | −0.24330 | 0.21186 | 2×10⁻⁶ |

H₁₁>0 is now a number from two
independent writings of the same
finite formula. χ₅/χ₃: Arch and P
agree to 10⁻⁴, difference 10⁻⁴.
χ₁₃: they do not; H₁₁ stays O(10⁻¹).

`code/H11_independent.py`,
`tests/test_H11_independent.py`.
The 2×2 off-diagonal is still
only on the hat projection.
