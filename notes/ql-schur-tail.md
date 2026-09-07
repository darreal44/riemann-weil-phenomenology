# Schur tail of Q̂_L on W_{log 3}

Preregistered (`report/prereg-ql-schur-tail.md`):
split h=2 in the cosine ONB. H is a finite
2×2. T and C are infinite, bounded, not
assembled. Not Galerkin of W_L. Not RH.

## Execution

`python code/ql_schur_tail.py`.
`report/ql-schur-tail.json`.

    Q = [ H  C ]
        [ C* T ]     β = λ_min(H) − ‖C‖_F² / δ

δ = inf_{n≥2} Q_nn − ‖Off_T‖. Off_T for
χ(2)=0 is the Hankel 1/(2(n+m)) (Dirichlet
cancellation of ∫ D₂ sin) plus an HS
remainder from I_sin(ω_n)−π/2. ‖[1/(n+m)]‖≤π
(Hilbert 1894). T₂, when present, is a
discrete Hilbert of op-norm ≤ 2|w₂|.

H and the diagonals n=2..40 match `scan_s`
on the 2×2 (S₀₀, S₁₁). inf Q_nn on that
range is at n=2; Q_{39} is still larger
(χ₈: 2.80 → 5.66).

| χ | χ(2) | λ_min(H) | δ | ‖C‖_F | β |
|---|---|---|---|---|---|
| χ₅ | −1 | +0.0530 | **−0.679** | 0.417 | — |
| χ₈ | 0 | +0.2575 | +0.876 | 0.421 | **+0.0549** |
| χ₄ | 0 | +0.0839 | +0.183 | 0.421 | −0.881 |
| χ₃ | −1 | +0.0185 | **−1.189** | 0.416 | — |

β>0 is sufficient for \(\hat Q_L\ge0\) on
W_{log 3} (completing the square). χ₈ has
no T₂, Q=A, and the remainder is positive.
χ₅ and χ₃: T₂ of size 0.98 eats δ. χ₄ has
no T₂ but qmin=2.11 is too close to π/2.

## Verdict: SURVIVE

This bound takes W_{log 3} for χ₈. It does
not take χ₅, χ₃, or χ₄. The (log 2, log 3]
step for χ(2)=−1 stays open. Not (∀ L).
Not RH.

Judge: `tests/test_ql_schur_tail.py`.

## Status

| Claim | Status |
|---|---|
| β>0 on χ₈ (takes W_L for χ₈) | judged, this note |
| β>0 on χ₅ | **false** (T₂, δ<0) |
| Galerkin takes the class | false (`pw-log3.md`) |
| Bochner α_line ≥ 0 | false (`ql-operator-bound`) |
| c_L^* ≥ 0 on W_{log 3} for every χ | **open; not taken** |
| (∀ L) Q_L ≥ 0 | RH; not this note |
