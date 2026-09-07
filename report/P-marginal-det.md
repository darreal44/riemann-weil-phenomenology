# Marginal Δdet of each prime power

Start from Arch alone (P=0), add
the n-terms of P in order. µ=16.

## χ₅

| n | χ(n) | w | Δdet | det after |
|---|---|---|---|---|
| — | | | | **−1.15** |
| 2 | − | −0.490 | +0.951 | −0.204 |
| 3 | − | −0.634 | +0.180 | −0.024 |
| 4 | + | +0.347 | +0.023 | −4.0×10⁻⁴ |
| 7 | − | −0.736 | +4.0×10⁻⁴ | −2.8×10⁻⁶ |
| 8 | − | −0.245 | +3.8×10⁻⁶ | +1.0×10⁻⁶ |
| 9 | + | +0.366 | −7.3×10⁻⁷ | +2.9×10⁻⁷ |
| 11 | + | +0.723 | −2.9×10⁻⁷ | **−1.2×10⁻⁹** |
| 13 | − | −0.711 | +1.4×10⁻⁸ | **+1.3×10⁻⁸** |
| 16 | + | +0.173 | 0 | +1.3×10⁻⁸ |

Arch alone is indefinite by O(1).
p=2 then p=3 cancel 98 % of that
deficit. The remaining 2 % is a
ladder of smaller updates. n=11
overshoots below zero; n=13
corrects it. n=16 is dead
(θ_{f₁}(log 16)=0).

## χ₃

Same pattern, different signs
(χ₃(3)=0, so no p=3 term).
p=2 cancels Arch almost alone
(−0.333 → −0.003). Then 4,5,7,8
juggle 10⁻² → 10⁻⁷. n=11 makes
it positive; n=13 shrinks det
by 40× but keeps the sign.

## Reading

The quadratic form on the 2-plane
is Arch (indefinite, det∼−1)
plus a signed atomic measure at
log n. The first two live atoms
do the O(1) work. SPD is a
property of the *whole* chain,
including the last atom whose
θ is 10⁻². There is no leading-
term criterion for the sign.
