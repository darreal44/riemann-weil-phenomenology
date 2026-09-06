# Lemma 2 — status

## What is stable

1. **Edge.** −2 ln|ψ(0)| / ell ∈ [0.82, 0.98]
   (`lemma2-edge-psi0.md`). λ₀ lives
   at the endpoint of the window.

2. **RH identification.** Two-sided
   Eval of the hats at ±γ gives
   σ_min² / λ₀ = 0.85–0.93
   (`lemma2-RH-eval.md`). On Q's
   own vector, 2∑ |F(γ)|² / λ₀ =
   0.91–0.93 (`lemma2-RH-tail.md`).
   The 7–9 % is T>320 + Γ.

3. **Not the desert Slepian.**
   That test function is 10⁶–10¹⁵
   above λ₀ (`lemma2-slepian-testfn.md`).
   F of the ground state vanishes
   on the first zeros and peaks
   past the last hat
   (`lemma2-F-at-zeros.md`).

4. **Not PW_τ Beurling.** The Gram
   of reproducing kernels on Λ_L
   has λ_min = O(1)
   (`lemma2-cartwright-gram.md`).
   Depth is σ_min of Eval on the
   *hat subspace*.

5. **Not a fitted C₀ τγ₁.**
   ell/(τγ₁) spans 2.3–6.3;
   jackknife moves a from 4.5 to
   6.5 (`lemma2-ell-robust.md`).
   log det of Slepian(E) tracks
   ell only on χ₅
   (`lemma2-Q-vs-det.md`).

6. **C = λ₀/ψ(0)²** sits in
   0.11–0.25. ∑ 2(1−cos(γL))/γ²
   is 0.12–0.61. Their ratio is
   not 1 (0.3–1.4). The endpoint
   model is the right *shape*,
   not a sharp prefactor.

## What Lemma 2 is

Under RH:

    λ₀(Q) = (1 + O(10⁻¹)) σ_min²(Eval_±).

The inequality to prove is

    σ_min(Eval : V_{N_B} → ℂ^{±Γ})
    ≥ exp(−C₀ τ γ₁ − C₁)

or the equivalent

    −ln|ψ(0)| ≤ C₀ τ γ₁ + C₁.

C₀ is of order one, not measured
as a universal number.

## What is not proved

A comparison function, written
by hand, whose Eval Rayleigh is
within a constant of λ₀. The
Slepian of [0,γ₁], the tent, the
finite Blaschke, Jensen, Landau–
Widom on E, all miss a factor
in the *exponent*. The object
that matches is Q's ground
state — circular as a proof.

## Files

`lemma2-proof.md`,
`lemma2-logdet-split.md`,
`lemma2-Q-vs-det.md`,
`lemma2-ell-fit.md`,
`lemma2-ell-robust.md`,
`lemma2-edge-psi0.md`,
`lemma2-psi0-predictors.md`,
`lemma2-slepian-testfn.md`,
`lemma2-F-at-zeros.md`,
`lemma2-finite-interpolant.md`,
`lemma2-cartwright-gram.md`,
`lemma2-eval-svd.md`,
`lemma2-RH-eval.md`,
`lemma2-RH-tail.md`.
