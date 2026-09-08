# Joint norm ||H − w2 Θ|| vs triangle

Target: s1_up(Off_Q) < 1.72 on the true kernel.
Proved triangle (ql_off_s1): 2.110 = π/2 + crumbs + |w2|.
Gap 0.39.

Off_Q on far hats = H + R − w2 Θ, H_nm = 1/(2(n+m)) (n≠m).

Finite sections, χ3, w2=−0.490:

    block     ||Off||2  ||H||2  ||Θ||2  triangle_sec  row-sum
    [32,48)    0.445     0.096   0.916    0.545         1.02
    [32,64)    0.467     0.168   0.943    0.630         1.26
    [32,96)    0.474     0.266   0.946    0.729         1.59
    row n=48, m=32..219 |Q| = 1.87 > 1.72

KILL as a proof:
- ||Θ||2 already ~0.95 on 32 modes; bound ||Θ||≤1 is sharp.
- corr(H,Θ) → 0 as the block grows.
- row-sum of |Off| exceeds 1.72 on a FINITE piece.
- section ||Off||~0.47 is not an operator-norm certificate.

Not a take. Not RH.
