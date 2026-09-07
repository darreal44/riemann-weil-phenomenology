# Convexity of G_reg on (0,L]

    G_reg(y) = D₂(y) − 1/y
    L = log 3

s₀=1/4 (χ₅,χ₈):

    G_reg(0⁺) ≈ +1/2
    decreasing to ≈ +0.39 at L
    second differences < 0
    → **concave**, not convex

s₀=3/4 (χ₃,χ₄):

    G_reg(0⁺) ≈ −1/2
    increasing to ≈ −0.48 at L
    second differences > 0
    → convex, but
    **increasing**, not ↓0

Pólya wants even,
convex, decreasing
to 0 on [0,∞).
Neither parity
gives that on
[0,L] already.
A tail past L
cannot repair
concavity (s₀=1/4)
or the wrong
monotone (s₀=3/4)
without changing
values inside
(0,L), i.e.
without changing
Q.

Textbook Pólya
on G_reg is
closed. The
remaining
constructions
are: a different
regularisation
(not D₂−1/y),
or Krein without
convexity
(moment problem,
not Pólya).
