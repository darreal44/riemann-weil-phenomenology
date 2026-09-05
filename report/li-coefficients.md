# Li coefficients (ζ)

λ_1 = 1 + γ/2 − ½ log(4π) = 0.023095708966

From 150 zeros (T≈319):

| n | λ_n (zeros only) |
|---|------------------|
| 1 | 0.02064 |
| 2 | 0.0825 |
| 3 | 0.1856 |
| 4 | 0.3295 |
| 8 | 1.309 |

λ_1 is 10 % low: missing tail t>319.
All computed λ_n > 0. That is the usual
finite check, not RH.

    python code/li_lambda.py --n 8
