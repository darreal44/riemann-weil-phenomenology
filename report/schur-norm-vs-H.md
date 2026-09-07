# Schur remainder vs λ_min(H) — χ₂₉ Gram

Wanted: ‖C T⁻¹ Cᵀ‖ < λ_min(H) ⇒ Δ>0 ⇒ Q>0.
Measured on the hat Gram (proxy for Q at 1%).

| μ | λ₀ | λ_min(H) | ‖Schur‖₂ | ratio | bound | λ_min(Δ)/λ₀ |
|---|---|---|---|---|---|---|
| 8 | 0.894 | 0.950 | 0.100 | 0.11 | yes | 1.012 |
| 11 | 0.298 | 0.338 | 0.054 | 0.16 | yes | 1.009 |
| 14 | 0.132 | 0.183 | 0.127 | 0.70 | yes | 1.012 |
| 18 | 0.026 | 0.056 | 0.167 | 3.0 | no | 1.006 |
| 22 | 0.004 | 0.037 | 0.164 | 4.4 | no | 1.007 |

The operator-norm test dies at the same
μ≈16 as A_eff and the union λ_max.

Δ stays positive: the Schur correction is
not aligned with the ground state of H.
κ(T) stays O(1) on this window.

A proof cannot use ‖·‖₂. It needs the
quadratic form of C T⁻¹ Cᵀ on the
2-level IR vector only.
