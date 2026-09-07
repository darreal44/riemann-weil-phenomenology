# Adaptive quadrature versus a hand bound

Adaptive Gauss– Kronrod (or a panel split driven by an error estimator)
computes I_true to any tolerance. The repo already has that number
(−0.7008) and panel agreement to 10⁻⁸ on H. Adaptive quadrature does not
produce Q_lo.

A hand bound needs a comparison function g_lo ≤ g whose integral is
elementary or has a finite Gauss table with positive weights on g_lo
itself. Adaptivity in that world is the quadratic mesh: split where g''
moves, not where the quadrature error of the true g is large.

Using an adaptive integrator on g_lo is fine (and already the judge
pattern: shipped a_lo integrated by the same nodes as a). It does not
replace the construction of g_lo.

Not a new take. Not RH.
