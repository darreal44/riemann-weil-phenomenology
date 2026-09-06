# λ in tau_curve

    ϑ(λ) g(r) = λ^{−1/2} g(r/λ)
    idx = floor(x_in / λ / h)
    τ(λ) = λ^{−1/2} ∑ W[idx, i] w_i

The slice coordinate λ
*is* the dilation
factor. Support of g
stretches by λ.
That is |u| acting by
dilation, i.e. the
**module** convention
λ = |u|_2, peak at
n=−1, mass 1/√2
after one √λ twist.

Then two extra
factors sit on top:

1. λ^{−1/2} already
   inside τ(λ)
2. w₂ = ∫ τ(λ) dλ/λ
   (another Haar)

A Dirac of mass m in
d*u, pushed sloppily,
can pick up 1, √λ, 1/λ
and land on
1/√2, (log 2)/√2, or
√2. That is why three
targets exist for one
peak.

#46 likes √2. The
formula of ϑ likes
1/√2. The integrand
dλ/λ likes a
multiplicative reading.
Until one of those
factors is dropped
on purpose and the
number freezes, the
identification is
not the code as it
stands.

Read of `trace_dist.py`
line 19: module
dilation. Read of
#46: inverse mass.
They disagree.
