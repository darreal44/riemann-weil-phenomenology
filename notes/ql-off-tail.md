<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Off tail, χ₃: S_k is Hankel, sections saturate

Not
Nehari.
Not
a
take.

## S_k identifies Hankel

θ_nm
=
2(n sin ω_n y − m sin ω_m y)
/
(π(m²−n²)),
m=n+k,
m²−n²=k(2n+k).
Then

    ∫ D₂ θ
      = 2(n S_n − m S_m)
        / (π k (2n+k)).

S
flat
⇒
n S_n − m S_m
= k S_∞
(not
(n+m)S).
The
k
cancels:

    ∫ D₂ θ
      ≈ 2 S_∞ / (π(n+m)).

S_∞=π/2
⇒
A_arch
= −½∫
= ½/(n+m).
The
extra
1/k
in
the
Pólya
skeleton
and
in
`report/S-k.md`
“hence
O(1/(k n))”
is
that
cancelled
factor.
Measured
ratio
A_arch
/
(½/(n+m))
= 1.000
on
(32,33),
(32,47),
(2,39).

Hilbert
π
on
[1/(n+m)]
is
therefore
the
right
essential-norm
majorant
for
*A_arch*.
S_k
does
not
make
it
HS.
Nehari
still
needs
a
Hankel
symbol;
Off_Q
has
none
(`report/hankel-symbol.md`).

## Growing sections n≥32

    dim  ‖Off‖  ‖A_arch‖=‖Hank‖  ‖Θ‖   ‖B₁‖  ½π
    16   0.445  0.096            0.916  0.396  1.571
    32   0.467  0.168            0.943  0.397  1.571
    48   0.468  0.222            0.945  0.397  1.571
    64   0.474  0.266            0.945  0.397  1.571

Off
sits
at
0.47.
Hankel
climbs.
B₁
is
already
saturated
(0.397,
`report/B1-analyse.md`).
‖Θ‖
stays
under
the
cap
1.
This
is
a
section,
not
s₁(Q_tail)
on
ℓ²(n≥32).
Hartman
still
says
the
Hankel
piece
alone
keeps
s₁=π
on
every
tail.

## Sign

w₂(χ₃)<0,
so
Off
= H + |w₂|Θ
on
the
off-diagonal
(same
sign,
not
a
minus).
Triangle
‖Off‖≤‖H‖+|w₂|‖Θ‖
is
the
old
Off_far
once
‖H‖_ess=π/2.

## Lag split

Each
Hankel
lag
has
weights
1/(2(2n+k))∈ℓ²,
hence
HS.
On
ℓ²(n≥N),
lags
1..K:

    ‖H^{(K)}‖₂
      ≤ √(K / (8(N−1))).

At
N=32,
K=7:
cap
0.168;
measured
H_near
on
the
windows
is
0.075.
Θ
lags
do
not
die
in
n
(B₁=0.397
on
every
dyadic).
On
[32,96)
k-split
8:

    ‖Off_near‖=0.513
    ‖Off_far‖=0.303
    (far
    grows
    with
    the
    window;
    near
    is
    Θ).

A
window
[N,N+L)
has
no
lags
≥L,
so
it
never
sees
Hartman’s
π/2.
That
is
why
0.47
is
not
s₁(P_{n≥32} Off P_{n≥32}).

## Dyadic blocks vs union

    [32,64)    Off=0.467  H=0.168  Θ=0.943  B₁=0.397
    [64,128)   Off=0.465  H=0.170  Θ=0.946  B₁=0.397
    [96,160)   Off=0.466  H=0.125  Θ=0.946  B₁=0.397
    [128,256)  Off=0.465  H=0.171  Θ=0.946  B₁=0.397
    [256,512)  Off=0.465  H=0.171  Θ=0.947  B₁=0.397

Off
is
uniform
on
dyadics
(Θ-local)
out
to
512.

## Long truncated tail [32,M)

Closed
form
Off=½/(n+m)−w₂Θ
(Gauss
cross-check
on
[32,48):
d=4×10⁻¹⁰).

    M    dim  Off    H      Θ      tri    rev
    128   96  0.502  0.332  0.946  0.796  0.131
    192  160  0.561  0.421  0.946  0.885  0.043
    256  224  0.608  0.480  0.947  0.944  0.016
    384  352  0.673  0.558  0.947  1.022  0.094
    512  480  0.719  0.609  0.947  1.073  0.145

Off
climbs
0.50→0.72
and
already
exceeds
0.6
at
M=256.
H
climbs
toward
π/2;
Θ
is
flat.
The
0.47
window
is
an
artefact
of
not
joining
scales.
s₁≤0.6
on
the
truncated
tail
is
dead.
This
is
still
not
‖P_{n≥32} Off P_{n≥32}‖
on
ℓ²
(Hartman
on
H
alone
is
π/2).

## Trial substitute (not a take)

Putting
the
dim-64
‖Off‖=0.474
in
place
of
Off_far
=½π+|w₂|‖Θ‖
drops
ρ
0.590→0.382
and
gives
S_lo=+0.0007.
At
M=512,
Off=0.719
still
gives
S_lo=+0.0001
because
ρ
is
mostly
ρ_N.
Neither
number
is
s₁
of
the
infinite
tail.
The
cran
of
`report/true-tail-s1.md`
(s₁≤0.6)
fails
already
on
[32,256).
Not
taken.

## B₁ cap

Theorem
remains
‖B₁^Θ‖≤4|w₂|/π≈0.624.
The
quasi-periodic
cap

    |θ̂_{n,n+1}(log 2)|
      → 2|sin(π log 2 / log 3)|/π
      ≈ 0.584

gives
2|w₂|·0.584≈0.572
as
a
limsup
bound,
not
0.45.
Equidistribution
still
does
not
close
the
section
0.397.

Not
RH.
One
L.
`python code/ql_off_tail.py`
`report/ql-off-tail.json`.
