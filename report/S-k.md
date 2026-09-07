# S_k = ∫ D₂ sin(ω_k y) dy

s₀=3/4,
L=log 3,
trapezoid:

    k     S_k      k S_k
    1     1.413    1.41
    8     1.547    12.4
    16    1.554    24.9
    32    1.553    49.7
    33    1.553    51.2
    40    1.551    62.0

S_k
tends
to
a
limit
≈1.55,
not
to
0.
k S_k
grows
linearly.
The
combination
for
adjacent
indices:

    32 S_32 − 33 S_33
      ≈ −1.545
      ≈ −S_∞

not
O(n).
Generally

    n S_n − m S_m
      = n(S_n−S_m) + (n−m) S_m
      = O(n |ΔS|) + k S.

S
flat
⇒
n|ΔS|
tiny
(0.008
at
n=32)
and
the
size
is
k S_∞.
Hence

    |∫ D₂ θ|
      ≈ 2 S_∞ / (π k (2n+k))
      = O(1/(k n)).

Row
sum
∑_k O(1/(k n))
= O((log n)/n).
The
harmonic
wall
falls
once
one
uses
n S_n−m S_m
instead
of
n|S_n|+m|S_m|.

A
proof
needs
S_k → S_∞
with
an
explicit
rate
(so
n|S_n−S_m|
stays
≤ k S
uniformly
for
m≥N).
The
table
is
not
that
rate.
It
is
the
reason
the
identity
is
the
right
one.

Not
RH.
