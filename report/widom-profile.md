# Eigenvalue profile versus the Widom sigmoid

Landau-Widom: lambda_k of the
limiter is ~ 1 for k < 2c,
~ 0 for k > 2c, and
drops through (delta, 1-delta)
over Delta k = O(log c).
Our ell_k = -ln lambda_k
(depth), so the plunge in
lambda becomes a rise of
ell through O(1) as k
crosses D_max.

mu=16, N=30 hats, c~N,
log c ~ 3.4. First ten
depths:

    k   chi5     chi8     chi13
    0   35.56    20.59    11.32
    1   20.99     7.37     1.73
    2    8.79     0.24    -0.28
    3    1.50    -0.30    -0.34
    4    0.17    -0.43    -0.73
    5   -0.20    ...      ...

    D_max  3.08     1.77     1.19
    k at cut 2   3        2        1

The index where ell crosses
2 is exactly round(D_max).
The next index is already
O(1) or negative: the
transition is *one rung*,
not a band of width 3.

A Fermi-Dirac fit
lambda ~ 1/(1+exp((k-2c)/w))
with w~log c / pi would
spread three rungs. The
hat Gram is steeper than
that. Either c_eff is
smaller than N (the hats
are not a full prolate
basis) or G is not the
limiter closely enough
for Widom's w to apply.

That is the transfer
obstruction, written as a
profile rather than a
count. Not RH.
