# What Fmat w₂ actually is

    w₂ = ∫_{|λ−2| < 0.12·2}
           d(λ) / λ  dλ
       = ∫_{window} d(λ) d*λ

d = τ_S − τ_arch
(`tau_curve`). d*λ = dλ/λ
is multiplicative Haar
on R>0.

So the campaign already
integrates against d*λ,
not against dλ. Bombieri
(log 2)/√2 was the
target if d were a
Lebesgue density and
one converted wrong.
The code’s own
integrand is the
module Haar on the
slice.

If d(λ) d*λ is the
push of Connes d*u,
the number w₂ should
approach a *shell
mass in d*u*:
1/√2 (module) or
√2 (inverse),
depending on
λ ↔ |u|_2 or
λ ↔ |u^{-1}|_2.

#46 goes to √2.
The remaining line
is: in `tau_curve`,
is λ = |u|_2 or
λ = |u^{-1}|_2?
That is a read of
the map r ↦ λ in
`trace_dist.py`,
not another job.
