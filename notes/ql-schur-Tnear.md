<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# S_T = H − C T_near^{-1} C*

Named in `report/S-diag-derivation.md`: S_diag is the Schur of diag(T),
not of T. This sitting inverts the Gauss T on hats 2…31 (30×30). Still
not S of the infinite tail. Not a take.

    χ     λ_H     S_diag    S_T      S_lo     tmin   ρ
    χ₅   +0.0530  +0.0417   +0.0437  +0.0291  2.06   0.52
    χ₈   +0.2575  +0.2427   +0.2443  +0.2350  2.76   0.33
    χ₄   +0.0839  +0.0680   +0.0700  +0.0573  2.07   0.39
    χ₃   +0.0185  +0.0076   +0.0097  −0.0086  1.55   0.59

T_near is SPD (tmin>1.5). S_T sits *above* S_diag on all four cells
(near Off gives back ~0.002, not a loss). χ₃ S_T=+0.0097>0. The drop to
S_lo=−0.0086 is the far envelope alone (0.018). χ₃ does not die on the
computed block.

Haynsworth on this finite truncation (hats 0…31) says Q>0 there: T>0 and
S_T>0. That is Courant on V_{32}, the wrong direction for W_{log 3}
(`notes/pw-log3.md`). The class step still needs the infinite tail. S_lo
is the proxy that sees it, and it is red for χ₃.

Not taken. Not RH. One L. `python code/ql_schur_Tnear.py`
`report/ql-schur-Tnear.json`.
