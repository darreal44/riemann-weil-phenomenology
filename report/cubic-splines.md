# Cubic splines

A C² cubic spline through g(y_i) is a better unsigned approximation than
broken parabolas (error O(h^4) with g^{(4)} bounded). Natural or clamped
ends change only the boundary constants.

It has the same defect as Hermite: the spline is not below g. Overshoot
on a convex well is typical (the spline cuts the chord and can rise
above a convex function between nodes depending on the end conditions).
Subtracting a uniform M₄ h^4 restores a lower bound and wipes the order
gain for Q_lo (`hermite-convergence.md`).

A *convex* spline (shape-preserving, e.g. a C¹ quadratic spline or a
PCHIP-type limiter) can be forced below g if g''>0, which is exactly the
supporting-parabola mesh already named. C² cubics are the wrong
regularity for a legal under-estimator.

Not a campaign. I_true does not need them.
