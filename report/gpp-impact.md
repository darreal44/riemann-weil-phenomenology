# Impact of g'' on I_{[0,1]}

Same witness. The gap fell when g'' entered the bound:

    bound              uses g''     gap
    chord of θ         no           0.215
    3-piece + t₀       no           0.224
    tangent/floor      no           0.088
    3-tangent env.     no           0.068
    quadratic #83      yes (m=4.22) 0.047

g''(0)≈9.6 is the true curvature at the origin. The legal
under-estimator cannot use 9.6 on the whole [0,y_min] because g'''<0:
g'' decreases to 4.22 at the min. Using m=inf g'' is what #83 did. Using
9.6 would not be a lower bound.

Each step that respected convexity without g'' left ~0.07. Putting the
worst-case g'' on a short initial interval ate 0.021 more. The ±0.003
A-window is still 15× away.

Next legal tightening is a piecewise quadratic (several m_i on
subintervals where g'' is monitored) or a cubic with a bound on g'''.
Not another global tangent.
