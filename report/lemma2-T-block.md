# The tail block T is not a spectator

T = Q on hats n≥3.

| L | µ | λ_min(T) | λ_max(T) | ‖C‖ | Corr\|ker | H\|ker |
|---|---|---|---|---|---|---|
| χ₅ | 16 | 0.24 | 4.0 | 0.95 | 3.13×10⁻⁶ | 3.21×10⁻⁶ |
| χ₅ | 38 | **4×10⁻⁸** | 5.0 | 0.82 | 2.41×10⁻⁷ | 2.41×10⁻⁷ |
| χ₃ | 16 | **6×10⁻⁴** | 3.6 | 0.92 | 6.27×10⁻⁸ | 6.31×10⁻⁸ |
| χ₈ | 16 | 0.90 | 4.2 | 0.89 | 1.6×10⁻⁴ | 1.7×10⁻⁴ |
| χ₁₃ | 16 | 1.54 | 5.6 | 1.29 | 8.2×10⁻⁴ | 2.1×10⁻³ |
| χ₃₁ | 38 | 0.69 | 6.3 | 0.54 | 3.1×10⁻⁴ | 2.3×10⁻² |

On χ₅-16, T is honest (0.24–4).
On χ₅-38 and χ₃-16, T has its
own tiny eigenvalues. Those
are the same 3-hat cancellation
shifted to n=3,4,5.

The rank-1 from λ_min(T) does
not reproduce Corr on ker
(overlap ~ 0). The Schur
correction is a full-T object,
not one tail mode.

## Picture

Wide desert, large N_B: Q is
a chain of nearly singular
3-hat blocks, coupled by C.
Each block wants ψ(0)=0 in
its own frequencies. λ₀ is
the joint cancellation after
they talk.

That is why a test function
supported on hats 0,1,2
(or a Slepian) cannot see λ₀:
the exponent is the
*communication* between
blocks, C T⁻¹ Cᵀ.

## Bound

A Poincaré / Schur inequality
that only uses ‖C‖ and
λ_min(T) gives

    Corr ≲ ‖C‖² / λ_min(T)

χ₅-16: 0.95²/0.24 ≈ 3.8, while
Corr|ker = 3×10⁻⁶. Off by 10⁶.
The coupling C is large in
Frobenius and small on ker.
The structure to write is
C restricted to ker ψ(0), not
‖C‖_F.
