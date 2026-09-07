# ‖Θ(y)‖ ≤ √2 for L/4 ≤ y < L/2

Preregistered (`report/prereg-ql-theta-sqrt2.md`):
geometric cap when #59 (y ≥ L/2) fails.
Then Neumann Q_pk, χ₃, μ=5. Finite
sections of Θ do not prove the cap.
Not RH.

## Lemma

Even L² on [−L/2, L/2], hat-unit f,
θ(y)=2⟨f, T_y f⟩. Restrict to the
half-window: h = √2 f|_{[0,L/2]},
‖h‖=1. For L/4 ≤ y < L/2 the shift
pair on [0, L/2] is disjoint:

    A = [0, L/2 − y],   C = [y, L/2],
    M = [L/2 − y, y] = M₁ ∪ M₂,
    M₂ = reverse(A) on [0, y].

Masses α, β, μ₁, μ₂. Then

    |θ| ≤ 2√(αβ) + 2√(α μ₂) + μ₁ ≤ √2

by Cauchy–Schwarz on the simplex
(the u-term only helps). At y ≥ L/2
the stronger cap 1 of #59 stays.

μ=5: log 4 < 5 < 16, so log 2 is in
the band. log 3 and log 4 stay ≥ L/2.

## Execution

`python code/ql_theta_sqrt2.py`.
`report/ql-theta-sqrt2.json`.
The CS majorant holds on a grid of
the simplex. Finite sections of Θ
at y=log 2, L=log 5:

| N | ‖Θ_N‖ |
|---|---|
| 8 | 1.407404 |
| 16 | 1.414206 |
| 32 | **1.414214** |
| 64 | **1.414214** |

√2 = 1.414214. Sharp. Not a proof
(Courant the wrong way); a check
that the cap is not exceeded.

t_atoms 1.327 → **1.040**.

| h | λ_H | S_lo (√2) | S_lo (cap 2) |
|---|---|---|---|
| 8 | +1.04×10⁻⁵ | −1.69×10⁻⁵ | −8.5×10⁻⁵ |
| 16 | +8.27×10⁻⁶ | **+5.04×10⁻⁶** | +2.53×10⁻⁶ |
| 24 | +7.91×10⁻⁶ | **+7.00×10⁻⁶** | +6.59×10⁻⁶ |

h=2,4,8 stay negative. The heads
that took log 3 still do not take.
S_lo(16) grows vs cap 2 and stays >0.

## Verdict: SURVIVE

The cap √2 is the lemma on the band.
It does not take χ₃ at h=8. Not
Weil-positive. Not (∀ L). Not RH.

Judge: `tests/test_ql_theta_sqrt2.py`.
