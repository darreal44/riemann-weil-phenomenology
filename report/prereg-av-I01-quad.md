# Preregistration: I_{[0,1]} quadratic support near 0

Locked before the run. Same witness
v=(4,−3,1)/√26, χ₅ μ=16. Not the
chord of θ (miss 0.22). Not the
parent 3-piece (miss 0.224). Not
the switch (miss 0.088). Not the
three-tangent envelope (miss
0.068). Origin named the loose
piece: g''(0)≈9.6 peels the
tangent at 0 (`g-convexity.md`).
Not Weil. Not RH.

g = 2 e^{−3y/2} − θ_v, elementary.
On [0, y_min], if g'''<0 then g''
decreases, so inf g'' = g''(y_min)
=: m > 0. Taylor with remainder:

    g(y) ≥ g'(0) y + (m/2) y²  =: q(y)

on [0, y_min]. q meets the floor
g_min at y_q. Then the envelope
of #82 after that: floor to y_meet,
tangent at y_inf, chord on the
concave tail.

Comparison g_lo:
  [0, y_q]         q
  [y_q, y_meet]    floor g_min
  [y_meet, y_inf]  tinf
  [y_inf, 1]       chord of g

a_lo = ½ w g_lo. Integrate a_lo,
not a. True I = ∫ a on [0,1],
same shipped a. Window ±0.003.
Finite μ, one v. Not (∀ L) Q_L≥0.

**Prediction.** g'''<0 on [0, y_min].
y_sw < y_q < y_min. The signed gap
I_true − I_lo is in (0.02, 0.065):
tighter than the envelope 0.068,
still outside ±0.003. Q_lo from
I_lo is negative. This comparison
does not close. It is not Weil
positivity.

**Kill.** g''' changes sign on
[0, y_min], or y_q not in
(y_sw, y_min), or gap < 0.003
(would have closed), or gap ≥ 0.068
(not tighter than the envelope).
