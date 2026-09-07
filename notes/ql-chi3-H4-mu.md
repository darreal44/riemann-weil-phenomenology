# χ₃: μ* of λ_min(H₄) is in (4.75, 5]

Preregistered (`report/prereg-ql-chi3-H4-mu.md`):
grid μ=3.5, 3.75, 4, 4.25, 4.5, 4.75, 5.
h=2 and 4. Same Q_window as #66/#67.
No Neumann. Not RH.

## Execution

`python code/ql_chi3_H4_mu.py`.
`report/ql-chi3-H4-mu.json`.
μ=3.5 and μ=5 match #66/#67.

| μ | L | log2≥L/2 | λ_min(H₂) | λ_min(H₄) |
|---|---|---|---|---|
| 3.50 | 1.253 | yes | +0.00762 | **+0.00268** |
| 3.75 | 1.322 | yes | +0.00488 | +0.00127 |
| **4.00** | 1.386 | yes | +0.00298 | +0.00063 |
| 4.25 | 1.447 | no | +0.00166 | +0.00036 |
| 4.50 | 1.504 | no | +0.00080 | +0.00024 |
| **4.75** | 1.558 | no | +0.00035 | **+0.00010** |
| **5.00** | 1.609 | no | +0.00024 | **−0.00016** |

H₂ stays positive. H₄ stays positive
through 4.75 and is negative at 5.
μ* ∈ (4.75, 5]. The hat-unit threshold
μ=4 is not the crossing: H₄(4)=+0.00063.
Primes stay {2,3}; χ₃ has χ(3)=0, so
the sign change is L (archimedean
pairing on a longer window), not T₃
and not T₅ (p=5 is the endpoint).

A negative H₄ is c_L^*<0 on that
4-plane. Positive H₄ is not a take
of W_L (Courant the wrong way).

## Verdict: SURVIVE

This construction for χ₃ goes negative
on the 4-plane in (4.75, 5]. We do not
identify that with a failure of RH.
Not (∀ L). Not RH.

Judge: `tests/test_ql_chi3_H4_mu.py`.

## Status

| Claim | Status |
|---|---|
| μ* ∈ (4.75, 5] | judged, this note |
| crossing at μ=4 (Θ-jump) | **false** |
| H₂>0 on the grid | judged |
| (∀ L) Q_L ≥ 0 | RH; not this note |
