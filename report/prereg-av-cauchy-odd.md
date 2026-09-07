# Preregistration: Cauchy majorant of |a_odd^{(6)}| on [0,1]

Locked before the run. Same v, μ=16, odd
integrand s₀=3/4. Tight window χ₃.
Not a covering lemma. Not RH.

Even side (#52): r=2, two Gauss panels,
elementary M, rem 3.39×10^{-4} ≤ room.
Odd a^{(6)} does not freeze in Chebyshev
(`odd-a6.md`); Markov N=16 rem 0.010
kills the χ₃ ball. Cauchy is the
transfer that does not use c_n.

Same poles kπi. w_odd = e^{-z/2}/sinh z
(even was e^{z/2}/sinh z). g_odd =
2 e^{-z/2} − θ_v.

Room: χ₃ termwise Qlo ≈ 0.00490
(`odd-ball.md`). Two-panel remainder
must stay below that.

**This run.** `code/av_cauchy_odd.py`:
sample |a_odd| on the r=2 stadium and
an elementary bound. Composite G₃ ±
Cauchy rem, same [1,L] termwise tail
as `av_enclose_odd_ball`.

**Prediction.** One panel too crude
(cosh(4π r/L) still large). Two panels
fit; χ₃ Qlo>0. Same pattern as even.

**Kill.** Elementary two-panel remainder
≥ 0.00490, or χ₃ Qlo≤0 after folding
it in. Sample-only fit is not a survive.
