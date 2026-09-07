# Chebyshev convergence, even vs odd

Even a on [0,1] (`av_a6.py`): coeffs after degree 12 sit at 10^{−15}
already at N=16. a^{(6)} on (0.05,1) is stable in N=16,24,32 at 324.5.
Endpoint pollution starts at N=40+.

Odd a (`av_a6_odd.py`): the same nodes do not lock a^{(6)}. The reported
max on [0.05,1] climbs with N and migrates to y=1. That is Runge on the
sixth derivative, not geometric decay of Chebyshev coeffs of a itself
(a_odd is still C^∞ on (0,1], but the 1/y weight times a shallower g
makes the high derivatives worse near the ends).

So “Chebyshev converges” is true for a and false for a^{(6)} odd on this
mesh. Do not feed the odd max into GAUSS3_REMAINDER_COEFF. The even 325
remains the only M the lab owns.

Not Weil.
