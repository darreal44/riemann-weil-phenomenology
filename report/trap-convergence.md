# Trapezoid remainder on [1, L]

enclose_cauchy uses
8+8 traps:

    [1, 1.59]   span 0.59   M₂=0.707
    [1.59, L]   span 1.18   M₂=0.552

Classic
E = (b−a) h²/12 M₂
= span³ M₂ / (12 n²).

    n     E[1,1.59]   E[1.59,L]    sum
    4     7.6×10⁻⁴    4.8×10⁻³    5.5×10⁻³
    8     1.9×10⁻⁴    1.2×10⁻³    1.4×10⁻³
   16     4.7×10⁻⁵    3.0×10⁻⁴    3.4×10⁻⁴
   32     1.2×10⁻⁵    7.4×10⁻⁵    8.6×10⁻⁵

1/n². The second
panel dominates
(longer span).
At the shipped n=8
the trap tail is
~1.4×10⁻³, larger
than the [0,1]
Cauchy room
(9.1×10⁻⁴) and
much larger than
Cauchy-8 on the
whole [1,L]
(elem 1.2×10⁻⁵).

Convergence is
not the issue:
n=32 already
beats 10⁻⁴. The
issue is the
*method* on a
smooth piece.
Gauss+Cauchy on
[1,L] at 8
panels is two
orders under
the current trap.
Executed: rewrite
(`notes/av-enclose-cauchy-tail.md`).
Not a larger n.
