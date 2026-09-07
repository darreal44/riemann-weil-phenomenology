# 1D finite elements, as a name

The supporting mesh is already a P2 element per slab with a one-sided
jet and a safe second derivative, not a Galerkin projection of −u''=g or
of a weak form of Q̂.

A standard P1 FEM on [0,1] would be the broken line through g(y_i):
chords, legal only on the tail. P2 Lagrange (three values) is Simpson’s
parabola, not below g. Hermite P3 is the interpolant already rejected as
a lower bound.

Céa and interpolation estimates ‖g−g_h‖_{H^k} = O(h^{p+1−k}) are
unsigned norms. Q_lo needs g_h ≤ g pointwise. FEM theory does not give
that for free.

No stiffness matrix on [0,1] is useful. H_n is the FEM of Q̂ in the
cosine ONB, a different interval and a different form
(`spectral-convergence-Hn.md`).

Not a campaign.
