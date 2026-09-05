# Li coefficients (ζ)

λ_1 = 1 + γ/2 − ½ log(4π) = 0.023095708966

150 zeros T≈319 + Weyl tail, scale 0.554
fitted on λ1.

| n | zeros | tail | scaled |
|---|-------|------|--------|
| 1 | 0.02064 | 0.00443 | 0.02310 |
| 2 | 0.0825 | 0.0177 | 0.0924 |
| 4 | 0.3295 | 0.0709 | 0.3688 |
| 8 | 1.3087 | 0.2835 | 1.4658 |

Scale 0.55 is the same 2-convention as the
Gram tail (s≈0.65). All λ_n>0. Not RH.

    python code/li_lambda.py --n 8
