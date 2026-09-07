# Residues of w, why r=2

The even/odd
integrand is
regularized

    a(z) = ½ w(z) (2 e^{-3z/2} − θ_v(z))
    w(z) = e^{-z/2} / sinh z

sinh z = 0 at
z = kπi, k∈ℤ.
k=0 is removable
in a (g(0)=0
cancels the pole
of w). The first
poles are ±πi.

Res_{kπi} csch
= 1/cosh(kπi)
= 1/cos(kπ)
= (−1)^k.

Res_{kπi} w
= e^{-kπi/2} (−1)^k
which is ±1 or ±i:

    k     Res w
   ±1     ±i
   ±2     −1
   ±3     ∓i

θ_v is entire
(sines, cosines).
So a has the same
poles as w, except
k=0. Distance from
[0,1] or [1,L] to
the nearest pole
is π. Cauchy at
r=2 < π stays in
the holomorphic
neighbourhood.
The residue itself
is not used in
the majorant:
only the existence
of the gap π−r.
A residue calculus
of ∫ a would be
another proof
(sum over kπi),
not #52/#53.
