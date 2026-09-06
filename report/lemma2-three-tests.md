# Three probes on the same unions

τ = π, Nyström sinc. Same E as
`lemma2-sampling-constant.md`.

| E | \|E\| | I_max | 1−λ₀ | #λ>½ | Σ log(1−λ)_hid | Σ log(1−λ)_all | I_cap | BM ∫ n_E/r² |
|---|---|---|---|---|---|---|---|---|
| [0,1] | 1.00 | 1.00 | 0.217 | 1 | −1.53 | −1.77 | 1.41 | 4.02 |
| [0,1.5] | 1.50 | 1.50 | 0.070 | 1 | −2.67 | −3.42 | 1.05 | 4.40 |
| [0,2] | 2.00 | 2.00 | 0.019 | 2 | −5.35 | −5.66 | 0.78 | 4.67 |
| [0,1]+0.3 close | 1.30 | 1.00 | 0.214 | 1 | −1.54 | −2.17 | 0.98 | 4.20 |
| [0,1]+0.3 far | 1.30 | 1.00 | 0.216 | 1 | −1.53 | −2.13 | 0.71 | 4.12 |
| [0,2]+0.5 | 2.50 | 2.00 | 0.019 | 2 | −5.46 | −6.40 | 0.34 | 4.80 |
| [0,1]+[0,1] | 2.00 | 1.00 | 0.124 | 2 | −3.28 | −3.78 | 0.54 | 4.48 |
| 1+two 0.3 | 1.60 | 1.00 | 0.208 | 1 | −1.57 | −2.57 | 0.64 | 4.32 |
| 0.8+three 0.3 | 1.70 | 0.80 | 0.302 | 1 | −1.20 | −2.45 | 0.43 | 4.24 |

Pearson (9 rows):

| object | corr(\|E\|) | corr(I_max) | sees |
|---|---|---|---|
| 1−λ₀ | −0.65 | **−0.93** | desert |
| Widom hidden (λ>½) | −0.82 | **−0.93** | desert |
| Widom all | **−0.90** | −0.91 | both |
| I_cap (Lebesgue energy) | **−0.79** | −0.16 | **union** |
| BM ∫ n_E(r)/r² dr | **+0.94** | +0.84 | **union** |

## Reading

1. **Beurling–Malliavin proxy.** The integral
   of the counting function of E tracks |E|
   (0.94). Adding a 0.3-gap moves BM by
   ~0.2, same order as lengthening the
   desert by 0.3. This is a one-set number.

2. **Widom det on hidden modes only.**
   Still the desert: one eigenvalue above
   ½ lives on I_max, so ∏_hid (1−λ) does
   not see a 0.3-gap (−1.53 vs −1.54).
   The *full* product over all λ does
   (−1.77 → −2.17). The plunge tail,
   not the top cluster, carries the gaps.

3. **Capacity.** I_cap drops when a piece
   is added, even far away (1.41 → 0.71
   for the same I_max). corr(I_max)=−0.16,
   essentially blind to the desert alone.
   This is the cleanest one-set scalar
   of the three.

## Consequence for Lemma 2

Do not prove 1−λ_max ≥ e^{−C dim}. That
inequality is true with I_max in place
of dim and false as a one-set statement.

Prove either

- log cap_τ(E) ≤ −c |E| + O(n_∂ log), or
- BM radius of ℝ\E ≥ τ/π − C |E|/L,

then pass to c_L via the sampling
constant of the complement. Widom-all
(∑ log(1−λ_j)) is a legitimate middle
step: it already moves with |E| in the
table. Widom-hidden is not.
