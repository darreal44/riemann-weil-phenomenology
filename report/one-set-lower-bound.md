# One-set lower bound

## Statement to prove

Let E_L be the one-set of `one-set-sampling.tex` (desert ∪ long
gaps), τ = L/2 = (log μ)/2. Let c_L = λ_min(Q_L). Then there is
an absolute C such that

    c_L  ≥  exp(− C τ |E_L|)
    i.e.  ell ≤ C τ |E_L|.

## Data (Q, not Gram)

ell / (τ |E|) on the hold-outs:

| χ | μ range | ell/(τ|E|) |
|---|---------|------------|
| χ₂₉ | 11–74 | 0.16–0.19 |
| χ₁₇ | 11–74 | 0.21–0.42 |
| χ₅ | 38–62 | 0.40 |

Max = 0.42. The inequality holds on every measured window with
C = 1/2, and with C = 1 by a factor two.

This is an *upper* bound on the depth: Slepian says one cannot
hide in a set of measure |E| faster than e^{−c τ |E|}. The
numbers say the actual hiding is slower than e^{−0.42 τ |E|}.

## What would prove C = 1/2

Landau–Widom on a finite union: λ_max(χ_E P_τ χ_E) ≤
1 − exp(−C τ |E|), or a coupling argument that the bottom
mode of Q is no deeper than the Slepian plunge of E. Two
obstacles already recorded:

- E is a union, not an interval. Plunge is governed by
  components and by |I_max|, and ell / (τ |I_max|) is *not*
  bounded (0.14 to 4.6 in `one-set-ratios.md`). So the bound
  must use |E|, not |I_max|.
- v0 does not live in E. It is odd on a short gap. The
  Slepian of E is the wrong eigenfunction. A proof that
  still uses |E| must pass through the participation of
  that pair in the union (the C(χ) tax), not through
  concentration on E itself.

DS + Bernstein on each gap: closed, negative bracket.

Beurling–Malliavin multiplier of E: named, radius not
computed (`beurling-malliavin-weighted.md`).

## Status

Numerically locked at C = 1/2 on the present Q table.
Not a theorem. Next analytic move is LW on the union
with the measured number of pieces (n_long+1), not a
new scan.
