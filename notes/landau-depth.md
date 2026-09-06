# Discrete Landau count and the scale 16 → 5

The depth law of `the-well` is two statements about the Gram of
hats at an arbitrary node set Γ, on the cosine window of length
L = log μ. No Euler product. No RH: Q_L is not used, only the
Gram G_{nm} = ∑_γ hat η_n(γ) hat η_m(γ). Primes never enter.

## 1. The count, from below

Hats {η_n}_{0≤n≤N} of frequencies ω_n = 2π n / L. For a cut ω,

    n(ω) = #{n : ω_n < ω},     N_Γ(ω) = #{γ ∈ Γ : γ < ω}.

**Lemma (evaluation kernel).** dim ker Eval_ω ≥ n(ω) − N_Γ(ω).

*Proof.* Eval_ω : V(ω) → ℂ^{N_Γ(ω)} is linear, dim V(ω) = n(ω),
rank ≤ number of targets. Rank-nullity. Any nodes. □

**Corollary.** K := max_ω (n(ω) − N_Γ(ω))_+ is a lower bound on
the dimension of functions in the hat space that vanish on all
nodes below some ω_⋆. The continuous interpolant

    D_max = max_γ (γ L / 2π − N_Γ(γ))

satisfies floor(D_max) ≤ K ≤ ceil(D_max) + 2
(`tests/test_dmax.py`), the +1 typically the constant hat.

## 2. Kernel directions are the well of the Gram

**Lemma (Rayleigh on the kernel).** For f ∈ ker Eval_{ω_⋆},

    ⟨G f, f⟩ = ∑_{γ ≥ ω_⋆} |hat f(γ)|².

In-band nodes below the cut contribute 0. No RH: G is the Gram
of the nodes, not Weil’s Q.

**Lemma (min-max).** λ_{K−1}(G) ≤ ‖G|_{ker}‖. If the out-of-cut
mass of every unit kernel vector is ≤ e^{−C}, then

    #{k : −ln λ_k(G) > C} ≥ K.

The implication is linear algebra. The hypothesis ‖G|_{ker}‖ ≤ e^{−2}
is Slepian (functions vanishing on the nodes are concentrated in
the desert); it is not proved here as a bound with an absolute C.
Thresholding at ℓ > 2 nats sits past the Landau–Widom plunge on
every resolved window in the table (`report/discrete-landau.md`).

**Count, judged.** On a resolved Gram (enough hats, depths that
float64 or mpmath can see),

    #{ℓ_k > 2} ∈ {round(D_max), ⌈D_max⌉},

off by at most one from either (the plunge). χ₈ (D=1.77): both
give 2. χ₂₉ (D=1.08): ceil=2 = count, round=1. χ₁₃ (D=1.19):
round=1 = count, ceil=2. Long wells in `the-well` (9.9→10,
4.96→5) make round=ceil. The linear-algebra integer is K;
the well-count is that integer past the plunge at ℓ>2. Judges:
`tests/test_landau_depth.py`. ζ μ=11 remains `test_depth_law.py`.

## 3. The scale 16 → 5 is the two ends of one well

Let ℓ_0 > ℓ_1 > … > ℓ_{m−1} > 2 be the well, m = round(D_max).
Rungs δ_k = ℓ_k − ℓ_{k+1} for k < m−1, and δ_{m−1} = ℓ_{m−1}
(the last drop to the bulk). Then

    ∑_{k=0}^{m−1} δ_k = ℓ_0,     mean(δ) = ℓ_0 / m.

**Identity.** If the rungs decline linearly from a first value A
to a last value B, the mean is (A+B)/2. Combined with the depth
law ℓ_0 ≈ 11 D_max ≈ 11 m,

    (A + B)/2 ≈ 11    ⇒    A + B ≈ 22.

The pair (16, 5) is that split: first rung of a long well (ζ μ=11:
16.1) and last (4.9). It is not a second universal constant. On
short wells (D_max ~ 2–3) both ends sit near the mean 11, so the
16→5 profile is invisible (`test_rungs_sum_to_ell0`).

## 4. Why the mean is π² plus O(1)

One-set Slepian: if I^c samples PW_{L/2} and |I| = D_max · (2π/L)
(D_max Nyquist cells), then

    −ln λ_min ≤ π · (L/2) · |I| + log(1/A) = π² D_max + log(1/A).

So ℓ_0 / D_max ≤ π² + log(1/A)/D_max. π² ≈ 9.87. The measured
mean rung 11 is this leading term plus a 1-nat/mode remainder
(`test_mean_rung_is_pi2_plus_unfixed_remainder`). A is not derived.

The first rung is the desert Slepian, reduced by the rest of the
nodes: on ζ, μ=11, τγ₁ ≈ 17 sits next to the first drop 16. The
last rung is the plunge edge, O(1) to a few nats (Landau–Widom
width O(log c)). Their average is the mean rung. No prime.

## 5. What is a theorem, what is judged, what is not

| Claim | Status |
|---|---|
| dim ker Eval ≥ n − N_Γ, any nodes | theorem |
| ⟨G f,f⟩ = out-of-cut mass on the kernel | theorem |
| λ_{K−1} ≤ ‖G\|_{ker} | theorem (min-max) |
| floor(D) ≤ K ≤ ceil(D)+2 | judged (`test_dmax`) |
| #{ℓ>2} ∈ {round(D), ⌈D⌉} on resolved Grams | judged |
| ∑ δ_k = ℓ_0, mean = ℓ_0/m | identity |
| linear rungs A→B ⇒ mean (A+B)/2 | identity |
| (16+5)/2 = 10.5 ≈ 11 | identification of the pair |
| ℓ ≤ π² D_max + log(1/A) | one-set bound, A not closed |
| ‖G\|_{ker} ≤ e^{−2} with an absolute C | not proved |
| O(log c) matching without threshold | not proved |
| (∀ L) Q_L ≥ 0 | RH; not this note |
