# Passage Q ↔ det(I−A): one numerical cut

E_L on ℝ₊ = desert [0,γ₁] plus
sub-Nyquist gaps with mid below the
8th hat frequency (T = 16π/L).
A = χ_E P_τ χ_E, τ = L/2 = (log µ)/2.
−ld = −∑_{λ>0.01} log(1−λ).

ell_Q is −ln λ₀ of prime-side Q
(windows already measured).

| L | µ | γ₁ | m | τγ₁ | −ld desert | −ld E | ell_Q | ell/τγ₁ | ell/−ld E |
|---|---|---|---|---|---|---|---|---|---|
| χ₅ | 16 | 6.65 | 3 | 9.2 | 11.4 | 30.7 | 27.2 | 2.95 | **0.89** |
| χ₅ | 38 | 6.65 | 3 | 12.1 | 19.2 | 60.2 | 49.0 | 4.05 | **0.81** |
| χ₃ | 16 | 8.04 | 3 | 11.2 | 16.4 | 60.3 | 34.8 | 3.12 | 0.58 |
| χ₃ | 38 | 8.04 | 2 | 14.6 | 27.7 | 53.3 | 58.9 | 4.03 | 1.10 |
| χ₄ | 16 | 6.02 | 4 | 8.4 | 9.5 | 65.2 | 28.9 | 3.46 | 0.44 |
| χ₈ | 16 | 4.90 | 4 | 6.8 | 6.5 | 33.4 | 18.4 | 2.70 | 0.55 |
| χ₁₃ | 16 | 3.12 | 4 | 4.3 | 3.0 | 21.0 | 10.0 | 2.30 | 0.47 |

## What holds

ell_Q / (τ γ₁) sits in 2.3–4.1.
Slepian on the desert alone
underestimates Q by a stable small
factor (the √c prefactor plus the
first plunge of a single interval).

On χ₅ — wide desert, m=3, gaps
few and large — ell_Q ≈ −ld(E)
to 20 %. That is the only row
where the full log-det of the
one-set E tracks Q.

## What does not

The ratio ell/−ld E collapses to
0.4–0.6 as soon as m=4 and γ₁ is
not large (χ₄, χ₈, χ₁₃). Extra
short gaps overtax the det relative
to what Q actually pays. Same
failure as the two-term law at
common T₀: the one-set E with
every ν-gap included is too fat
for Q.

χ₃ at two µ is not even monotone
in the ratio (0.58 then 1.10): a
gap crosses T_cut.

## Status of the passage

Not a constant × log det(I−A) on
the full E_L. Compatible with

\[
-\log\lambda_0(Q)
\;\asymp\;
\tau\gamma_1
\;+\;
O(m_{\mathrm{long}}),
\]

long = gaps that survive a cutoff
of order 1/τ, not every
sub-Nyquist gap up to T=320.

That is the same split as
`lemma2-logdet-split.md`, now
read on real zeros. The missing
lemma is still the comparison of
Q's Rayleigh to this truncated
det, not an identity.
