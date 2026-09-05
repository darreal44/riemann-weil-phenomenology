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

**The harvester itself is right; only its counter was two-sided.** `harvest_weyl.py` uses the
completed L, Λ(s,χ) = (q/π)^{(s+a)/2} Γ((s+a)/2) L(s,χ), whose root number is 1 for every real
primitive χ (Gauss: τ(χ) = √q or i√q), so Λ(½+it) is real on the line (|Im Λ| ≤ 10⁻¹⁶ on a grid)
and its sign changes are exactly the zeros: 11 on (0, 30] for χ₅, the 11 of the cache to 0.02.
(Sign changes of the *uncompleted* Re L would double count — 11 on [6, 20] against 6 zeros —
but that is not what the script does.) Its `expected_N` was the two-sided formula, so it printed
"Weyl = 0.50" on complete harvests; corrected to the one-sided count in this commit. Lists
produced by the script before the fix are complete; only their printed ratio was halved.

**Consequences.** §77–79 stand (complete caches for 14 characters). The predictions of
`prereg-chi29.md` (37 zeros to 52.9) and of the χ₁₇ run (23 zeros) use *short* caches:
γ*(22) = 138, so their gap sums are truncated and biased low by ~10–15% (§77); their ratios
0.89 and 0.71 are consistent with the law within that bias and the transient-low measurements
of narrow deserts (§78–79), not tests against it. Guarded by `tests/test_weyl_onesided.py` (one-sided count = cache = 11 on (0,30]; Λ real and its sign changes = the zeros).
