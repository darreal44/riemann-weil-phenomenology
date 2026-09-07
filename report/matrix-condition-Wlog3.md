# Matrix condition on W_{log 3}

2×2 H:
    κ(H) = λ_max/λ_H
         ≈ H₁₁ / λ_H

    χ₈   2.23/0.257 ≈ 9
    χ₄   1.54/0.084 ≈ 18
    χ₅   1.63/0.053 ≈ 31
    χ₃   1.12/0.018 ≈ 62
    χ₇   0.338 λ_H, comfortable
    χ₁₇  0.692 λ_H, comfortable

χ₃ is the
worst 2×2
(the well).
κ~60 is
harmless
in float64
(eps·κ
~10⁻¹⁴).

T section
n=2..31
(`chi3-S-exact.md`):
    λ_min(T) 1.55–2.76
    Q_nn last ~4–5
    κ(T) = O(1)–O(10)
Same
story as
χ₂₉’s T
(`numerical-stability.md`):
the tail
is the
well-
conditioned
piece.

What
would
be ill-
conditioned:
the
cosine
Vandermonde
at many
close t_j
in an
atomic
fit.
Our t
were
spaced
~4–5.
Not
that
regime.

S_lo
divides
by
(1−ρ).
ρ=0.52
(χ₅)
gives
2.1;
ρ=0.59
(χ₃,h=2)
gives
2.4.
That
amplifies
C, it
does
not
make
H
singular.
At
h=4,
ρ_N
drops
to
0.18
(χ₃):
better
κ on
the
Neumann
factor,
which
is
why
S_lo
crosses.
