# Cauchy majorant on [1, L], μ=16

Same a, r=2 < π.
h = L−1 = 1.773.
Gauss-3 remainder
on n equal panels:
c₆ M₆ h^7 / n^6.

Elementary rectangle
(cruder than [0,1]:
xmax=L+2):

    M = 10646    M₆ = 1.20×10⁵

    n     rem
    1     3.27
    2     5.10×10⁻²
    4     7.98×10⁻⁴
    8     1.25×10⁻⁵

Sample on the
stadium (coarse):
M=151, four panels
already 1.1×10⁻⁵.

#52 room 9.1×10⁻⁴
was the [0,1] A
budget. On [1,L]
the enclose still
uses a trap
remainder
(`enclose_cauchy`).
Four elementary
panels beat 10⁻³;
eight beat the
[0,1] room.

Executed: enclose rewritten
(`notes/av-enclose-cauchy-tail.md`).
8-panel rem is the tail.
Not RH.

    python code/av_cauchy_tail.py
