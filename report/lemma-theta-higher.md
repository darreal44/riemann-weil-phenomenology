# Higher-order corrections

## 1. Quartic of the bulk

    log ψ(L/2 + u) = const − a u² − b u⁴ + ⋯

| µ | a | b | b/a² | a L² | −ln λ₀ |
|---|---|---|---|---|---|
| 8 | 9.01 | 4.62 | 0.057 | 39.0 | 43.7 |
| 11 | 7.88 | 2.53 | 0.041 | 45.3 | 48.5 |
| 16 | 6.72 | 1.38 | 0.031 | 51.7 | 53.9 |

b/a² falls. The next Hermite is a few percent
and shrinking: the Gaussian is the right
leading shape, not a lucky quadratic window.

## 2. Edge residual is a constant

    R  :=  −ln λ₀ − 2 (−ln|ψ(0)|)

| µ | R | R/L |
|---|---|---|
| 8 | 2.38 | 1.14 |
| 11 | 2.45 | 1.02 |
| 16 | 2.35 | 0.85 |

R = 2.4 ± 0.05 nats, not growing with L.
So

    λ₀  =  C · ψ(0)² ,     C = e^{−R} ≈ 0.091

independent of µ at this precision. The
factor 2 is exact autocorrelation; C is
the kernel mass that turns the edge value
into the quadratic form. It is the one
number left that might see Weil (γ, log 4π,
the 2-adic tower). It does not track L.

## 3. Finite-width correction to v₀/v₁

The first correction beyond a delta at L/2
is already the form factor

    exp(π² / (a L²))  =  1 + π²/(a L²) + ⋯

because ⟨G, η₁⟩ picks −cos(2π u/L) ≈ −1 + 2(π u/L)²
and σ² = 1/(2a). No extra term is required
at this accuracy (0.3–2 % on ζ). Using −ln λ₀
in place of a L² is slightly cleaner on ζ
because a L² = −ln λ₀ + O(quartic).
Off ζ, use a L² (χ₅: a L² plateaus, −ln λ₀ does not).
