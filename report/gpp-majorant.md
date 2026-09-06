# g'' on [1, y*]: formula and failed termwise bound

    g(y) = 2 e^{-3y/2} − θ_v(y)
    g''(y) = (9/2) e^{-3y/2} − θ_v''(y)

θ_v'' is the same six lag
kernels, differentiated
twice (`code/av_gpp.py`).
Checked against a second
difference at y=1.2
(1.3270 vs 1.3270).

## Sampled range

    θ_v'' ∈ [0.864, 1.704]
    g''   ∈ [−0.707, −0.411]

on [1, 1.59], 400 nodes.
Always negative: g concave,
as used in `g-concavity.md`.

## Termwise / interval bound

|sin|,|cos|≤1, even restricted
to the actual angles

    ω₁ y ∈ [130°, 206°]
    ω₂ y ∈ [260°, 413°]

gives

    θ_v'' ∈ [−6.0, 8.3]
    g''   ∈ [−8.0, 7.0]

Useless: ten times the
sampled range. The large
pieces are θ₁₁'' (up to 8)
and θ₂₂'' (interval width
48). They cancel inside
v₁² θ₁₁ + v₂² θ₂₂ + 2 v₁ v₂ θ₁₂.
Taking max first throws
the cancellation away —
the same pattern as
H₁₂ and det H.

## What would prove |g''|≤0.71

Keep the combination as
one trig polynomial of
frequencies 0, ω₁, ω₂,
2ω₁, 2ω₂ (products of
sin/cos already linear
after differentiation).
Bound that polynomial
on a compact interval
by a Markov brothers'
inequality from a grid,
or by evaluating the
explicit form at the
critical points g'''=0.
Not written.

Until then |g''|≤0.71
is a measurement, and
the trapezoid error
~2×10^{-3} on four
slabs is conditional
on that measurement.
