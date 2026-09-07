# Norm of the Hilbert kernel

Continuous: (Hf)(x)=p.v. ∫ f(y)/(x−y) dy on L²(ℝ) has ‖H‖=π (or π
depending on the 1/π normalisation; the lab’s π is the discrete Hankel
constant, not this operator).

Discrete Toeplitz [1/(n−m)]_{n≠m} is the discrete Hilbert transform,
‖·‖≤π again (the code’s THETA_OP=2 used
|θ_nm|≤2/(π|n−m|)
⇒ ‖Θ‖≤2 before #89).

Discrete Hankel [1/(n+m)] is the one in Off_T and in Off_far. Same
numeral π, different kernel (sum, not difference). Do not import the
continuous p.v. bound to tighten the Hankel: the symbols are not the
same.

#89 replaced the difference-kernel bound ‖Θ‖≤2 by √2 on one band. It did
not touch the sum-kernel π.

Not a new π.
