# Weil's criterion and the windowed obstruction

The Clay / Riemann statement, in full:

> If ζ(s) = 0 and s is not a negative even integer, then Re(s) = 1/2.

This note records the only equivalence this repository is entitled to
use, the only reduction that would cover the whole critical strip, and
the step that is missing. It does **not** prove the statement above.

## 1. Weil's theorem (global, known)

Let W be Weil's quadratic form on the class of admissible test
functions h on ℝ (even, Schwartz-class Fourier pair, the Bombieri–Weil
normalization of App. B of `quorum-theorem`). Then the following are
equivalent:

1. RH: every nontrivial zero lies on Re = 1/2.
2. W(h) ≥ 0 for every admissible h.

This is Weil 1952. No window, no finite Euler product, no height
cutoff. The class of h is infinite-dimensional and not supported in a
fixed compact.

A proof of RH in this language is a proof of (2) with no extra
hypothesis.

## 2. The windowed form Q_L (this repository)

Fix L = log μ > 0. Let W_L be even functions supported in [−L/2, L/2]
(equivalently the cosine hats on [0, L]). The truncated pairing Q_L is
W restricted to W_L, assembled from the pole, the archimedean term,
and the prime towers n ≤ μ. Unconditionally

    Q_L(f) = ∑_ρ ĝ_f(ρ)

over all nontrivial zeros. On the line, ĝ_f(1/2 + iγ) = F(γ)². Off the
line the term is not a real square (`sampling-debranges-route`,
`visibility-offline`).

### What is proved here

- At μ = 11, on V_47, the *complete* Euler product is positive definite
  by ball arithmetic (`positivite_certifiee.py`). Finite L, finite
  dimension.
- Every proper sub-product on that same window admits a negative
  witness (quorum theorem). Finite L.
- Under RH, Q_L equals the Gram of the hats at the zeros and
  c_L = inf Q_L / ‖f‖² > 0 by Beurling (`sampling-floor`, Theorem 1).
  The hypothesis is RH.
- An off-line zero at height γ becomes visible to Q_L once L is large
  enough that PW_{L/2} can peak there (`visibility-offline`: the App. B
  term opens at −σ² on the ground state). Schematic, not a bound
  uniform in γ.

### What is not proved here

- |Q − Gram| < λ_min(Gram) on any window. That bound, even on one
  window, would exclude off-line zeros *visible to that window*. It is
  not in the repository (`FREEZE.md`). It would still leave zeros at
  heights the window does not resolve.
- Q_L ≥ 0 for every L. Positivity at μ = 11 is compatible with an
  off-line zero at height 10⁶
  (`sampling-debranges-route`: “A single certified window does not
  force RH”).
- W(h) ≥ 0 on the full Weil class.

## 3. The only covering of the strip

Visibility: an off-line zero ρ = 1/2 + σ + iγ with σ ≠ 0 makes Q_L
negative for all sufficiently large L (type τ = L/2 must exceed a
constant times |σ| + 1, and γ must lie in the spectral band the
window can see). Therefore:

    (∀ L > 0)(Q_L ≥ 0)  ⇒  there is no off-line zero at any height.

That implication is the covering step. It is a reduction, not a proof:
the hypothesis (∀ L) Q_L ≥ 0 is exactly the restriction of Weil
positivity to compactly supported test functions, which is again RH
(`sampling-debranges-route`, remark after §2).

There is no further reduction in this repository that turns
(∀ L) Q_L ≥ 0 into a finite check. Certificates at μ = 11, 16, 22,
scans to μ = 80, zero lists to T = 320, and |G/Q − 1| ~ 10 % on χ₂₉
are all finite. A compact height interval, or a density-T remainder,
does not cover the strip.

## 4. Where a proof would have to start

An unconditional argument for RH via this route must produce one of:

- A. W(h) ≥ 0 for all admissible h, by an estimate that does not
  truncate the Euler product or the test class.
- B. Q_L ≥ 0 for all L, by a uniform (in L) bound, not a certificate
  per window. Annexe H records this as open: “Point 1 … 
  unconditionally NOT PROVED.”
- C. |Q_L − Gram_L| < λ_min(Gram_L) with Gram built from *all* zeros
  (not a harvest to finite T), for a sequence of L → ∞ that eventually
  sees every height. The identity Q = Gram still uses the zeros; the
  inequality would have to be proved without assuming they lie on the
  line. The repository does not have this inequality even at one L
  against a complete Gram.

None of A–C is available. Li's criterion, the Weil–Guinand explicit
formula at infinite support, and Beurling sampling without RH, are
outside what is proved here; they are not supplied by the scans.

## 5. Conclusion

The Clay / Riemann statement is the intended theorem of this note.
The only global equivalence used is Weil's theorem (W ≥ 0 ⇔ RH).
The only covering of infinitely many zeros is the implication
(∀ L) Q_L ≥ 0 ⇒ no off-line zero. The hypothesis of that implication
is not proved. Finite-window certificates and finite-T harvests do
not substitute for it.

**This note does not prove RH.** It locates the missing lemma
(unconditional positivity of Q_L for every L, or of W on the full
class) and records that the repository's phenomenology does not
cross it. `README.md` Main results and `report/FREEZE.md` already
state the same: none of it bears on RH; the repo is not a proof of RH.
