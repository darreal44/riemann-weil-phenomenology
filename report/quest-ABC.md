# A, B, C after the freeze

## A. Same window, Frobenius

`RETURN_S=1 python code/compare_QG.py chi29 μ N dps`

| μ | G/Q (λ0) | ||G−Q||_F / ||Q||_F |
|---|----------|----------------------|
| 11 | 0.929 | 0.065 |
| 22 | 0.882 | 0.054 |
| 38 | 0.826 | 0.041 |

Four to seven percent on the whole matrix; F-norm falls with μ.
The drift in λ0 is the same size as the matrix
discrepancy. Not 1 %, not a proof.

## B. Constant mode, μ=2

`python code/q_mu2_constant.py`

θ_00(log 2)=0 when L=log 2, so p=2 does not enter
the (0,0) entry. Q_00 is pure arch:

    χ₅: CST=0.175, Q_00=0.393 > 0
    χ₄: CST=−0.048, Q_00=0.513 > 0

This is a 1×1 integral, not eigh. Full-window λ0
at μ=2 was 0.325 (χ₅): the extra modes pull it down
but stay positive. Still not a hand bound on Γ′/Γ;
it is a quadrature of an explicit positive-looking
kernel (int=0.43>0 plus CST).

## C. A on Iᶜ

`python code/sampling_A.py name μ N`

A_hat = λ0(Gram) exp(π τ γ1)

| L | μ | πτγ1 | λ0 | A_hat |
|---|---|------|-----|-------|
| χ₂₉ | 11 | 6.76 | 0.281 | 242 |
| χ₂₉ | 22 | 8.71 | 3.67e-3 | 22 |
| χ₂₉ | 38 | 10.25 | 5.75e-6 | 0.16 |
| 11a1 | 22 | 30.89 | 1.38e-10 | 3.6e3 |

A_hat is not stable in μ. The Slepian ceiling is
loose; A is a window-dependent remainder, not a
constant of the zero set. Lemma 2 stays valid as
an inequality, not as a way to read a universal A.
