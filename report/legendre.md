# Legendre polynomials in this code

They enter twice: Gauss
quadrature of the
archimedean panel, and
the classical expansion
of PSWF.

## Quadrature of Q

`scan_s.assemble` uses
DEG-point Gauss–Legendre
on each of 3N+12 panels
of [0, L]. Default DEG=12.

χ₅ μ=8 N=6, λ₀ and Q₀₀
against DEG = 4,6,8,12,16:
all give

    λ₀  = 1.0081×10⁻⁶
    Q₀₀ = 0.126570
    Q₀₁ = 0.194610

to the printed digits.
The panel split already
resolves the kernel.
Raising DEG does not
move the well. The
quadrature is not the
error term in det H.

## PSWF at c = π

ψ₀, ψ₁ expanded in
P_n on [−1,1]:

    ψ₀ = 0.669 P₀ − 0.511 P₂
         + 0.077 P₄ − 0.005 P₆
         + 0.0002 P₈
    ψ₁ = 1.182 P₁ − 0.486 P₃
         + 0.055 P₅ − 0.003 P₇

Odd coefficients of ψ₀
are 10⁻¹⁵ (parity). Two
or three Legendre
polynomials already make
the two-mode Slepian
(`prolate-profiles.md`).

That basis is the natural
one for the *desert*
operator, not for Q.
v₀ of Q is a combination
of hats φ₀, φ₁, not of
P₀, P₂. Expanding v₀ in
Legendre on [0, L] would
just rewrite the two
cosines 1 and cos(2π y/L)
as an infinite Legendre
series — worse, not
better.

## Reading

Legendre is a converged
integrator here, and a
short expansion of the
wrong operator (Slepian
instead of Weil). It does
not give a new handle on
det(A−P).
