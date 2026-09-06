# ell_Q ≈ C₀ τ γ₁ + C₁ m_long ?

11 windows with a measured prime-side
−ln λ₀ and a zero list.

m>kν = 1 + (number of gaps longer
than k · 2π/L inside the first 12
hat frequencies).

| L | µ | ell | τγ₁ | m>ν | m>2ν | m>3ν |
|---|---|---|---|---|---|---|
| χ₅ | 16 | 27.2 | 9.2 | 5 | 1 | 1 |
| χ₅ | 38 | 49.0 | 12.1 | 5 | 2 | 1 |
| χ₃ | 16 | 34.8 | 11.2 | 6 | 1 | 1 |
| χ₃ | 38 | 58.9 | 14.6 | 5 | 2 | 1 |
| χ₃ | 80 | 111.1 | 17.6 | 3 | 3 | 2 |
| χ₄ | 16 | 28.9 | 8.4 | 6 | 1 | 1 |
| χ₄ | 38 | 51.6 | 11.0 | 5 | 2 | 1 |
| χ₈ | 16 | 18.4 | 6.8 | 6 | 1 | 1 |
| χ₁₃ | 16 | 10.0 | 4.3 | 6 | 1 | 1 |
| χ₂₉ | 38 | 11.9 | 3.3 | 6 | 2 | 1 |
| χ₃₁ | 38 | 8.5 | 3.7 | 4 | 1 | 1 |

## Fits

    ell = 6.10 τγ₁ − 19.3              rms 10.3  (28 %)
    ell = 5.18 τγ₁ − 8.2 (m>ν) + 31    rms 8.0   (21 %)
    ell = 4.51 τγ₁ + 16.4 (m>2ν) − 30  rms 6.2   (17 %)
    ell = 4.53 τγ₁ + 39.6 (m>3ν) − 48  rms 4.8   (13 %)

The last line is not a law. m>3ν
equals 1 on ten of eleven rows; the
coefficient 40 exists only to absorb
χ₃ µ=80 (the one row with a second
very long gap). Drop that row and
m>3ν is constant.

m>ν is worse than no m: too many
short gaps, same overtax as the
raw log-det.

## Reading

Leading term of −ln λ₀(Q) is τγ₁,
factor ~4–6 (Slepian 2c = τγ₁ would
be factor 1 on the leak; Q pays the
whole −ln λ₀ ~ a few times the
desert exponent). Extra gaps of
length ≲ 2ν do not show up as a
stable C₁ on this sample.

That is consistent with
`lemma2-Q-vs-det.md`: only long
pieces move Q; the one-set E with
every ν-gap is too fat.

Eleven points cannot separate C₁
from the intercept. A hold-out
character with a *second* gap ≫ 3ν
and a small desert would.
χ₃ µ=80 is the only such row we
have, and it is also the row with
N_eff=3, so C and the four-mode
state are entangled with m.

## Lemma 2 after the fit

The inequality to prove is closer to

\[
c_L \;\ge\; C\exp(-C_0\tau\gamma_1)
\]

with C₀ of order one, than to
exp(−C dim E). The gap tax, if it
exists in Q, is O(1) per *long*
gap and is not visible here as a
second regression term.
