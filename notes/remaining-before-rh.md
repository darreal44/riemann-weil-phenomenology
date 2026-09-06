# Remaining demonstrations (before any RH covering lemma)

Demonstrations that closed after this note: `notes/demonstrations.md`
(Courant, Schur sign, θ_{f₁}, edge split), `notes/av-gauss.md`
(Gauss of A(v)), `notes/landau-depth.md` (kernel count, rungs
sum to ℓ₀, (16+5)/2=11), and `notes/log2-log3-step.md` (1999
finite part vs Sonin remainder), and `notes/pw-log3.md` (Galerkin
is Courant the wrong way for \(W_{\log3}\); the class step is
not taken). The covering lemma is not among them.

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
windows we ran. On the K*-plane itself (`report/ker-ells.md`,
`report/G-on-ker.md`) the spectrum splits deep / plunge / anti:

    χ₅  K*=5:  26.1, 14.9, 5.3, 1.18, −1.23     (3+1+1)
    χ₁₃ K*=3:  8.82, 1.46, −1.30                 (1+1+1)

`‖G|_ker‖ ≈ 3.4`, so C = −ln‖‖ is negative. The hypothesis
`‖G|_ker‖ ≤ e^{−2}` that would force #{ℓ>2} ≥ K* fails by two
orders of magnitude. The extra kernel directions are real and
shallow (`report/anti-well.md`). They are sampling, not a
wrong time-norm: the hats are already an L²[0,L] ONB
(`report/anti-well-norm.md`). The cut `ℓ>2` is a choice that
keeps only the deep block. It is not RH. (`ζ` `μ=11` needs
mpmath: `test_depth_law.py`.)

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
constraints on a window). At μ=16 (`report/edge-ratio-mu16.md`)
edge/ℓ is 0.73–0.90 except χ₃=0.37 (R=44, not O(1) relative to ℓ).
The jump sum matches λ₀ to 7% (χ₁₃) and 2% (χ₄) when λ₀ is
above 10^{-16} (`report/jump-heuristic-mu16.md`); χ₅/χ₃ underflow.
S uses the measured ψ(0). Evidence, not an a priori O(1).

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

**Drop p=3, preregistered §116.** Executed
(`notes/gl2-37a1-drop3.md`, `code/gl2_quorum_scan.py`): full
prime-side λ₀ = 5.258×10⁻⁷, ℓ = 14.46; drop-3 λ₀ = **+0.093**.
The last recalcitrant is still dispensable. KILL. Every other
voting prime is necessary; 17 and 19 are mute (a_p=0). Control
at μ=38 matches the journal (+0.38 vs +0.37). 19 processes,
216 s. Judge: `tests/test_gl2_37a1_drop3.py`.

**67a1 μ=74, preregistered §113.** Executed
(`notes/gl2-67a1-mu74.md`): full λ₀ = 4.92×10⁻⁸, ℓ = 16.83;
drop 2, 5, 13 all negative (−0.42, −1.02, −0.14). Quorum stays
complete. SURVIVE. 22 processes, 219 s. Judge:
`tests/test_gl2_67a1_mu74.py`.

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

**The other mechanism** is Connes 1999, not a second remainder
(`notes/log2-log3-step.md`, `code/log2_log3_step.py`): subtract
`2 h(1) log' Λ` first. That volume vanishes at the Sonin cutoff
`Λ=1`. The HS logarithm is in `1/h`, not in `Λ`. Interior primes
on `(log 2, log 3]` are `{2}`. Theorem 4 says the finite part
*is* the S-local Weil pairing — no positivity for free. The
Paley–Wiener step is not taken. Judge:
`tests/test_log2_log3_step.py`.

**2-adic mass at `λ=2`.** Exact shell pairing
(`notes/2adic-shells.md`, `code/tau2_local.py`): module twist
gives 1/√2; inverse twist and the Lebesgue Jacobian both give √2;
Bombieri (log 2)/√2 is a different Haar. The Fmat grid is not
that Dirac. Sub-shells: Fg = ∑_n ½ ĝ(2^n ·) − ½ ĝ(·/2)
(`code/subshells.py`).

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

---

## 8b. What remains of the (log 2, log 3] step

The Paley–Wiener class of type \(\log 3\) is not certified.
Courant on nested hats: \(\lambda_{\min}(V_N)\ge c_L^*\), so
\(Q>0\) on \(V_{31}\) is the wrong direction for the class
(`notes/pw-log3.md`). Prime-side ladder at \(\mu=3\) is nested
and positive (\(\zeta\): \(1.026\times10^{-7}\to6.27\times10^{-8}\)
at \(N=9,17,25\), tracking the Gram floor). That is not
\(c_L^*\ge0\). Operator-level \(\int'\) by subtracting the
sub-shells \(1+2^k\mathbb Z_2\) from \(D_S\circ Q\) is still a
construction (journal §108, `report/subshell-ops.md`).

---

## 8b. A(v) versus P(v) as μ grows

Same v. Both diverge like −c L with
c ≈ 0.33 (table `report/Av-Pv-divergence.md`).
The φ₀ piece is v₀² A₀₀ ∼ −4L/13; the
measured slope is a bit steeper
(`report/why-L3.md`, `report/A-4L13.md`).
Q = A−P sits in a 0.004–0.009 band
from μ=16 to 37. A linear model of Q
would cross 0 and is the wrong
remainder. Not (∀ μ).

## 8c. Q(v) band versus unfinished limits

Q(v) ∈ [0.003, 0.009] for μ=16..80
(`report/Q-convergence.md`). Split
Q = (A−P₂−P₃) − P_rest: both sides
shrink together (`report/Q-split-23.md`).
P₂+P₃ → −2.25 (Θ→2I). A has not
frozen. Two readings, not resolved
at μ=80. Not (∀ μ).

## 9. What this list is not

None of the items above is the covering lemma, Weil's criterion
on the full class, Li's criterion on all `n`, or Nyman–Beurling.
Finite-window positivity, a 2×2 enclosure, a Schur identity, a
Landau *inequality*, and a measured edge ratio are compatible
with an off-line zero beyond the Paley–Wiener type of the window.

The living index of the repository is `README.md`. Dated campaign
logs (`report/STATUS.md`, `report/FREEZE.md`) do not supersede it.
