# 3-point Gauss of a_odd on [0,1]

Same nodes as the even
side: ½ ± √(3/5)/2, ½.

    G₃           = −0.010913
    trap[10^{-4},1] = −0.010878
    difference     3.5×10^{-5}

Sixth-difference estimate
of max|a^{(6)}| on [0.05, 1]
is ~381, remainder coeff
4.96×10^{-7} ⇒

    |G₃ − ∫₀¹ a_odd| ≲ 1.9×10^{-4}

inside the χ₃ room
(~0.005). First node at
0.113, away from y=0
(a_odd → −0.481).

This is the same class of
check as `notes/av-gauss.md`:
an arithmetic G₃ plus a
sampled-d6 remainder, not
a majorant of a^{(6)}.
Folding ±1.9×10^{-4} into
the termwise χ₃ ball gives

    Q₃ ∈ [0.00471, 0.00743]

still positive.
