# Preregistration: leftover-driven adaptive mesh

Locked before the run. Same witness
v=(4,−3,1)/√26, χ₅ μ=16. Named in
`report/adaptive-methods.md`: split a
panel when leftover = g''(left)−m_i
is large, not when a Kronrod estimator
on a is large. Parent is tailq
(gap 0.002793). Not Weil. Not RH.

Start from uniform N=4 well + N=4
rise. Eight leftover-driven
bisections on [0, y_inf] (N=8 budget
on well+rise). Tail parabolas of
tailq stay. q_i matches the 1-jet of
g, m_i = g''(right). a_lo = ½ w g_lo.
True I = ∫ a on [0,1], same shipped a.
Window ±0.003. Finite μ, one v.
Not (∀ L) Q_L≥0.

**Prediction.** Origin uniform N=8
rate ~7×10^{-4} (`Oh2-I01.md`).
Adaptive puts the extra h on high
leftover slabs. Signed gap in
(0.0003, 0.0020), inside ±0.003,
tighter than 0.002793. Still one v,
not Weil.

**Kill.** Gap ≥ 0.002793 (not tighter
than tailq), or leftover-driven split
not used, or g_lo built from Kronrod
on a, or g''' changes sign on [0, y_inf].
