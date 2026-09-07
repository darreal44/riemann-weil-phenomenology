# Preregistration: Schur with Neumann T^{-1}, not Frobenius/δ

Locked before the run. L=log 3, h=2.
Named in `chi5-hankel-not-enough.md` and
`schur-diag-T.md`: the obstruction is the
majorant of C, not C. S_diag=+0.042 is a
number until T^{-1} is bounded near D^{-1}.

T = D^{1/2}(I+A)D^{1/2}, A=D^{-1/2} Off D^{-1/2}.
Split A into near / coupling / far. ρ is the
2×2 block-norm of (ρ_N, ρ_B, ρ_far). If ρ<1,

    T^{-1} ≤ D^{-1}/(1−ρ)
    S ≥ H − C D^{-1} C* / (1−ρ)

Not Galerkin of W_L. Not a covering lemma.
Not RH.

**This run.** `code/ql_schur_neumann.py`:
near n=2..31 (Gauss), far Hankel+Θ bound
over qmin_far, coupling Frobenius plus
Hankel tail. Four characters.

**Prediction.** ρ(χ₅)<1 and S_lo(χ₅)>0
(takes χ₅). χ₃ still S_lo≤0. χ₈ and χ₄
stay positive.

**Kill.** S_lo(χ₅)≤0 or ρ(χ₅)≥1.
