# Preregistration: enclose A(v) with Gauss+Cauchy on [1,L]

Locked before the rewrite. Same v, μ=16.
Not a covering lemma. Not RH.

`enclose_cauchy` still uses 8+8 trapezoid
on [1,L] with catalogued |g''|. Trap n=8
remainder ~1.4×10^{-3} (`trap-convergence.md`).
Cauchy on [1,L] at 8 panels is elementary
1.25×10^{-5} (`av-cauchy-tail.md`). Replacing
the tail is a rewrite, not a larger n.

**This run.** Shipped `code/av_enclose_cauchy.py`:

- even: 2-panel G₃ on [0,1] ± Cauchy rem
  + 8-panel G₃ on [1,L] ± Cauchy rem
- odd: same panels, odd elementary M, χ₃/χ₄/χ₇

No trapezoid. No |g''| catalogue.

**Prediction.** Even A-ball stays inside
[−0.8303, −0.8244], Qlo>0. χ₃ Qlo>0.
Tail rem is negligible next to the [0,1]
two-panel rem.

**Kill.** Even A-ball leaves the window,
or even Qlo≤0, or χ₃ Qlo≤0.
