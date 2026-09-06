# Lemma 2, the sampling constant

Wanted, under RH:

\[
c_L
\;\ge\;
\exp\bigl(-C\dim(E_L)\bigr),
\qquad
\dim(E_L)=n_L(E)-n_\partial.
\]

`lemma2-filled.md` reduces this to
\(1-\lambda_{\max}(A|_V)\ge e^{-C_0\dim}\),
\(A=\chi_E P_\tau\chi_E\). That reduction
is the wrong eigenvalue for a one-set law.

## What λ_max actually sees

Nyström on the sinc kernel, τ=π.
\(E=I_{\mathrm{des}}\cup I_{\mathrm{gap}}\).

| E | \|E\| | I_max | 1−λ_max | e^{−τ I_max} | ratio |
|---|---|---|---|---|---|
| [0,1] | 1.00 | 1.00 | 0.217 | 0.043 | 5.0 |
| [0,1]∪0.4∪[0.3] | 1.30 | 1.00 | 0.214 | 0.043 | 5.0 |
| [0,1]∪1.5∪[0.3] | 1.30 | 1.00 | 0.216 | 0.043 | 5.0 |
| [0,2] | 2.00 | 2.00 | 0.019 | 0.0019 | 10 |
| [0,2]∪1.0∪[0.5] | 2.50 | 2.00 | 0.019 | 0.0019 | 10 |
| [0,1]∪0.5∪[0,1] | 2.00 | 1.00 | 0.124 | 0.043 | 2.9 |

A small extra interval does not move
1−λ_max. The top prolate sits in the
longest piece. Coupling raises λ_max
only when two pieces are comparable
(last row), and even then the leak
stays a constant times e^{−τ I_max}.

So, unconditionally on a finite union,

\[
1-\lambda_{\max}(A)
\;\asymp\;
e^{-\tau\,|I_{\max}|}
\;=\;
e^{-(L/2)\,\gamma_1}
\]

up to the Slepian √c prefactor (ratio
5–10 in the table). Dirichlet at the
ends (the passage to V) can only
increase the leak. Step A+B of
`lemma2-filled.md` is therefore true,
and gives

\[
c_L
\;\ge\;
C\,\alpha\,e^{-L\gamma_1}.
\]

That is the **desert** bound. It is
not the one-set bound. dim(E_L) counts
every sub-Nyquist gap; I_max does not.

## Why exp(−C dim) is the wrong target
if taken from λ_max

dim(E) ∼ (τ/π)|E|. e^{−C dim} is much
*smaller* than e^{−τ I_max} as soon as
E has more than one piece. A lower
bound e^{−C dim} would follow from
e^{−τ I_max} with room, and would say
almost nothing: the constant C can
eat the extra gaps. The phenomenology
to prove is the opposite — that those
gaps *cost*, additively in the
exponent, not that they can be
ignored.

λ_max cannot see them. A proof of
Lemma 2 that goes through
1−λ_max(A|_V) will always return
the desert.

## What would see the gaps

One of:

1. **Beurling density of the complement.**
   Γ ∩ (ℝ \ int E) must sample PW_τ
   with constant ≥ e^{−C dim}. The
   complement has a hole at every
   component of E. Beurling–Malliavin
   radius of that hole set is the
   object. Not λ_max.

2. **Product over the plunge.**
   ∏_j (1−λ_j(A|_V)) over the
   dim hidden modes. The determinant
   of (I−A) on that subspace *does*
   see every piece. Widom's multi-
   interval determinant formula is
   the analytic name of this. It is
   not in the repo.

3. **Capacity / equilibrium of E.**
   log c_L ≲ −cap_τ(E). For a union
   of intervals the capacity is
   roughly ∑ |I_j| plus interaction,
   which *is* one-set.

(1) or (2) is the remaining lemma.
λ_max is done.

## Status

| claim | status |
|---|---|
| 1−λ_max(A) ≍ e^{−τ I_max} on a union | numerical, this note |
| c_L ≥ C e^{−L γ_1} under RH | follows from the above + sampling on the complement (α) |
| c_L ≥ exp(−C dim E) with C independent of the partition of E | **open**, and not implied by λ_max |
| the gaps enter the exponent | needs BM radius or Widom det |
