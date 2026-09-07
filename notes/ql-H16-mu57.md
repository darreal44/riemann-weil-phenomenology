<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# χ₃ H₁₆ on (5, 7]: T₅ does not jump; 5 drifts and L eat the sliver

Preregistered (`report/prereg-ql-H16-mu57.md`):
identified Q_pk, head 16, μ from 5
to 7. T₅ at 5.1, then 5 interior.
No Neumann. A negative section is
not a disproof of RH. Not RH.

## Execution

`python code/ql_H16_mu57.py`.
`report/ql-H16-mu57.json`.
Endpoints match #72.

| μ | n | H₀₀ | λ_min(H₁₆) |
|---|---|---|---|
| 5.0 | 2,3,4 | 0.070 | +8.27×10⁻⁶ |
| 5.1 | +5 | 0.078 | +6.10×10⁻⁶ |
| 5.5 | 2,3,4,5 | 0.106 | +1.29×10⁻⁶ |
| 6.0 | 2,3,4,5 | 0.134 | +1.72×10⁻⁷ |
| 6.5 | 2,3,4,5 | 0.157 | +2.54×10⁻⁸ |
| 7.0 | 2,3,4,5 | 0.177 | +4.81×10⁻⁹ |

T₅: Δλ = −2.2×10⁻⁶, not 10⁻².
Then each +0.5 in μ cuts λ_min by
about 10. H₀₀ *rises* (χ₃(5)=−1
helps the constant); the well is
not φ₀. No sign change. Smooth
in L and the drift of 5, not a
cran.

## Verdict: SURVIVE

The collapse 8×10⁻⁶→5×10⁻⁹ is
T₅ plus 5 drifting plus L, not a
crossing. Not Weil-positive. Not
Weil-negative. Not (∀ L). Not RH.

Judge: `tests/test_ql_H16_mu57.py`.
