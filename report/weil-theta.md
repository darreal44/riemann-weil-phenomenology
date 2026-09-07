# Weil’s θ

Not Jacobi’s θ.
Weil’s test
function on the
additive line,
even, compactly
supported in
[−L,L], with
θ(0)=2 in the
normalisation
of this repo
(the hats).

On a pair of
modes (n,m)
the kernel is
`theta_hat` in
`ql_schur_tail.py`:

    n=m=0:  2(L−y)/L
    n=0:    −2 sin(ω_n y)/(√2 π n)
    n=m:    2((L−y)cos(ω_n y)/L
            − sin(ω_n y)/(2π n))
    n≠m:    2(n sin(ω_n y)−m sin(ω_m y))
            / (π(m²−n²))

That is the
matrix element
of the even
cosine ONB
against the
delay. Q pairs
it with D₂
(archimedean)
and with the
atoms at
log p (T_p).

#59: on
(log 2, log 3]
one has
log 2 ≥ L/2, so
the two even
halves of a
hat-unit f are
disjoint at
y=log 2 and
|θ_f(log 2)|≤1.
Finite
sections hit 1
to 10⁻¹⁵.
That bound is
sharp. It
replaced
‖Θ‖≤2
(discrete
Hilbert).

θ is not PD
and not a
symbol. It is
the *test*
that Q eats.
m_Q is the
symbol;
θ builds the
matrix
elements.
