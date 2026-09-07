# Preregistration: I_{[0,1]} N=4 quadratic mesh

Locked before the run. Same witness
v=(4,−3,1)/√26, χ₅ μ=16. Named in
`report/quadratic-mesh.md`: broken
supporting parabolas, local inf g''.
N=1 is #83 (miss 0.047). N=4 is the
h≲0.1 count of `quadratic-error.md`.
Not another global tangent. Not Weil.
Not RH.

Uniform nodes 0=y₀<…<y₄=y_min,
h=y_min/4. On I_i=[y_i, y_{i+1}]

    m_i = inf_{I_i} g'' = g''(y_{i+1})
    (g'''<0 ⇒ g'' decreases)
    q_i(y) = g(y_i)+g'(y_i)(y−y_i)
             +(m_i/2)(y−y_i)²

q_i ≤ g on I_i (matches jet 1 at
y_i). g_lo is that broken parabola
on [0, y_min], then floor / tinf /
chord after y_min as in the envelope.

a_lo = ½ w g_lo. Integrate a_lo,
not a. True I = ∫ a on [0,1],
same shipped a. Window ±0.003.
Finite μ, one v. Not (∀ L) Q_L≥0.

**Prediction.** Origin: four pieces
may halve 0.047, not close ±0.003.
Signed gap I_true − I_lo in
(0.008, 0.040). Q_lo from I_lo is
negative. This comparison does not
close. It is not Weil positivity.

**Kill.** g''' changes sign on
[0, y_min], or gap < 0.003 (would
have closed), or gap ≥ 0.047 (not
tighter than N=1 / #83).
