# Trapezoid error

One panel [a,b], h=b−a:

    ∫_a^b f − (h/2)(f(a)+f(b)) = − h³ f''(ξ) / 12.

If f''≥m>0 (convex), the trapezoid (the chord) is above f and the error
is negative. A lower bound for the integral of a convex f is not the
trapezoid; it is a tangent or a supporting parabola. If f''≤M<0
(concave), the chord is below f and is the legal g_lo on that panel
(#chord).

Composite: sum of those remainders. The unsigned bound h²(b−a)/12
‖f''‖_∞ is the m=0 EM bound already written.

On the well, using the trapezoid as g_lo would be illegal (chord above
convex g). That is why #79’s 3-piece that kept a tangent then a floor
beat a naive composite trapezoid, and why the mesh never switched to
chords before y_inf.

No new constant.
