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

- majorant of a^{(6)} on [0,1]
  (even and odd)
- comparison estimate of I_{[0,1]}
- (∀ L) Q_L ≥ 0   (= RH)

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
