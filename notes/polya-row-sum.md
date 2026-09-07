<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Row-sum bound for T_far (the Pólya-style majorant)

Not
a
PD
extension.
For
n≠m,
both
≥1,
F0=0
and

    Q_nm
      = −½ ∫_0^L D₂(y) θ_nm(y) dy
        − w₂ θ_nm(log 2).

|θ_nm(y)|
≤
2/(π|n−m|)
for
every
y
(closed
form).
One
must
*not*
write
|∫ D₂ θ| ≤ 2/(π|n−m|) ∫ D₂:
D₂ ∼ 1/y
and
∫_0 D₂ diverges.
θ_nm(0)=0
saves
it.
Near
zero,

    |θ_nm(y)|
      ≤ (4y/L) (n+m)/|n−m|.

Split
[0,δ]∪[δ,L]:
the
first
piece
is
O(δ) (n+m)/|n−m|,
the
second
is
O(1/|n−m|) ∫_δ^L D₂
with
∫_δ^L D₂ < ∞.
Pick
δ=L/n
or
a
fixed
δ
and
absorb
n
into
the
constant
only
on
the
near
off-diagonals
(already
computed).

Far
row
sum,
k=|n−m|≥1,
m≥N:

    ∑_{k≥1} 1/(k (2n+k))
      = O((log n)/n).

Times
a
constant
depending
on
δ,s₀,w₂
gives

    ∑_{m≠n, m≥N} |Q_nm|
      = O((log n)/n)
        + |w₂| O((log n)/n).

Q_nn
stays
Θ(1)
(measured
~4
on
χ₃).
Gershgorin
then
says
λ_min(T_far)>0
for
large
n,
with
room
~4 − C(log n)/n.

What
this
is
not
yet:
a
numerical
C
small
enough
to
replace
½π
in
ρ_far
and
flip
χ₃’s
S_lo.
The
split
at
0
must
be
closed
with
an
explicit
δ
and
an
explicit
∫_δ^L D₂
(s₀=3/4).
That
page
is
the
proof.
This
note
is
the
skeleton.

Not
RH.
LICENSE.md
