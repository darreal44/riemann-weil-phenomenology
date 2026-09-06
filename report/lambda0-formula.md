# What λ₀ is

On the cosine hats
η_n(t) on [0, L], L=log μ,
n=0..N,

    Q(f) = A(f) − P(f)

A = archimedean panel
(s₀ = 1/2 and 1 for GL2,
s₀ = 1/4 or 3/4 for GL1)
plus CST. P = sum over
prime powers of
Λ_f(n) n^{−1} θ(log n)
(GL2 FIX path), or
χ(n) Λ(n) n^{−1/2} θ
(Dirichlet).

The matrix S is

    S_{nm} = A(η_n,η_m) − P(η_n,η_m).

Then

    λ₀ = λ_min(S)     (mp.eigsy)
    ℓ₀ = −ln |λ₀|     if λ₀ ≠ 0

That is the number printed
as `lam0` in `scan_s`,
`scan_q_gl2`, and the
quorum scan.

## Two different λ₀

- **Q / quorum.** S = A−P
  as above. No zeros.
  λ₀>0 is a positive
  witness on this
  Galerkin space. λ₀<0
  after drop p means p
  is necessary.
- **Gram / wells.**
  G = 2 Φ*Φ, Φ = hats
  sampled at the zeros.
  λ₀(G) is e^{−ℓ₀} with
  ℓ₀ = 11–35. Different
  matrix, different
  meaning.

Do not add them.

## What λ₀ is not

Not inf_{W_L} Q
(#42: Galerkin is Courant
the wrong way). Not a
zero of L. Not the
Mott gap. A certificate
λ₀>0 on V_N is an upper
bound on the depth of
the well of *this* S,
nothing else.
