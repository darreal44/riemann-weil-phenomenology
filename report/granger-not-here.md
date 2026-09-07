# Granger tests, not here

Granger: X “causes” Y
if past X improves
the forecast of Y
beyond past Y alone.
It needs a *series*
(dozens of lags),
stationarity or a
careful difference,
and a lag order.

We have three μ
(80, 84, 100) and
two drops. That is
not a series. An
F-test on two lags
with n=3 is
undefined. Fitting
drop-3_t ~ drop-3_{t-1}
+ drop-83_{t-1} has
zero degrees of
freedom.

What Granger would
require here: a
2-unit grid on
[80, 120], two
columns (drop-3,
drop-83), then a
lag-1 VAR and an
exclusion test.
Even then it would
say “helps
forecast”, not
“83 makes 3
necessary”. μ is
not time in a
stationary market;
each step adds a
prime and lengthens
L. The innovations
are arrivals, not
noise.

The timed fact we
already have does
not need Granger:
at the only arrival
we resolved, 83
moved drop-3 and
did not flip it
(`temporal-causality.md`).
That is a lead-lag
of one night, read
off the table.
