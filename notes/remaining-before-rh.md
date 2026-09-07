<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
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
and a bound on `C`. On the small window \(W_{\log 3}\), a
Hilbert–Hankel bound on the infinite tail takes χ₈
(`notes/ql-schur-tail.md`, β=+0.055) and fails for χ₅/χ₃
(T₂ eats δ). That is not Lemma 2 at μ=16. The identity does not
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

**Drop 3 at μ=74 and 80.** Preregistered linear crossing ~70
(`report/prereg-37a1-mu74.md`). Executed
(`notes/gl2-37a1-mu74.md`): drop-3 λ₀ = **+0.090** at both
windows (full ℓ = 16.82 and 17.37). Plateau, not a delay.
KILL. Judge: `tests/test_gl2_37a1_mu74.py`.

**Drop 3 at μ=100..250, then isolate 83.** Executed
(`notes/gl2-37a1-drop3-hi.md`, `notes/gl2-37a1-drop83.md`):
drop-3 is −0.418 at μ=100, still +0.048 at μ=84, and
μ* ∈ (84, 86] (`notes/gl2-37a1-mu-star.md`). μ** of
drop-83 is the same bin (`notes/gl2-37a1-mu-star83.md`). Drop-83
is necessary at μ=100 (−0.080) and mute at μ=82. Drop-89
and drop-97 stay positive. 83 is the only new voter on
(80,100], not the sign change of 3. Not RH.

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
that Dirac. At Λ=24 and 32 it still climbs through 0.49 toward
√2 (`notes/2adic-peak-lamge16.md`). Sub-shells:
Fg = ∑_n ½ ĝ(2^n ·) − ½ ĝ(·/2) (`code/subshells.py`).

---

## 8a. Rational witness v = (4, −3, 1)/√26 at μ=16

One vector, three hats, no eigensolver.
Index: `report/witness-status.md`.

**Even (s₀=1/4).** Same integrand for all a=0.
Gauss+Cauchy on [0,1] and [1,L]
(`notes/av-enclose-cauchy-tail.md`): χ₅
Q ∈ [0.00516, 0.00587]. Trap path still
in `av_enclose.py`. Eight even characters:
`code/av_enclose_even.py`, all Qlo>0, χ₅
tightest.

**Odd (s₀=3/4).** Gauss+Cauchy on [0,1]
and [1,L]: χ₃ Q ∈ [0.00570, 0.00610]
(`notes/av-enclose-cauchy-tail.md`).
Chebyshev a^{(6)} still does not freeze.
The convex well of g survives at s₀=3/4
on the same v (ymin=0.180, N=4 gap
0.00284); g_lo is not a χ₅ artefact
(`notes/av-I01-odd.md`).

**Not RH.** Finite μ, one v. A(v) even and
odd are Gauss+Cauchy on [0,1] and [1,L]
(`notes/av-enclose-cauchy-tail.md`). The
chord comparison of I_{[0,1]} is still
open: Gauss-3 = −0.700661; a 3-piece
bound of g misses by 0.224 and Q_lo<0
(`notes/av-I01-compare.md`). A tangent/floor
switch at y_sw=g_min/g'(0)=0.1786 misses
by 0.088, Q_lo=−0.082, still outside
±0.003 (`notes/av-I01-switch.md`). A
three-tangent envelope (t0, floor, tinf)
misses by 0.068, Q_lo=−0.062
(`notes/av-I01-envelope.md`). A quadratic
support near 0 (m=g''(y_min), named in
`report/g-convexity.md`) misses by 0.047,
Q_lo=−0.042 (`notes/av-I01-quad.md`). A
two-piece quadratic (split at y_min/2)
misses by 0.024, Q_lo=−0.019
(`notes/av-I01-quad2.md`). Still one v,
not Weil. (∀ L) Q_L ≥ 0 is still the
covering lemma.
Q_lo=−0.042 (`notes/av-I01-quad.md`). An
N=4 quadratic mesh (named in
`report/quadratic-mesh.md`) misses by
0.0053, Q_lo=+0.0002; the I-gap is still
outside ±0.003 (`notes/av-I01-mesh.md`).
Extending the mesh through the convex
rise [y_min, y_inf] misses by 0.00315
(`notes/av-I01-rise.md`). Tail parabolas
leave 0.002793 (`notes/av-I01-tailq.md`).
A leftover-driven adaptive mesh (eight
bisections on well+rise) has gap
0.000433, inside ±0.003
(`notes/av-I01-adapt.md`). Still one v,
not Weil. (∀ L) Q_L ≥ 0 is still the
covering lemma.
(`notes/av-I01-rise.md`). Uniform N=8
well+rise (the named rate test) has
gap 0.000405, leftover cap ratio
0.123 (`notes/av-I01-n8.md`). Still
one v, not Weil. (∀ L) Q_L ≥ 0 is
still the covering lemma.

---

## 8b. What remains of the (log 2, log 3] step

The Paley–Wiener class of type \(\log 3\) is not certified
for every χ. Every primitive χ already in `scan_s`
takes at μ=3 by Neumann (`notes/ql-class-mu3.md`,
13 extra, all S_lo(h=2)>0.64). That is a finite
list. Bochner α_line still fails.
Courant on nested hats: \(\lambda_{\min}(V_N)\ge c_L^*\), so
\(Q>0\) on \(V_{31}\) is the wrong direction for the class
(`notes/pw-log3.md`). Prime-side ladder at \(\mu=3\) is nested
and positive (\(\zeta\): \(1.026\times10^{-7}\to6.27\times10^{-8}\)
at \(N=9,17,25\), tracking the Gram floor). That is not
\(c_L^*\ge0\). The Bochner / Fourier sufficient bound of the
cutoff kernel is negative on χ₅, χ₈, χ₄, χ₃
(`notes/ql-operator-bound.md`: α_line = −0.418 on χ₅);
no windowed cosine kills the class. The Schur tail at
h=2 takes χ₈ (β=+0.055) and not χ₅ (`notes/ql-schur-tail.md`).
‖Θ(log 2)‖≤1, not 2 (`notes/ql-theta-tail.md`); χ₅ still
δ<0. χ₄ at larger h: first β>0 at h=20
(`notes/ql-schur-chi4-h.md`). Both χ(2)=0 are taken.
Neumann T^{-1} takes χ₅ (S_lo=+0.029);
χ₃ at h=4 (`notes/ql-schur-chi3-h.md`);
χ₇ (χ(2)=+1) at h=2
(`notes/ql-schur-chi7-h.md`);
χ₁₇ (even +1) at h=2
(`notes/ql-schur-chi17-h.md`).
The six (s₀, χ(2)) cells each have
one representative.
μ=3.5, primes {2,3}: T₃ kills h=2 on
χ₅ and χ₄; raise-h at h=4 restores
(`notes/ql-schur-mu35.md`). One extra L,
not (∀ L).
μ=5: χ₃ has λ_min(H_4)<0
(`notes/ql-schur-mu5.md`). This
construction is not ≥0 on W_{log 5}
for χ₃. Not a disproof of RH.
μ* of that sign change is in (4.75, 5];
μ=4 (Θ-jump) is not the crossing
(`notes/ql-chi3-H4-mu.md`).
Q_pk adds 2² at μ=5 (ΔH₀₀=−0.096);
the 4-plane becomes **positive**
(`notes/ql-chi3-H4-pk.md`). CST+Gauss
on φ₀ is not C_A_lo
(`notes/ql-cst-gamma.md`).
The 4-plane sign disagrees under
2 m_Q(ω_n) on the diagonal
(`notes/ql-arch-4plane.md`). Neumann
Q_pk does not take χ₃ at h=2,4
(`notes/ql-schur-pk-mu5.md`). T₅ at
5.1 does not jump λ_min
(`notes/ql-T5-H4.md`). CST+Gauss on
W_L is the classical Γ pairing
(Frullani, Weierstrass; the
digamma writing agrees to 10⁻¹⁴;
`notes/ql-arch-weil.md`). Mixing
(ψ(s₀)+γ)I is not that pairing.
λ_min(Q_pk H₄)=+1.4×10⁻⁵ is a
4-plane of the identified form,
neither Weil-positive nor
Weil-negative (Courant).
‖Θ(y)‖≤√2 on L/4≤y<L/2
(`notes/ql-theta-sqrt2.md`); the
simplex is a theorem and the three
coverings are identified
(`notes/ql-theta-overlap.md`). At
μ=5 this is log 2, t_atoms
1.33→1.04. S_lo of identified
Q_pk takes W_{log 5} for χ₃ at
h=16 with cap 2 already
(`notes/ql-slo-identified.md`,
+2.5×10⁻⁶); the √2 cap raises
it to +5.0×10⁻⁶. Not Weil-positive
(one L). H₁₆ stays + through 7
and 8=2³; the sliver collapses
8×10⁻⁶→5×10⁻¹¹, no sign change
(`notes/ql-H16-mu.md`). Neumann at
μ=7 and μ=8: ρ≥1 except (7, h=24)
where S_lo=−0.45. The W_log5 take
does not extend
(`notes/ql-schur-mu78.md`).
H_n at μ=7 and μ=8 through n=48 stays +;
H₄₈/H₁₆≈0.7, so the well is L
not missing modes
(`notes/ql-Hn-mu78.md`). H₁₆ on
(5, 7]: T₅ Δλ=−2.2×10⁻⁶, then
5 drifts and L cut λ_min by ~10
per 0.5 in μ; H₀₀ rises
(`notes/ql-H16-mu57.md`). χ₃ Neumann
take on (5, 7] is **only μ=5**;
dead at 5.5 (`notes/ql-schur-chi3-mu57.md`).
Quorum at μ=7: χ₈ and χ₁₇ still
take, χ₃ and χ₇ do not, χ₄/χ₅
slivers at h=24
(`notes/ql-schur-quorum-mu7.md`).
ρ_far crosses 1 on (5.5, 6] after
T₅ lifts t_atoms 1.04→1.76
(`notes/ql-rhofar-mu.md`). χ₃ take
dies at T₅ arrival μ=5.1
(`notes/ql-chi3-mu51.md`). χ₁₇ dies
at μ=8 (prereg KILL); χ₈ still
takes at h=24
(`notes/ql-chi817-mu8.md`). χ₇ vs
χ₁₇: same t_atoms, split is
qmin_far / s₀, not T₇
(`notes/ql-chi7-vs-chi17.md`). χ₈ take
dies at 2³ μ=8.1 (`notes/ql-chi8-mu81.md`).
χ₄/χ₅ slivers die at μ=8
(`notes/ql-chi45-mu8.md`). χ₇ survives
T₅ as a sliver, dead by μ=7
(`notes/ql-chi7-mu.md`). No tracked
quorum take past 8. χ₇ sliver
flickers on (5.1, 6.5]
(`notes/ql-chi7-mu57.md`). 2³ does
not jump χ₈ t_atoms (χ₈(8)=0);
death is a head well
(`notes/ql-chi8-far.md`, KILL).
T₅ at 5.1 kills only χ₃ of the six
(`notes/ql-quorum-mu51.md`). Not (∀ L).
Not RH.
Bernstein vs Â is infinite for χ(2)=−1 (A(constant)<0).
Operator-level \(\int'\)
by subtracting the sub-shells \(1+2^k\mathbb Z_2\) from
\(D_S\circ Q\) is still a construction (journal §108,
`report/subshell-ops.md`).

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
P₂+P₃ → −2.25 is only n=2,3.
The 2–3 *towers* sum to −1.40
(`report/P23-all-powers.md`). All
prime towers together do not
converge (`report/all-towers.md`).
A has not frozen. Two readings,
not resolved at μ=80. One point at μ=150
(`notes/av-mu150.md`): A−P₂₃ = −0.020
went through 0; P_rest = −0.024 went
with it. They did not cross. Q=0.0041.
The μ=16 pencil at the same window
(`notes/av-other-v-mu150.md`): five of
five still Q>0, v_min still on the
pencil. Not a sixth slope. Not (∀ μ).

## 8d. P is an arrival process

A prime enters at y=L (kick 0)
then drifts toward 2w (`report/arrival.md`).
Eventual flux per unit L is 2e^{L/2},
the same divergence as the tower walk
(`report/arrival-flux.md`). A saturates
via D₂. There is no P_∞ to subtract
from A_∞. Not (∀ μ).

## 8e. Off tail (χ₃): S_k is Hankel; windows are not the tail

S_k with \(n S_n-m S_m \approx k S_\infty\) identifies
the archimedean off-diagonal as \(\tfrac12/(n+m)\), not
\(1/(k(n+m))\). The extra \(1/k\) in the Pólya skeleton
is a cancelled factor. Ratio \(A_{\mathrm{arch}}/(½(n+m))=1.000\)
on three pairs (`notes/ql-off-tail.md`,
`code/ql_off_tail.py`). \(w_2(\chi_3)<0\), so Off \(=H+|w_2|\Theta\)
(same sign). Hilbert \(\pi\) stays the essential-norm
majorant of \(H\). Nehari does not apply to Off_Q
(`report/hankel-symbol.md`).

Each Hankel lag is HS: \(\|H^{(K)}\|_2\le\sqrt{K/(8(N-1))}\)
on \(\ell^2(n\ge N)\) (cap 0.168 at \(N=32\), \(K=7\);
measured \(H_{\mathrm{near}}=0.075\)). \(\Theta\) lags do not
die (\(B_1=0.397\) on every dyadic). A window \([N,N+L)\)
has no lags \(\ge L\), so it never sees Hartman \(\pi/2\).

Dyadic Off is uniform: \(0.467,0.465,0.466,0.465,0.465\)
on \([32,64)\) through \([256,512)\). Long truncated tails
\([32,M)\): Off \(=0.502,0.561,0.608,0.673,0.719\) at
\(M=128,192,256,384,512\); H climbs \(0.332\to 0.609\);
Θ stays \(0.947\). Off already exceeds \(0.6\) at \(M=256\).
The window \(0.47\) is an artefact of not joining scales.
A numerical substitute Off_far\(=0.474\) still gives
\(S_{\mathrm{lo}}=+0.0007\); at \(M=512\), \(+0.0001\).
Neither is \(s_1(P_{n\ge32}\mathrm{Off}\,P_{n\ge32})\).
The cran of `report/true-tail-s1.md` (\(s_1\le 0.6\))
fails on \([32,256)\). Not taken. B₁ theorem still
\(4|w_2|/\pi\approx 0.624\); limsup cap \(0.572\) is not
\(0.45\). Not RH.

---

## 8f. \(S_T\): Schur of the computed \(T_{\mathrm{near}}\)

\(S_{\mathrm{diag}}\) is the Schur of \(\mathrm{diag}(T)\),
not of \(T\) (`report/S-diag-derivation.md`). Inverting the
Gauss \(T\) on hats \(2\ldots31\) gives
\(S_T=H-C T_{\mathrm{near}}^{-1}C^*\) (`code/ql_schur_Tnear.py`).
χ₃: \(\lambda_H=+0.0185\), \(S_{\mathrm{diag}}=+0.0076\),
\(S_T=+0.0097>0\), \(S_{\mathrm{lo}}=-0.0086\). \(T_{\mathrm{near}}\)
is SPD (\(t_{\min}=1.55\)). Near Off *returns* ~0.002 versus
\(D^{-1}\). χ₃ does not die on the computed block: the drop
to \(S_{\mathrm{lo}}\) is the far envelope (0.018). Haynsworth
on this truncation is Courant on \(V_{32}\), the wrong
direction for \(W_{\log 3}\). Still not \(S\) of the infinite
tail. Not taken. Not RH.

---

## 8g. Proved \(s_1(\mathrm{Off}_Q)\): triangle, not 0.8

`report/drop-half-pi.md` asks to replace the Hankel+Θ
split by a certified \(s_1(\mathrm{Off}_Q)\). That split
*was* the triangle. Written (`code/ql_off_s1.py`):

    \(\tfrac\pi2-|w_2| \le s_1^{\mathrm{ess}}(\mathrm{Off})
      \le \tfrac\pi2 + r_N + |w_2|\).

χ₃: lower \(1.081\), upper \(2.110\) = Off_far.
`ql_schur_neumann` now calls `s1_off_q_upper`; \(S_{\mathrm{lo}}\)
unchanged. \(s_1\le 0.6\), \(0.8\), \(1.0\) lie *below*
the essential lower bound, hence false. Dropping \(\tfrac\pi2\)
flips \(S_{\mathrm{lo}}\) by \(+0.0005\) and is false.
The flip needs Off_far \(\lesssim 0.539 < 1.081\): no
proved \(s_1(\mathrm{Off}_Q)\) can replace Off_far and
flip χ₃. \(\tfrac\pi2\) stays. Not taken. Not RH.

---

## 9. What this list is not

None of the items above is the covering lemma, Weil's criterion
on the full class, Li's criterion on all `n`, or Nyman–Beurling.
Finite-window positivity, a 2×2 enclosure, a Schur identity, a
Landau *inequality*, and a measured edge ratio are compatible
with an off-line zero beyond the Paley–Wiener type of the window.

The living index of the repository is `README.md`. Dated campaign
logs (`report/STATUS.md`, `report/FREEZE.md`) do not supersede it.
