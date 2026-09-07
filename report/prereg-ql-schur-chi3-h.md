# Preregistration: Schur χ₃ at larger h

Locked before the run. L=log 3. χ₃ only.
Grid h = 2, 4, 8, 16, 20, 24, same as
`ql-schur-chi4-h.md`. T stays infinite.
Not Galerkin of W_L. Not a covering
lemma. Not RH.

Two bounds on the same split, same
Q_nm Gauss:

1. β = λ_H − ‖C‖_F²/δ, Off_T =
   Hankel π/2 + HS rem + T₂
   (the #60 machine, with T₂ because
   χ(2)=−1). C: Gauss to M=40 plus
   `c_tail_sq`.
2. Neumann S_lo of #61, head = h,
   N_NEAR = max(32, h+16), M_C =
   N_NEAR+8. Certificate is S_lo>0
   and ρ<1, not S_exact of a section.

Named in `chi3-obstacles.md`: h alone
may not copy χ₄ because χ₃ still has
T₂. Combining with Neumann is the
test. Do not take S_exact=+0.0097
as a certificate (`chi3-S-exact.md`).

**Prediction.** β never positive
(δ<0 at h=2,4; β<0 after). S_lo(2)<0
(matches #61). S_lo>0 at h=4,8,16,20,24.
First positive on the grid is 4, so
h* ∈ (2, 4]. Takes W_{log 3} for χ₃.
λ_H falls (Courant).

**Kill.** S_lo(24)≤0, or S_lo(2)>0
(would contradict #61).
