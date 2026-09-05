# Daubechies wavelets on the slice

Daubechies dbN are compactly supported orthogonal wavelets
on R, vanishing moments N. They are built for additive
translation, not for Haar measure on R_+*.

## Against τ₂

τ₂ is a train of Diracs at λ=2^n in d*λ. A wavelet with
vanishing moments, integrated in dλ against a Dirac, returns
the wavelet itself at that point — an oscillating number
that depends on the scale and the shift. It does *not*
return the mass. Masses are low-pass (scaling function
φ, integral 1). The Daubechies scaling function on the
*additive* log-coordinate t=log λ is a Haar filter with
a smoother window. For a window narrower than log 2 it
again returns 1/√2. That is H_ε with a different shape.
Already answered.

## Against τ_Λ

Projecting the Fmat curve on dbN details at small scale
isolates the Gibbs ringing (the high-pass part). The
scaling coefficients at scale ~Λ^{-2} are the unresolved
peak. Changing N (more vanishing moments) makes the
ringing look nicer; it does not move the integral to
1/√2. Same verdict as Hann and Haar filters.

## Status

No implementation. Daubechies are the wrong group (R,+)
for a question already settled on (R_+*, d*λ). The
scaling-function pairing is the Haar filter of
`haar-filters.md`.
