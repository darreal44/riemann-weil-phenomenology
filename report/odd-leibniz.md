# Leibniz M for a_odd

    g = 2 e^{−y/2} − θ_v
    g'' = ½ e^{−y/2} − θ_v''
    w = 2 e^{−3y/2}/(1−e^{−2y})
    w'/w = −3/2 − 2 e^{−2y}/(1−e^{−2y})

Checked a'' at y=1.2
(−0.029167 vs FD −0.029167).

## Envelopes on [1, L]

              [1, 1.59]     [1.59, L]
    |w|       0.516         0.192
    |w'|      0.936         0.305
    |w''|     2.070         0.519
    |g|       0.719         0.722
    |g'|      0.614         0.276
    |g''|     1.401         0.652
    |a''|     0.373         0.105

Termwise (no cancellation):

    M₁ ≤ 1.680     (sampled 0.373)
    M₂ ≤ 0.334     (sampled 0.105)

Fat by 4–5 on the first
half. Still:

    err₁+err₂ = 1.17×10^{-3}
    Q₃ ∈ [0.00490, 0.00724]

stays positive. Sampled-M
ball [0.00574, 0.00639]
is the tight one; the
termwise ball is the one
that only uses endpoint
envelopes of w (monotone)
plus max|g|,|g'|,|g''|.
