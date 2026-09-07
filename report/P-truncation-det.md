# Truncating P flips the sign of det H

Independent 2×2, µ=16. P kept only
for n ≤ cutoff. Arch full.

| cutoff | χ₅ det | χ₃ det | χ₈ det | χ₁₃ det |
|---|---|---|---|---|
| 2 | −0.20 | −2.8×10⁻³ | −1.03 | +0.60 |
| 3 | −0.024 | −2.8×10⁻³ | −0.10 | −0.41 |
| 4 | −4×10⁻⁴ | −0.015 | −0.10 | −0.98 |
| 5 | −4×10⁻⁴ | −2×10⁻⁴ | **+0.024** | −0.24 |
| 7 | −3×10⁻⁶ | −1×10⁻⁵ | +1.6×10⁻³ | −0.014 |
| 8 | **+1×10⁻⁶** | −5×10⁻⁷ | +1.6×10⁻³ | +0.022 |
| 9 | +3×10⁻⁷ | −5×10⁻⁷ | **−3×10⁻⁴** | −0.001 |
| 11 | **−1×10⁻⁹** | **+2×10⁻⁸** | +1.8×10⁻⁴ | +0.005 |
| 13 | +1.3×10⁻⁸ | +5.7×10⁻¹⁰ | +2.0×10⁻⁴ | +0.005 |

The last change of sign is late:

- χ₅ : still negative at 11, positive
  at 13. Prime 13 decides SPD.
- χ₃ : positive only from 11.
- χ₈ : false positive at 5–8, dip
  below 0 at 9, recovered at 11.
- χ₁₃ : oscillates through 9.

2 and 3 dominate the *size* of
P(f₁) (~1 against Arch ~1). They
do not dominate the *sign* of
det. A bound that keeps only
p=2,3 proves the wrong matrix.

The finite sum is the object.
Dropping n > 8 is not a rounding
error; it is a different quadratic
form, often indefinite.
