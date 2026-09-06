# Lemma 2 and the 2-plane

Two objects share a name in the
repo. They are not the same
lemma. The 2-plane is the
computable core of one of them.

## Two statements

**Lemma 2 (one-set, `one-set-lemmas.md`).**
A multiplier B_E of small type
that vanishes on ∂E, so that
F = B G on the subspace V of
functions vanishing on ∂E, and
a bound Q(F) ≥ c ‖G‖². Open:
the constant.

**Lemma 2 (window, `lemma2-STATUS.md`).**
On a resolved window,

    λ₀(Q) = λ_min(H − C T⁻¹ Cᵀ)
          = (1+O(10⁻¹)) σ_min²(Eval_±),

    −ln|ψ(0)| = ℓ/2 + O(1).

H is Q on a 2-plane inside the
first three hats. C T⁻¹ Cᵀ is
the Schur tail of hats n≥3.
The edge law is measured
(0.82–0.98). The lower bound
on λ_min(Δ) is the hole.

The 2-plane is how the second
statement begins.

## The plane

Hats φₙ on [0, L], L=log µ.
ψ(0) = f(0) ∝ v₀ + √2 Σ vₙ.
Inside span{φ₀,φ₁,φ₂},

    ker ψ(0) = span{e₁, e₂},

    e₁ = (√2, −1, 0)/√3,
    e₂ = (−√2, −2, 3)/√15.

e₁ is the raised cosine
√(8/L) sin²(π y/L), zero at
0 and L. Independent of χ and µ.

    H_{ij} = ⟨Q eᵢ, eⱼ⟩ = Arch − Primes.

On three hats, λ_min(H) sits
1.4–2.4× above λ_min(Q|_{3}).
The factor 10⁶–10¹⁴ in the
STATUS file is λ_max(3×3) / λ₀,
not H versus Q|_{3}.

## When the plane is the ansatz

From `N_eff-impact.md`:

    N_eff ≤ 2.2 and |⟨e₁,v₀⟩| ≥ 0.95
        →  v₀ ∈ span{e₁,e₂} to a few %
           Lemma 2 (window) applies
           as a 2×2 plus a Schur tail

    N_eff ≥ 2.9
        →  mass on hats 0–2 is still
           0.95, but Ritz of the plane
           is ℓ=20 against ℓ=111
           (χ₃ µ=80). The 2-plane is
           the sketch of v₀, not a
           variational certificate.

χ₅ µ=16 is the model case
(N_eff=2.14, overlap 0.97,
mass 1.000). χ₃ µ=80 is the
counter-model (N_eff=3.00,
overlap 0.83, H=T and C=−2H
across every cut).

χ₂₉ µ=16 has N_eff=1.92 but
overlap 0.46: two hats, not
e₁. H’s ground state is near
e₂. The plane is right, the
first basis vector is not.

## What is proved on the plane

- The frame {e₁,e₂} and f₁, f₂
  in closed form.
- H = A − P, A the 10-term
  Laplace series, P nine or so
  prime-power samples of Θ.
- λ_min(H) ≥ det H / tr H, equal
  to 10⁻³ on four characters.
- Weyl and Gershgorin miss the
  sign; the content is
  det(A−P)>0 on three residuals
  of size 10⁻⁴–10⁻³
  (χ₅: margin 30 %).
- Primes 2 and 3 dominate P.

## What is not

- det(A−P)>0 by hand.
- The Schur factor T⁻¹ that
  takes λ_min(H)~10⁻⁶ down to
  λ₀~10⁻¹⁵ on χ₅, or 10⁻⁴⁹
  on χ₃ µ=80. That factor is
  the identity H_block = T_block
  with C=−2H (`v0-tail.md`),
  not a small perturbation.
- Transfer of the 2×2 to a
  window with D_max ≫ N_eff
  (χ₃ µ=80: 14 versus 3).

A proof of Lemma 2 that stops
at H>0 proves positivity of a
different operator — the one
whose depth is 13 nats on χ₅,
not 33, and 20 nats on χ₃ µ=80,
not 111.
