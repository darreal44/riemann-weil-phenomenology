# Exact 2-adic shell masses and the semi-local sub-shells

The Fmat grid of `weights_2adic.py` is not a local integral: its
mass at λ=2 walks through 0.49 toward ~1.4 as h↓0
(`report/campaign_2adic_large.jsonl`). This note records the
*exact* pairing of Connes (1999) Theorem 4 on shells, and the
construction of the semi-local Fourier as a sum of those shells.
No RH. No finer grid.

## 1. Haar and |1−u|_2

Normalize ∫_{Z₂*} d*u = 1. Each shell 2^n Z₂* has measure 1
(`report/dstar-identification.md`). n = ord₂(u), |u|_2 = 2^{−n}.

    |1−u|_2 = 1           if n > 0   (|u|_2 < 1)
            = |u|_2 = 2^{−n}  if n < 0   (|u|_2 > 1)
            ≤ 1/2         if n = 0   (units 1+2Z₂; not a Dirac at 2^{±1})

**Lemma (raw weights).** meas(shell)/|1−u|_2 equals 1/2 on n=−1
(λ=2) and 1 on n=+1 (λ=1/2), and 0 on units.

*Proof.* n=−1: |1−u|_2 = 2, 1/2. n=+1: |1−u|_2 = 1, 1/1. □

Shipped: `tau2_local.raw_weight`.

## 2. Three numbers that look like “the mass”

The operator ϑ(λ)g(r) = λ^{−1/2} g(r/λ) already contains a twist.
The archimedean calibration τ_∞ = λ^{1/2}/2 · (1/(1+λ)+1/|1−λ|)
contains √λ. The 2-adic partner in *that* calibration multiplies
the raw weight by √λ.

**Lemma (module twist).** With λ = |u|_2, the twisted masses at
n=±1 are both 1/√2.

    n=−1:  (1/2)·√2 = 1/√2
    n=+1:  1 · √(1/2) = 1/√2

**Lemma (inverse twist).** Theorem 4 writes h(u^{−1}). If the
slice coordinate is λ = |u^{−1}|_2, the peak at λ=2 is the shell
n=+1 and the twisted mass is 1·√2 = √2.

**Lemma (Lebesgue Jacobian).** d*λ = dλ/λ, so
δ(λ−2) dλ = 2 δ_{λ=2} d*λ. Reading the module-twist Dirac as a
Lebesgue density at λ=2 produces (1/√2)×2 = √2, the same number
as the inverse twist, for a different reason.

**Lemma (Bombieri).** (log 2)/√2 is 1/√2 read against
dλ/(λ log 2) = d log₂ λ, or the Weil–Bombieri local factor.
It is not a third local integral.

Shipped: `mass_at_two("module")` = 1/√2,
`mass_at_two("inverse")` = √2,
`lebesgue_jacobian_at_two()` = √2,
`bombieri()` = (log 2)/√2.

The Fmat integral ∫ (τ_S−τ_A) dλ/λ is a pairing against a *window*
of width ~Λ^{−2}, not against a Dirac. That is why it walks
through 0.49 toward ~1.4 (`prereg-2adic-mass.md`). Closing the
grid is not how the mass is computed.

## 3. Sub-shells: the semi-local Fourier

On the ord₂=0 slice, functions invariant under Z₂* are determined
by g on [0,∞), and Connes (1999, §VII) gives

    Fg(ρ) = ½ [ ∑_{n≥0} ĝ(2^n ρ) − ĝ(ρ/2) ].

**Lemma (construction).** Fg = ∑_{n≥0} F^{(n)} g + F^{inv} g with

    F^{(n)} g = ½ ĝ(2^n ·)     (n ≥ 0)
    F^{inv} g = −½ ĝ(·/2)      (the n=−1 shell)

Each F^{(n)} is one 2-adic unit sub-shell (lacunary dilation).
Unitarity of F is Proposition 1 of `notes/semilocal-step.tex`
(dyadic Plancherel). The matrix discretization of the same
splitting is `code/subshell_op.py`.

Shipped: `subshells.F_from_shells`, `shell_term`. Judge: the sum
of shells equals F, and F equals `semilocal.F_cell`.

The first semi-local step (log 2, log 3] still cannot be taken by
transporting CC’s Λ=1 Sonin remainder: that remainder changes
sign (`notes/semilocal-step.pdf`). The sub-shells are the
*construction* of F, not a substitute positivity. The other
mechanism is the 1999 finite part (`notes/log2-log3-step.md`):
subtract 2h(1)log'Λ first; it vanishes at Λ=1. The Paley–Wiener
step is not taken.

## 4. Status

| Claim | Status |
|---|---|
| raw weights 1/2 and 1 on n=±1 | theorem |
| module twist ⇒ mass(λ=2) = 1/√2 | theorem, this convention |
| inverse twist ⇒ mass(λ=2) = √2 | theorem, Thm 4’s h(u^{−1}) |
| Lebesgue Jacobian ⇒ √2 from 1/√2 | theorem |
| Bombieri (log 2)/√2 | different Haar, not a third integral |
| F = ∑ sub-shells | theorem / identity |
| Fmat integral = one of those Diracs | false (unresolved peak) |
| (log 2, log 3] by CC remainder | negative, measured |
| (log 2, log 3] by 1999 finite part | named, not taken (`log2-log3-step`) |
| (∀ L) Q_L ≥ 0 | RH; not this note |
