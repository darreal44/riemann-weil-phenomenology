# Lemma 2 — status

## Stable facts

1. **Edge.** −2 ln|ψ(0)| / ell ∈ [0.82, 0.98]
   (`lemma2-edge-psi0.md`).

2. **RH.** 2∑ |F(γ)|² / λ₀ = 0.91–0.93
   on Q's vector (`lemma2-RH-tail.md`).
   Two-sided Eval: 0.85–0.93
   (`lemma2-RH-eval.md`). Leftover
   = T>320 + Γ.

3. **3 hats.** Mass of the ground
   state on n=0,1,2 is 0.99998.
   Shape (+,−,+) in ker ψ(0)
   (`lemma2-three-hats.md`).
   λ₀ = λ_min(H − C T⁻¹ Cᵀ)
   to 0.4 % (`lemma2-schur-3.md`).

4. **H|ker = Arch − Primes.**
   Two O(1) terms. On a wide
   desert they agree to 6–8
   digits; that agreement is
   λ_min(H) (`lemma2-H-arch-primes.md`).
   Primes 2 and 3 carry P
   (`lemma2-primes-on-ker.md`).
   The Schur then subtracts
   another 10⁴–10¹⁴
   (`lemma2-H-on-ker.md`).

5. **Not** the desert Slepian
   (10⁶–10¹⁵ too big), not
   PW_τ Beurling (Gram O(1)),
   not a universal C₀
   (`lemma2-slepian-testfn.md`,
   `lemma2-cartwright-gram.md`,
   `lemma2-ell-robust.md`).

## What Lemma 2 is

    λ₀(Q) = λ_min( H − C T⁻¹ Cᵀ )
          = (1+O(10⁻¹)) σ_min²(Eval_±)

and

    −ln|ψ(0)| = ell/2 + O(1).

To prove: a lower bound on
λ_min(Δ) or on |Arch(k)−Primes(k)|
after the Schur, of the shape
exp(−C₀ τγ₁ − C₁).

## What a hand proof can reach

- 3-hat |A−P| without zeros:
  truncated Weil on one test
  function. Gives λ_min(H),
  which is 10⁶–10¹⁴ above λ₀
  on χ₅/χ₃, ~40× on χ₁₃.
- The Schur factor has no
  comparison function yet.

## Files (25)

edge, RH-eval, RH-tail,
three-hats, schur-3, H-on-ker,
H-arch-primes, primes-on-ker,
F-at-zeros, eval-svd,
slepian-testfn, cartwright-gram,
finite-interpolant, ell-fit,
ell-robust, Q-vs-det,
logdet-split, psi0-predictors,
sampling-constant, isoperimetric,
spectral-tail, three-tests,
filled, proof, STATUS.
