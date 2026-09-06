# Finite part of the semi-local HS norm

`||P₁𝔉P₁||_HS²` diverges as `0.65 log₂(1/h)`,
`h = R/N` = cell width. Not as `log N`.

At fixed `h` the sum is independent of `R`
(R=2..5, h=1/40: sum = 3.257 exactly in the run).

| R | N | 1/h | ∑λ² | 0.65 log₂(1/h) | pf |
|---|---|-----|-----|----------------|-----|
| 4 | 40 | 10 | 1.958 | 2.159 | −0.201 |
| 4 | 80 | 20 | 2.643 | 2.809 | −0.166 |
| 4 | 160 | 40 | 3.257 | 3.459 | −0.202 |
| 2 | 80 | 40 | 3.257 | 3.459 | −0.202 |
| 5 | 200 | 40 | 3.257 | 3.459 | −0.202 |

`pf ≈ −0.20` at this normalisation. The constant
depends on how `F[:,j]` is scaled; the coefficient
0.65 is the same as δ_S.

`python code/finite_part_HS.py`
