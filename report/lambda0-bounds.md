# Bounds on λ0

Lemma 2 (Gram, one desert I, sampling on Iᶜ):

    λ0 ≥ A exp(−π τ |I|),
    ell = −log λ0 ≤ π τ |I| + log(1/A).

τ = L/2 = (1/2) log μ, |I| ≈ γ1.

## Upper bound on ell (the only proved direction)

| object | μ | τ | γ1 | π τ γ1 | ell meas. | ratio |
|--------|---|---|----|--------|-----------|-------|
| 11a1 | 22 | 1.55 | 6.36 | 30.9 | 22.7 | 0.73 |
| 11a1 | 38 | 1.82 | 6.36 | 36.4 | 33.0 | 0.91 |
| Δ⊗χ₄ | 22 | 1.55 | 2.30 | 11.2 | 4.76 | 0.43 |
| Δ⊗χ₄ | 38 | 1.82 | 2.30 | 13.1 | 10.6 | 0.81 |
| Sym² E₁₁ | 22 | 1.55 | 3.90 | 19.0 | 6.87 | 0.36 |
| Sym² E₁₁ | 38 | 1.82 | 3.90 | 22.3 | 9.57 | 0.43 |
| maass3 | 8 | 1.04 | 2.90 | 9.5 | 30.8 | 3.2 |

Ratio < 1 : measured ell sits *below* the Slepian
ceiling, as it must if A is not tiny. maass3 μ=8
overshoots (ratio 3) — the window is too small and
the list too short; Lemma 2 does not apply (sampling
on Iᶜ is not granted at N=25, T=115).

## Lower bound on λ0

Equivalent: λ0 ≥ e^{−C τ γ1} with C=π if A=1.
Measured λ0 is larger than that floor for the
rows with ratio < 1 (Gram is not as small as the
pure Slepian prediction). A < 1 raises the ceiling
on ell and lowers the floor on λ0; we do not
measure A separately.

## What is not a bound

λ0 of Q (scan_s) is a different number. The table
is Gram only. Q for χ can have λ0 ~ 10^{-6} at
μ=38 with a smaller γ1; that still fits a C < π
but is not the lemma.

No matching *lower* bound ell ≥ c τ γ1 is proved.
The numerics suggest c ≈ 0.3–0.9 depending on μ.
