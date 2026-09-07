# Stationarity, for these series

A series x_t is
(weakly) stationary
if E x, Var x, and
Cov(x_t, x_{t+k})
do not depend on t.

drop-3(μ) on 37a1
is not that:

    μ     drop-3
   62     +0.093
   80     +0.089
   84     +0.048
  100     −0.418
  150     −0.826
  250     −1.016

Mean and variance
depend on μ. After
100 the series sits
on a shelf then
drifts down. That
is a level shift
plus a slow trend,
not a stationary
noise around 0.

Why: each step μ
changes the
*operator* (new
primes, larger L).
The increment is
an arrival, not an
iid shock. L=log μ
is logarithmic
time. Even Δ
drop-3(μ) is not
stationary — the
cliff is one
jump, then a
shelf.

Differencing once
would turn the
cliff into a spike
and the shelf into
near-zero. It would
not make a Granger
test legal on three
points, and it would
throw away the
object we care
about (the sign).

Full λ₀(μ) is worse:
it falls like a
well depth, roughly
log-linear in ℓ,
exponential in the
printed λ₀. log λ₀
might look smoother.
Still not a reason
to VAR it.

Stationarity is a
hypothesis about
one data-generating
process repeating.
Here the process
is the explicit
formula with a
moving cutoff.
It does not
repeat.
