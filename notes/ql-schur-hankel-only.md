<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# w₂=0: B₁^Θ off, Hankel only

Not the Weil form of χ₃. Diagnostic: Q = A − w₂ θ(log 2) with w₂ forced
to 0, Off_far without |w₂|‖Θ‖. Named in `report/w2-impact.md`.

    χ     S_lo full   S_lo Hank   λ_H Hank   ρ Hank
    χ₅    +0.0291     −0.2405     −0.2125    0.369
    χ₈    +0.2350     +0.2350     +0.2575    0.335
    χ₄    +0.0573     +0.0573     +0.0839    0.388
    χ₃    −0.0086     −0.2357     −0.2037    0.415

χ₈ and χ₄ already have w₂=0; unchanged. χ₅ and χ₃ share w₂=−log 2/√2.
Stripping B₁^Θ makes λ_H of the *head* negative (−0.21). The 2-tower is
what carries λ_H through zero, not what kills χ₃ in the far envelope.

Hankel alone is already indefinite on the 2×2 for those two q. S_lo of
that proxy is not a take and is not the form of χ₃.

Not taken. Not RH. One L. `python code/ql_schur_hankel_only.py`
`report/ql-schur-hankel-only.json`.
