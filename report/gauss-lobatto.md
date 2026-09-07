# Gauss–Lobatto

n-point Gauss–Lobatto includes both endpoints and is exact for
polynomials of degree ≤ 2n−3. The error involves f^{(2n−2)} and a
positive kernel on a positive weight — so the sign of the error tracks
that derivative, not a supporting property of g.

3-point Lobatto on [0,1] is the endpoints plus the midpoint, i.e.
Simpson up to a scale. The repo already has a 3-node Gauss table of θ_v
(#79) and panel Gauss on a and a_lo.

Lobatto is useful when one must hit y=0 and y=1 exactly (g(0)=0 is
already used). It does not build g_lo. A Lobatto rule on g_lo is again
just an integrator.

Not a campaign.
