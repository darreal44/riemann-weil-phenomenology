# Proof of Weil’s criterion (the equivalence, not RH)

Weil 1952 is an *equivalence*, not a positivity theorem.
The proof has two directions and one identity.
None of the three is RH.

## The identity (explicit formula)

For an admissible even test function h
(Schwartz, or compact support with a
smooth Fourier pair — Bombieri–Weil
normalization),

    W(h)  =  ∑_ρ ĥ(ρ)

        =  ĥ(0) + ĥ(1)
           − ∑_{n≥2} Λ(n) n^{-1/2} h(log n)
           − Arch_Γ(h).

The left-hand side is a sum over
nontrivial zeros of ζ (or of L(s,χ)).
The right-hand side is poles + primes +
Gamma. No hypothesis on the zeros.
This is Guinand–Weil. Q_L of the repo
is the same identity restricted to
supp h ⊂ [−L, L] (hats on [0, L],
n ≤ µ = e^L).

## Direction RH ⇒ W ≥ 0

Assume every nontrivial zero is
ρ = 1/2 + iγ. Then ĥ(ρ) is evaluated
on the line. For the even real
normalization used here,

    ĥ(1/2 + iγ) = F(γ)²    (F = Fourier of the windowed f),

so

    W(h) = ∑_γ F(γ)²  ≥ 0.

That is a sum of real squares. The
archimedean and prime sides are not
used. Compact support is not used.
This direction is elementary once the
identity is granted.

On a window: Q_L(f) = ∑_γ F(γ)² under
RH, which is the zero Gram. Beurling
then gives c_L > 0. That last step
still assumes RH.

## Direction W ≥ 0 ⇒ RH

Contrapositive. Suppose there is a
zero ρ = 1/2 + σ + iγ with σ ≠ 0.
Zeros come in the pack

    {ρ, 1−ρ, ρ̄, 1−ρ̄}.

The corresponding terms of W are

    ĥ(ρ) + ĥ(1−ρ) + ĥ(ρ̄) + ĥ(1−ρ̄),

which is *not* a sum of squares.
One can choose an admissible ĥ
peaking at ρ (Paley–Wiener of large
type, or a Schwartz bump) so that
this pack contributes a strictly
negative amount, larger in absolute
value than the contribution of all
other zeros (those are controlled
by the decay of ĥ). Then W(h) < 0.

That construction is the content of
Weil’s argument and of Bombieri’s
later write-up. It uses:

- the four-term pairing, not F(γ)²,
- a test function that *sees* height
  γ and displacement σ,
- a tail estimate on the rest of the
  spectrum.

It does *not* produce an explicit h
for a given ρ; it proves existence.
Visibility in the repo
(`visibility-offline`) is the same
construction restricted to a window
of type L/2: the App. B term opens
at −σ² on the ground state once L
is large enough. Schematic, not
uniform in γ.

## What is proved and what is not

| claim | status |
|---|---|
| explicit formula W = poles − primes − Arch | proved (Guinand–Weil) |
| RH ⇒ W(h) ≥ 0 for all admissible h | proved (squares) |
| W(h) ≥ 0 for all h ⇒ RH | proved (peak at an off-line pack) |
| W(h) ≥ 0 for all h | **open** (this is RH) |
| Q_L ≥ 0 for one L | certificates, finite |
| (∀ L) Q_L ≥ 0 | **open**, equivalent to RH on compactly supported tests, which is again RH |

The “proof of the criterion” is the
middle two rows. The “proof of RH”
would be the fourth. Confusing them
is the error the freeze forbids.

## Why compact support does not help

W restricted to compactly supported
h is Q_L as L runs. The implication

    (∀ L) Q_L ≥ 0  ⇒  no off-line zero

is the covering step of
`notes/rh-weil-criterion.md`. It is
the second direction of Weil, with
the peak constructed inside some
PW_{L/2}. The hypothesis is still
positivity for every L. A certificate
at µ=11, or a scan to µ=80, is one
value of L.

det(A−P)>0 on the 2-plane is
positivity of Q on a two-dimensional
subspace at one L. It does not
enter either direction of the
criterion.

## Reference shape

Weil, *Sur les “formules explicites”
de la théorie des nombres premiers*,
Comm. Lund 1952.
Bombieri, *Remarks on Weil’s explicit
formula*, in several expositions of
the explicit formula and the
positivity criterion.
The repo’s App. B / quorum notes use
that normalization; they do not
replace it.
