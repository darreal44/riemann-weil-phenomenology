# Adaptive methods, two kinds

**Adaptive quadrature** (QUADPACK, Gauss–Kronrod pairs): split a panel
when the error estimator on the *true* integrand is large. Gives I_true.
Already closed.

**Adaptive mesh for g_lo**: split a panel when leftover = g''(left)−m_i
is large. That is where g''' is large (near 0 and through the well).
Uniform N=4 already left leftover 1.3–1.6 on the last well slabs
(`local-curvature.md`). An adaptive split would put N=8 budget on those
slabs first, not on the tail.

The second kind is the only adaptivity that can still move Q_lo. It is
the same construction as N=8 with a non-uniform h. Not RK, not CC, not
Laguerre.

Executed (`notes/av-I01-adapt.md`): eight leftover bisections, gap
0.000433, inside ±0.003. Still one v.

Not Weil. One v.
