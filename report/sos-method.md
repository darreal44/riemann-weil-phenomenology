# SOS method, as it stands

Three identities
on a window with
Q≻0, V_N hats:

    Q = ∑ λ_j v_j v_jᵀ     spectral
      = Cᵀ C                Cholesky
      = ∑_γ η̂(γ) η̂(γ)ᵀ     zeros

The first two
are SOS. They
were computed
(μ=11: 47
squares,
congruence).
They are not
arithmetic:
rows of C are
coordinates,
not lags.

Arithmetic
intent:

    T_L^* T_L = A + P − ∑ T_p
    each row of T_L is
    a local pairing
    (archimedean kernel
    or τ_{log p^k}).

Ansatz on one
prime (μ=3):

    (T f)_2 = √(log 2)·2^{-1/4}
              (α f + β τ_{log 2} f)
    plus a row T_∞ f.

Four real
scalars plus
T_∞ cannot
reproduce a
9×9 of rank 9.
Internal lags
2^k≤3 do not
exist.

Why the count
fails: Euler
has as many
rows as prime
powers ≤μ
(one tower at
μ=3, four at
μ=11). The
zero-side
factor has
one row per
γ in band —
the right
dimension.
An arithmetic
SOS must
therefore use
a *continuous*
archimedean
fibre (the
Weil integral
in y), not
only discrete
lags. That
fibre is not
itself a
square for
L>0.85
(λ_min(Q_∞)
<0). Mixing a
non-square
continuous
piece with
discrete
indefinite
T_p is the
whole method
problem.

Schur (#58)
bounds Q̂_L
without
factoring it.
SOS wants
the factor.
They are
not the same
route.

Status in
`notes/sos-arithmetic.tex`:
explored, not
constructed.
Closed SOS =
zeros. Every L
= RH.
