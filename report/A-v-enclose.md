# One-command enclosure of A(v)

    python3 code/av_enclose.py

No flint. Pieces already
written: CST elementary,
G₃ of `av_gauss`, 8+8
trapezoid of a, Leibniz
M from endpoint values
of w and the numbers
g(1), g'(1), |g''|≤0.707
/ 0.552.

    CST            −0.108593739
    G₃ [0,1]       −0.700661341
    trap[1, 1.59]  −0.035266 ± 0.000359
    trap[1.59, L]  +0.016368 ± 0.000876
    I_{[1,L]}      [−0.02013, −0.01766]
    A(v)           [−0.82939, −0.82692]

Inside the room
[−0.8303, −0.8244] that
keeps Q(v)>0 after ±0.003
on P_rest.

Exit status 0 iff the
A-ball sits in that room.
The trap tail is superseded
for the Cauchy enclose
(`notes/av-enclose-cauchy-tail.md`):
8-panel G₃ ± 1.25×10^{-5},
no |g''|. `av_enclose.py`
keeps this trap path.
Not RH.
