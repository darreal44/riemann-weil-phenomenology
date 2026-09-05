# Haar filters on the module

A Haar filter of multiplicative width ε around α ∈ R_+* is

    (H_ε φ)(α) = (1/(2ε)) ∫_{log(λ/α) ∈ [-ε,ε]} φ(λ) d*λ
               = (1/(2ε)) ∫_{α e^{-ε}}^{α e^{ε}} φ(λ) dλ/λ.

It is the average for Haar measure, not a linear average in λ.
As ε→0, H_ε φ(α) → φ(α) at continuity points; against a Dirac
of mass m at α it returns m as soon as the window contains
no other atom.

## Against τ₂

Shells sit at λ=2^n. The gap in log-scale is log 2. Any
Haar filter about λ=2 with ε < log 2 sees only n=−1 and
returns the shell mass 1/√2. That is ⟨τ₂, h_ε⟩ for
h_ε = (1/(2ε)) 1_{[2e^{-ε}, 2e^{ε}]}, a test function
allowed by Theorem 4. No Fmat.

## Against τ_Λ (finite cutoff)

H_ε τ_Λ(2) is exactly the Fmat integral we already ran,
with a multiplicative window instead of |λ−2|<0.12·2.
The peak is still width ∼Λ^{-2} with Gibbs lobes. Changing
the window shape (Haar / Hann / trapezoid) does not turn
that bump into a Dirac. We tried Hann (`campaign_2adic_taper`).
A Haar filter on the same curve is the same number to
O(ε²). Do not run it.

## Wavelets

The Haar *wavelet* (difference of two adjacent averages) on
d*λ would see the jump of a step, not a Dirac mass. τ₂ is
a combination of Diracs. The useful filter is the average
H_ε, not the wavelet. High-pass Haar coefficients of τ_Λ
are the Gibbs ringing.

## Status

Analytic Haar filter: mass 1/√2 for ε < log 2. Numerical
Haar filter on Fmat: already answered by the trapezoid
campaign. No new run.
