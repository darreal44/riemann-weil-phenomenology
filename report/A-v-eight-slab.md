# Eight-slab trapezoid: A(v) inside the window

Remainder n h³/12 M with
M = max|a''| sampled
(1.333 on [1, 1.59],
0.344 on [1.59, L]).

## Halves

              n=4              n=8
    [1, 1.59] [−0.0372, −0.0344]  [−0.0356, −0.0349]
    [1.59, L] [ 0.0128,  0.0187]  [ 0.0156,  0.0171]

Eight + eight:

    I_{[1,L]} ∈ [−0.02000, −0.01780]
    true        −0.01850

## A(v)

    CST = −0.108593739
    G₃  = −0.700661
    + I ∈ [−0.02000, −0.01780]

    A(v) ∈ [−0.82925, −0.82705]

The room that keeps Q>0
after ±0.003 on P_rest is
[−0.8303, −0.8244]
(`rational-witness-chi5-mu16.md`).
This interval sits *inside*
that room.

## Cost

Nine evaluations of θ_v
on [1.59, L] plus five
on [1, 1.59], all
elementary. M is still
a sampled max of a'',
not a majorant. With a
proved M ≤ 1.4 and
M₊ ≤ 0.35 the same
arithmetic is a proof
of A(v) ∈ [−0.8303, −0.8244]
and therefore of Q(v)>0
for this rational
witness, without Arb
and without an
eigensolver.

That is the last
analytic missing piece
on this vector: bound
a'' = (½ w g)'' from
the already written
g'', w', w''.
