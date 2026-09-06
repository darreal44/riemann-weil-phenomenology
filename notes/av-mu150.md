# One point at μ=150: A−P₂₃ versus P_rest

Preregistered (`report/prereg-av-mu150.md`): a linear
fit of A−P₂₃ on 16→50 would hit 0 near μ≈150. If P_rest
stayed positive, Q would die when A−P₂₃ crossed P_rest.
One point, same v, χ₅, three hats. Not a sixth slope.
Not RH.

## Execution

Shipped `code/av_split23.py`. P₂₃ is n=2 and n=3 only.
Calibration on the 16→50 table of `Q-split-23.md` to
0.0001.

    μ     A        P₂₃     A−P₂₃    P_rest     Q    cross
   16   −0.828    −0.903    0.075     0.070    0.0055   no
   50   −1.293    −1.345    0.052     0.048    0.0034   no
   80   −1.449    −1.476    0.026     0.022    0.0049   no
  150   −1.635    −1.615   −0.020    −0.024    0.0041   no

## Verdict

A−P₂₃ did go through 0, on the naive scale. P_rest went
through 0 with it, a little further. They did **not**
cross each other. Q = 0.0041, still in the [0.003, 0.009]
band.

Reading 2 of `Q-convergence-2.md` needed P_rest to stay
positive. It did not. The two unfinished limits are still
tracking. The meeting of A−P₂₃ with *zero* is not the
meeting of A−P₂₃ with P_rest.

Judge: `tests/test_av_split23.py`.

## Status

| Claim | Status |
|---|---|
| 16→50 table of A−P₂₃, P_rest | reproduced |
| A−P₂₃ = 0 near μ=150 (naive line) | roughly yes (−0.020) |
| A−P₂₃ crosses P_rest at μ=150 | **no** |
| Q(v) leaves [0.003, 0.009] | no (0.0041) |
| (∀ μ) Q(v)>0 | open; not this point |
| (∀ L) Q_L ≥ 0 | RH; not this note |
