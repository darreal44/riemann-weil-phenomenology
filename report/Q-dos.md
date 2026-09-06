# Spectral density of Q

χ₅. Empiricial DOS: a few
atoms at 0, a hole, then
a bulk on [1, 4].

## Atoms and hole

| μ | N | # λ < 10⁻³ | # in [0.05,1] | # ≥ 1 |
|---|---|---|---|---|
| 8 | 8 | 1 | 0 | 7 |
| 16 | 8 | 2 | 1 | 5 |
| 16 | 12 | 3 | 1 | 9 |
| 22 | 8 | 3 | 1 | 4 |

The atoms are k=0,1 (and k=2
once it has left the head).
Between 10⁻³ and 1 there is
at most one eigenvalue —
the plunging Slepian, not
a continuum.

## Bulk = spec T

Pooled T at N=8, μ=8,16,22:

    [0,0.5)  ###
    [0.5,1)
    [1,2)    ##
    [2,3)    ######
    [3,4)    ######
    [4,5)    #

mean 2.43, var 1.49,
min 0.02, max 4.1.

Not a Wigner semicircle
(that would be centered
at 0). Closer to a shifted
Marchenko–Pastur / “I plus
a kernel of size 1”, which
is what a Gram matrix of
almost-orthogonal hats
looks like. The mean ~2.5
is the typical diagonal of
T (`Q-matrix.md`).

## Reading

The DOS of Q is the DOS of
T, plus two (then three)
outliers that T does not
see. There is no spectral
sea around the well. ρ(λ)
near 0 is a sum of deltas,
not a density that could
be integrated to a Weyl
law. Counting functions
for zeros live in Gram,
not here.
