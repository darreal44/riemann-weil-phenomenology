# Cauchy majorant of |a^{(6)}| on [0,1]

Preregistered (`report/prereg-av-cauchy-a6.md`):
a is holomorphic on dist(z,[0,1])<π. Cauchy
|a^{(6)}| ≤ 6! M / r^6 at r=2. One Gauss
panel may miss the A-room 0.00091; two
panels of length 1/2 scale the remainder
by 1/64. Elementary M, not the sample.
v=(4,−3,1)/√26, χ₅ μ=16. Not RH.

## Execution

`python code/av_cauchy.py`, 32 cores on the
stadium, 0.5 s. Table:
`report/av-cauchy-a6.json`.

    r=2 < π
    sample max |a| = 221
    elementary M    = 3889   (|θ_v|≤cosh, |w|≤e^{x/2}/|sin r|)
    M₆ elem         = 4.37×10⁴
    rem 1-panel     = 2.17×10^{-2}   > 0.00091
    rem 2-panel     = 3.39×10^{-4}   ≤ 0.00091

min |sinh| on the caps equals |sin 2|
(attained at ±2i). Composite G₃:

    G₃[0,1]              = −0.700661
    G₃[0,½]+G₃[½,1]      = −0.700797

Same tail as `av_enclose` (8+8 trapezoid,
catalogued |g''|). With ±rem on the
composite G₃:

    A(v) ∈ [−0.829863, −0.826716]
    Q(v) ∈ [ 0.003542,  0.006688]

Inside [−0.8303, −0.8244]. Qlo>0.

## Verdict: SURVIVE (two panels)

The [0,1] Gauss remainder is a Cauchy
estimate: six elementary |θ_nm| by
cosh(ω r), |w|=e^{Re z/2}/|sinh z|,
|sinh| ≥ |sin r| on |Im z|=r and on
the caps (floor attained at ±ri).
One panel is too crude. Two panels
fit. The chord comparison of I_{[0,1]}
is still dead (misses 0.22). The tail
still uses catalogued |g''|. One v,
finite μ. Not RH.

Judge: `tests/test_av_cauchy.py`.

## Status

| Claim | Status |
|---|---|
| a holomorphic for dist(z,[0,1])<π | identity (poles kπi) |
| 1-panel Cauchy remainder ≤ room | **false** (0.022) |
| 2-panel Cauchy remainder ≤ room | judged (3.39×10^{-4}) |
| A-ball inside the Q-window | judged |
| Qlo>0 with this remainder | judged (0.00354) |
| chord comparison of I_{[0,1]} | still open (misses 0.22) |
| (∀ L) Q_L ≥ 0 | RH; not this note |
