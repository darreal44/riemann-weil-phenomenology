# Pólya tail

Pólya: even,
continuous on ℝ,
convex and
decreasing to 0
on [0,∞) ⇒ PD.

The continuous
piece of G on
(0,L] is D₂
(plus a constant
from CST). On
(0,L]:

    D₂(y)=2 e^{-2 s₀ y}/(1−e^{-2y})
    ∼ 1/y   as y→0
    decreasing, convex
    (second
    differences >0)

At L=log 3,
D₂(L)≈1.30,
D₂′(L)<0. A
C¹ tail that
stays convex and
hits 0 is easy
(linear to some
Y>L, or
exponential).
That tail would
be a Pólya
extension of D₂
**if D₂ were
continuous at 0**.

It is not.
φ(0)=+∞. Pólya’s
criterion as
stated does not
apply to the raw
archimedean
kernel. The
Weil form never
feeds G to a
test with g(0)≠0
in the singular
term: g(0)=0
cancels 1/y.
Bochner/Pólya
on the line
ignore that
cancellation
unless one
builds φ from
the *regularised*
kernel
(G(y)−G_sing(y)
with the 1/y
removed, plus
the rule at 0
fixed by CST).

The atom ±log 2
is a second
obstruction
(`kernel-extension-WL.md`):
a Pólya tail
does not touch
it.

What a Pólya
attempt can
still do:
regularise at 0
(replace 1/y by
a bounded even
convex bump
that agrees
with D₂ on
[δ,L] and has
the right
∫ against
functions with
g(0)=0), then
attach a
decreasing
convex tail
past L, then
read ˆφ.
If that ˆφ
dominates
|w₂|, the
symbol of
φ − w₂(δ_{log 2}
+δ_{−log 2})
might stay
non-negative.
That is a
construction,
not the
textbook
criterion.

Not done.
Not RH.
