# Weighted-shift bound

Let
B
be
the
symmetric
codiagonal
with
weights
a_n = Q_{n,n+1}.
Then

    ⟨Bx,x⟩
      = 2 ∑ a_n x_n x_{n+1}
      ≤ 2 M ∑ |x_n x_{n+1}|
      ≤ M ∑ (x_n² + x_{n+1}²)
      ≤ 2 M ‖x‖²,

where
M = sup |a_n|.
Hence
‖B‖ ≤ 2M.

On
B₁^Θ
one
has
M ≤ |w₂| · 2/π ≈ 0.312
(closed)
or
0.286
(measured
up
to
n=399),
so
‖B₁^Θ‖ ≤ 0.624
or
0.572.
The
section
hits
0.396.

The
bound
is
not
sharp
when
a_n
changes
sign
(here
it
does,
every
few
n).
A
sign-aware
estimate
is
possible
but
is
another
note.
Other
lags
need
their
own
2M_k;
∑_k 2M_k
diverges
if
M_k ∼ 1/k.

Not
RH.
