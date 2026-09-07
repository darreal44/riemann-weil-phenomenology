<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# χ₃ H₁₆ stays positive through 7 and 8=2³; the sliver collapses

Preregistered (`report/prereg-ql-H16-mu.md`):
identified Q_pk, head 16, μ through
T₇ and 2³. No Neumann. A negative
section is not a disproof of RH.
Not RH.

## Execution

`python code/ql_H16_mu.py`.
`report/ql-H16-mu.json`.
λ_min(H₁₆) at μ=5 matches #70
(+8.27×10⁻⁶).

| μ | n | λ_min(H₁₆) |
|---|---|---|
| 5.0 | 2,3,4 | +8.27×10⁻⁶ |
| 7.0 | 2,3,4,5 | +4.81×10⁻⁹ |
| 7.1 | +7 | +3.14×10⁻⁹ |
| 8.0 | 2,3,4,5,7 | +8.09×10⁻¹¹ |
| 8.1 | +8=2³ | **+5.33×10⁻¹¹** |

T₇: Δλ = −1.7×10⁻⁹. 2³: Δλ = −2.8×10⁻¹¹.
No jump of size 10⁻², same as T₅.
No sign change. The 16-plane sliver
shrinks by 10⁵ from μ=5 to 8.1.
That is Courant from above: not a
take of the class, and not a
negative direction.

## Verdict: SURVIVE

T₇ and 2³ are not a crossing of
H₁₆. The well of the 16-plane is
collapsing toward 0, still +.
Not Weil-positive. Not Weil-negative.
Not (∀ L). Not RH.

Judge: `tests/test_ql_H16_mu.py`.
