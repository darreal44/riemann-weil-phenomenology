# Remaining demonstrations (before any RH covering lemma)

Demonstrations that closed after this note: `notes/demonstrations.md`
(Courant, Schur sign, θ_{f₁}, edge split), `notes/av-gauss.md`
(Gauss of A(v)), and `notes/landau-depth.md` (kernel count, rungs
sum to ℓ₀, (16+5)/2=11). The covering lemma is not among them.

This note records what is proved, what is an identity of matrices,
what is measured with a shipped judge, and what is still open — on
the list that stands *before* the covering implication

    (∀ L > 0)(Q_L ≥ 0)  ⇒  no off-line zeros.

That implication is equivalent to RH (Weil 1952 + visibility of an
off-line term once the Paley–Wiener type sees it). It is not claimed
here, and nothing below is a substitute for it.

Judges live in `tests/`. A number enters a table only if a shipped
function reproduces it.

---

## 1. Discrete Landau: the inequality, the threshold, the plunge

**Proved (linear algebra, any nodes).** Let hats `{φ_n}_{0≤n≤N}` be
the cosine basis of type `2π n / L` on `[0, L]`, `L = log μ`. Let
`Eval_ω` send a coefficient vector to the samples of the corresponding
function at the zeros `γ_k < ω`. Then

    dim ker Eval_ω  ≥  n(ω) − N_Γ(ω),

where `n(ω) = 1 + #{n : 2π n / L < ω}` and `N_Γ(ω) = #{γ_k < ω}`.
The right-hand side, maximised over `ω`, is `D_max`. This is the
discrete Landau density lower bound (`code/dmax.py`,
`tests/test_depth_law.py`, `tests/test_landau_matching.py`).

**Not proved: equality of the well-count without a threshold.**
The Gram of in-band hats has `#{ℓ_k > 2} = round(D_max)` on the
windows we ran. The cut `ℓ > 2` sits in the Landau–Widom plunge
(eigenvalues of a time-frequency limiter between `δ` and `1−δ`,
width `O(log c)`, `c ∼ τ L ∼ N`). Removing the cut, the count
`#{ℓ_k > 1/2}` is strictly larger (`test_landau_matching` on
`χ₁₃` `μ=16`, float64). The `O(log c)` matching of that plunge
for the *hat* Gram — not for `χ_E P χ_E` — is the remaining
analytic step. It is not RH. (`ζ` `μ=11` needs mpmath:
`test_depth_law.py`.)

**The constant 11.** One-interval Slepian on a desert of length
`|I|` gives `−ln λ_min = π τ |I| + log(1/A) + o(1)`. Writing
`ℓ ≈ 11 D_max` as `π² + log(1/A)/D_max` is an identity of form:
`π² ≈ 9.87`, so the remainder is `O(1)` per Nyquist cell. The
prefactor `A` is not derived (`test_landau_matching`: rung on
`χ₈` `μ=16` is `π²` plus an `O(1)` remainder, not zero). No
universal `A` is claimed.

---

## 2. Edge lemma

**Statement.** Among unit-norm functions on `[0, L]` whose Fourier
transform vanishes on the in-band zeros (to the observed hyper-null
order), the minimal edge value should satisfy

    −ln |ψ(0)|_min  =  ℓ/2 + O(1),

equivalently `λ₀ ≍ ψ(0)² S` with `S` the leakage of an edge jump
onto the zeros beyond the band (`notes/the-well.tex` §5).

**Measured.** `ψ(0) = L^{−1/2}(v_0 + √2 ∑_{n≥1} v_n)`,
`edge = −2 ln|ψ(0)|`, `R = ℓ − edge`. On the scan of
`report/edge-value-scan.md`, `edge/ℓ ∈ [0.82, 0.98]` except a
precision glitch at `ζ:16`. A cheap judge
(`tests/test_edge_remainder.py`, `χ₁₃` `μ=16` `NB=12`) finds
`R = O(1)` and `edge/ℓ` in `(0.70, 1.15)`.

**Not a proof.** The extremal problem is harmonic analysis (linear
constraints on a window). The jump heuristic
`∑_{γ_k > ω_max} 8 ψ(0)² sin²(γ_k L/2)/γ_k²` matches `λ₀` to a
factor `∼1.5` on `ζ` at `μ=11`. That is evidence, not an estimate
with an `O(1)` remainder derived from first principles.

---

## 3. det(A − P) > 0 by estimates

On the raised-cosine 2-plane `{e₁, e₂} ⊂ span{φ₀, φ₁, φ₂}`,

    H = A − P,     P_{ij} = ∑_{n≤μ} χ(n) Λ(n) n^{−1/2} θ_{ij}(log n).

No zeros enter. `tests/test_H2_det_positive.py` drives
`H_2plane_independent.H2`: det `H > 0` and `λ_min(H) > 0` on
`χ₅, χ₃, χ₄, χ₈, χ₁₃` at `μ=16`.

**What a hand bound would need.** Truncating `P` at `n ≤ 8` (or
even `n ≤ 11` on `χ₅`) flips the sign of det
(`tests/test_P_truncation_det.py`, `report/P-truncation-det.md`).
Primes 2 and 3 dominate the *size* of `P(f₁)`, not the *sign* of
the determinant. Weyl (`tr H > 0`) and Gershgorin (`H₁₁ ≥ |H₁₂|`)
fail on the same 2×2. A proof by estimates must keep every
prime power `n ≤ μ`.

An Arb enclosure (`code/H2_arb.py`, `tests/test_H2_arb.py`) that
excludes 0 is a *verification* of the 2×2, in the style of the
`μ=3` 5×5 certificate. It is not the estimate.

---

## 4. Schur `T⁻¹`: identity versus bound

Split the hat matrix

        [ H  C ]
    Q = [ Cᵀ T ],     Δ = H − C T⁻¹ Cᵀ  (H is 3×3).

Block elimination gives the identity `λ₀(Q) = λ_min(Δ)`
(`code/schur_head.py`). On `χ₁₃` `μ=16` `NB=12` the ratio is 1 to
2% and `κ(T) < 10³` (`tests/test_schur_head.py`). On the table of
`report/lemma2-schur-3.md` the ratio is 1.000–1.004 across eight
windows, including `χ₅` `μ=38` where `κ(T) ∼ 10⁸`.

**The missing bound.** `H` on the 2-plane is `O(10⁻⁴)` to
`O(10⁻⁶)`; `λ₀` is `10⁻⁸` to `10⁻⁴⁹`. The factor is
`C T⁻¹ Cᵀ`. A lower bound on `λ₀` from a lower bound on `H`
requires an upper bound on `‖T⁻¹‖` (or a spectral gap of `T`)
and a bound on `C`. None is proved. The identity does not
transfer 2-plane positivity to `λ₀`
(`test_two_plane_does_not_transfer_to_lambda0`: `λ_min(H)/λ₀ > 10`
already on the narrow desert `χ₁₃`).

At `χ₃` `μ=80`, `N_eff = 3.00`: the ground state is not in the
2-plane (overlap `∼0.83`, Ritz of the plane `ℓ ∼ 20` against
`ℓ ∼ 111`). Lemma 2 (window) as a 2×2 plus Schur tail applies
when `N_eff ≤ 2.2`; that is the model case `χ₅` `μ=16`, not
`χ₃` `μ=80`.

---

## 5. χ₃ `μ=80`: two assemblies, one judged window

`scan_s.assemble` uses `NPANEL = 3 NB + 12` and 5 Newton steps
for Gauss–Legendre nodes. `spectro.run` uses `NPANEL = 5 NB + 20`
and 6 Newton steps (`tests/test_chi3_assemblies.py`).

Judged (`tests/test_chi3_mu80_judge.py`):

| assembly | NB | dps | λ₀ | ℓ |
|---|---|---|---|---|
| `scan_s` | 8 | 28 | >0 | >40 |
| `scan_s` | 24 | 50 | 4.183×10⁻⁴⁹ | 111.4 |
| `scan_s` | 32 | 70 | <0 | — |

The last row is Galerkin/quadrature unsaturated on *that*
assembly. `edge_value_scan` (spectro) at NB=32 dps=70 gave
λ₀>0 and ℓ=135. Different quadrature, no judge. **Do not
harvest ℓ=135.** At the cheap window `χ₃` `μ=16` `NB=8` both
signs are positive and depths agree to 25%.

---

## 6. 37a1: prime-side Q versus Gram

Rank 1: the zero Gram includes the central zero once on the
constant mode; the prime-side `Q` does not, until the rank is
read (`tests/test_gl2_eight_curves.py`).

Judged without identifying the two matrices
(`tests/test_gl2_37a1_Q_vs_gram.py`, `tests/test_gl2_37a1_mu62.py`):

- `scan_q_gl2.assemble` at `μ=11` `NB=12`: λ₀>0 but shallow
  (`ℓ < 2`); the Gram at the same window is already a well
  (`ℓ > 5`). The rank is unread on the prime side.
- `scan_gl2.gram` at `μ=62` `NB=80`: λ₀>0, `ℓ ∈ (10, 40)`.

A 201 s prime-side run at `μ=62` (`report/parallel-run/`) is an
artifact of that assembly, not a second name for the Gram.

---

## 7. Maass Q

Inputs exist: `zeros_maass{1..5}_weyl.pkl`,
`code/maass_an_*.json` (Zenodo 15490636), Laplace parameters `R`.
The completed Gamma is `Γ_R(s+iR) Γ_R(s−iR)`, not `Γ(s)` and not
the weight-2 pair `Γ_R(s) Γ_R(s+1)` of `scan_q_gl2`.

Shipped path: the zero Gram (`scan_gl2.gram`). `maass1` at `μ=16`
is INDEF (desert / short list). Booker–Then Table 1 at `μ=8`
`N=25` has `ℓ≈35` (`λ∼10⁻¹⁵`): float64 reports INDEF. A slightly
smaller window `μ=6` `NB=12` is isolated with `ℓ ∈ (20, 40)`
(`tests/test_maass_q.py`). There is no prime-side `assemble` for
Maass. Building one is a code path, not a covering lemma.

---

## 8. Connes–Consani sub-shells and the 2-adic mass

**Sub-shells.** The first semi-local step on `(log 2, log 3]`
cannot be taken by transporting the `Λ=1` Sonin mechanism of
Connes–Consani 2021 (`notes/semilocal-step.pdf`). The
archimedean operator is rebuilt to the published digits
(`code/cc_arch.py`, `tests/test_cc_2adic_status.py`). The
semi-local remainder is predominantly *positive* on the test
functions where CC's is essentially negative. That is a negative
result, measured. It is not a replacement pairing.

**2-adic mass at `λ=2`.** Exact shell pairing
(`notes/2adic-shells.md`, `code/tau2_local.py`): module twist
gives 1/√2; inverse twist and the Lebesgue Jacobian both give √2;
Bombieri (log 2)/√2 is a different Haar. The Fmat grid is not
that Dirac. Sub-shells: Fg = ∑_n ½ ĝ(2^n ·) − ½ ĝ(·/2)
(`code/subshells.py`). The (log 2, log 3] step remains a
measured negative (`notes/semilocal-step.pdf`).

---

## 8a. Rational witness v = (4, −3, 1)/√26 at μ=16

One vector, three hats, no eigensolver.
Index: `report/witness-status.md`.

**Even (s₀=1/4).** Same integrand for all a=0.
G₃ + 8+8 + Leibniz |a''|. a^{(6)} Markov
M≤1370 from verified c_n (`report/a6-markov.md`).
χ₅ Q ∈ [0.00334, 0.00717] after that remainder.
Eight even characters: `code/av_enclose_even.py`,
all Qlo>0, χ₅ tightest.

**Odd (s₀=3/4).** a^{(6)} does not freeze.
a^{(4)} does (23.5 sampled, ≤60 Markov).
Composite 2-point Gauss on two halves
(`code/av_odd_gauss2.py`) + Leibniz [1,L]:
χ₃ Q ∈ [0.00388, 0.00795] with M₄=60.
χ₃ is the tight odd window.

**Not RH.** Finite μ, one v. I_{[0,1]} is
now a quadrature with a coefficient bound
on a derivative, not a comparison estimate
of the integrand. (∀ L) Q_L ≥ 0 is still
the covering lemma.

## 9. What this list is not

None of the items above is the covering lemma, Weil's criterion
on the full class, Li's criterion on all `n`, or Nyman–Beurling.
Finite-window positivity, a 2×2 enclosure, a Schur identity, a
Landau *inequality*, and a measured edge ratio are compatible
with an off-line zero beyond the Paley–Wiener type of the window.

The living index of the repository is `README.md`. Dated campaign
logs (`report/STATUS.md`, `report/FREEZE.md`) do not supersede it.
