# Preregistration: ‖Θ(log 2)‖ on the tail, not Hilbert 2

Locked before the run. L = log 3, y = log 2.
Not Galerkin. Not a covering lemma. Not RH.

#58 used |θ_nm| ≤ 2/(π|n−m|) and the discrete
Hilbert transform to get ‖Θ‖ ≤ 2, hence
t2_op = 2|w₂| ≈ 0.98, which ate δ on χ₅.

On (log 2, log 3] one has y = log 2 ≥ L/2
(because 2 ≥ √3). For even f, the overlap
J and its source sit in opposite halves and
are disjoint; with the repo’s θ(0)=2,

    |θ_f(log 2)| ≤ 1    (hat-unit f).

So ‖Θ(log 2)‖ ≤ 1 on W_L and on the tail
n≥2. Sharp: finite sections hit 1 to 1e-15.

**This run.** Shipped `code/ql_theta_tail.py`:
lemma y≥L/2; finite-section ‖Θ‖; Schur β
with t2_op = |w₂|·1 instead of |w₂|·2.
C and Hankel+R unchanged from #58.

**Prediction.** ‖Θ‖ ≤ 1. t2_op halved
(0.98 → 0.49). χ₅ and χ₃ still δ<0
(Hankel+R leave 0.30 of qmin, |w₂|=0.49
eats it). χ₈ unchanged (no T₂). χ(2)=−1
not taken.

**Kill.** Finite-section ‖Θ‖ > 1.001, or
χ₅ δ>0, or χ₈ β≤0.
