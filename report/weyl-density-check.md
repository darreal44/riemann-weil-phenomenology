# Weyl density of the zero caches: a convention check (5 September 2026)

`cache-chi5-149.md` (Grok, 4 September) states that the χ₅ cache has *half* the Weyl density
("have / expected = 0.50 at every T") and concludes that the geometric-law matches on χ₅ are
matches against a thinned set. This note shows the factor 0.50 is a convention, not a hole.

**Two counting formulas.** For a primitive χ mod q, the zeros of L(s,χ) with |γ| ≤ T number
N(T) ≈ (T/π) log(qT/2πe) — *both signs of γ*. The caches store γ > 0 only; the expected count
on (0, T] is half: (T/2π) log(qT/2πe). At T = 149, q = 5: 89.6. The χ₅ cache has 89.

**Independent count.** |L(½+it, χ₅)|² scanned at step 0.02 on (0, 30] (Hurwitz representation,
dps 15, `kronecker.chi_tab(5,5)`): 11 minima below 10⁻², at 6.64, 9.84, 11.96, 16.04, 17.56,
19.54, 22.22, 24.58, 26.78, 28.46, 29.70. The cache has 11 zeros on (0, 30], agreeing to 0.01.
One-sided Weyl: 10.4. The harvest is complete.

**Why a sign-change harvester doubles.** On [6, 20], Re L(½+it, χ₅) changes sign 11 times and
Im L 11 times, while |L| has only the zeros of the list there. Without the root-number phase
(Λ(½+it) = ε^{1/2}·real), both Re L and Im L vanish between consecutive zeros as well: a
harvester by sign change of L, or of a "completed L" whose phase is not the root number, counts
about twice the zeros. Any `zeros_*_weyl.pkl` produced that way, and any test asserting
"have/expected → 1" against the two-sided formula, will pass on a doubled list.

**Consequences.** §77–79 stand (complete caches for 14 characters). The predictions of
`prereg-chi29.md` (37 zeros to 52.9) and of the χ₁₇ run (23 zeros) use *short* caches:
γ*(22) = 138, so their gap sums are truncated and biased low by ~10–15% (§77); their ratios
0.89 and 0.71 are consistent with the law within that bias and the transient-low measurements
of narrow deserts (§78–79), not tests against it. Guarded by `tests/test_weyl_onesided.py`.
