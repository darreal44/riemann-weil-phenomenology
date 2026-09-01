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
python3 code/squares47_arb.py 4         # enclosure Arb 5x5 (~1 s, python-flint)
python3 code/map2.py                    # carte 2-var vs hold-out
```

## Documents

- `notes/quorum-theorem.pdf` — *Proper sub-Euler products violate Weil
  positivity on a fixed window: certified witnesses* (5 pp.). The certified
  quorum theorem: statement, ball-arithmetic certification, full derivations
  of the correlation table (App. A) and of the exact Weil–Bombieri
  normalization for ζ and Dirichlet (App. B). Its 340 witnesses, certificate
  tables and engines live in `code/`.
- `notes/suzuki-conjecture-note.pdf` — companion note (4 pp.): the numerical
  study of Suzuki's Conjecture 1.2, identification of the constant as
  ‖Φ‖_{L²}, the L²/uniform split, and the Dirichlet extension.
- `notes/depth-phenomenology.pdf` — *Depth phenomenology of truncated Weil
  quadratic forms: fifteen L-functions, one ladder* (4 pp.): the affine depth
  law and its map (with the full preregistered stress record), bandwidth vs
  counting, the universal rung profile, the recruitment law, and the quorum
  as phenomenon.
- `notes/lemma-delta-profile.pdf` — lemma candidate for the universal rung
  profile Δ(ℓ): ramp-then-plateau reading, the 2π-comb control (off-profile:
  universality is a property of the Weil family, not of arbitrary spectra),
  and the L-variation at fixed χ₋₈ (spacing tracks the level, not the window).
- `notes/lemma-speed-s.pdf` — lemma candidate for the drilling speed:
  s(χ) = κ_win·Λ(χ), with S1 (linearity = PNT on the radical) and S2
  (s as the per-digit cost of reading γ₁ — the measured precision law).
- `notes/lemma-quorum-scales.pdf` — B1/B2: the every-scale quorum reduction
  (diagonal silence + surviving coupling ⇒ every proper sub-product indefinite).
- `notes/squares47.pdf` — the prime-side/zero-side identity on V: 47 squares,
  500-zero reconstruction, residual 4.1% with an explicit O(1/G) tail envelope; Arb 5×5 block: 15/15 difference balls contain 0, certified upper bound 3.6×10⁻².
- `notes/missing-characters.pdf` — χ₋₈, χ₋₂₀, χ₋₂₃ instantiated: Kronecker
  tables, harvested zeros (independently cross-checked), preregistered map
  predictions — **outcome: χ₋₈ passes; χ₋₂₃ kills the map as written (−29%,
  20th preregistered execution); χ₋₂₀ likely kills it from above** — both
  failures landing exactly on the two documented fragility axes.
- `notes/lemma-map2.pdf` — two-variable candidate $s=c\gamma_1^\alpha\rho^{[odd]}$ dies on $\chi_{-23}$ (+97%); parity is the killing axis.
- `notes/lemma-delta-2pie.pdf` — plateau vs $2\pi e$: $\chi_3$ hovers 16.8--17.1, $\chi_4$ sits above; interval $[16.8,18.2]$.
- `notes/chi20-mu50.pdf` — $\chi_{-20}$ at $\mu=50$: last secant 0.59 vs 0.57 (+4%); the 20% kill from above is not fired.
- `report/le-milieu-des-premiers-v2.md` — the full lab notebook (1710
  lines, 97 journal steps): every measurement, every artifact caught, every
  hypothesis executed.

Independent numerical exploration of the truncated Weil quadratic form — the object
behind the recent Connes–Consani(–Moscovici), Connes–van Suijlekom, Suzuki and Groskin
line of work on the Riemann Hypothesis. Everything here is **measurement**, not proof:
the point is to treat the semi-local Weil form as an experimental system and report
reproducible laws, with the same care about artifacts as in a physics lab.

Companion lab notebook (full narrative, French, 1400+ lines): [`report/le-milieu-des-premiers-v2.md`](report/le-milieu-des-premiers-v2.md).

## Main results

**1. First numerical test of the *function-level* convergence in Suzuki's conjecture (1.2)**
(arXiv:2606.09096), and identification of its normalization constant.

Let v_a be the L²-normalized ground state of the semi-local Weil form on the window
[−a, a] = [−L/2, L/2], built from primes only (Connes–Consani ζ-cycles basis,
arXiv:2106.01715). Then, numerically:

- **v_a converges in L² to Φ/‖Φ‖**, where Φ is the inverse Fourier transform of
  ξ(1/2+iz) — the classical Riemann theta kernel. Overlap 0.99964 at µ = e^L = 11;
  L² deficit ≈ (sup-residual)²/2 at every µ tested (quadratic law).
- Hence the normalization constant of (1.2) is **c_∞ = ‖Φ‖_{L²(ℝ)} = 1.130932026...**
  (with ξ(s) = s(s−1)π^{−s/2}Γ(s/2)ζ(s), Suzuki's convention).
- The **uniform (sup-norm) convergence is much slower**: max relative residual
  ≈ e^{−L}/3, concentrated in the zero-free infrared band [0, γ₁) — while the *zeros*
  of the ground-state transform converge superexponentially (Connes, Groskin).
  The conjecture thus splits: L²-version fast (quadratic), uniform version slow,
  bottlenecked by the Γ-bulge below the first zero.

**2. The same identification holds across the Dirichlet family, parameter-free.**
For the five real primitive characters mod 3, 4, 5, 7, 8 (no pole term in the form):
c_∞(χ) = ‖Φ_χ‖ with the exact theta kernels
Φ_χ(u) = 2e^{u/2}·Σχ(n)e^{−πn²e^{2u}/q} (even χ) and 2e^{3u/2}·Σχ(n)·n·e^{−πn²e^{2u}/q} (odd χ).
Projection estimates agree to ≤ 4×10⁻⁴ at µ = 16, six for six, with the predicted
quadratic approach to the exact norms (12 digits, closed form).

**3. A linear depth law for the quasi-radical ladder of Dirichlet forms.**
−ln λ_min = s(χ)·µ, strikingly linear and basis-converged:

| χ | q | parity | γ₁ | s(χ) | shape constant C |
|---|---|--------|------|--------|------|
| χ₈ | 8 | even | 4.90 | 1.53 ± 0.02 | ≈ 0.53 |
| χ₇ | 7 | odd  | 4.48 | 1.70 ± 0.05 | ≈ 0.43 |
| χ₅ | 5 | even | 6.65 | 2.47 ± 0.02 | ≈ 0.50 |
| χ₄ | 4 | odd  | 6.02 | 3.04 ± 0.02 | ≈ 0.39 |
| χ₃ | 3 | odd  | 8.04 | 4.00 ± 0.10 | ≈ 0.41 |
| ζ  | 1 | (pole) | 14.13 | 11.7 ± 0.2 (the apparent bend *was* a basis artifact; the ladder is linear, intercept ≈ −20) | ≈ 0.33 |

(Slopes uniformized at µ = 30–38 with matched, depth-adequate bases; see report
§13–14. Final state of the empirical map, four variables on the twelve-character
training set: ln s = 1.32·ln γ₁ + 0.45·ln(γ₂−γ₁) − 0.13·D + 0.28·[odd] − 1.95
(D = removed prime mass Σ_{p|q} log p/(√p−1)), RMS 6.1%, leave-one-out 4.8%.
Preregistered stress record: χ₁₉ killed the γ₁-only and prime-conductor
hypotheses; the twin pair mod 24 established the arithmetic-density variable;
χ₂₁ landed at +9%; χ₁₇ missed by −26% exactly where the gap variable
extrapolates below its fitted range, and the 14-point refit moves the exponents
(0.45 → 0.68). Honest status: **a map at ~10% with charted failure modes, not a
closed law** — details and protocol in `notes/depth-phenomenology.pdf` and report §13–14.)

The depth s grows with the width γ₁ of the zero-free infrared desert (ζ's pole pushes
γ₁ to 14.13, hence its abyssal ~11.7µ ladder), with a clear **parity signature**: odd
characters dive faster than even ones at comparable γ₁ (two concordant inversions),
and even characters carry the larger shape constant C (C ≈ 0.50–0.53 even,
0.39–0.43 odd, 0.33 for ζ; residual law R ≈ C·e^{−L} throughout). The exact form of
s(γ₁, parity) is open; the naive candidate γ₁²/(2πe) is falsified by χ₄. This
baseline is the prerequisite for a "Landau–Siegel seismograph": an exceptional zero
would make a ladder anomalously deep for its (γ₁, parity).

**4. A theory of the generic regime, and the ladder architecture** (report §14).
The generic closure rate ("0.41/dim") is explained parameter-free by a
*harvest-front* model — margin ≈ e^(−s²γ²_front), rate s²γ/ρ(γ), confirmed over
four decades — with the Slepian plunge onset at J* = U·γ_max/2π + 1 (predicted
24.9, measured 26). Synthetic tests show the regime is arithmetic-blind (uniform
grid ≡ true zeros) while Poisson frequencies are *more dangerous*: GUE rigidity
maximizes the margin. The quasi-null ladders of all 15 L-functions share one
architecture: rung spacings collapse onto a single spacing-vs-level profile
Δ(ℓ) (±12%, ζ indistinguishable from the characters at equal level). A
"dilated-Slepian" reading of that profile — (1−λ_k)^κ with κ ≈ 2.85 — was
proposed and then dissolved by its own precision campaign: extended 10-rung
ladders fit the Fuchs form beautifully per ladder, but the fitted exponent
does not transfer (3.5–5.4 with c free), so the model has no well-defined κ
and the "e or 3?" question was ill-posed. What survives, model-free, is the
universal Δ(ℓ) collapse itself — the surviving lemma candidate for a pure
harmonic-analysis proof. Linearity of −ln λ_min in µ is shown to
be the signature of the integer lattice (continuum mechanisms cap at log µ).
Surgical experiments (removing prime 2, or the pole, from ζ's form) reveal that
explicit-formula consistency is load-bearing: prime removal collapses positivity
by O(1) in six directions; pole removal collapses exactly one direction by
−6.49 ≈ −32sinh²(L/4)/L (match to 0.3%). Radical *spectroscopy* — projecting
each component form (pole, archimedean, one tower per prime) onto the bottom
eigenstates — then yields the microscopic law: **rung k of the quasi-null ladder
recruits the (k+1)-th χ-supported prime**, in order, with the next prime
whispering one rung before its turn and tower signs modulated by χ(p) (for χ₃,
where χ(2) = −1, the 2-tower *supports* the ground state). The 2-tower is O(1)
on every rung — explaining the six-direction collapse — and µ-linearity of the
depth is reframed as the prime number theorem seen from the radical: each new
prime power p^k ≤ µ reinforces the rungs that recruited p, and the Λ-weighted
count of prime powers is ψ(µ) ≈ µ. Finally, a cumulative-sum experiment shows
that **positivity is a quorum**: every partial Euler product inside the window
has a *negative* smallest eigenvalue (the residual negatives being the exact
echo of the off-line pseudo-zeros of sieve truncation), and adding the last
interior prime makes the form land instantly on the complete 48-digit-deep
ladder — a razor's-edge landing at every µ. Depth is not decomposable into
per-prime contributions; ladder *architecture* (which prime sits on which rung)
and ladder *existence* (the quorum) are distinct questions, and the second one
carries the content of RH.

*(Status split: points 1–4 and 6 are measurements with stated error bars, not theorems; point 5 is a theorem about the explicitly defined forms Q_S, machine-certified, and asserts nothing about RH.)*

**5. A certified theorem.** Using ball arithmetic (Arb via
python-flint), the quorum is now *certified*: every proper sub-Euler product
of the windowed Weil form admits an explicit negative witness — exhaustively
at µ = 11 (15/15 proper subsets), µ = 16 (63/63), µ = 22 (255/255), and for
χ₃ at µ = 11 (7/7, no pole: the phenomenon belongs to the Euler product, not
to ζ's pole). 340 certified violations, zero exceptions. Engine:
`code/quorum_general.py` (8–14 s per scale, `verify` mode replays the frozen
dyadic witnesses in `code/witnesses_*.json`); certificate tables with
per-line certified radii: `code/quorum_cert_*.txt`; the identification of
the certified forms with the Weil–Bombieri pairing is independently
checkable via `code/weil_normalization_check.py` (pole identity exact to
12 digits, archimedean identity against the direct ψ-integral). Note:
`notes/quorum-theorem.pdf`.

**6. Lock-picking.** The complete form at µ = 11 is now *certified
positive definite* (`code/positivite_certifiee.py`: eigen-congruence +
Gershgorin + Sylvester through condition number ~10⁴⁸; the critical row is
the razor itself, 3.58317×10⁻⁴⁸ ± 3×10⁻⁵⁴) — both halves of the quorum
exist at µ = 11: every proper Q_S is certified negative, the complete Q is
certified positive. The radical is a rigorous MUSIC noise subspace
(Q(v)=λ ⇒ |v̂(γ)| ≤ √(λ/2)): `code/music_zeros.py` recovers the zeros of
ζ to 10⁻¹⁹ and γ₁(χ₃) to 4×10⁻⁵⁸ (at µ=38) from prime-built matrices.
Measured precision law: error ≈ e^(−s(χ)µ) — *the drilling speed is the
per-digit cost of reading the first zero* — via a new structural fact,
hyper-nullity: the radical's residual mass is expelled to the band
frontier. The leakage spectrum obeys |v̂₀(γ)| ≈ e^(−τ(ω_max−γ)); D2 (µ-independence
of τ) died at the 85-digit zeros. The single measured root of hyper-nullity,
the precision law and the profile is the endpoint law
|v̂₀(γ₁)| ≈ C·λ₀ with C ∈ [7, 25] over sixty orders, equivalent to
τ ≈ sµ/(2ω_max) to 6% on ζ (notebook §15.6–16.7). The complete
form's positivity at µ = 11 is a finite-window certificate, not a claim
about RH.

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

Points 1–4 and 6 are measured laws with stated error bars. Point 5 is a
theorem about the explicitly defined forms Q_S (340 ball-arithmetic witnesses,
zero exceptions) and asserts nothing about RH. The shape law rests on six µ
points (two basis-extrapolated); ladder slopes on three µ points each; the c_∞
identification on closed-form norms plus overlap/deficit consistency. All
measurement claims are falsifiable by extending the series with this code.
References: Connes–Consani arXiv:2106.01715; Connes–Consani–Moscovici
arXiv:2511.22755; Connes–van Suijlekom arXiv:2511.23257; Connes
arXiv:2602.04022; Suzuki arXiv:2606.09096; Groskin arXiv:2605.20224.
