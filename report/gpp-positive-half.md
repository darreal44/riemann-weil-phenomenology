# g'' on [1.59, L]

Two simple zeros of g''':

    [1.8341, 1.8365]   g'' = −0.55166
    [2.5688, 2.5711]   g'' = +0.14786

Ends:

    g''(1.59) = −0.45002
    g''(L)    = +0.0703125 = 9/128

The last one is exact:
θ_v''(L)=0 (every kernel
θ_nm and its second
derivative vanishes at
y=L except the cancelled
F₀ pieces that sit in
CST), and
g''(L) = (9/2) e^{−3L/2}
       = (9/2)·(1/64) = 9/128.

Hence on [1.59, L]

    −0.55166 ≤ g'' ≤ 0.14786
    |g''|    ≤ 0.55166 < 0.552

The ceiling 0.552 used in
`av_enclose.py` is this
critical value, isolated
in an interval of width
0.0024 where g'' is flat
to 10^{-5}.

Together with
|g''|≤0.707 on [1, 1.59]
(`gppp-isolation.md`),
both M inputs of
`av_enclose.py` are now
catalogued extrema, not
grid maxima.
