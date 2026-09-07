# Error of the quadratic support

On an interval of length h the Taylor remainder after the quadratic is

    R(y) = g'''(ξ) y³ / 6 (or (y−y_i)³ / 6 on a piece).

#83 avoids that formula by using m=inf g'' instead of g''(0). The price
is a systematic gap of order

    ∫_0^{y_q} ½ (g''(0)−m) y² dy ∼
    (9.6−4.2) y_q³ / 6 ≈
    5.4 × (0.21)³ / 6 ≈
    0.008

on g itself, before the weight ½w and before the rest of [0,1]. That is
the right order of the 0.021 improvement from #82 to #83 (the rest is
where the floor meets q).

A piece of length h with oscillation Δg'' has error ~ Δg'' h³/6 on g. To
put the g-error under 10⁻³ on [0,0.41] one wants h ≲ 0.1 if Δg''∼5 (four
or five pieces). That still leaves the integral against ½w and the
concave tail. The A-window ±0.003 is an integral error, not a pointwise
one; four pieces can plausibly halve 0.047 again, not divide it by 15.

No new run.
