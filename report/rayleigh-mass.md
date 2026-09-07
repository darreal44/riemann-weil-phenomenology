# Out-of-cut mass of the ground well

Rayleigh on ker Eval_ω*
(`landau-depth.md`): for the
min eigenvector x of G,

    xᵀ G x = 2 ∑_γ |η(γ)|²
            = mass on γ ≥ ω*
              if x is in the
              kernel below ω*.

μ=16, N=30, ω* = argmax
(n(ω)−N_Γ(ω)):

    χ      D_max  K*   ω*    frac(γ≥ω*)   ell_0
    χ₅     3.08   5   16.03  1.0000       35.6
    χ₈     1.77   3    4.90  1.0000       20.6
    χ₁₃    1.19   3    7.23  1.0000       11.3

In-band mass below ω* is
10^{-10} or smaller
(float64 zero for χ₈).
The well *is* the out-of-cut
mass. Lemma checked.

## What would close the count

A Slepian / Beurling bound

    mass(γ ≥ ω*)  ≤  e^{−C}
    with C > 2, uniformly
    on the unit sphere of
    ker Eval_ω*,

would give #{ℓ > 2} ≥ K*
by min-max, and K* ~
round(D_max). That is the
threshold-free equality,
and it is exactly the
hypothesis the depth note
already flags as unproved
("If ‖G|_ker‖ ≤ e^{−C}").

The number e^{−ell_0} is
the mass of *one* vector,
the ground well. The bound
has to hold for the whole
K*-plane. Measuring ell_0
does not give it.
