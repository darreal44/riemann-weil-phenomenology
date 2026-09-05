# Computational methods in this repo

## 1. Zeros — PARI `lfunzeros`

`lfunzeros(L, T)` on the critical line of L, realprecision 19.
We keep t>10^{-12} (drops the central zero of rank ≥1
curves, e.g. 37a1). One-sided Weyl check:
Dirichlet ~ (T/π)log(qT/2π), GL2 extra −T/π.
`--all 320` without `--tmax` is parsed as a *name*. Always
`--tmax`.

Known failure: `lfunsympow(mfDelta())` returned ζ
(n=150, γ1=14.135). Constructor must be checked by γ1.

## 2. Gram — hats at the zeros

    hat_n(γ) = ∫_{-L/2}^{L/2} η_n(x) e^{iγx} dx

closed form sin(γL/2) / (γ²−ω_n²). G = 2 ΦᵀΦ, Φ rows =
hats. numpy eigh. INDEF when γ1 is large and the band is
thin (ζ, Δ, χ₅ at large μ). Then switch to prime-side Q.

## 3. Q — `scan_s` / `scan_q_*`

Same cosine window. Archimedean = sum of Γ_R panels
s0=1/4+μ/2. Primes = a_n log p / n^{k/2} on prime powers
n≤μ. mpmath dps 40–50, Gauss–Legendre panels.

Do not copy a character table. 11a1 A11 had a16=+4
(true −4) and flipped the sign of Q. Hecke from a_p, or
gp `ellan` with a printed cap.

## 4. What we do not compute

- Γ′/Γ(k/2+it) from scratch (we copy Dirichlet CST).
- Infinite-volume operators, Lyapunov, MPS.
- T_p on the window (not defined).
- Two-sided Weyl (root number 1 lists are one-sided).

## 5. Order of a new L

1. Harvest T=80, read n and γ1.
2. If γ1 equals 14.135, abort (ζ contamination).
3. T=320 with `--tmax`.
4. Gram μ=22 then 38. If INDEF, stop or write Q with
   the right (k,μ) panels — do not scan μ first.
