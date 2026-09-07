# Schur χ₇: the χ(2)=+1 cell takes at h=2

Preregistered (`report/prereg-ql-schur-chi7-h.md`):
χ₇, q=7, d=−7, s₀=3/4, χ(2)=+1,
w₂=+log 2/√2. Grid h=2,4,8,16,20,24.
T infinite. Not Galerkin of W_L. Not RH.

The four takes filled χ(2)∈{0,−1} only.
This is the missing sign: Q=A−|w₂|Θ,
the atom lowers H₀₀.

## Execution

`python code/ql_schur_chi7_h.py`.
`report/ql-schur-chi7-h.json`.

w₂=+0.4901, χ(2)=+1, −w₂ θ₀₀(log 2)=−0.362.
H₀₀=0.351 still (CST at q=7 pays the
atom). λ_H(2)=0.338, 18× χ₃'s 0.0185.

| h | λ_min(H) | ρ | S_exact | S_lo | β |
|---|---|---|---|---|---|
| **2** | 0.3384 | 0.473 | +0.309 | **+0.276** | −1.033 |
| 4 | 0.3114 | 0.464 | +0.306 | +0.300 | **+0.065** |
| 8 | 0.3074 | 0.455 | +0.306 | +0.304 | +0.114 |
| 16 | 0.3061 | 0.444 | +0.306 | +0.305 | +0.150 |
| 20 | 0.3059 | 0.439 | +0.306 | +0.305 | +0.162 |
| 24 | 0.3058 | 0.424 | +0.306 | +0.305 | +0.147 |

Neumann takes at h=2. β takes at h=4
(χ₄ needed h=20). The χ(2)=+1 odd cell
is easy: no 2×2 well. S_exact is a
section, not the certificate. S_lo>0 is.

## Verdict: SURVIVE

This bound takes W_{log 3} for χ₇.
The missing sign of the interior prime
is not the obstruction that χ₃ was.
χ₁₇ (same sign, s₀=1/4) is another
line. Not every χ. Not (∀ L). Not RH.

Judge: `tests/test_ql_schur_chi7_h.py`.

## Status

| Claim | Status |
|---|---|
| S_lo>0 on χ₇ at h=2 | judged, this note |
| β>0 on χ₇ at h=2 | **false** |
| β>0 on χ₇ at h=4 | judged |
| χ(2)=+1 is χ₃-hard | **false** |
| c_L^* ≥ 0 for every χ | **open; not taken** |
| (∀ L) Q_L ≥ 0 | RH; not this note |
