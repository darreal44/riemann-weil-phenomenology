# Preregistration: Schur χ₇, the χ(2)=+1 cell

Locked before the run. L=log 3. χ₇ only
(q=7, d=−7, s₀=3/4, χ(2)=+1, w₂=+log2/√2).
Grid h = 2, 4, 8, 16, 20, 24, same as
`ql-schur-chi3-h.md`. T stays infinite.
Not Galerkin of W_L. Not a covering
lemma. Not RH.

The four takes (#58,#60,#61,#63) filled
χ(2)∈{0,−1} only. This is the missing
sign: Q = A − |w₂|Θ, the atom lowers
H₀₀. Same Neumann + raise-h machine.

**This run.** `code/ql_schur_chi7_h.py`.
β = λ_H − ‖C‖_F²/δ with T₂. S_lo is
the #61 Neumann bound, head=h,
N_NEAR=max(32,h+16). Local Q_nm, not
an edit of the four-character CHARS.

**Prediction.** w₂>0. S_lo(2)>0 (takes
at h=2, unlike χ₃). β(2)<0, β(4)>0.
λ_H falls. The χ(2)=+1 odd cell is
easy: λ_H(2) is O(0.3), not χ₃'s 0.018.

**Kill.** S_lo(2)≤0.
