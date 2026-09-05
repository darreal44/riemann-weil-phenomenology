# Duffin–Schaeffer, as it applies here

## The theorem

Let τ>0 and let Λ ⊂ R be separated. If the gaps of Λ satisfy
λ_{n+1}−λ_n ≤ π/τ (= ν when τ=L/2 and ν=2π/L), then Λ is a
sampling set for PW_τ: there is A>0 with

    Σ_{λ∈Λ} |F(λ)|²  ≥  A ||F||_{L²(R)}²
    for all F ∈ PW_τ.

The constant A depends on the gap bound and on a separation
δ=inf(λ_{n+1}−λ_n)>0. If the gaps reach exactly Nyquist and
δ=0 (accumulation), the statement fails. A uniform δ>0 gives
A ≳ δ² times a power of τ, not an exponential in the length
of a hole.

## Where it applies

S = R_+ \ E_L, represented by the zeros that bound short gaps
(Δ≤ν). By construction those gaps are ≤ ν = π/τ. If in addition
min short gap ≥ δ>0 — true on each finite list, δ≈0.10 on χ₂₉ —
Duffin–Schaeffer gives a sampling inequality on that finite
piece of Γ ∩ S. This is the “short holes sample” of
`short-holes.md`. It yields c_L ≥ A_δ > 0 *inside a model
where only S is seen*.

## Where it was broken

`lemma2-proof.md` / `sampling-floor` §4: apply DS on each
*short* gap separately and Bernstein (|F'|≤τ||F||) to control
the integral over a *long* gap. The bracket
1−λ_0(desert) − C(τ Δ_short)² is negative of order e^{-Lγ₁}.
The constant A of DS on a short interval is not large enough
to beat the Slepian leak of the neighbouring desert. DS does
not see E as a set; it only sees a gap bound.

## What it does not give

An exponential A ≥ exp(−C τ |E|). DS constants are polynomial
in the gaps, exponential only if one lets δ→0. Our charged
pair has δ∼0.4 ν, not a collapsing gap. The depth ell ∼ 5–80
is not a DS constant.

## Status

On S, DS is the reason Γ still samples once E is removed.
On E ∪ S together, DS + Bernstein is the route already closed.
The theorem is used as a sampling statement on short holes,
not as a formula for C(χ).
