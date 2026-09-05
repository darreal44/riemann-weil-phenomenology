# Operator norm of D = G − Q

||D||₂ = σ_max(D) = σ₀ of the residual SVD.

| μ | ||D||₂ | ||Q||₂ (≈ λ_max) | ||D||₂/||Q||₂ | ||D||_F/||Q||_F |
|---|--------|-------------------|----------------|-----------------|
| 11 | 1.615 | 7.45 | 0.217 | 0.065 |
| 22 | 1.703 | ~10 | ~0.17 | 0.054 |
| 38 | 1.880 | — | — | 0.041 |

||D||₂ grows like σ₀, slowly. The operator
relative error is *larger* than the Frobenius
relative error: the residual is concentrated
in one direction, so the 2-norm feels all of
it and the F-norm averages over 25–67 modes.

||D||₂ ≫ λ_min(Q) at every window
(1.6 vs 0.30 at μ=11; 1.88 vs 7e-6 at μ=38).
As an operator, D is not a small perturbation
of Q on the whole space. It is a small
perturbation *on the ground-state line*
(Rayleigh −0.015) and a large one on a
high-k line.

That is the precise sense in which “G→Q”
is true (bulk, F-norm) and false (operator
norm, RH bound).
