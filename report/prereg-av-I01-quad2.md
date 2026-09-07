# Preregistration: I_{[0,1]} two-piece quadratic on the well

Locked before the run. Same witness
v=(4,−3,1)/√26, χ₅ μ=16. Not the
single-m quadratic of #83 (miss
0.047), which used inf g'' on the
whole [0, y_min]. Origin: spend
nodes near 0 or a quadratic on a
short initial interval
(`g-convexity.md`). Not Weil.
Not RH.

g'''<0 on [0, y_min] ⇒ g''
decreases. Split at y_h = y_min/2.

  m1 = g''(y_h)
  m2 = g''(y_min)
  q1(y) = g'(0) y + (m1/2) y²
  on [0, y_h], then
  q2(y) = q1(y_h) + q1'(y_h)(y−y_h)
          + (m2/2)(y−y_h)²
  until it meets the floor g_min
  at y_q. Then floor / tinf /
  chord as in the envelope.

a_lo = ½ w g_lo. Integrate a_lo,
not a. True I = ∫ a on [0,1],
same shipped a. Window ±0.003.
Finite μ, one v. Not (∀ L) Q_L≥0.

**Prediction.** y_h < y_q < y_min.
The signed gap I_true − I_lo is in
(0.01, 0.045): tighter than 0.047,
still outside ±0.003. Q_lo from
I_lo is negative. This comparison
does not close. It is not Weil
positivity.

**Kill.** g''' changes sign on
[0, y_min], or y_q not in
(y_h, y_min), or gap < 0.003
(would have closed), or gap ≥ 0.047
(not tighter than the single-m
quadratic).
