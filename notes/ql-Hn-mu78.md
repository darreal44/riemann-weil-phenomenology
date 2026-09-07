<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# χ₃ H_n stays positive at μ=7 and μ=8; the well is L, not n

Preregistered (`report/prereg-ql-Hn-mu78.md`):
identified Q_pk, heads 16, 24, 32, 48.
No Neumann. A negative section is not
a disproof of RH. Not RH.

## Execution

`python code/ql_Hn_mu78.py`.
`report/ql-Hn-mu78.json`.
H₁₆ matches #72. Courant holds.

| μ | H₁₆ | H₂₄ | H₃₂ | H₄₈ |
|---|---|---|---|---|
| 7 | +4.81×10⁻⁹ | +3.98×10⁻⁹ | +3.58×10⁻⁹ | **+3.26×10⁻⁹** |
| 8 | +8.09×10⁻¹¹ | +7.16×10⁻¹¹ | +6.65×10⁻¹¹ | **+6.00×10⁻¹¹** |

No sign change. H₄₈/H₁₆ ≈ 0.68 (μ=7)
and 0.74 (μ=8): the 16-plane already
sees the same well. The collapse
8×10⁻⁶ → 10⁻¹¹ from μ=5 to 8 is L
(and arriving primes), not missing
modes. Courant from above: still
not a take of the class.

## Verdict: SURVIVE

No negative section of the identified
form through n=48. Not Weil-positive.
Not Weil-negative. Not (∀ L). Not RH.

Judge: `tests/test_ql_Hn_mu78.py`.
