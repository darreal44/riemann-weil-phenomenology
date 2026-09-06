# Marchenko–Pastur versus the bulk of T

MP law: ESD of (1/p)XXᵀ,
X n×p iid, c=n/p, variance σ².
Support

    [(1−√c)² σ², (1+√c)² σ²],
    mean = σ².

T is deterministic (one Gram
per window). This is a shape
comparison on 32 pooled
eigenvalues > 0.5, not a test.

## Fit

Pooled bulk: min 1.07, max 4.41,
mean 2.95.

Edge ratio ⇒ c = 0.12, σ² = 2.95.
MP support [1.28, 5.29] —
too far right, a bit too
tight on the left.

## DOS

    bin        emp    MP
    [1.0,1.5]  0.19   0
    [1.5,2.0]  0.13   0.34
    [2.0,2.5]  0.13   0.36
    [2.5,3.0]  0.63   0.33
    [3.0,3.5]  0.38   0.29
    [3.5,4.0]  0.31   0.24
    [4.0,4.5]  0.25   0.19
    [4.5,5.0]  0      0.13

The mass sits in [2.5, 3.5],
narrower and more peaked
than MP. MP wants a long
right tail to 5.3 that T
does not have.

## Reading

T is not a Wishart. The hats
are a deterministic ONB of
a short interval, not iid
columns. Diagonals of T are
already 2–3 (`Q-matrix.md`);
the off-diagonals are a
smooth kernel, not noise.
A shifted MP with c≈0.1
is a coarse envelope
(support width ~3), not
a law of T.

The outliers λ < 0.5 were
excluded on purpose: they
are the collapsing Slepian
of T, a feature MP does
not produce at this c.
