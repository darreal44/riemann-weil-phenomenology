# ‖Θ(log 2)‖ ≤ 1 on W_{log 3}

Preregistered (`report/prereg-ql-theta-tail.md`):
the discrete-Hilbert bound ‖Θ‖≤2 of #58 is
false once y≥L/2. Not Galerkin. Not RH.

## Lemma

On (log 2, log 3], the only interior prime
is 2, and y=log 2 ≥ L/2 because 2≥√3
(y/L=log 2/log 3≈0.6309). Hats are an ONB
of even L², θ(0)=2. For y≥L/2 the overlap
J=[y−L/2, L/2] sits in [0, L/2], disjoint
from the opposite half; evenness gives
‖f‖_J ≤ ‖f‖/√2, and θ=2⟨f, T_y f⟩, so

    |θ_f(log 2)| ≤ 1    (hat-unit f).

Hence ‖Θ(log 2)‖ ≤ 1 on W_L and on the
tail n≥2. Sharp: finite sections N=40
give 1 to 2×10⁻¹⁵.

## Execution

`python code/ql_theta_tail.py`.
`report/ql-theta-tail.json`.

Schur β with t2_op = |w₂|·1, Hankel+R and
C as in #58.

| χ | t2 old | t2 now | δ | β |
|---|---|---|---|---|
| χ₅ | 0.980 | **0.490** | **−0.189** | — |
| χ₈ | 0 | 0 | +0.876 | **+0.055** |
| χ₄ | 0 | 0 | +0.183 | −0.881 |
| χ₃ | 0.980 | **0.490** | **−0.699** | — |

Hankel+R leave 0.30 of χ₅’s qmin=2.23;
|w₂|=0.49 still eats δ. Even if T₂=0 at
h=2, ‖C‖_F²/δ > λ_min(H): C is a second
obstruction. χ₈ unchanged.

## Verdict: SURVIVE

‖Θ‖≤2 is dead. ‖Θ(log 2)‖≤1 is the lag
bound on this window. It does not take
χ₅. χ(2)=−1 still open. Not (∀ L). Not RH.

Judge: `tests/test_ql_theta_tail.py`.

## Status

| Claim | Status |
|---|---|
| ‖Θ(log 2)‖ ≤ 2 | **false** (≤1, sharp) |
| y=log 2 ≥ L/2 | theorem (2≥√3) |
| χ₅ taken at h=2 after the 1 | **false** (δ<0) |
| χ₈ still taken | judged (#58, unchanged) |
| c_L^* ≥ 0 for every χ | **open; not taken** |
| (∀ L) Q_L ≥ 0 | RH; not this note |
