# Equivalents of RH, and what the judged calculations actually show

## 1. Li's criterion (theorem, not a calculation)

Let ξ(s) = ½ s(s−1)π^{−s/2}Γ(s/2)ζ(s). Li (1997): RH if and only if

    λ_n = ∑_ρ [1 − (1 − 1/ρ)^n]  ≥ 0    for every n = 1, 2, 3, …

the sum over nontrivial zeros of ξ, counted with multiplicity
(Lagarias form). The n=1 term has the closed value

    λ_1 = 1 + γ/2 − ½ log(4π) > 0.

`code/li_lambda.py` evaluates a *finite* prefix from a harvest of
zeros on the line plus a Weyl tail. Tests
(`tests/test_li_lambda.py`) drive that function: λ_1^closed matches
the formula, λ_n(zeros)>0 for n=1..8, and the raw zero-sum
undershoots λ_1 (the tail is missing). A positive prefix is
compatible with RH and with a first off-line zero far to the right
of the harvest. It is not a proof.

## 2. Weil's criterion (theorem)

W(h) ≥ 0 for every admissible h on ℝ  ⇔  RH.
Q_L is W restricted to even functions supported in [−L/2, L/2].
Positivity of one Q_L is not Weil's criterion
(`notes/rh-weil-criterion.md`, `sampling-debranges-route`).

The implication that *would* cover the strip is

    (∀ L > 0)(Q_L ≥ 0)  ⇒  no off-line zero at any height,

by visibility of an off-line term once the Paley–Wiener type sees
it. The hypothesis is not proved. That is the missing lemma, and
it is equivalent to RH.

## 3. The truncated Gram inequality is false, hence not a proof

A proposed finite-window stand-in was |Q − Gram_T| < λ_min(Gram_T),
Gram_T built from zeros with |γ| ≤ T. Under RH, Q = Gram_∞, so
the difference is the tail of high zeros, not off-line zeros.

On χ₂₉, μ=11, N=25, the shipped pair `scan_s.assemble` +
`compare_QG.gram` gives (`tests/test_compare_QG.py`):

    λ_min(Q) > 0,  λ_min(G) > 0,  λ_min(G)/λ_min(Q) ∈ (0.85, 1),

and ‖G − Q‖_F > λ_min(G). So even the Frobenius norm of the
discrepancy exceeds the ground-state eigenvalue. The inequality
|Q − Gram_T| < λ_min cannot hold for this truncated list. The
obstruction is the missing tail of *on-line* zeros, not evidence
about off-line zeros. This route is closed as a proof, in the
journal's sense: the proposed bound fails its own judge.

## 4. det(A − P) on the raised-cosine 2-plane

H = A − P is the 2×2 of Q on span{e₁, e₂}, A the archimedean
quadrature, P the finite prime-power samples of Θ, no zeros in
the formula (`H_2plane_independent.py`). Tests require det H > 0
and λ_min(H) > 0 on five characters at μ=16, and |P₁₁| ≳ 0.1 |A₁₁|
(the primes are not a rounding error; truncating P flips the sign,
`P-truncation-det.md`).

This is an identity of 2×2 matrices, not a proof that det(A−P)>0
by estimates. A hand bound would have to keep every n ≤ μ: 2 and 3
dominate the *size* of P, not the *sign* of the determinant.

## 5. Discrete Landau (already written)

`notes/discrete-landau.tex`: dim ker Eval_ω ≥ n(ω) − N_Γ(ω) for
arbitrary nodes. Mean rung 11 = π² + log(1/A)/D, not derived to
the digit.

## 6. What remains a demonstration, not a scan

- (∀ L) Q_L ≥ 0, or W(h) ≥ 0 on the full class: RH.
- det(A−P) > 0 by estimates that do not drop n > 8.
- The O(log c) matching of the Landau count for hats.
- Nyman–Beurling / Báez–Duarte: ‖χ − ∑ c_n φ_{θ_n}‖_{L²(0,1)} → 0
  ⇔ RH. A decaying residual up to N=30 is the same finite-prefix
  phenomenon as Li's λ_n. Not implemented here; not a proof either.
