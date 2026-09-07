# Rational witness — status

v = (4, −3, 1)/√26, three hats,
μ=16, no eigensolver. Not RH.

## Even (s₀=1/4), enclosed

Same integrand for every a=0.
CST = log(q/π)−γ−log(1−1/256).

    python3 code/av_enclose.py        # χ₅
    python3 code/av_enclose_even.py   # eight even χ

    χ₅   Q ∈ [0.00402, 0.00649]
    χ₈   Q ∈ [0.08529, 0.08776]
    …    all eight Qlo>0
    χ₅ is the tight even window.

Pieces: elementary CST, G₃ of a,
8+8 trapezoid, Leibniz |a''| from
endpoint w and catalogued g''
extrema. G₃ remainder (a^{(6)})
is still a check, not a majorant.

## Odd (s₀=3/4), enclosed on [1,L]

Different a. G₃ is a check.
Leibniz M on [1,L] from
catalogued g_odd'' extrema.

    python3 code/av_enclose_odd_ball.py

    χ₃   Q ∈ [0.00574, 0.00639]   sampled M
         Q ∈ [0.00490, 0.00724]   termwise M
         Q ∈ [0.00441, 0.00743]   G2∘G2 M4=23.5 + Leibniz
         Q ∈ [0.00388, 0.00796]   G2∘G2 M4=60 Markov + Leibniz
    χ₄   Q ∈ [0.01754, 0.01819]
    χ₇   Q ∈ [0.11661, 0.11726]
    χ₃ is the tight odd window.

g(L)=1/2, g''(L)=1/8 exact.

## Still open on this vector

- comparison estimate of I_{[0,1]}
  (chord misses by 0.22)
- (∀ L) Q_L ≥ 0   (= RH)

Even a^{(6)} on [0,1]: Cauchy
two-panel (`notes/av-cauchy-a6.md`).
Odd a^{(6)} on [0,1]: Cauchy
two-panel (`notes/av-cauchy-odd.md`).
Chebyshev-Markov of a_odd^{(6)}
does not freeze; Cauchy does.

## Tail of v (hats n=3,4,5)

Q_head = 0.00551. Schur
correction vᵀ C T⁻¹ Cᵀ v
= 0.00403. Left 0.00148.
Elementary lower bound
Q_head − ‖Cᵀv‖²/λ_min(T)
= 0.0002 > 0
(`report/schur-v.md`).
Higher hats do not eat
the sign.

## Other windows, same v

μ-scan on χ₅ (`v-vs-mu.md`,
`v-prime-jumps.md`): Q>0
from μ=7 to 31, minimum
0.0049 at μ=17, then a
0.005–0.009 band.

Six characters at μ=16
(`v-across-chi.md`): χ₃
0.0059, χ₅ 0.0055, others
0.018–0.39. Both parities.
Not (∀ χ)(∀ μ).

## H-budget at μ=16

∂Q/∂H₀₁ = −0.92. Killing
Q needs |ΔH₀₁|≳0.006
(`report/H-impact.md`,
`report/H-sensitivity.md`).
cond(H)=1.6×10⁴ is the
well, not entry noise.
