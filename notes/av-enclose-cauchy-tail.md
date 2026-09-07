# Enclose A(v) with Gauss+Cauchy on [1,L]

Preregistered (`report/prereg-av-enclose-cauchy-tail.md`):
replace the 8+8 trapezoid (catalogued |g''|, rem ~1.4×10^{-3})
by 8-panel G₃ ± elementary Cauchy rem (1.25×10^{-5}).
[0,1] stays two-panel Cauchy (#52 / #53). No trap.
Same v, μ=16. Not RH.

## Execution

`python code/av_enclose_cauchy.py`.
`report/av-enclose-cauchy-tail.json`.

Even χ₅:

    I_{[0,1]}  = −0.700797 ± 3.39×10^{-4}
    I_{[1,L]}  = −0.018500 ± 1.25×10^{-5}
    A(v) ∈ [−0.828243, −0.827540]
    Q(v) ∈ [ 0.005162,  0.005865]

Inside [−0.8303, −0.8244]. Qlo>0.
Old trap enclose was A ∈ [−0.82939, −0.82692],
Q ∈ [0.00402, 0.00649]. The ball is tighter
because the tail rem dropped two orders.

Odd:

    χ₃  Q ∈ [0.00570, 0.00610]
    χ₄  Q ∈ [0.01749, 0.01790]
    χ₇  Q ∈ [0.11656, 0.11697]

χ₃ Qlo>0. Tail rem 1.88×10^{-6}.

## Verdict: SURVIVE

The whole remainder of A(v) is now Cauchy
(cosh / |sinh| on r=2). The |g''| catalogue
is not used. Trap n=8 is obsolete for this
enclose. Chord comparison of I_{[0,1]} is
still open. One v, finite μ. Not RH.

Judge: `tests/test_av_enclose_cauchy.py`.
`av_enclose.py` keeps the trap path.

## Status

| Claim | Status |
|---|---|
| trap n=8 rem > Cauchy-8 rem | judged (`trap-convergence.md`) |
| even A-ball inside window | judged |
| even Qlo>0 | judged (0.00516) |
| χ₃ Qlo>0 | judged (0.00570) |
| |g''| still required | **false** (this enclose) |
| (∀ L) Q_L ≥ 0 | RH; not this note |
