# (∀ L) Q_L ≥ 0  and  RH

Weil 1952: the quadratic
form of the explicit
formula is positive on a
suitable class of test
functions if and only if
every non-trivial zero
has real part 1/2.
Li / Bombieri–Lagarias
is the same statement
in another basis.

In the repo’s language
the implication that
would cover RH is

    (∀ L>0)( Q_L ≥ 0 on W_L )
        ⇒  no off-line zero.

An off-line zero at
β+iγ with β≠1/2 produces
a negative direction in
the explicit formula
once a Paley–Wiener
function of type ≥|γ|
can see it. If every
window is positive, no
such zero exists. That
is RH, provided the
class W_L is rich enough
to make every off-line
zero visible (Weil’s
class, or a dense
subclass).

## What Q_L is here

Q_L = A_L − P_L, the
archimedean plus prime
side on functions of
type L. Under RH this
equals the zero side
and is ≥0. The repo
computes a Galerkin
slice S on cosine hats
of length L, not the
infimum on W_L.

Courant:

    λ_min(S) ≥ inf_{W_L} Q_L.

A certificate λ_min(S)>0
is an *upper* bound on
the infimum’s depth, not
a lower bound on the
class (#42). So

    (∀ L) λ_min(S_L)>0

is weaker than
(∀ L) Q_L≥0 on W_L,
and is still not proved
(only measured on a
list of L, for one v
or one quorum).

## What this note is not

Not a new criterion.
Not a proof that the
hats are dense enough
in Weil’s class. Not
(∀ L) for the slice.
The covering implication
stands *after* every
item of
`remaining-before-rh.md`.
