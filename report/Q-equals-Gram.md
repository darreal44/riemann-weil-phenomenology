# Closing (1): Q versus Gram

## Identity

Let f live in the cosine window of length L=log μ,
g = f ★ f̃ (even, supp g ⊂ (−L,L)). Then

    ∑_ρ ĥ(g)(ρ)  =  arch(g) − ∑_{n < μ} (Λ(n)/√n) g(log n)

LHS at ρ = 1/2 + iγ is the Gram of the hats.
RHS is the matrix Q assembled in scan_s / scan_q_*.

Hence, as quadratic forms on that window:

    Gram(f) − Q(f)  =  ∑_{ρ : Re ρ ≠ 1/2} ĥ(g)(ρ)
                       + (poles of L, if any).

## What “close (1)” can mean

Under RH (and after removing the pole of ζ), the sum
vanishes and **Q = Gram**. That is Weil’s explicit
formula, not a new lemma.

Unconditionally the difference is exactly the off-line
zeros. A uniform bound |Q−Gram| ≤ ε||f||² for all f
in the window, with ε smaller than λ_min(Gram), would
force those zeros not to exist — i.e. would prove RH
for that L. We do not have that ε.

## What we will not claim

That Lemma 2 on the Gram transfers to Q without RH.
That a numerical factor 2 between scan_s λ0 and
scan_gl2 λ0 “closes” the identity (conventions on
hats differ; both positive is consistent with RH,
not a proof).

## Status of (1)

Closed as an *identification*. Open as an
*unconditional inequality*. The remaining object is
RH, not a missing archimedean panel.
