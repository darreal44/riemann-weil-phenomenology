# Numerical phenomenology of the Weil positivity criterion

[![DOI](https://zenodo.org/badge/1351526407.svg)](https://doi.org/10.5281/zenodo.22215278)


## Tests

```
python3 -m pytest tests -q              # campagne + quorum artefacts (<15 s)
python3 tests/test_theta_endpoints.py   # identites de la table de correlation (App. A)
python3 tests/test_cert_mu11.py         # coherence tables de certificats <-> temoins JSON
python3 code/quorum_general.py 11 46 22 zeta verify   # rejeu certifie complet (python-flint requis)
python3 code/positivite_certifiee.py    # Q>0 certifie a mu=11 (~150 s, python-flint)
python3 code/music_zeros.py zeta 11 46 50 6   # MUSIC depuis le radical
python3 code/music_zeros.py chi3 16 36 48 3   # cran Dirichlet : zéros de L(s,χ₃)
python3 code/squares47_arb.py 4         # enclosure Arb 5x5 (~1 s, python-flint)
python3 code/map2.py                    # carte 2-var vs hold-out
```

## Documents

Sixteen notes, one lab notebook. They are not of equal standing; read them by tier.

**Living corpus — four notes, publishable as they stand.**

- `notes/quorum-theorem.pdf` — *Proper sub-Euler products violate Weil positivity on a fixed
  window: certified witnesses* (5 pp.). The theorem of the repository: 340 ball-arithmetic
  witnesses (exhaustively at µ = 11, 16, 22 for ζ; χ₃ at µ = 11), with the full derivations
  of the correlation table (App. A) and of the Weil–Bombieri normalization (App. B). Its
  missing half — the complete form is positive definite at µ = 11 — is certified in the
  next note. Engines, frozen dyadic witnesses and certificate tables live in `code/`.
- `notes/zeros-from-the-radical.pdf` (v3) — MUSIC on the truncated Weil form: the admission
  bound |v̂(γ)| ≤ √(λ/2), Proposition A (the transforms of the bottom vector at the zeros
  are the bottom eigenvector of the zero Gram), zeros of ζ to 10⁻¹⁹ and γ₁(χ₃) to 4×10⁻⁵⁸
  from prime-built matrices, err ≈ e^(−sµ), the endpoint law |v̂₀(γ₁)| ≈ C_γ λ₀ and the
  leakage spectrum, and the certified positive definiteness of the complete form at µ = 11.
- `notes/depth-geometry-quorum-mechanism.pdf` (v2) — §1 (under RH): the depth law as a
  sampling constant of the zero set; the geometric law −ln c_L ≈ a L(γ₁−ν)₊ + b L Σ(gap−ν)₊
  with (a, b) fitted on four scales of ζ, predicting s(χ) out of sample (median 0.89, 10/14
  within 20%); the Slepian share of the depth. §2 (no zeros): the unconditional 2×2
  interlacing lemma — depth × coupling — its certified µ = 11 instance (15/15 sub-products
  on one vector), the µ-content at three scales, δ_p ~ e^(−7p), κ_p ~ e^(−4p).
- `notes/sampling-floor.pdf` — Theorem 1 (under RH): c_L > 0 and λ_min(N) ↓ c_L, Beurling
  read through the explicit formula; the desert quantified by Slepian's constant; why
  Duffin–Schaeffer/Bernstein cannot give a quantitative lower bound. Says no more than
  Beurling.

**Campaign notes — useful measurement, titles to be read as dated records.**

- `notes/depth-phenomenology.pdf` — *superseded as a result, kept as a campaign.* "Fifteen
  L-functions, one ladder" holds on the ramp (rungs 9–14) only; the four-variable map it
  presents is dead out of sample (χ₋₂₃, −29%, 20th preregistered execution) and replaced
  by the geometric law above. The preregistered stress record, the bandwidth-vs-counting
  test, the recruitment law and the quorum-as-phenomenon remain valid measurements.
- `notes/lemma-speed-s.pdf` — *superseded.* s = κ_win·Λ(χ) is a dead map; its S2
  (err ≈ e^(−sµ)) lives in zeros-from-the-radical.
- `notes/lemma-delta-profile.pdf` — Δ(ℓ) universal on the ramp 9–14 only; the 2π-comb
  control (off-profile) and the L-variation at fixed χ₋₈ remain good controls.
- `notes/lemma-delta-2pie.pdf`, `notes/lemma-delta-inf.pdf` — negative findings: two
  clusters ([16.8, 17.1] and [17.9, 18.2]), not 2πe, not split by parity.
- `notes/lemma-quorum-scales.pdf` — *superseded as master text.* B1/B2 are now the 2×2
  lemma of depth-geometry-quorum-mechanism; this note is the pointer to their origin.
- `notes/lemma-map2.pdf`, `notes/missing-characters.pdf`, `notes/chi20-mu50.pdf` — the
  execution record of the maps, dated: χ₋₈, χ₋₂₀, χ₋₂₃ instantiated with independently
  cross-checked zeros; the four-variable map killed by χ₋₂₃; the two-variable successor
  killed harder (+97%); χ₋₂₀ does not kill — its secants climb to s_∞ ∈ [0.58, 0.62] at
  µ ≤ 74 (the early "kill from above" was a short-sieve artifact, notebook §18 erratum).
- `notes/lemma-C.pdf` — C = κ as an identity of form only; κ is unreadable on the same Q.
- `notes/squares47.pdf` — the prime-side/zero-side identity on V: on the 5×5 block the
  residual is O(1/G²) once the truncated zero sum is completed by the density tail and the
  boundary term C_G/G, C_G = 2Λ(µ)/(πL√µ) (notebook §42–50); on the full 47×47 the
  difference is an Arb enclosure with 0 in every entry, bound 6×10⁻³ set by the tail
  budget (§65).

**Other thread.**

- `notes/suzuki-conjecture-note.pdf` — the numerical study of Suzuki's Conjecture 1.2:
  identification of the constant as ‖Φ‖_{L²}, the L²/uniform split, the Dirichlet
  extension. Independent of the quorum thread; not to be mixed with it.

**The laboratory.**

- `report/le-milieu-des-premiers-v2.md` — the full lab notebook (French): every
  measurement, every artifact caught (eleven families), every hypothesis executed
  (twenty-three), in the order things were understood. Its Annexe H is the single status
  page of the project; Annexes C and G are historical.

## Main results

Ordered as the living corpus in *Documents*: theorem first, then what the radical knows, then the floor and the mechanism, then the campaigns, then the other thread. Points 1–3 are theorems or certified computations about the explicitly defined forms (the conditional part is marked); points 4–5 are measurements. None of it bears on RH.

**1. The quorum theorem, both halves certified.** Using ball arithmetic (Arb via
python-flint), every proper sub-Euler product of the windowed Weil form admits an
explicit negative witness — exhaustively at µ = 11 (15/15 proper subsets), µ = 16
(63/63), µ = 22 (255/255), and for χ₃ at µ = 11 (7/7, no pole: the phenomenon belongs
to the Euler product, not to ζ's pole). 340 certified violations, zero exceptions
(`code/quorum_general.py`, frozen dyadic witnesses `code/witnesses_*.json`, certificate
tables `code/quorum_cert_*.txt`; the identification with the Weil–Bombieri pairing is
independently checkable via `code/weil_normalization_check.py`). The other half: the
*complete* form at µ = 11 is certified positive definite (`code/positivite_certifiee.py`:
eigen-congruence + Gershgorin + Sylvester through condition number ~10⁴⁸; the critical
row is the razor itself, λ_min = 3.58317×10⁻⁴⁸ ± 3×10⁻⁵⁴). Notes:
`notes/quorum-theorem.pdf`, `notes/zeros-from-the-radical.pdf`. A finite-window
certificate, not a claim about RH.

**2. What the radical knows: MUSIC, the Gram duality, the precision law.** If Q(v) = λ
then |v̂(γ)| ≤ √(λ/2) at every zero: the low end of the spectrum is a rigorous MUSIC
noise subspace, and `code/music_zeros.py` recovers the zeros of ζ to 10⁻¹⁹ from a 47×47
matrix built from five primes, and γ₁(χ₃) to 4×10⁻⁵⁸ at µ = 38 (checked against a
60-digit Hurwitz computation; the localization mechanism err = |v̂|/|v̂′| closes to three
digits). Proposition A: the transforms of the bottom vector at the zeros are the bottom
eigenvector of the zero Gram — the radical and the quasi-kernel of the zero Gram are the
same object. Precision law err(γ₁) ≈ e^(−s(χ)µ), full depth — *the drilling speed is the
per-digit cost of reading the first zero* — rooted in the endpoint law |v̂₀(γ₁)| ≈ C_γ λ₀
(C_γ ∈ [7, 28] in the configurations measured): the radical's residual mass is expelled to
the band edge (leakage spectrum |v̂₀(γ)| ≈ e^(−τ(ω_max−γ)), τ ≈ sµ/(2ω_max) to 6% on ζ).
Note: `notes/zeros-from-the-radical.pdf`.

**3. The floor and the mechanism.** *(Under RH)* the infimum c_L of the truncated form
over the whole window space is strictly positive — it is a sampling constant of the zero
set for PW_{L/2}, positive by Beurling — and λ_min(N) decreases to it: saturation is
visible at µ = 3 (c_log3 ≈ 5.55×10⁻⁸ from N = 9…61), a decelerating trend at µ = 11
(3.59 → 1.86 → 1.54×10⁻⁴⁸ for N = 47, 57, 67). The depth law −ln c_L = s(χ)µ + b is
thereby a *geometric* property of the zeros: −ln c_L ≈ 1.69·L(γ₁−2π/L)₊ +
0.82·L·Σ(gap−2π/L)₊, the two coefficients fitted on four scales of ζ alone, predicts s(χ)
out of sample with median ratio 0.89 (10 of 14 characters within 20%, no parameter per
character); the desert alone (Slepian's constant) accounts for 75% / 28% / 21% of the depth
at µ = 3 / 11 / 16. *(No zeros)* the quorum has a mechanism: an unconditional 2×2
interlacing lemma — Q_S = Q + T_M is indefinite as soon as (ε + vᵀT_Mv)·d < κ², depth ×
coupling — whose three quantities are certified at µ = 11 (all 15 proper sub-products
re-proved indefinite on the *same* bottom vector, `code/quorum_2x2.py`) and measured at
µ = 8, 11, 16 (14/14, 14/14, 62/62; silence δ_p ~ e^(−7p), coupling κ_p ~ e^(−4p): the
coupling decays at half the rate of the silence, which is what makes the determinant
negative). Notes: `notes/depth-geometry-quorum-mechanism.pdf`, `notes/sampling-floor.pdf`.

**4. The depth campaign (measurements; the maps it produced are dead).** Fifteen
L-functions were drilled with matched, depth-adequate bases at µ = 30–38. What survives
as measurement: the quasi-null ladders are linear in µ (the signature of the integer
lattice; continuum mechanisms cap at log µ); the *recruitment law* — rung k of the ladder
recruits the (k+1)-th χ-supported prime, in order, tower signs modulated by χ(p) — read
by radical spectroscopy; the *harvest-front* model of the generic regime (margin ≈
e^(−s²γ²_front), Slepian plunge onset predicted 24.9 / measured 26); surgical removals
(prime 2 collapses positivity in six directions; the pole collapses one, by exactly
−32sinh²(L/4)/L); and positivity as a *quorum* observed before it was certified. What is
dead: the per-character linear map s(γ₁, gap, D, parity) (RMS 6% in training, −29% on
χ₋₂₃ out of sample — 20th preregistered execution; the two-variable successor −97%; the
three-variable successor −24%), and the universal rung profile Δ(ℓ) beyond the ramp
9–14 (two clusters at depth, not 2πe, not split by parity). The measured s(χ) table
(χ₈ 1.47, χ₇ 1.58, χ₅ 2.41, χ₄ 2.93, χ₃ 4.00, ζ 11.7, …) is the *target* of the geometric
law of point 3, not a law itself. Notes: `notes/depth-phenomenology.pdf` (read as a dated
campaign), the `lemma-*` and map notes (execution record).

**5. Other thread: Suzuki's conjecture (1.2) and its Dirichlet extension.** Let v_a be
the L²-normalized ground state of the semi-local Weil form on [−a, a], built from primes
only. Numerically, v_a converges in L² to Φ/‖Φ‖, Φ the inverse Fourier transform of
ξ(1/2+iz) (overlap 0.99964 at µ = 11; L² deficit ≈ (sup-residual)²/2 at every µ tested),
hence the normalization constant of (1.2) is c_∞ = ‖Φ‖_{L²(ℝ)} = 1.130932026…; the
uniform convergence is much slower (max relative residual ≈ e^(−L)/3, concentrated in the
zero-free band [0, γ₁)), so the conjecture splits into a fast L² version and a slow uniform
one. The identification holds across the Dirichlet family, parameter-free: for the five real
primitive characters mod 3, 4, 5, 7, 8, c_∞(χ) = ‖Φ_χ‖ with the exact theta kernels,
projection estimates agreeing to ≤ 4×10⁻⁴ at µ = 16, six for six. Note:
`notes/suzuki-conjecture-note.pdf`. Independent of the quorum thread.

## Reproduce

```bash
pip install -r requirements.txt
cd code

# zeta zeros cache (~45 s; pickles are provided, so optional)
python3 zeros_cache.py

# regime matching & Slepian plunge (§9)                     ~1 min each
python3 raccord.py
python3 plunge.py

# Suzuki shape test for zeta:  mu  N_basis  dps  GL_degree  (§10)
python3 shape7.py 5.5 20 55 14        # ~5 s
python3 shape7.py 11 46 85 16         # ~70 s ; lambda_min = 3.58e-48 (cf. CC's 2.389e-48)
python3 shape8.py 11 46 85 16         # + theta-kernel overlap 0.99964  (§12)

# conventions & c_inf identification (§12)                  ~10 s
python3 denouage_A.py
python3 phi_exact.py                  # exact ||Phi_chi|| , 12 digits (§13.4)

# Dirichlet scan (§13): mu = 5.5 and 11 per character       ~1 min each
python3 dirichlet_step1.py            # Frullani validation + L(chi3) zeros (~3 min)
python3 dscan.py chi3
python3 dscan.py chi4
python3 dscan.py chi5
python3 dscan.py chi7
python3 dscan.py chi8
# third ladder point, e.g.:
python3 -c "import dscan, mpmath as mp; dscan.run('chi4', mp.mpf('16'), 46, 60)"
```

Every pipeline is validated against independent anchors: closed-form identities
(pole term, digamma/Frullani vs the spectral Q_∞, the 2.00963 coefficient of
Connes–Consani Fig. 4), the zero side of the explicit formula (280 ζ zeros, 40–70
zeros per L(s,χ)), and the published λ_min = 2.389×10⁻⁴⁸ at µ = 11.

## Artifact taxonomy (hard-won, please reuse)

1. float64 eigenvalues below ~10⁻¹⁵·‖K‖ produce **fake RH violations** (negative λ).
2. Sieve truncation creates off-line pseudo-zeros beyond U ≈ 0.65·log N.
3. Finite archimedean cutoff T (Groskin's diagnosis — structurally absent here:
   all archimedean integrals are closed on [0, L]).
4. Quadrature nodes imported in float64 floor the whole matrix at 10⁻¹⁶
   (Newton-refine Gauss–Legendre nodes in multiprecision).
5. Splitting a smooth integrand into two near-divergent halves destroys composite
   Gauss–Legendre accuracy.
6. Two-limit protocol: shape residuals converge **from below** in basis size
   (small bases flatter the test) — extrapolate in N before fitting in µ.
7. Basis demand grows with ladder depth: an under-sized Galerkin basis inflates
   λ_min by orders of magnitude and fakes a *downward bend* of deep ladders
   (χ₃ at µ = 38: slope 3.35 → 4.02 when N goes 63 → 75); ζ's apparent
   non-linearity is suspect for the same reason.

## Epistemic status

Point 1 is a theorem about the explicitly defined forms Q_S (340 ball-arithmetic witnesses, plus the certified positive definiteness of the complete form at µ = 11) and asserts nothing about RH. Point 2 contains two proved statements (the admission bound, Proposition A) and measured laws. Point 3 contains one theorem under RH (the floor, Beurling) and one unconditional lemma (2×2), with a certified instance; its geometric law is a two-coefficient fit on ζ tested out of sample. Points 4–5 are measurements with stated error bars.
theorem about the explicitly defined forms Q_S (340 ball-arithmetic witnesses,
zero exceptions) and asserts nothing about RH. The shape law rests on six µ
points (two basis-extrapolated); ladder slopes on three µ points each; the c_∞
identification on closed-form norms plus overlap/deficit consistency. All
measurement claims are falsifiable by extending the series with this code.
References: Connes–Consani arXiv:2106.01715; Connes–Consani–Moscovici
arXiv:2511.22755; Connes–van Suijlekom arXiv:2511.23257; Connes
arXiv:2602.04022; Suzuki arXiv:2606.09096; Groskin arXiv:2605.20224.
