# S_lo of identified Q_pk takes W_log5 at h=16, cap 2

Preregistered (`report/prereg-ql-slo-identified.md`):
re-judge #70 Neumann after #71. The
archimedean gap 0.6 is dead. Same
cap ‖Θ‖=2 for y<L/2. T infinite.
Not a new lemma. Not RH.

## Execution

`python code/ql_slo_identified.py`.
`report/ql-slo-identified.json`.
Same numbers as #70:

| h | λ_H | S_lo |
|---|---|---|
| 2 | +1.85×10⁻⁴ | −1.31 |
| 4 | +1.43×10⁻⁵ | −1.19 |
| 8 | +1.04×10⁻⁵ | −8.5×10⁻⁵ |
| **16** | +8.3×10⁻⁶ | **+2.5×10⁻⁶** |
| 24 | +7.9×10⁻⁶ | **+6.6×10⁻⁶** |

S_lo(2) and S_lo(4) stay negative.
S_lo(h≥16)>0, ρ<1, T infinite: this
is a take of W_{log 5} for χ₃ in the
sense of `certificates-Wlog3.md`.
Gauss of D₂ is 10⁻¹⁰, below the
sliver. It is not Weil-positive
(one L, not Weil 1952). The thinness
is the cap 2 on Θ(log 2), not an
unidentified Γ.

## Verdict: SURVIVE

The dead gap was the wrong reason to
refuse S_lo(16). The take is of one
window, one χ. Not (∀ L). Not RH.

Judge: `tests/test_ql_slo_identified.py`.
