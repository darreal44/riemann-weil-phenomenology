# Cauchy majorant of |a_odd^{(6)}| on [0,1]

Preregistered (`report/prereg-av-cauchy-odd.md`):
same r=2, two Gauss panels, elementary M.
Odd integrand s₀=3/4. Chebyshev-Markov of
a_odd^{(6)} does not freeze (`odd-a6.md`)
and rem 0.010 kills χ₃. Cauchy does not
use c_n. Same v, μ=16. Not RH.

## Execution

`python code/av_cauchy_odd.py`, 0.6 s.
`report/av-cauchy-odd.json`.

    r=2 < π
    sample max |a_odd| = 236
    elementary M         = 2307   (w_odd = e^{-x/2}/sinh)
    rem 1-panel          = 1.29×10^{-2}   > 0.00490
    rem 2-panel          = 2.01×10^{-4}   ≤ 0.00490

    G₃[0,1]         = −0.010913
    G₃ two-panel    = −0.010925

Same [1,L] termwise tail as
`av_enclose_odd_ball`. Folding ±rem:

    χ₃  Q ∈ [0.00469, 0.00743]
    χ₄  Q ∈ [0.01648, 0.01922]
    χ₇  Q ∈ [0.11555, 0.11829]

χ₃ Qlo>0. Markov N=16 remainder 0.010
would have gone through 0; two-panel
Cauchy does not.

## Verdict: SURVIVE (two panels)

The even transfer works for the odd
integrand. One panel is still too
crude. Two panels fit. Tail still
uses catalogued odd |g''|. One v,
finite μ. Not RH.

Judge: `tests/test_av_cauchy_odd.py`.

## Status

| Claim | Status |
|---|---|
| a_odd holomorphic dist(z,[0,1])<π | identity |
| Chebyshev-Markov a_odd^{(6)} closes χ₃ | **false** (`odd-a6.md`) |
| 1-panel Cauchy rem ≤ room | **false** (0.013) |
| 2-panel Cauchy rem ≤ room | judged (2.01×10^{-4}) |
| χ₃ Qlo>0 with this rem | judged (0.00469) |
| (∀ L) Q_L ≥ 0 | RH; not this note |
