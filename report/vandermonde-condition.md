# Cosine Vandermonde on [0,L]

Columns
1, cos(t_j y),
y∈[0.02,L],
60 points.
t_j of the
χ₈ fit.

    #cols   κ
    1       1.0
    2       2.66
    3       3.00
    4       3.19
    5       3.19
    6       3.21

Spaced t
(~4–5)
stay at
κ≈3.
lstsq is
stable.
rms 10⁻⁴
is not
κ.

Same
grid,
t=1.85
and 1.95
(Δt=0.10):
κ≈285.
That is
the
ill-
conditioned
regime
(almost
collinear
cosines
on a
short
interval).
The
greedy
fit
avoided
it by
construction
(Δt≥0.12
and
actual
gaps
~4).

No
reason
to
regularise
the
atomic
lstsq
on this
t-set.
