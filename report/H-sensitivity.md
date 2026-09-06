# Sensitivity of H

χ₅ μ=16, 3-plane.

    spec(H) = {3×10^{-5}, 0.0023, 0.522}
    cond    = 1.6×10^4
    ‖H‖_F   = 0.48
    ‖H‖₂    = 0.52

H is ill-conditioned
because of the well, not
because the entries are
wild. The entries are
O(0.1).

Budget to kill Q=0.0055
with one entry
(`H-impact.md`):

    |ΔH₀₁| ≳ 0.006
    |ΔH₀₀| ≳ 0.009
    |ΔH₂₂| ≳ 0.14

A 5% relative error on
H₀₁ (0.133±0.007) is
enough to wipe the
witness. A 5% error on
H₂₂ is irrelevant.

That is the quadrature
budget for A: the
integral that feeds
H₀₁ must be good to
~5×10^{-3} absolute.
The Q-v-ball
[0.0040, 0.0065] is
exactly that budget
spent on A(v) rather
than on each entry.

cond(H) being 10^4 does
not mean the witness is
unstable under *entry*
noise of size 10^{-4}.
It means λ_min is small.
Those are different
sensitivities.
