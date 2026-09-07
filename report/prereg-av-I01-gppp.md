# Preregistration: I_{[0,1]} cubic Taylor, |g'''| by lag amplitudes

Locked before the run. Same witness v=(4,−3,1)/√26, χ₅ μ=16.
Not a mesh. Not leftover-adaptive. Not N=8. Not Weil. Not RH.

g = 2 e^{−3y/2} − θ_v, elementary six lags. Bound |∂_{yyy} θ_nm|
by replacing every sin and cos with 1 (closed amplitudes). Then

    |g'''| ≤ K := 6.75 + ∑_{n,m≤2} |v_n v_m| Amp(θ_nm''').

Lagrange remainder after order 2:

    g(y) ≥ g'(0) y + g''(0) y²/2 − (K/6) y³    on [0,1].

g'(0) and g''(0) are the shipped jet at 0. a_lo = ½ w g_lo, integrate
a_lo. True I is ∫ a, same shipped a. Window ±0.003. Finite μ, one v.
Not (∀ L) Q_L ≥ 0.

**Prediction.** K covers the sampled |g'''|. The cubic is a legal
lower bound and misses the ±0.003 window by a lot (K too crude
near 0 where w ~ 1/y). Q_lo < 0. Verdict KILL. Not a take.
