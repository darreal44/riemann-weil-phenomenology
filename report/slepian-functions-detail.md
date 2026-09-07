# Slepian functions in this problem — detailed map

## 1. What they are

On L²(I), I a finite union of intervals, the
Slepian (prolate) operator is

    (K f)(t) = ∫_I [sin(τ(t−s))/(π(t−s))] f(s) ds.

Eigenvalues 1 ≥ λ₀ ≥ λ₁ ≥ ⋯ ≥ 0. λ_k is the
energy of the k-th prolate that stays inside
the Paley–Wiener band [−τ,τ] after restriction
to I. Time-bandwidth: c = τ|I|.

In our window: τ = L/2 = (log μ)/2, hats live
in PW_τ on the y-line, I is a set of gaps on
the t-line (zeros).

## 2. Spectrum, χ₂₉ μ=11 (Nyström 240)

Nyquist cell 2π/L = 2.62.

| I | |I| | c=τ|I| | λ₀ | λ₁ | λ₂ | −log(1−λ₀) |
|---|---|---|---|---|---|---|
| desert [0,γ₁] | 1.79 | 2.15 | 0.608 | 0.078 | 0.002 | 0.94 |
| hole (γ₁,γ₂) | 3.52 | 4.22 | 0.900 | 0.401 | 0.047 | 2.30 |
| Nyquist cell | 2.62 | 3.14 | 0.785 | 0.207 | 0.012 | 1.54 |
| early [0,γ₃] | 6.76 | 8.10 | 0.996 | 0.920 | 0.542 | 5.62 |

Only one eigenvalue above 1/2 on the desert
and on the true hole. This is the *moderate-c*
regime. The large-c law

    1−λ₀ ∼ 4√(πc) e^{−2c}

or the even cruder 1−e^{−π τ|I|} (πc = 6.76
would give 1−λ₀ ∼ e^{−6.8}) is false here:
measured 1−λ₀ = 0.39, not 10⁻³.

## 3. What Slepian does give

A number for one interval:

    ell ≤ −log(1−λ₊(I,τ)) + log(1/A).

On the true hole at μ=11: −log(1−λ₊)=2.31,
ell_Gram=1.26, so the bound holds with A=1.
It dies at μ≳14 when K extra sub-Nyquist
gaps appear (K=5 at μ=18, 12 at μ=38):
ell outruns any single-interval λ₊.

Landau–Widom on a *union* adds pieces near
λ=1; it does not shrink λ₊ of the first
piece. Additive holes aL(desert)+bL∑(gap−Nyq)
are a local fit (a≈1.7–2.1, b≈0.82), not
the sampling constant of one set.

## 4. What Slepian does not give

- v₀. DPSS of length 25 overlaps v₀ at most
  0.39 (wrong space: n-index vs t-line).
  On [0,L], v₀ is φ₀+φ₁ (99 %), the cheapest
  edge jump, not the prolate of [0,γ₁].
- A test function for Q. Inserting the desert
  prolate into Q overshoots λ₀(Q) by 10⁶–10¹⁵
  on wide deserts (χ₅, χ₃). Q cancels on the
  later zeros; the Slepian does not.
- The prefactor A. Identity
  ell ≈ π² D_max + log(1/A) leaves an O(1)
  per Nyquist cell that is not derived.
- Transfer Gram → Q. That remains RH-shaped.

## 5. One-set object that is still missing

Beurling–Landau sampling constant of

    Λ_early = {γ_k : γ_k ≤ γ_*}

as a single non-uniform set for PW_{L/2}.
Desert then sub-Nyquist stretch, not a sum
of Slepian holes. That is the analytic step
still open in `notes/desert-slepian.tex`.
It is not RH.
