# Beurling density of the zeros

PW_τ = { f entire, |f(z)| ≤ C e^{τ|Im z|}, f|ℝ ∈ L² }.
Nyquist density for PW_τ is τ/π (radians). A discrete
set Λ ⊂ ℝ is a *sampling set* if

    A ||f||² ≤ ∑_{λ∈Λ} |f(λ)|² ≤ B ||f||²    ∀ f ∈ PW_τ.

Beurling: if the lower uniform density

    D⁻(Λ) = lim_{r→∞} inf_x  #(Λ ∩ [x,x+r]) / r

satisfies D⁻(Λ) > τ/π, then Λ is sampling (and if
D⁻ < τ/π it is not). Equality is delicate (Beurling–
Malliavin radius).

## Zeros of L-functions

Weyl: n(T) ∼ (T/π) log(q T / 2π)  (GL1).
Local density around height T is (1/π) log T, which
→ ∞. For a *fixed* window of bandwidth τ = L/2 =
(1/2) log μ, Nyquist is τ/π = L/(2π).

At height T the zeros are much denser than Nyquist
as soon as log T > L/2. That is the bulk. The desert
[0, γ1] has D⁻ = 0 on that interval: it is a hole of
length γ1, density zero *there*, not in the limit r→∞.

Beurling’s D⁻ is a limit at infinity. It does not see
a compact hole. That is why Lemma 2 splits: Slepian
on the hole, Beurling only on Iᶜ after the first zero.

## What we can say on Iᶜ

On a compact segment [γ1, ω_max] the number of zeros
we actually have is n. The empirical density is
n / (ω_max − γ1). Sampling in the finite-dimensional
cosine window of size N is a matrix question (the
Gram), not D⁻.

Measured (μ=22, ω_max≈73):

| L | n in band | n / 73 | Nyquist L/(2π) |
|---|-----------|--------|----------------|
| 11a1 | 71 | 0.97 | 0.49 |
| χ₂₉ | 63 | 0.86 | 0.49 |
| Δ⊗χ₅ | 84 | 1.15 | 0.49 |
| maass3 (T=115 only) | 34 | 0.47 | 0.49 |

11a1, χ₂₉, Δ⊗χ₅ sit above Nyquist in the window.
maass3 Table 1 is *at* Nyquist — that is the rank
drop at N=37, not a Beurling failure at infinity.

## Limit of the language

D⁻(zeros of ζ) = ∞. So ζ is a sampling set for every
PW_τ. That does not make Q positive and does not bound
ell. The one-set cost is the compact hole, handled by
Slepian, not by D⁻.

Beurling–Malliavin would be the tool if we wanted the
*exact* radius of a sampling set with a slowly drifting
density. We do not need that radius to write ell ≤ π τ |I|
on one interval plus a sampling constant A on Iᶜ.
