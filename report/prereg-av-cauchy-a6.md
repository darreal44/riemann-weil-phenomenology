# Preregistration: Cauchy majorant of |a^{(6)}| on [0,1]

Locked before the run. v=(4,−3,1)/√26, χ₅, μ=16.
Not a covering lemma. Not RH.

G₃ of a on [0,1] is an arithmetic check
(`av-gauss.md`). The remainder is
c₆ a^{(6)}(ξ) with c₆ ≈ 4.96×10^{-7}.
A 6th-difference estimate (~325) is not
a majorant. Chebyshev-Markov 1370 uses
interpolated c_n, not certified |c_n|.

a is holomorphic on dist(z,[0,1]) < π
(poles of w at kπi, k≠0). Cauchy:

    |a^{(6)}| ≤ 6! M / r^6,    r=2 < π.

Room in the A-window after the current
enclose (`A-v-enclose.md`): Alo − window
= 0.00091. One panel needs M₆ ≤ 1840.
Two Gauss panels of length 1/2 scale
the remainder by 1/64.

**This run.** Sample |a| on the r=2
stadium (32 cores) and an elementary
bound of |θ_v| and |w| on the containing
rectangle. Shipped `code/av_cauchy.py`.

**Prediction.** Elementary M is too
crude for one panel (cosh(4π r / L) is
large). Two panels fit: remainder ≤ 0.00091,
so composite G₃ + Cauchy is a proof of
the [0,1] piece. Still one v, finite μ.

**Kill.** Elementary two-panel remainder
exceeds the room. Then G₃ is still not
a hand proof. A sample-only fit is not
a survive (max modulus sampled is not
the majorant).
