# Chebyshev polynomials

Same two roles as Legendre:
a possible integrator, and
an expansion of the PSWF.

## PSWF at c = π, L²-coeffs of T_n

    ψ₀ = 0.669 T₀ − 0.770 T₂
         + 0.099 T₄ − 0.018 T₆
    ψ₁ = 1.182 T₁ − 0.716 T₃
         + 0.032 T₅ − 0.033 T₇

Parity exact. Comparable
length to the Legendre
series (`legendre.md`):
three terms give the
shape, the rest is 10⁻².
Chebyshev does not
compress the two-mode
Slepian better than P_n.
The function is smooth
and even/odd; any
polynomial basis with
parity sees that.

## Integrator

`assemble` maps each
panel by Gauss–Legendre,
not Clenshaw–Curtis.
On this kernel the
panels already make
DEG=4 exact at printed
precision. Replacing
the nodes by Chebyshev
extrema would change
the constant A at
10⁻¹⁶, not H₁₁.

Chebyshev nodes cluster
at the ends of each
panel. The archimedean
weight is singular at
y=0 like 1/y. That
singularity is handled
by the first panel and
by writing
(F₀ e^{…} − θ)/ (e^y−e^{-y}),
not by endpoint
clustering.

## Reading

T_n is a sibling of P_n
for the desert operator
and a non-event for Q.
v₀ remains a two-hat
vector, not a short
Chebyshev series on
[0, L].
