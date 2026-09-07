# Two truncations still in Q_lo

Q_lo = CST + I_lo + I1L_LO − P.

    I_lo hand mesh on [0,1]. Remainder 0.00279 (`taylor-remainders.md`).
    I1L_LO = −0.018513 Cauchy floor of ∫_1^L a (`av-enclose`). A
    truncation of the far integral, not of g on [0,1].
    P exact for this v (finite lags).

Tightening I_{[0,1]} below 10⁻³ does not touch I1L_LO. If that floor is
loose by more than 0.003, Q_lo can stay shy of a comfortable plus even
with a perfect I_{[0,1]}. The enclose note already put the Cauchy
remainder at 1.25×10⁻⁵ on top of −0.018500 — that piece is tight. The
open truncation on [0,1] is the mesh leftover, O(h²).

Do not mix with Neumann T or H_n versus Q̂.
