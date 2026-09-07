# The Weil matrix

Weil positivity: Q(f)≥0
for a class of test
functions, for all
characters / L-functions
in play, is equivalent
to RH (Li / Bombieri–
Lagarias on the right
class). The repo never
takes that step. It
computes a *matrix* of Q
on a finite cosine basis.

## Entries

Hats on [0, L], L=log μ:

    η₀ = L^{−1/2}
    η_n = (2/L)^{1/2} cos(2π n t / L)

    S_{nm} = Q(η_n, η_m)
           = A_{nm} − P_{nm}

**Archimedean A.** For
each Gamma factor with
shift s₀,

    A_{nm} = (F₀/2) CST
           + ½ ∫_0^L D₂(y)
             ( F₀ e^{−(2−2s₀)y}
               − θ_{nm}(y) ) dy

    D₂(y) = 2 e^{−2 s₀ y}
            / (1 − e^{−2y})
    θ_{nm} closed
    (sines, `th_hat`)
    F₀ = 2 δ_{nm} for the
    diagonal of the
    unfolding at 0.

CST holds log(q/π)−γ
and the Frullani tail
−log(1−e^{−2L}).

**Prime P.**

    P_{nm} = ∑_{n≤μ}
             w(n) θ_{nm}(log n)

    GL1: w = χ(n) Λ(n) n^{−1/2}
    GL2 FIX: w = Λ_f(n) / n
             (Hecke recurrence)

No zeros enter S.
Zeros enter the *other*
matrix G=2Φ*Φ
(`lambda0-formula.md`).

## Spectrum

    S = Sᵀ
    λ₀ = λ_min(S)
    Q(v) = vᵀ S v   for
           coefficients v

The rational witness is
v=(4,−3,1)/√26 in the
first three coordinates,
zero after. The quorum
drops one Hecke prime
from P and watches the
sign of λ₀.

## What the matrix is not

Not the Weil explicit
formula written in full
(the zero side is absent
by construction: Q here
is the prime+archimedean
side). Not a Hamiltonian.
Not χ_E P χ_E. A 3×3 or
81×81 block of S is a
Galerkin slice of one
quadratic form.
