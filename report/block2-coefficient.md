# Coefficient of block(2) in τ(λ)

## The maps, as written

    F_∞ = block(1)
    F_S = ½ ( −block(½) + ∑_{n≥0} block(2ⁿ) )
        = ½ block(1) + ½ block(2) + ½ block(4)+…
          − ½ block(½)

    ΔF := F_S − F_∞
        = −½ block(1) + ½ block(2) + ½ block(4)+…
          − ½ block(½)

So in ΔF the linear
coefficient of block(2)
is **+½**.

    A = P F P
    W = F A = F P F P
    τ(λ) = λ^{−1/2} ∑_i W(x_i/λ, x_i) w_i

τ is *quadratic* in F.
The piece of τ_S−τ_∞
that is linear in
block(2) comes from
the cross terms

    F_∞ P (½ B₂) P
    + (½ B₂) P F_∞ P

not from (½ B₂)P(½ B₂)P
(second order in the
2-adic scales).

At the probe λ=2 the
prefactor λ^{−1/2} is
**2^{−1/2}**. Sampling
sits at r = x/2, which
is the scale that
block(2) was built for
(Si(2π·2·x_out·x_in)).

Then

    w₂ = ∫_{window at 2} τ(λ) dλ/λ
       = ∫ τ  d*λ

If τ were a Dirac in
d*λ of mass m, w₂→m.
The linearised mass
from block(2) alone
would be

    m_lin = ½ · 2^{−1/2} · κ
          = 1/(2√2) · κ

where κ is the pairing
of the kernel B₂ against
the archimedean state
P F_∞ P (the cross
term), including the
cell averaging of Si.

## Against the two shells

    twisted_module(−1)  = ½ · √2 = 1/√2
        (n=−1, |u|_2=2, raw 1/2,
         one √λ twist)

    twisted_inverse(+1) = 1 · √2 = √2
        (n=+1, |u|_2=½, raw 1,
         inverse twist)

    m_lin / (1/√2) = κ/2
    m_lin / √2     = κ/4

Equality: κ=2 (module)
or κ=4 (inverse).
(The earlier 4/8 split
was an arithmetic slip:
κ/(2√2) × √2 = κ/2.) κ is *not*
1: it is the matrix
element of B₂ on the
archimedean compression.
It depends on Λ and on
the Si-kernel, and it
is why w₂ still moves
with cpu.

## What this does not do

It does not compute κ.
That is one inner
product in
`trace_dist.py`:
replace Fmat by
block(2) only, keep
A from F_∞, probe at
λ=2, integrate d*λ.
If that number tends
to 4·(1/√2)=2√2 or to
8·(1/√2) wait no:

m_lin = κ/(2√2).
Set m_lin = 1/√2 ⇒ κ=2.
Set m_lin = √2     ⇒ κ=4.

A freeze of that
single-block probe
at 4 or 8 would pick
the convention. The
full S−A also has
−½ B₁, −½ B_{1/2},
½ B₄, … and the
quadratic B₂ P B₂
term. Those are why
the peak is a window,
not a Dirac.

Shipped identity:
coeff of B₂ in ΔF is
½; probe brings
2^{−1/2}; Haar is
d*λ. Product of the
three explicit
factors: 1/(2√2).
The unknown is κ.
