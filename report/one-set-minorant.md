# One-set bound: what is proved, what is not

Claim in the project: ell ≤ C τ |E|, E = desert ∪ sub-Nyquist
gaps, τ = bandwidth of the window (here τ = L/2, L = log μ).

## 1. Landau–Widom is the wrong operator

LW describes the eigenvalues of K = χ_E P_τ χ_E on L²(E):

    # { λ_j(K) ≥ 1−δ } = (τ|E|)/π + (1/π²) log(τ|E|) + O(1).

That is a *count* in the plunge of a time-frequency restriction.
ell is −log λ_min of a different matrix: the Gram of hats
at the zeros, or Q on the cosine window. LW does not name
that matrix. Citing LW does not prove the claim.

## 2. Lemma (Gram, one interval, Slepian)

Let P_τ be the projection onto PW_τ. Let I ⊂ ℝ be one
interval (the desert). For f ∈ PW_τ,

    ||χ_I f||² ≤ λ₊(I,τ) ||f||²,

with λ₊ = λ_max(χ_I P_τ χ_I) = 1 − exp(−π τ |I| + o(τ|I|))
(Slepian, one dimension, one piece). Hence

    ||f||_{Iᶜ}² ≥ exp(−π τ |I| + o()) ||f||².

If the zeros in Iᶜ form a *stable sampling set* for PW_τ
restricted to Iᶜ — Beurling density > Nyquist, uniform
gap — then

    ∑_γ |hat f(γ)|² ≥ A ||f||_{Iᶜ}² ≥ A exp(−π τ |I|) ||f||².

The Gram G of the hats therefore satisfies
λ_min(G) ≥ A exp(−π τ |I|), so

    ell = −log λ_min(G) ≤ π τ |I| + log(1/A) + o(τ|I|).

That is ell ≤ C τ |E| with C = π, E = I, **once sampling
on Iᶜ is granted**. A is the sampling constant of the
zero set in Iᶜ; it does not come from LW.

## 3. What is missing for a theorem

(i) Iᶜ is not an interval. E is a desert plus many short
    gaps. Slepian for a union is LW: λ₊(E,τ) = 1 −
    exp(−π τ |E| + (K−1) log + …) only after the number
    of pieces K is controlled. We do not control K
    unconditionally.

(ii) Sampling on Iᶜ. Under RH the zeros in Iᶜ have density
    ~ (1/π) log t and Beurling applies on compact windows.
    Unconditionally a large hole in Iᶜ would destroy A.
    That hole is exactly a zero off the line — the
    contrapositive of Weil, not a proof of RH.

(iii) Q ≠ Gram. Q = arch − primes + (implicitly) zeros.
    The prime sum can push λ_min down. The bound on the
    Gram does not pass to Q without a comparison
    |Q(f) − ∑ |hat f(γ)|²| ≤ ε||f||², which we do not have
    uniformly on the window.

## 4. Status

- Gram + one desert + sampling on the complement:
  Lemma 2, C = π, proved as a Slepian estimate.
- Union of gaps, number of pieces, Q, no RH:
  **not proved**. LW is the count, not that estimate.

Numerics (ell / (τ|E|) ≲ 0.42 on Dirichlet Q) sit below
π, which is consistent with Lemma 2 and does not close
(iii).
