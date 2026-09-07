# Closed form of θ, for ∫ D₂ θ

ω_k = 2π k / L.

    n=m=0
      2(L−y)/L
    one
    index
    0
      −2 sin(ω_j y) / (√2 π j)
    n=m≥1
      2(L−y)/L cos(ω_n y)
      − sin(ω_n y)/(π n)
    n≠m
      2 (n sin(ω_n y) − m sin(ω_m y))
      / (π (m²−n²))

The
last
line
is
the
far
off-diagonal.
∫ D₂ θ
reduces
to
two
sines
against
D₂,
divided
by
m²−n²
which
already
supplies
1/(k(2n+k)).

Define
S_k
= ∫_0^L D₂(y) sin(ω_k y) dy
(improper
at
0,
integrable
because
sin(ω y)~ω y).
Then
for
n≠m

    ∫ D₂ θ
      = 2 (n S_n − m S_m) / (π (m²−n²)).

S_k
is
a
function
of
one
integer,
not
of
a
pair.
If
S_k
is
bounded
or
S_k = O(1)
(the
Fourier
table
says
the
sine
part
sits
near
1.5),
then
|∫ D₂ θ|
= O( (n+m) / |m²−n²| )
= O(1/k)
again,
same
harmonic
wall
unless
n S_n − m S_m
cancels
better
than
O(n+m).

If
S_k ∼ c / k
or
S_k ∼ c
with
a
slowly
varying
c,
the
combination
n S_n − m S_m
must
be
computed,
not
bounded
by
n|S_n|+m|S_m|.

That
combination
is
the
next
identity
to
write.
Not
a
new
θ.

Not
RH.
