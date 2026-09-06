# First arrival of a prime in P

μ grows, L=log μ.
When μ crosses an integer
n=p^k that carries
w(n)≠0, that n *arrives*
in P.

At the instant of
arrival, y=log n = L,
so θ_{nm}(L)=0
(`th_hat`: the window
ends at the sample).
The kick is zero that
instant (`P-dynamics.md`).
Then L grows past log n,
y/L drops from 1 toward
0, and that term walks
from 0 toward 2 w(n).

## The process

    arrivals ~ primes in
    dμ, density 1/log μ
    (not Poisson in L:
    dμ = e^L dL, so in L
    the rate is e^L / L)

Each arrival injects a
term that starts at 0
and drifts to 2w(p)
on a time scale
ΔL ~ O(1) (y/L from 1
to 1/e is ΔL=1).
Amplitude 2w(p) ~
2 χ(p) log p / √p
shrinks like
L e^{−L/2}.

Late arrivals are
smaller and rarer in L
(rate e^L/L grows, but
each kick shrinks
faster). Early arrivals
(2, 3) are the large
drifting terms we
already split out.

## What this is not

Not a Poisson point
process of zeros
(that is G, not P).
Not first-arrival
percolation. Not a
proof that the sum of
kicks stays behind A.
It is the mechanism
that makes P a
process with no P_∞
(`all-towers.md`).
