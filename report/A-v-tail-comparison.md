# Comparison bound of I_{[1,L]} after #36/#37

Arb (#36) already encloses
the tail. Gauss (#37) closed
[0,1] as an arithmetic
check (remainder estimate
1.6×10^{-4}, not a
majorant of a^{(6)}).
This note records a
comparison on [1, L]
that does not use Arb.

## Sign change

    g(y) = 2 e^{-3y/2} − θ_v(y)

One zero y* ≈ 1.5900 in
(1, L). |g| is decreasing
on [1, y*] (sampled;
g(1)=−0.2229, g(y*)=0).
On [y*, L], g rises to
0.056 at y≈2.06 then
falls to g(L)=1/32.

w is decreasing
(1.403 → 0.502).

## Bounds

    |I₋| ≤ ½ w(1) |g(1)| (y*−1)
         = 0.092     (box)
         = 0.046     (triangle, |g| linear)

    I₊  ≤ ½ w(y*) max g · (L−y*)
         = 0.031

    I_{[1,L]} ∈ [−0.046, 0.031]

True value −0.0185 sits
inside. The interval is
ten times Q(v)≈0.0055
and three times the
±0.003 A-window.

## What it gives

A sign-split comparison
without quadrature. It
does *not* close Q(v)>0
by hand: feeding the
triangle into

    A = CST + I_{[0,1]} + I_{[1,L]}

with G₃ = −0.70066 and
CST = −0.10859 yields

    A ∈ [−0.855, −0.778]

which overflows
[−0.8303, −0.8244].
The missing factor two
on the tail is the
whole gap.

## Next

Prove |g| concave on
[1, y*] (then the
triangle is a theorem)
and a matching concave
majorant of g on
[y*, L] of height
< 0.03. Or write the
|a^{(6)}| majorant on
[0,1] so G₃ becomes a
proof, and keep Arb
for the tail.
