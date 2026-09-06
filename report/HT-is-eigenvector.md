# H = T is the eigenvector equation

Cut v₀ = h ⊕ t. Write

    H = hᵀ Q_{HH} h,     T = tᵀ Q_{TT} t,
    C = 2 hᵀ Q_{HT} t.

If Q v₀ = λ v₀ then the two blocks
read

    Q_{HH} h + Q_{HT} t = λ h,
    Q_{TH} h + Q_{TT} t = λ t.

Multiply by hᵀ and tᵀ:

    H + C/2 = λ ‖h‖²,
    T + C/2 = λ ‖t‖².

On every window we have measured,
λ is 10⁴–10⁴⁴ below H. Hence

    C = −2H + O(λ),     T = H + O(λ),

which is the identity recorded in
`v0-tail.md`. It holds at every
cut because it does not use the
cut: it uses Qv=λv and λ≈0.

(√H − √T)² = λ is the same
statement under H=T>0, up to
the phase that makes C negative.

## What this is not

It is not an arithmetic matching
of Arch and primes across a
wall of hats. Any near-null
vector of any SPD matrix, split
anywhere, gives H≈T≈−C/2.

The content is the existence of
that near-null vector — Weil on
the window — not the split.

## What remains of Lemma 2

- On N_eff ≤ 2.2: produce
  λ_min(H|_{e₁e₂}) > 0 by hand
  (det(A−P)>0 on three residuals).
  The Schur that follows is
  “there exists a tail making
  Qv≈0”, which is λ₀ itself.
- On N_eff ≈ 3: the 2-plane
  Rayleigh is not small. H=T
  still holds for the *true* v₀
  and says nothing about e₁.

A proof cannot treat the Schur
as a small perturbation of H.
It is the rest of the kernel
vector. Bounding λ_min(H) bounds
the head energy, not λ₀.
