# Gaussian quadrature in this repo

gauss_on in av_I01_compare is a fixed panel Gauss rule applied to a and
to a_lo. n=48 per piece is far past WINDOW. That is how I_true and I_lo
are scored, not how g_lo is built.

Classical Gauss–Legendre n nodes on [−1,1] is exact for degree ≤ 2n−1.
The error involves f^{(2n)} and a positive kernel. Same story as Lobatto
and Simpson: a machine value, not a supporting function.

#79 used a 3-node table as an arithmetic check of θ_v, not as Q_lo.
Positive Gauss weights on g_lo are legitimate because g_lo is already
below g; the weights do not create the comparison.

No new rule is needed. N=8 on the mesh is still the only open cut on
I_{[0,1]}.
