# −log det = desert + gap tax

Split ∑_{λ>0.01} −log(1−λ_j)
= −log(1−λ₀) + tax.

| E | m | I_max | −logdet | −log(1−λ₀) | tax | tax/(m−1) | τ Δ\|E\| |
|---|---|---|---|---|---|---|---|
| [0,1] | 1 | 1.00 | 1.77 | 1.53 | 0.24 | — | 0 |
| [0,2] | 1 | 2.00 | 5.66 | 3.97 | 1.69 | — | 0 |
| 1+0.3 close | 2 | 1.00 | 2.20 | 1.58 | 0.62 | **0.62** | 0.94 |
| 1+0.3 mid | 2 | 1.00 | 2.14 | 1.55 | 0.59 | **0.59** | 0.94 |
| 1+0.3 far | 2 | 1.00 | 2.13 | 1.53 | 0.59 | **0.59** | 0.94 |
| 1+two 0.3 | 3 | 1.00 | 2.57 | 1.57 | 1.00 | **0.50** | 1.89 |
| 1+three 0.3 | 4 | 1.00 | 2.97 | 1.58 | 1.39 | **0.46** | 2.83 |
| 0.8+three 0.3 | 4 | 0.80 | 2.45 | 1.20 | 1.25 | 0.42 | 2.83 |
| 1+1 | 2 | 1.00 | 3.77 | 2.09 | 1.69 | 1.69 | 3.14 |

A 0.3-gap costs **0.46–0.62 nats**,
independent of where it sits. Three
of them cost 1.39, not 3×0.94.
The tax is **O(1) per piece**, not
O(τ |gap|).

That is Widom's perimeter term
(n_∂/4π) log(τ · sep), seen in the
product rather than in the count.
Distance of the gap almost drops
out (0.62 close vs 0.59 far).

The formula log(1+|I_j|/mid_j)
failed: on a desert [0,L] it is
constant. BM ∫ n_E/r² still
correlates with −logdet (0.94)
because both grow with |E|, but
the residual that is the gaps is
this O(m) tax.

## Lemma 2, constant

If the comparison Q ↔ det(I−A)_+
holds, then

\[
-\log c_L
\;=\;
C_0\,\tau\,|I_{\max}|
\;+\;
C_1\,(m-1)
\;+\;O(1),
\]

not C · dim(E) with dim ∼ τ|E|.
dim overcounts the gaps by a factor
τ. The one-set law, if true at this
precision, is desert Slepian plus a
piece-counting correction — closer
to Landau–Widom than to a single
Beurling density of E.

Still unproved: the passage from
det(I−A) to the Rayleigh of Q.
