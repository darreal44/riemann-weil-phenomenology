# Convexity of g on [0,1]

#79–#82: g = 2 e^{−3y/2} − θ_v on the witness v=(4,−3,1)/√26, χ₅, μ=16.
Six lags, elementary.

Reported shape:

    g(0)=0 unique min at y=0.410 (g=−0.529) inflection at y=0.772 convex
    on [0, y_inf] concave after

That is why every tangent on [0, y_inf] is a lower bound (#82) and why a
floor at g_min is legal on that interval. The concave tail only admits a
chord as a lower bound (a tangent there would cut above g).

g''(0)≈9.6 (#79) makes the tangent at 0 peel off fast: that was the
loose piece of the parent 3-piece (miss 0.224) and still the first
segment of the envelope (miss 0.068). A tighter hand bound has to spend
nodes near 0 or use g'' (a quadratic under-estimator on a short initial
interval), not another global tangent.

This shape is for one v and one μ. It is not convexity of G_reg or of
D₂−1/y (`archimedean-kernel.md`).
