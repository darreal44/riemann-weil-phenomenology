# Running det(A−P) as prime powers are added

μ=16, 2-plane {e₁,e₂}. H = A − P_{n≤N}.

## χ₅ (the thin case)

| N | H₁₁ | H₁₂ | H₂₂ | det |
|---|---|---|---|---|
| 2 | −0.34 | 0.35 | 0.23 | −0.20 |
| 3 | 0.089 | −0.12 | −0.10 | −0.024 |
| 4 | −0.026 | 0.085 | −0.26 | −4.0×10⁻⁴ |
| 7 | −8.2×10⁻⁴ | 1.8×10⁻³ | −7.4×10⁻⁴ | −2.8×10⁻⁶ |
| 8 | 2.9×10⁻³ | −0.011 | 0.046 | +1.0×10⁻⁶ |
| 11 | 6.4×10⁻⁵ | −4.6×10⁻⁴ | 3.3×10⁻³ | **−1.2×10⁻⁹** |
| 13 | 9.3×10⁻⁵ | −5.9×10⁻⁴ | 3.9×10⁻³ | +1.3×10⁻⁸ |
| 16 | 9.3×10⁻⁵ | −5.9×10⁻⁴ | 3.9×10⁻³ | +1.3×10⁻⁸ |

Sign flips at 8, 11, 13.
n=11 is enough to un-prove a
bound that stopped at 8.

## χ₁₃ / χ₈

χ₁₃: det negative through n=7,
positive from n=8 on (stable).
χ₈: negative through n=4,
positive from n=5 on.

## What this kills

Any estimate that discards
n > n₀ with n₀ < μ can flip
the sign. The last terms are

    χ(n) Λ(n) n^{-1/2} θ(log n)
    = O( n^{-1/2} (L − log n)/L )

~ 0.05 at n=13, μ=16. They
correct a 10⁻⁸ determinant.
There is no tail small enough
to ignore relative to det H.

A hand bound must keep every
prime power ≤ μ. That is a
finite sum of explicit terms
— exactly what the Arb 2×2
already checks. It is not an
estimate in n, L, q.

det(A−P)>0 stays a verification
on each window, not a theorem
in the conductor.
