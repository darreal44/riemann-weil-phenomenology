# The hat Gram is not a DPSS matrix

A discrete prolate matrix
with Shannon number ~ D_max
has ~ D_max eigenvalues
*near 1* (concentrated
modes, ell = -ln λ ~ 0)
and a plunge of width
O(log c) down to λ~0.

Our wells are the opposite
end: ell_0 = 11–35 means
λ(G) = e^{-ell} = 10^{-5}
to 10^{-15}. They are the
*small* eigenvalues of G,
the kernel of evaluation
(Rayleigh lemma in
`landau-depth.md`), not
the concentrated cluster
of a limiter.

A raw overlay
"G ≈ χ_E P χ_E" therefore
compares two different
ends of two different
spectra. Landau–Widom
controls the *plunge of
the limiter*. The hat
Gram's plunge (one rung
at k = D_max in
`widom-profile.md`) is
the drop of -ln λ(G)
as one leaves the kernel
of Eval. Same word
"plunge", two operators.

Identifying them requires
a relation

    G  ≈  (out-of-band mass)
            of the limiter
            on ker Eval,

not G ≈ limiter. That
identity is not written.
Until it is, Widom's
O(log c) width does not
have to show up as three
rungs of ell_k, and the
one-rung profile is not
a contradiction — only
evidence that the transfer
is not naive.
