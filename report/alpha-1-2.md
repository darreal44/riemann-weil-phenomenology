# α₁, α₂

np.linalg.eigh(H) already
had them. av_other_v.py
now ships evals, evecs,
alpha.

μ=16:  λ = (2.3×10⁻⁶,
0.00225, 0.522)
μ=150: λ = (7.8×10⁻⁹,
0.00031, 0.394)

    v          α₁16   α₂16    Q16
    (4,−3,1)  −0.027  0.103  0.0055
    (5,−4,1)  −0.016  0.052  0.0014
    (4,−3,0)   0.119 −0.030  0.0005
    (1,−1,0)   0.022 −0.134  0.0094
    (3,−2,1)  −0.045  0.191  0.0190

(4,−3,0) loads the
*middle* mode
(λ₁=0.002) and almost
misses λ₂=0.52. That
is the 0.03 vs 0.50
in Q/(1−α₀²). The
other four sit on λ₂.

Reconstruction
∑ λ_i α_i² = Q
to the printed digit.
No new assemble.
