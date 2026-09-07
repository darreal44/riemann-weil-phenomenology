# Impact of v on Q

Q is a quadratic form
on the 3-plane. On an
eigenvector q_i of H,

    Q(v) = λ₀ α₀² + λ₁ α₁² + λ₂ α₂²

λ₀ = λ_min ≪ λ₁,λ₂.
A vector close to
v_min is dominated
by λ₀; a vector
orthogonal to v_min
sees only the bulk
O(0.1).

μ=16 and μ=150,
overlap with v_min:

    v          ov16    Q16      ov150   Q150
    (5,−4,1)   0.999   0.0014   ~1      0.0010
    (4,−3,1)   0.994   0.0055   0.995   0.0041
    (4,−3,0)   0.992   0.0005   ~0.99   0.0003
    (1,−1,0)   0.98    0.0094          0.0070
    (3,−2,1)   0.97    0.019           0.014
    e₁, e₂     low     0.19–0.24       0.15–0.17

Q tracks 1−⟨v,v_min⟩²
times the bulk, plus
λ₀. That is why
(4,−3,0) is the
smallest Q in the
pencil (almost
v_min) and (3,−2,1)
the largest, and why
all five stay
positive: they all
have a bulk piece
λ₁α₁² > |λ₀|α₀² on
this window.

Moving v by 1%
toward v_min cuts Q
sharply (`v-sensitivity`);
moving along the
pencil keeps the
sign. The dangerous
direction is onto
v_min, not along it.
