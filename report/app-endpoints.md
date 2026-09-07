# Extrema of w'' and g' are at the ends

## w''

No zero of w''' on [1, L]
(400-node sign chart).
w'' is positive and
decreasing:

    w''(1)    = 1.9432
    w''(1.59) = 0.4951
    w''(L)    = 0.1374

So max|w''| is an
endpoint value, elementary
(closed form in `av_app.w_pp`).

## g' on [1, 1.59]

g'' < 0 already
(`gpp-critical.md`), so
g' is decreasing and has
no critical point.

    g'(1)    = 0.5510
    g'(1.59) = 0.2398

max|g'| = g'(1).

## g' on [1.59, L]

One zero of g'' at
y ≈ 2.341. There
g' = −0.0556.

    g'(1.59) = +0.2398
    g'(2.34) = −0.0556
    g'(L)    = −0.0278

max|g'| = g'(1.59), an
endpoint of this half
and already used above.

## Termwise M from endpoints

    [1, 1.59]
      |w|≤w(1)=1.4029
      |w'|≤|w'(1)|=1.1406
      |w''|≤w''(1)=1.9432
      |g|≤|g(1)|=0.2229
      |g'|≤g'(1)=0.5510
      |g''|≤0.707
      M ≤ ½(1.943·0.223 + 2·1.141·0.551 + 1.403·0.707)
        = 1.341

    [1.59, L]
      |w|≤w(1.59)=0.942
      |w'|≤|w'(1.59)|=0.553
      |w''|≤w''(1.59)=0.495
      |g|≤0.0564
      |g'|≤0.2398
      |g''|≤0.552
      M ≤ 0.407

Same numbers as
`app-leibniz.md`, now
justified by monotonicity
plus one interior critical
point of g' whose value
is smaller than the end.

g'(1) and g(1) still use
θ_v(1) and θ_v'(1), six
sines at y=1, t=1/L.
