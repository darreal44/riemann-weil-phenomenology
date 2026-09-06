# Isoperimetric profile of E, for Lemma 2

Fix |E| and vary the number m of
intervals (perimeter P=2m). Three
scalars: log-cap energy I of
normalised Lebesgue, cap = e^{−I},
and the single-interval comparison
|E|/4.

## Fixed |E|=2

| E | m | I | cap | |E|/4 | I − I_{interval} |
|---|---|---|---|---|---|
| [0,2] | 1 | 0.78 | 0.46 | 0.50 | 0.09 |
| 1.6+0.4 | 2 | 0.65 | 0.52 | 0.50 | −0.05 |
| two 1, gap 0.5 | 2 | 0.54 | 0.58 | 0.50 | −0.15 |
| two 1, gap 2 | 2 | 0.18 | 0.83 | 0.50 | −0.51 |
| three 0.6 | 3 | 0.43 | 0.65 | 0.50 | −0.26 |
| four 0.5 | 4 | 0.31 | 0.73 | 0.50 | −0.38 |

Lebesgue energy, not equilibrium:
the 0.09 on the interval is the
arcsine gap. Direction is robust.

## Two laws, opposite in m

**Capacity / spread.** At fixed |E|,
the interval *minimises* cap. Splitting
and separating raises cap (0.46 → 0.83
at gap 2). Classical: among connected
sets the interval is the only shape;
among disconnected sets, cap grows
with the diameter. Polya–Szegő.

**Slepian / λ_max.** At fixed |E|, the
interval *maximises* λ_max (minimises
the leak 1−λ_max). Dust of the same
measure does not concentrate. Faber–
Krahn for the time-frequency window.

So cap and 1−λ_max move against each
other when E is cut. The table of
`lemma2-three-tests.md` is this
isopérimètre: 1−λ₀ tracks I_max, I_cap
tracks the spreading.

## What Weil does

The measured depth s *increases* when
a sub-Nyquist gap is added (the
two-term law that later failed at a
common T₀, but the sign of the gap
term was +). Gaps *cost*. That is the
monotonicity of BM ∫ n_E/r² and of
Widom-all, not of λ_max and not of
cap as an upper bound.

Isoperimetric form that matches the
sign:

\[
\int_0^\infty \frac{n_E(r)}{r^2}\,dr
\;\ge\;
c\,|E|
\qquad\text{and grows with }m\text{ at fixed }|E|.
\]

The interval realises the minimum of
that integral among E of a given
measure sitting near the origin
(desert). Extra components add a
positive term. This is the 1-d
isoperimetric inequality for the
Beurling–Malliavin density of a hole
set, not for logarithmic capacity.

## What this does *not* prove

An isoperimetric inequality for BM or
for cap is not yet c_L ≥ e^{−C dim}.
It names the functional whose
minimiser is the desert and whose
value grows when gaps appear — the
functional Lemma 2 has to bound.
λ_max is the functional with the
wrong minimiser (it likes dust).

## Next analytic target

BM isoperimetric on a finite union of
intervals:

\[
\int\frac{n_E(r)}{r^2}\,dr
\;=\;
\sum_j \log\Bigl(1+\frac{|I_j|}{\mathrm{dist}(I_j,0)}\Bigr)
\;+\;O(1).
\]

The right-hand side is one-set, has
the desert as leading log(1+γ₁), and
adds a log per extra gap. If c_L is
comparable to exp(−C · that), Lemma 2
is the comparison of Q's Rayleigh
quotient to this integral. That
comparison is still open.
