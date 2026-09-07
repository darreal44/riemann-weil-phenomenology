# Clenshaw–Curtis

Chebyshev nodes on [−1,1], weights from a DCT. Exact for degree ≤ n
(practically often as good as Gauss until high n). Nested nodes make it
adaptive-friendly.

Same role as Gauss here: an integrator of a or of a_lo. g is a mixture
of exponentials and a handful of cosines, so both rules are exact for
practical purposes at n=16 already. The repo does not need a DCT.

CC does not build g_lo. Chebyshev interpolants oscillate (Runge is mild
on Chebyshev nodes, but the interpolant is still not below g).

Not a campaign.
