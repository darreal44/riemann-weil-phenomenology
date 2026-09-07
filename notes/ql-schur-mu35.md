# Schur at μ=3.5: prime 3 enters, raise-h still takes

Preregistered (`report/prereg-ql-schur-mu35.md`):
L=log(3.5). Interior primes {2,3}.
Q = A − ∑_{p<μ} χ(p)(log p)/√p Θ(log p).
T infinite. Not Galerkin of W_L. Not RH.

There is no window in (log 3, log 4)
with only the prime 2: any μ>3 admits 3.
χ₃ has χ(3)=0, so only L grows. The
others get a second atom |w₃|=log3/√3
=0.634, larger than |w₂|=0.490.
‖Θ(log p)‖≤1 still.

## Execution

`python code/ql_schur_mu35.py`.
`report/ql-schur-mu35.json`.
Q at μ=3 matches Q_nm (judge).

| χ | χ(3) | h | λ_H | S_lo |
|---|---|---|---|---|
| χ₃ | 0 | 2 | 0.0076 | −0.0121 |
| χ₃ | 0 | **4** | 0.0027 | **+0.0001** |
| χ₃ | 0 | 8 | 0.0020 | +0.0016 |
| χ₅ | −1 | 2 | 0.0307 | −0.0496 |
| χ₅ | −1 | **4** | 0.0158 | **+0.0067** |
| χ₄ | −1 | 2 | 0.0503 | −0.0251 |
| χ₄ | −1 | **4** | 0.0265 | **+0.0189** |
| χ₈ | −1 | 2 | 0.1758 | **+0.116** |
| χ₇ | −1 | 2 | 0.2532 | **+0.098** |
| χ₁₇ | −1 | 2 | 0.5481 | **+0.458** |

T₃ kills h=2 on χ₅ and χ₄; the same
raise-h as #63 restores them at h=4.
χ₃'s sliver at h=4 is 10⁻⁴ (L ate H);
h=8 is comfortable. S_exact stays
positive on every row (section, not
the certificate).

## Verdict: SURVIVE

The bound takes W_{log 3.5} for these
six, with h*=4 on χ₃, χ₅, χ₄ and h=2
on χ₈, χ₇, χ₁₇. One extra L, not (∀ L).
Not every χ. Not RH.

Judge: `tests/test_ql_schur_mu35.py`.

## Status

| Claim | Status |
|---|---|
| S_lo>0 on χ₃,χ₅,χ₄ at h=4 | judged |
| S_lo>0 at h=2 after T₃ on χ₅,χ₄ | **false** |
| only prime 2 on (log 3, log 4) | **false** |
| c_L^* ≥ 0 for every χ | **open; not taken** |
| (∀ L) Q_L ≥ 0 | RH; not this note |
