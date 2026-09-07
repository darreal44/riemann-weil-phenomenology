# Lower bounds in the M page

M-by-hand is an
*upper* bound.
The lower bounds
that feed it:

    ln 2 > 0.693
        ⇒ π/ln 2 < 4.534
    sin 2 > 0.9
        ⇒ 1/sin 2 < 10/9
    e² < 7.389 is an
    upper; the matching
    lower e² > 7.389
    is not needed
    for M.

A lower bound *for
M itself* is the
sampled max |a| on
the stadium: 221.
So

    221 ≤ M_* ≤ 4010

The true max on the
r=2 neighbourhood
sits in between.
The certificate
uses 4010. The
factor 18 is slack,
not a hole.

Qlo = Alo − P is
the live lower
bound of the
witness:

    Q ≥ 0.00516
    (#54, machine G₃)
    R₂ hand < 3.53×10⁻⁴
    so if one keeps
    the machine G₃
    and swaps in
    the hand R₂,
    Qlo drops by
    at most
    3.53e-4 − 3.39e-4
    ≈ 1.4×10⁻⁵
    still > 0.005.

A hand *lower*
bound of G₃ would
need interval
evaluation of a
at the three
nodes (the step
we refused).
Without it, the
lower bound on Q
still leans on
the machine G₃.
The hand work
closed only the
remainder.
