# Parallel run 6 September — judged numbers only

Protocol: a number enters this table only if a shipped function
reproduces it in `tests/`. Two scripts that disagree are an
artifact, not a result (journal: family « conclure avant le juge »).

## Heavy tests

`tests/run_heavy.py -j 6`: 8 files, 77 s, 0 failed.
Locked by that runner.

## χ₃ μ=80 (scan_s.assemble)

Judge: `tests/test_chi3_mu80_judge.py`.

| NB | dps | λ₀ | ℓ |
|---|---|---|---|
| 8 | 28 | >0 | >40 |
| 24 | 50 | 4.183×10⁻⁴⁹ | 111.4 |

**Not harvested.** `scan_s` at NB=32 dps=70 gave λ₀ < 0;
`edge_value_scan` (spectro.py, more quadrature panels) gave λ₀ > 0
and ℓ=135. Different assemblies, no judge. Do not quote ℓ=135.

## Li coefficients (ζ)

Judge: `tests/test_li_lambda.py`, shipped `code/li_lambda.py`.
λ₁ closed form 0.023095708966. Prefix n=1..12 from 150 zeros
all positive; zeros undershoot λ₁ (tail missing). Finite check,
not RH.

## Q vs Gram, χ₂₉ μ=11 N=25

Judge: `tests/test_compare_QG.py`.
G/Q(λ₀)=0.929, ‖G−Q‖_F / ‖Q‖_F=0.065.
‖G−Q‖_F > λ_min(G): the truncated-list inequality
|Q−Gram|<λ_min does **not** hold. Route closed as a proof
(missing high zeros, not off-line zeros).

## det(A−P) on the 2-plane, μ=16

Judge: `tests/test_H2_det_positive.py`, `H_2plane_independent.H2`.
det>0 and λ_min(H)>0 for χ₅, χ₃, χ₄, χ₈, χ₁₃.
P is O(A), not a rounding term.

## 37a1 μ=62 (preregistered §116)

Judge: `tests/test_gl2_37a1_mu62.py`, `scan_gl2.gram`.
Zero-Gram λ₀>0, ℓ∈(10,40). Rank-1 well, central zero in the Gram.
Prime-side Q from `scan_q_gl2` (ℓ=14.46) is a different matrix
(no central zero on the prime side until the rank is read).
Do not identify the two numbers.
