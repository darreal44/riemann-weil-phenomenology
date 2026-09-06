# Numerical precision limits

Three ceilings, not one.

## 1. IEEE float64

53 bits ≈ 16 decimal digits.
A Rayleigh quotient assembled in
float64 cannot resolve λ ≲ 10⁻¹⁶
against Q-entries of size 1.
That is ℓ ≲ 37. Every scan that
prints ell=50 in float64 is
already in the underflow of the
type, not in Q.

`scan_s.py` uses mpmath. The
limit below is mpmath’s, not
NumPy’s.

## 2. Working precision versus cond(Q_N)

χ₃ µ=80, N=25, same matrix, dps
raised:

| dps | λ₀ | ℓ₀ | sign |
|---|---|---|---|
| 28 | −3.2×10⁻²⁹ | 65.6 | − |
| 36 | −1.1×10⁻³⁶ | 82.8 | − |
| 42 | −2.0×10⁻⁴⁴ | 100.6 | − |
| 48 | +5.6×10⁻⁴⁹ | 111.1 | + |
| 56 | +4.2×10⁻⁴⁹ | 111.4 | + |

Until dps ≈ 48 the computed λ₀ is
negative and |λ₀| ≈ 10^{−dps}.
That is the residual of `eigsy`
on a matrix of condition
cond(Q) ∼ 1/λ_min ∼ 10^{ℓ/ln 10}
≈ 10^{0.434 ℓ}. At ℓ=111 one
needs ≈ 48 decimals plus a guard
band. dps=42 is not enough; the
sign is garbage. dps=48 and 56
agree to 0.3 nats (relative 25 %
on λ, which is one digit — the
eigenvalue is at the last place
of dps=48).

Rule used in the scans: dps ≳
0.45 ℓ + 8. The pair
(NB=24, dps=48) sits on that
line. (NB=26, dps=56) is the
last certified SPD window.
(NB=28, dps=64) flips sign
again; raising dps does not
bring it back. That flip is
Galerkin, not rounding.

## 3. Cancellation inside a correct eigenvalue

Even at dps=48, with λ trusted
to one digit, the split

    H + C + T = λ,    H = T,    C = −2H

is a cancellation of two terms of
size 10⁻⁴ down to 10⁻⁴⁹ — fifty
decimals of internal loss. It
only sums if H, C, T are formed
in the same mpmath matrix that
`eigsy` used. Forming them in
float64 after the fact gives
H+C+T ∼ 10⁻¹⁸ and a meaningless
partition (the “share” column
that blew up to 10³³).

The identity H=T is therefore a
statement at working precision,
not a float64 observation.

## What the digits do not give

- A proof that λ_min > 0. Extra
  dps after 48 changes the 25th
  bit of a 10⁻⁴⁹ number; it does
  not produce a symbol.
- The value 111.1 as an analytic
  constant. It is Galerkin-plus-
  rounding at the certified edge.
- Any entry of H = A−P at the
  10⁻⁶ scale on a 3×3 (those
  entries are O(10⁻⁴) against
  O(1) summands — four digits,
  comfortable in dps=16 already).

Short windows (χ₅ µ=16, ℓ=33)
are in the safe zone of dps=40
with twenty digits to spare.
The deep well is not.
