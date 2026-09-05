# Gram artifacts and saturation

## Saturation in N (basis)

At fixed μ, λ0 of the Gram *rises* a few percent from N=25 to
N=67 (ell falls). χ₂₉ μ=22: 6.90e-3 → 7.76e-3. 11a1 μ=22:
1.76e-10 → 3.51e-10. The extra cosines do not invent a
deeper mode; they slightly lift the floor. N=37 is already
on that plateau for the isolated characters.

## Artifact: indefinite Gram

χ₅ at μ=22 and μ=38: λ0 is 10^{-15} *negative* for N=25 and
37, still negative at μ=38 N=67. That is not a physical
negative Weil form. The cosine basis truncated at NB, with
hats evaluated only on zeros below ~ω_max, is an incomplete
quadrature of a positive kernel. χ₅ has the large desert:
few zeros under the band at large μ (19–32 points at μ=38
for N=25–37), the Gram is rank-deficient + rounding.

Rule: if λ0 < 0 or |λ0| < 10^{-14} with a sign flip under N,
**discard the Gram ell**. Use prime-side Q (`scan_s`), which
stayed positive for χ₅ (ell=86.7 at μ=38).

## Who is clean

χ₂₉, χ₃₁, 11a1–67a1: λ0 > 0 and monotone in N at these
windows. Their Gram ell is comparable across N. χ₅ Gram is
not. 11a1 at μ=38 sits at 10^{-15}: on the edge; ell~33 is
a log of a rounding scale — treat the *slope* 22→38 as
softer than χ₂₉.

## What saturation is not

The freeze of C(χ) in μ (`nonlinear-saturation.md`) is
not this N-effect. One is a physical plateau in the window
length; the other is “we gave the basis enough bars.”
