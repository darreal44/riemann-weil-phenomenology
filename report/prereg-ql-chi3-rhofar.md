# Preregistration: χ₃ ρ_far, larger N_NEAR / 3-layer

Locked before the run. L=log 3, h=2,
same cosine ONB and same Neumann split
as #61 (`ql-schur-neumann.md`). T stays
infinite. Not Galerkin of W_L. Not a
covering lemma. Not RH.

Named in `chi3-obstacles.md` item (3):
the far tail of A (ρ_far=0.50 at N=32)
is the piece a larger split might eat,
as raising h did for χ₄. χ₃ still has
T₂, so N alone may not copy. Do not
raise h of H (Courant lowers λ_H).

Need ρ<0.41 for S_lo(χ₃)>0, because
S_diag=+0.0076 leaves 0.0109 of
λ_H=0.0185, and 0.0109/(1−ρ)<0.0185
forces ρ<0.41. ρ ≥ ρ_far, and

    ρ_far = (π/2 + 1/(4N) + r_F + |w₂|)
            / qmin_far

Hilbert π/2 is N-independent on the
continuous analog. |w₂|=log 2/√2.

**This run.** `code/ql_chi3_rhofar.py`.
2-layer grid N_NEAR=24,32,40,48,64,80
(M_C=40,40,56,64,80,96). 3-layer split
n=2..23 / 24..47 / ≥48, far Hilbert+Θ
over qmin on [48,64). Hankel-only
diagnostic (t₂=0) on the same rows.
Four numbers from Q_nm Gauss, same
function as #61.

**Prediction.** S_lo(χ₃)<0 on the whole
2-layer grid. ρ_far(80)≥0.41. ρ_N
climbs with N (finite Hankel filling).
S_diag stays +0.0075 (C already in the
N=24 block). 3-layer ρ ≥ ρ_far(48)>0.41
and S_lo<0. Hankel-only ρ still >0.41
(T₂ is not the only wall). χ₃ not taken.

**Kill.** Any S_lo(χ₃)>0, or ρ_far(80)<0.41.
