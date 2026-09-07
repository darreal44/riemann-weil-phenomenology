# Schur with T diagonal (χ₅, χ₈)

Finite C: 2 × 38,
T replaced by its
diagonal (the
Q_nn already
computed). Not a
bound: off-
diagonals of T
can make T^{-1}
larger.

    χ     λ_H     λ_min(S_diag)   β_Frob (δ=qmin)
    χ₅   0.053    **+0.042**      −0.018
    χ₈   0.257    +0.243          +0.198

On χ₅ the true-ish
coupling C D^{-1} C*
only eats 0.011 of
λ_H. The
Frobenius/qmin
majorant ate more
than λ_H and
declared β<0
even at Off_T=0.

So the obstruction
named in
`chi5-hankel-not-enough.md`
is the *majorant
of C*, not C.
A take of χ₅ by
Schur is possible
if one bounds
T^{-1} close to
D^{-1} (diagonal
dominance of the
tail, or a
controlled
Gershgorin on
Off_T). Until
that bound
exists, +0.042
is a number,
not a
certificate.

Executed
(`ql-schur-neumann.md`):
Neumann bound
gives S_lo=+0.029
on χ₅. Certificate,
not the diagonal
number.

χ₈: S_diag stays
well above 0,
consistent with
#58.
