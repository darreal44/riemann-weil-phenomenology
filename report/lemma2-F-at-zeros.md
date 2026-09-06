# |F(γ)| of the ground state

Fourier of the hat reconstruction of
Q's minimizer, at the first zeros.
Share = |F(γ_k)|² / ∑_{j≤15} |F(γ_j)|².

## χ₅ µ=16 (ell=27.2, L=2.77, last hat 2π·8/L ≈ 18)

| k | γ | \|F\| | share |
|---|---|---|---|
| 1–4 | 6.6–16.0 | 10⁻¹¹–10⁻⁹ | 0 |
| 5 | 17.6 | 2.0×10⁻⁸ | 0.001 |
| 6 | 19.5 | 1.4×10⁻⁷ | 0.039 |
| **7** | **22.2** | **5.5×10⁻⁷** | **0.62** |
| 8 | 24.6 | 2.6×10⁻⁷ | 0.14 |

## χ₃ µ=16 (ell=34.8)

Zeros 1–4: share 0. Peak at γ₅=20.5
(share 0.50), then 24–31.

## χ₁₃ µ=16 (ell=10.0)

γ₁ already 3.1, |F| = 4×10⁻⁵, share
still 0. Mass at γ₆–γ₈ (15–19).

## χ₃₁ µ=38 (ell=8.1)

Same shape: first four zeros
cancelled, mass at γ₇–γ₁₀ (13–17).

∑_{15} |F|² is the same order as λ₀
(factor 2–4: Weil's 2π and the
negative axis).

## Reading

The ground state does not hide in
the desert. It **interpolates the
first zeros to almost zero** and
dumps the residual on the first
uncancelled zero past the hat
band edge 2π N_B / L.

That is why the desert Slepian is
10⁶–10¹⁵ too large: it only uses
the hole [0,γ₁]. Q uses every
γ_k below the cutoff as a
interpolation node.

Lemma 2's comparison function, if
it is not Q itself, has to be an
interpolant at {γ₁,…,γ_m} with
m ≈ number of zeros in (0, 2π N_B/L),
not a Slepian of one interval.

The cost of that interpolant in
PW_{L/2} is the one-set problem
restricted to a *finite* node set —
Beurling on m points, type τ.
That is a classical bound
(Levin, Duffin–Schaeffer on a
finite set) and may be the
provable form of Lemma 2.
