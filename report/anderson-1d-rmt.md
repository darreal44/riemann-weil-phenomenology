# 1D Anderson and random matrices

## 1D Anderson

On ℓ²(Z), −Δ + V_ω with iid V localizes at every energy, any
λ>0: Lyapunov exponent γ(E)>0, eigenfunctions e^{-γ|n-n0|}.
No mobility edge in 1D.

The cosine chain of the window is a finite path of length N.
A 1D Anderson model on that path would need a random on-site
potential. Q’s diagonal in that basis is not iid: it is the
Gram of {φ_n(γ)} against a deterministic Γ. Transfer-matrix
Lyapunov of Q has no meaning at N=33.

If one insists: v0 decaying after n=2 is *faster* than any
1D Anderson ξ (two sites). That is a two-level system, not
a localized 1D wave.

## Random matrices

Two different matrices in this project.

1. **Q / Gram**, class AI / GOE symmetries (`altland-zirnbauer.md`).
   Finite, deterministic given Γ. Eigenvalue law is one isolated
   λ0 plus a bulk O(1), not Wigner’s semicircle. Level spacings
   of the bulk of Q have never been a GUE/GOE test here (N too
   small, and the bulk is not a continuum spectrum).

2. **The zeros Γ themselves.** Montgomery–Odlyzko: pair
   correlation of γ agrees with GUE. That is a statement about
   L-functions, not about spec(Q). The charged pair being
   tighter than ν is compatible with GUE level repulsion
   *failing locally* at that height (a small gap), which GUE
   allows with small probability. It is not an RMT prediction
   of v0.

## What not to mix

Anderson 1D ⇒ all states localized, any disorder.
GUE zeros ⇒ local statistics of Γ.
GOE class of Q ⇒ T²=+1 on a real Gram.

Three sentences, three objects. None gives C(χ) or c_L
without RH. No 1D Lyapunov to compute on these dumps.
