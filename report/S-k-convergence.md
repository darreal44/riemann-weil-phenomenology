# Convergence of S_k

Same integral, finer trapezoid (N=12000). Quadrature moves the fourth
digit (S_32 was 1.553 at N=8000, 1.557 here). Shape is stable:

    k     S_k
    8     1.548
    16    1.556
    24    1.558
    32    1.557
    48    1.555
    64    1.551

A hump near k=24, then a slow decrease. Not a clean S_∞+c/k yet. On this
range S_k stays in [1.41, 1.56]. That is enough to treat S as bounded in
a proof sketch (|S|≤2 say) and to keep n S_n−m S_m = k S + nΔS with
|nΔS| small when k≪n.

A theorem needs either an explicit primitive (Ei against the geometric
series of D₂) or a monotonicity statement for large k. The table is not
that theorem. It does not threaten O(1/(k n)) at N_NEAR=32.

Not RH.
