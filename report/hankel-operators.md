# Hankel operators in the tail

A Hankel operator on ℓ²(ℕ) has matrix H_{n m}=c_{n+m} (or c_{n+m+1}).
Here the smooth part of T off the head is essentially

    Off_{n m} ∼ 1/(n+m)

coming from the integral of a slow kernel against two high cosines
(integration by parts / Hilbert kernel). That is a Hankel matrix with
c_k=1/k.

Nehari: ‖H‖ equals the distance of the symbol to H^∞. Hilbert’s
inequality gives ‖[1/(n+m)]‖≤π without naming the symbol. The scripts
use that norm, not a Nehari computation.

A true Hankel would have exactly c_{n+m}, no T₂ atoms, no head cut. T is
Hankel plus a finite-rank (or HS) error plus the lags log p. ρ_far sees
the sum of those pieces divided by qmin_far. When the atoms grow, the
matrix is less Hankel, not more.

No Adamyan– Arov– Krein or Hartman theorem is used. Those would be
another way to bound the same tail, not a new take of W_L.
