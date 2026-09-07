# a_odd^{(6)} does not freeze like the even side

Even a: c₁₆ = 5×10^{-14},
M=324.5 stable for N=16–24.
Odd a (s₀=3/4):

    n     c_n (odd)
    0     −0.0514
    1     +0.299
    2     −0.122
    6     −1.9×10^{-5}
   12     +1.1×10^{-8}
   16     +5.7×10^{-9}

Still 10^{-8} at n=16.
Same poles y=iπk, but
the numerator 2e^{−y/2}−θ_v
no longer cancels the
1/y of w as cleanly in
the higher modes (g_odd
does not vanish at 0 to
as high an order in the
Chebyshev basis).

## Interior max versus N

    N    max|a₆| on [0.05,0.95]
   12    331
   16    3181
   20    1.2×10^4
   24    1.5×10^4   (and 1.9×10^5 at y=1)

No plateau. Markov on
N=16 gives M≤2.1×10^4,
remainder 0.010, which
*kills* the χ₃ ball
(0.00490−0.010<0).

N=12 (M=331, rem 1.64×10^{-4})
would leave Q₃>0.003, but
that M is not stable
under N. The even-side
trick — freeze N, then
Markov the frozen c_n —
does not transfer.

χ₃ keeps the sampled /
termwise-on-[1,L] ball.
Closing a^{(6)} for a_odd
needs a different strip
or a cutoff away from
y=1, not this sum.

Executed: Cauchy r=2, two
panels (`notes/av-cauchy-odd.md`).
Elementary rem 2.01×10^{-4}.
χ₃ Qlo=0.00469>0. The
Chebyshev sum is not the
majorant; Cauchy is.
