# Catalog of “proofs” in the repo

None of these is RH.
Judges live in `tests/`.

## Proved (linear algebra / identities)

- Courant–Fischer on hats:
  λ_min(V) ≥ λ_min(Q).
  2-plane SPD does not
  lift. (#42: same fact
  the other way for W_L.)
- Schur: T>0 ⇒
  Q>0 ⇔ Δ>0.
  Sign is an identity.
  ‖C T⁻¹ Cᵀ‖ bound is
  not.
- Discrete Landau:
  dim ker Eval ≥ n(ω)−N_Γ(ω).
  Any nodes. Equality
  #{ℓ>2}=D_max is not
  an identity.
- θ_{f₁}≥0 closed
  (`demonstrations.md`).
- Edge split
  ψ̂ = jump + r, exact
  algebra.

## Killed predictions (not theorems)

- 37a1 drop-3 → − at
  μ=62 (#41), μ=74, μ=80
  (#44). Linear μ≈70
  dead.
- A−P₂₃ crosses P_rest
  at μ=150 (#45). They
  went through 0
  together.
- Landau well-count
  without a cut:
  ‖G|_ker‖≈3.4, not
  e^{−2}.
- Hubbard / Kondo / BCS
  / friction: dictionaries
  closed, no operator.

## Measured, not proved

- Q(v)∈[0.003,0.009]
  on μ=16..150, this v.
- Drop-3 floor ≈0.09
  on 62..80.
- 67a1 μ=74 quorum
  complete (#43).
- A₀₀ saturates via D₂.
- P has no P_∞
  (tower walk).

## Still missing for a proof of positivity

A class of test
functions on which
Q>0 is known a priori,
or a bound that keeps
Δ>0 when T is only
estimated, or
inf_{W_L} Q ≥ 0.
Courant the wrong way
blocks the last one
from a Galerkin
certificate.
