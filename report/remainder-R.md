# The remainder R

Gauss–Legendre n=3
on the unit interval:

    R = c₆ a^{(6)}(ξ)
    c₆ = (3!)⁴ / (7 (6!)³)
       = 4.960317×10⁻⁷
    ξ ∈ (0,1) unknown

On a panel of
length h the affine
map multiplies by
h⁷:

    R(h) = c₆ h⁷ a^{(6)}(ξ_h)

Two panels of
length 1/2:

    |R_tot| ≤ 2 · c₆ · (1/2)⁷ M₆
            = c₆ M₆ / 64

ξ is not computed.
The proof replaces
|a^{(6)}(ξ)| by M₆
= 6! M / r⁶, r=2.
That is the only
loss besides M
itself.

Sample M=221 vs
elementary M=3889:
R₂ shrinks from
3.39×10⁻⁴ to
1.93×10⁻⁵. The
certificate uses
the larger M
(rectangle, not
the stadium
sample).

R is O(h⁷). That
is why two panels
beat one by 64,
and why [1,L]
with h=1.77 needs
n≥4 elementary
panels before R
drops under 10⁻³
(h⁷ / n⁶).
