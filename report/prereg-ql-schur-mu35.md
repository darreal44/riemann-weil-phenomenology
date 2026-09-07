# Preregistration: Schur at μ=3.5, prime 3 enters

Locked before the run. L=log(3.5). Interior
primes {2,3} (`interior_primes(3.5)`).
On (log 2, log 3] only 2 sat inside; any
μ>3 admits 3. χ(3) may vanish (χ₃).
T infinite. Not Galerkin of W_L. Not a
covering lemma. Not RH.

Q = A − ∑_{p<μ} χ(p) (log p)/√p Θ(log p).
At μ=3 this is the old Q_nm. At μ=3.5
a second atom T₃ of weight |χ(3)|log3/√3
=0.634 when χ(3)≠0. ‖Θ(log p)‖≤1 still
(log 2 and log 3 are ≥ L/2). Same Neumann
split, N_NEAR=max(32,h+16). DELTA_N_MAX=0.40
still covers IBP at this L.

**This run.** `code/ql_schur_mu35.py`.
h-grid 2,4,8,16,20,24 on χ₃, χ₅, χ₄
(the ones T₃ hits). Snapshot χ₈, χ₇, χ₁₇
at h=2. Control: Q at μ=3 equals Q_nm.

**Prediction.** χ₃: S_lo(2)<0, S_lo(4)>0
(χ(3)=0, only L grew). χ₅ and χ₄:
S_lo(2)<0, S_lo(4)>0 (T₃ kills h=2,
raise-h restores). χ₈, χ₇, χ₁₇ stay
S_lo(2)>0. Not (∀ L).

**Kill.** S_lo(24)≤0 on χ₃ or χ₅ or χ₄,
or S_lo(2)≤0 on χ₈.
