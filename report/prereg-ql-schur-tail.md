# Preregistration: Schur tail of Q̂_L on W_log3

Locked before the run. L = log 3. Split h=2
in the cosine ONB. Four characters χ₅, χ₈,
χ₄, χ₃. Not Galerkin of W_L: H is a finite
block, T and C are infinite and bounded,
not assembled. Not a covering lemma. Not RH.

    Q = [ H  C ]
        [ C* T ]

    β = λ_min(H) − ‖C‖_F² / δ
    δ = inf_{n≥2} Q_nn − ‖Off_T‖

Off_T for χ(2)=0 is the Hankel 1/(2(n+m))
plus an HS remainder from I_sin(ω_n)−π/2.
‖[1/(n+m)]‖ ≤ π (Hilbert 1894). T₂, when
present, is a discrete Hilbert 1/(n−m) of
norm ≤ 2|w₂|.

H and the listed Q_nn, Q_0j, Q_1j are 1D
Gauss of the regular integrand (same path
as `ql_operator_bound.Q_cosine`). Infinite
tails of C are 1/j² sums.

**Prediction.** β > 0 on χ₈ (the bound
takes W_{log 3} for χ₈, where Q=A). β < 0
on χ₅ and χ₃ (T₂ Hilbert eats δ). χ₄ is
computed; not predicted to take. The class
step for characters with χ(2)=−1 stays
open. Not (∀ L).

**Kill.** β ≤ 0 on χ₈, or β > 0 on χ₅.
