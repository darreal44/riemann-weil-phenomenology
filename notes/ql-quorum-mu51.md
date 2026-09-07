<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# T₅ arrival at μ=5.1 kills only χ₃ of the six

Preregistered (`report/prereg-ql-quorum-mu51.md`):
six χ, h=16 and 24. Identified Q_pk.
Not RH.

## Execution

`python code/ql_quorum_mu51.py`.
`report/ql-quorum-mu51.json`.
ns=[2,3,4,5].

| χ | taken h |
|---|---|
| χ₃ | — |
| χ₅ | 16, 24 |
| χ₄ | 16, 24 |
| χ₈ | 16, 24 |
| χ₇ | 24 |
| χ₁₇ | 16, 24 |

Five of six still take. T₅ arrival
is χ₃-specific (χ₃(5)=−1 and the
deep well). χ₇ is already reduced
to a sliver. Not Weil-positive.

## Verdict: SURVIVE

T₅ is not a quorum-wide kill.
Not (∀ χ). Not (∀ L). Not RH.

Judge: `tests/test_ql_quorum_mu51.py`.
