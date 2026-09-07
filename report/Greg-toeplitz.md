# Toeplitz test of G_reg on [0,L]

Delays kΔ ≤ L.
T_ij = G_reg(|i−j|Δ)
minus w₂ on the
lag ≈ log 2.
Not the full Q
(CST and ∫g/y
were peeled off).

    s₀    atom     n    λ_min
   1/4    no      32   +7.4×10⁻⁴
   1/4    χ₅      16…64  −0.489  (stable)
   1/4    χ₈=0    64   +3.6×10⁻⁴
   3/4    no      32   −16.1
   3/4    χ₃      32   −15.7

Even continuous
part, no atom:
barely ≥0, λ_min
shrinks ~1/n.
Could be 0⁺.
χ₅ atom (w₂<0)
makes λ_min ≈ −1/2
independent of n:
G_reg+atom is
**not** PD on
the interval.

Odd G_reg < 0
on the whole
[0,L]. Raw
Toeplitz cannot
be PD. The
∫g/y + CST
piece that we
removed is
what makes
scan_s Q>0
on hats. This
test does not
kill Q̂_L.
It kills
“G_reg itself
is a Krein
kernel” for
s₀=3/4 and
for χ₅+atom.

So the
inequality
Krein wants,
applied to
G_reg alone,
fails in the
cases that
matter. A
Krein proof
has to keep
the regular
1/y+CST
terms in the
same kernel,
or work with
the full G
as a
distribution.
