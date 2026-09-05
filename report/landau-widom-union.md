# Landau–Widom on the union E_L

Landau–Widom 1980, finite unions of intervals: the concentration
operator χ_E P_τ χ_E has

    #{λ > α} = K + (1/π²) log((1-α)/α) log c + o(log c),

Shannon number K = 2 τ |E| / π, c a large scale. Leading term
depends on the *measure* |E|, not on the number of pieces.
The pieces enter the o(log c) and the geometry of the plunge,
not K.

## Numbers

| χ | μ | pieces | K | ell | ell/K |
|---|---|--------|---|-----|-------|
| χ₂₉ | 22 | 8 | 18.5 | 5.5 | 0.30 |
| χ₂₉ | 74 | 42 | 103 | 26.5 | 0.26 |
| χ₁₇ | 22 | 8 | 21 | 12.3 | 0.59 |
| χ₅ | 38 | 54 | 139 | 86.7 | 0.63 |

ell / log K is 2–24, not O(1): measured depth is not the
plunge width. ell / K sits in 0.26–0.63, the same range as
ell/(τ|E|) up to the factor 2/π.

## What LW gives for the bound

- λ_max(χ_E P_τ χ_E) is exponentially close to 1, at a rate
  set by the largest component (at least as good as Slepian
  of I_max). That is how well a PW function *can* hide in E.
- The cluster of ~K eigenvalues near 1 is the “can hide”
  space. n_pieces does not enlarge K.
- Q is not χ_E P χ_E. v0 is odd on a short gap, outside E.
  LW on E describes the hiding space we do not occupy.

A proof of ell ≤ C τ |E| via LW would be: the bottom of Q
cannot be deeper than the *decay region* of a related
operator whose Shannon number is K, hence ell = O(K) =
O(τ|E|). That is C of order 1, which the table already
allows (C_τ = 1/2). Making it a theorem is identifying Q
with (a compression of) that operator — the missing step
since sampling-floor.

## Pieces

Using n_pieces as a Shannon correction (K' = K + n_pieces)
changes K by 10–40 %, not the form. LW 1980 does not add
one dimension per gap at leading order. The codimension
count dim = n_L − n_∂ of `one-set-lemmas.md` is a different
index (interlacing), not the LW K.
