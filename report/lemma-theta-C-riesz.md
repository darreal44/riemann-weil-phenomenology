# Two different C's

Evaluation at t=0 in the hat basis is

    ε  =  w · v,     w = (1, √2, √2, …, √2).

Two quadratic-form problems.

**A. Ground state (the bump).**
min vᵀ Q v on ‖v‖=1. Output λ₀, ε₀ = w·v₀,
C_bump = L λ₀ / ε₀².  This is the C of the
tables (0.09 on ζ, 0.12–0.16 off ζ).

**B. Cheapest edge (Riesz).**
min vᵀ Q v on w·v = 1. Output
1 / (wᵀ Q⁻¹ w),
C_Riesz = L / (wᵀ Q⁻¹ w).

A = B iff v₀ ∥ Q⁻¹ w, i.e. iff the ground
state is the representer of δ₀. It is not:
v₀ is a bump at L/2 whose tail at 0 is an
accident of cancellation. Q⁻¹ w is an
edge spike.

µ=11, ζ, dps=22:

| dim | C_Riesz | C_bump | λ_min |
|---|---|---|---|
| 2 | 0.071 | 0.162 | 7.4×10⁻⁶ |
| 3 | 0.042 | — | 3.5×10⁻⁹ |
| 4 | 0.031 | 0.112 | 3.0×10⁻¹² |
| 5 | 0.025 | — | 7.9×10⁻¹⁵ |

C_Riesz is systematically smaller: it is
cheaper to spend the mass at the edge than
to leak from the middle. The factor ~2
between C_bump and C_Riesz at two modes is
that price.

1/(4e) = 0.092 is C_bump after four modes
on ζ, not C_Riesz (which is already 0.03
at four modes). Identifying 1/(4e) with a
local kernel of δ₀ was the wrong object.

The identity that remains is still
C_bump = L λ₀ / ε(v₀)². Closing it means
controlling ε(v₀) for the bump, not
inverting Q on w.
