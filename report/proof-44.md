# What #44 proves — and does not

#44 is not a proof. It is
a killed prediction plus
two json tables.

## The prediction (locked)

Linear in μ through
(+0.38 at 38) and
(+0.093 at 62) crosses
zero at μ≈70. Same
crossing in ℓ of the
full form (ℓ≈16.2).
Claim: drop-3 λ₀(74)<0
and λ₀(80)<0.

## The execution

`gl2_quorum_scan.py` on
the prime-side S=A−P,
NB=80, dps=50.

    μ=74  drop-3 λ₀ = +0.090
    μ=80  drop-3 λ₀ = +0.090
    |Δ| < 0.01  (judge)

Full λ₀ kept falling
(5.3×10^{-7} → 2.8×10^{-8}).
Every other interior
voter stayed necessary.

## What that establishes

1. The linear model in μ
   (and the linear model
   in ℓ) is false on this
   range. A line is not
   a crossing-time
   (`linearity-kill.md`).
2. On 62–80, drop-3 λ₀
   is a plateau at 0.09,
   not a delay.
3. “3 joins once ℓ≳16”
   is false for 37a1.

## What it does not

- Not Q_L≥0 for all L.
- Not “3 is forever
  dispensable”. A later
  μ can still flip.
- Not a theorem about
  the floor: 0.09 is
  measured twice, not
  derived from A−P.
- Not Gram, not RH.

The judge only checks
the json against the
preregistration. It does
not certify the assemble.
