# Impact of assuming linearity

Preregistration after the
μ=62 KILL: drop-3 λ₀
went 0.38 (μ=38) → 0.093
(μ=62). A straight line
crosses 0 at

    μ ≈ 38 + 0.38×24 / 0.287
      ≈ 69.8

so the prediction was
λ₀(74)<0 and λ₀(80)<0.

Measured:

    μ     linear     actual
   62     0.093      0.093
   70     0.000      —
   74    −0.050     +0.090
   80    −0.122     +0.090

The line is already
wrong by 0.14 at μ=74.
Drop-3 has a *floor*
near +0.09 while the
full λ₀ keeps falling
(5.3×10^{-7} → 2.9×10^{-8}).
Linearity mixed two
scales: the well of the
full form (exponential
in L) and the drop-3
remainder (O(10^{-1}),
stuck).

Impact: a linear
preregistration on λ₀
is not a bound and not
a crossing-time. It
killed itself (#44).
Same lesson as Q(v) vs
μ (`Av-Pv-divergence.md`):
a line through a mid
window is not the limit.
