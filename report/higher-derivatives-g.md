# Higher derivatives of g

g = 2 e^{−3y/2} − θ_v.
The
Bose
piece
is
closed:

    ∂_y^k (2 e^{−3y/2})
      = 2 (−3/2)^k e^{−3y/2}.

At
y=0
that
is
2(−1.5)^k:
2,
−3,
4.5,
−6.75,
10.125, …
already
the
numbers
in
g_pp(0)
and
g_ppp
before
θ.

θ_v
is
a
3×3
combination
of
sines
and
cosines
at
ω_n=2π n/L
(L=log 16≈2.773,
ω₁≈2.27,
ω₂≈4.53).
Each
extra
derivative
brings
a
factor
ω
and
rotates
sin↔cos.
Hence

    |θ_v^{(k)}|
      ≤
    C ρ^k,
    ρ ≈ ω₂ ≈ 4.5.

|g^{(k)}|
grows
like
max(1.5, 4.5)^k = 4.5^k.
A
Hermite
remainder
g^{(4)} h^4/384
on
h=0.1
is
order
4.5^4 × 10^{-4}/384
∼
410×10^{-4}/384
∼
10^{-4}
if
C∼1,
larger
if
the
3×3
sum
amplifies.
That
is
why
Hermite
would
look
tight
*unsigned*
and
still
need
a
safe
bound
on
g^{(4)}
to
stay
below
g.

For
the
legal
mesh
one
needs
g''
and
at
most
g'''
(`gpp-profile.md`).
g^{(4)}
is
only
for
a
different
interpolant.
No
code
path
computes
it.
