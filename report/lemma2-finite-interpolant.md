# Lemma 2 as finite interpolation

ω̂ = 2π N_B / L, the last hat.
m = #{ γ_k : 0 < γ_k < ω̂ }.

| L | µ | N_B | ω̂ | m | γ_m | ell | ell/m | m log(ω̂/γ₁) | ∑ log(ω̂/γ) |
|---|---|---|---|---|---|---|---|---|---|
| χ₅ | 16 | 8 | 18.1 | 5 | 17.6 | 27.2 | 5.4 | 5.0 | 2.2 |
| χ₅ | 38 | 12 | 20.7 | 6 | 19.5 | 49.0 | 8.2 | 6.8 | 2.9 |
| χ₃ | 16 | 8 | 18.1 | 3 | 15.7 | 34.8 | 11.6 | 2.4 | 1.4 |
| χ₃ | 38 | 12 | 20.7 | 5 | 20.5 | 58.9 | 11.8 | 4.7 | 2.0 |
| χ₃ | 80 | 24 | 34.4 | 10 | 33.9 | 111.1 | 11.1 | 14.5 | 5.5 |
| χ₄ | 16 | 8 | 18.1 | 4 | 16.3 | 28.9 | 7.2 | 4.4 | 2.1 |
| χ₈ | 16 | 8 | 18.1 | 6 | 17.0 | 18.4 | 3.1 | 7.9 | 3.3 |
| χ₁₃ | 16 | 8 | 18.1 | 7 | 16.3 | 10.0 | 1.4 | 12.3 | 4.6 |
| χ₂₉ | 38 | 12 | 20.7 | 11 | 18.5 | 11.3 | 1.0 | 26.9 | 8.4 |
| χ₃₁ | 38 | 12 | 20.7 | 12 | 20.5 | 8.1 | 0.67 | 27.9 | 8.9 |

ell/m is not a constant
(0.67–11.8). Jensen
∑ log(ω̂/γ_k) is 5–20 times
smaller than ell. A product
over the nodes, with the naive
radius ω̂, does not pay what Q
pays.

## Statement

Let τ = L/2 and Λ_L = {γ_k : 0 < γ_k < 2π N_B/L}.
Let F ∈ PW_τ be the hat reconstruction
of Q's ground state. Then F(γ) = o(residual)
on Λ_L minus the last node, and the
residual sits at γ ≈ ω̂
(`lemma2-F-at-zeros.md`).

**Lemma 2 (finite form).** There is an
absolute C such that every F ∈ PW_τ with
‖F‖₂ ≤ 1 satisfies

\[
\sum_{\gamma\in\Lambda_L}|F(\gamma)|^2
\;\ge\;
\exp\bigl(-C\,\tau\,\gamma_1 - C' m\bigr)
\;\|F\|_2^2
\]

or, weaker, the same lower bound at a
single node γ_m. Either inequality
plus the edge identity ell ≈ −2 ln|ψ(0)|
gives the desert bound on −ln λ₀ up to
the C′ m term.

## What is classical

On a finite set, PW_τ-interpolation is
Levin / Duffin–Schaeffer: if the points
are separated by ≥ π/τ they form a
sampling sequence for a subspace of
dimension ~ τ|I|/π. Our points are
*farther* than π/τ in the desert
(γ₁ ≫ π/τ) and closer later. The
constant is not the regular-grid one.

The table says the regular-grid /
Jensen constant is too optimistic
(undershoots ell). The missing C is
the interpolation constant of this
particular irregular set — still
Lemma 2, now on m points instead of
a continuous E.

## Next proof step

Write F(z) = s_τ(z) · P(z) / Q(z)
with s_τ the sine-type function of
PW_τ and P the monic polynomial on
Λ_L. Bound |F| at 0 or at ω̂ by
the Cartwright indicator. That
computation is explicit and finite.
It either produces C₀, C′ or shows
they depend on the character
(same obstruction as the
regression).
