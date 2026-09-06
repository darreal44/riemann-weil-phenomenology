# Convergence of Q(v)

Same v, χ₅, 3-plane H=A−P.

    μ      Q(v)
    7      0.072
    8      0.060
   11      0.028
   16      0.0055
   17      0.0049
   19      0.0070
   23      0.0060
   29      0.0090
   37      0.0040
   50      0.0034
   80      0.0049

After the drop 7→17, Q
lives in [0.003, 0.009].
Eleven points, no
monotonic limit, no
1/μ slope that would
hit 0. Mean on μ≥16:
0.0056. Std: 0.0018.

This is consistent with
a positive limit plus
χ(p)-noise of size
0.002 (`P-dynamics.md`).
It is also consistent
with a slow drift that
has not shown yet.

What “convergence of Q”
is *not*:
- λ_min(H₃) → 0 in
  float64 for μ≥16. That
  is the well of the
  3-plane, a different
  number, already on the
  floor.
- Q_L on the whole
  Paley–Wiener class
  (#42). Galerkin on
  three hats is Courant
  the wrong way for that
  infimum.

Q(v) looks like it has
settled. Settled is not
proved, and it is not
inf_{W_L} Q.
