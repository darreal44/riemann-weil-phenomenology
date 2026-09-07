# a^{(6)} on [0,1] by Chebyshev

Plain 6th differences explode
(h^{-6} noise). A Chebyshev
interpolant of a on [0,1]
is stable: coeffs after
degree 12 sit at 10^{-15}
already at N=16.

    N     max|a^{(6)}| on [0.05,1]    rem = c₆ M
    16    3.245×10² at y=0.466       1.610×10^{-4}
    24    3.245×10² at y=0.466       1.610×10^{-4}
    32    3.245×10² at y=0.466       1.610×10^{-4}

N=40+ pollutes a^{(6)}(0)
(endpoint Runge on the
sixth derivative). The
interior consensus is
324.5.

At the Gauss nodes (N=24):

    y=0.113   a^{(6)} ≈ +11
    y=0.500   a^{(6)} ≈ −321
    y=0.887   a^{(6)} ≈ +47

The mid-node carries the
max. This is the same
325 that `av_gauss.max_abs_d6`
reported; the Chebyshev
says it is not an FD
artefact.

A Markov bound from
‖a‖_∞≤1.5 and degree 16
is ~10^8 — useless. The
working ceiling is 325,
and the G₃ remainder
1.61×10^{-4} stays inside
the ±0.003 A-window.
Not a majorant derived
from the closed form of
a^{(6)}.
