# Fmat semi-local is a dyadic sum

    F_S = ½ ( −block(½) + ∑_{n≥0} block(2ⁿ) )
    F_∞ = block(1)

block(s) = cell-average of
Si(2π s x_out x_in) /
(π s). That is the
kernel at scale s.

S−A is therefore the
scales {½, 1, 2, 4, …}
minus the archimedean
s=1. The probe
ϑ(λ)g(r)=λ^{−1/2}g(r/λ)
looks at scale λ.
A bump of S−A at
λ=2 is the block(2)
term being read by
ϑ(2).

In tau2_local,
n = −1 is |u|_2=2,
n = +1 is |u|_2=½.
Fmat’s block(2) is
the first; block(½)
is the second
(already with a
minus in F_S).

That minus on
block(½) is a
convention in the
finite-part sum,
not a Haar mass.
It is a plausible
origin of a sign
or a √2 versus
1/√2 mix-up, not
a proof of either
target.

The dictionary
block(2ⁿ) ↔ shell n
is the line
`fmat-integrand.md`
asked for. It is
still a dictionary,
not d*λ=d*u.
