# Simpson error

One
panel
of
width
2h
(three
nodes
a, a+h, a+2h):

    ∫_a^{a+2h} f
    − (h/3)(f(a)+4f(a+h)+f(a+2h))
      = − h⁵ f^{(4)}(ξ) / 90.

Composite
on
[A,B]
with
n
even
subintervals
of
width
h:

    − (B−A) h⁴ f^{(4)}(ξ) / 180.

Sign
tracks
−f^{(4)}.
g^{(4)}
is
not
of
constant
sign
on
[0,1]
(Bose
piece
+10.1 e^{−3y/2}
versus
θ^{(4)}
at
ω₂⁴).
A
signed
Simpson
bound
needs
inf
or
sup
g^{(4)}
on
each
double
panel,
i.e.
the
Hermite
problem
again
(`hermite-error.md`).

The
parabola
through
three
nodes
is
not
q_i
(q_i
uses
g,g',m
at
one
end,
not
three
values).
No
reason
to
swap.

Not
a
campaign.
