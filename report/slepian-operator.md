# Slepian operator on I=[0, γ1(χ₂₉)]

Kernel sin(τ(t−s))/π(t−s), τ=L/2, I length 1.794.
240-point Nyström.

| μ | τ | πτ|I| (old) | λ₊ num | 1−λ₊ | −log(1−λ₊) |
|---|---|----------------|--------|------|------------|
| 11 | 1.20 | 6.76 | 0.608 | 0.392 | 0.94 |
| 22 | 1.55 | 8.71 | 0.728 | 0.272 | 1.30 |
| 38 | 1.82 | 10.25 | 0.802 | 0.198 | 1.62 |

Time-bandwidth τ|I|≈2.2–3.3: only one
moderate eigenvalue, not 1−e^{−6}. The
exponential used in Lemma 2 is the large-c
formula; we are not in that regime.

ell_Gram at μ=11 is −log 0.281=1.27, against
−log(1−λ₊)=0.94. Same order. A ≈ λ0/(1−λ₊)
≈ 0.28/0.39 ≈ 0.72 — a plausible sampling
constant, no longer the unstable A_hat that
assumed e^{−πτ|I|}.

Lemma 2 should read

    ell ≤ −log(1−λ₊(I,τ)) + log(1/A)

with λ₊ computed, not replaced by 1−e^{−πτ|I|}.
