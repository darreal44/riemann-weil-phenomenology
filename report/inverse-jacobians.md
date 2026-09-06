# Jacobians of the inverse shell

n=+1, |u|_2=½,
|1−u|_2=1, raw
weight 1.
Inverse twist:
λ_slice interpreted
as |u^{-1}|_2=2.

    d*u  →  weight 1
    √|u^{-1}|_2 twist → ×√2
    mass_at_two('inverse') = √2

That √2 is *one*
Jacobian (the module
of the inverse). It
does not know about
Fmat.

## Extra maps in τ

    F_S carries ½ on
    every block
        → × ½
    ϑ(λ) puts λ^{−1/2}
    at λ=2
        → × 2^{−1/2}=1/√2
    w₂ integrates d*λ
    = dλ/λ
        → already Haar
          on R>0

Product of the
*code* factors,
before Si:

    ½ · 2^{−1/2} = 1/(2√2)
                  ≈ 0.354

If the inverse mass
√2 were just these
factors times raw=1,
we would see
0.354, not 1.414.
The ratio is

    √2 / (1/(2√2)) = 4
    wait: 1.414/0.354=4

That 4 is *not*
κ. κ was defined
so that
m = κ/(2√2).
m=√2 ⇒ κ=8.

So two 2's are
missing if one
naively multiplies
½ and 2^{−1/2}
onto the inverse
twist:

    √2 · ½ · 2^{−1/2} = ½
    (would be m=0.5)

To land on √2 one
needs an extra ×4
from the Si pairing
*or* one must *not*
attach both ½ and
λ^{−1/2} to a mass
that is already
twisted.

## Clean accounts

**Account I**
(inverse, κ=8).
Keep every code
factor. Declare
κ=8 to be the
value of the
Si-matrix element
that makes m_lin=√2.
Then the Jacobians
are:

    raw 1
    · inverse twist √2
    · ½
    · 2^{−1/2}
    · κ=8
    = √2

Check:
1·√2·½·2^{−1/2}·8
= √2 · 4 · 2^{−1/2}
= 4 / √2
= 2√2
which overshoots.
Do not multiply
the inverse twist
*and* κ as if they
were independent:
κ already eats
the Si *and*
whatever convention
sits in B₂.

The definition
that does not
double-count:

    m_lin = (½)(2^{−1/2}) κ_Si
    set equal to
    twisted_inverse(1)=√2
    ⇒ κ_Si = 8

Here κ_Si is *not*
« times the inverse
twist ». It is the
number that makes
the Fmat linear
probe match that
twist. One equation,
one unknown.

**Account II**
(Lebesgue).
δ(λ−2) dλ = 2 δ d*λ,
so a Lebesgue Dirac
of mass 1/√2 becomes
√2 in d*λ. Same
number as the
inverse twist,
different story
(`lebesgue_jacobian
_at_two` in
`tau2_local.py`).
κ=8 would not
distinguish I from
II.

**Account III**
(module, κ=4).
Same formula,
target 1/√2,
κ_Si=4. Inverse
Jacobians unused.

## What to write
after the server

If κ→8: say
« Fmat linear probe
matches inverse
(or Lebesgue×module),
κ_Si=8 », not
« we multiplied √2
by four Jacobians ».
If κ→4: inverse
Jacobians are the
wrong chain.
