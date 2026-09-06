# λ₀ = λ_min of the 3×3 Schur

Split Q as

        [ H  C ]
    S = [ Cᵀ T ]

H is 3×3 (hats n=0,1,2), T the rest.
Eliminate the tail:

    Δ = H − C T⁻¹ Cᵀ

| L | µ | λ₀ | λ_min(Δ) | Δ/λ₀ |
|---|---|---|---|---|
| χ₅ | 16 | 1.584×10⁻¹² | 1.584×10⁻¹² | 1.000 |
| χ₅ | 38 | 5.254×10⁻²² | 5.276×10⁻²² | 1.004 |
| χ₃ | 16 | 7.713×10⁻¹⁶ | 7.722×10⁻¹⁶ | 1.001 |
| χ₄ | 16 | 2.917×10⁻¹³ | 2.918×10⁻¹³ | 1.001 |
| χ₈ | 16 | 1.068×10⁻⁸ | 1.069×10⁻⁸ | 1.000 |
| χ₁₃ | 16 | 4.787×10⁻⁵ | 4.789×10⁻⁵ | 1.000 |
| χ₂₉ | 38 | 1.283×10⁻⁵ | 1.284×10⁻⁵ | 1.000 |
| χ₃₁ | 38 | 3.064×10⁻⁴ | 3.077×10⁻⁴ | 1.004 |

The other Schur (tail after
eliminating the head) is 200–
50 000 times larger: the small
eigenvalue lives in the 3-hat
plane, not in the tail.

## Head = ker ψ(0)

v₀₁₂ lies in the plane
v₀ + √2 (v₁+v₂) = 0
(inner product with that kernel
= 0.994–1.000). That is the
unique 3-hat combination with
ψ(0)=0 at leading order.
χ₅-16: residual 5×10⁻⁴.

## Lemma 2, matrix form

    λ₀(Q) = λ_min( H − C T⁻¹ Cᵀ )

H is explicit (three hats, prime
kernel). T is well-conditioned
on the narrow deserts (κ ~ 4–10)
and worse on χ₅-38 (κ ~ 10⁸,
still λ_Δ/λ₀ = 1.004).

A lower bound on λ_min(Δ) is a
lower bound on λ₀. Δ is 3×3.
The desert enters in C (how
strongly hats 0,1,2 talk to
n≥3) and in H (how close H
already is to singular on
ker ψ(0)).
