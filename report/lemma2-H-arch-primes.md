# H|ker = Arch − Primes, two O(1) terms

On the plane v₀ + √2(v₁+v₂) = 0:

| L | µ | Arch\|ker | Primes\|ker | Arch−Primes | A−P (scalar) |
|---|---|---|---|---|---|
| χ₅ | 16 | −1.182 | −1.183 | **3.2×10⁻⁶** | 7.7×10⁻⁴ |
| χ₅ | 38 | −1.560 | −1.560 | **2.4×10⁻⁷** | 3.4×10⁻⁴ |
| χ₃ | 16 | −0.688 | −0.690 | **6.3×10⁻⁸** | 1.3×10⁻³ |
| χ₁₃ | 16 | −0.227 | −0.422 | 2.1×10⁻³ | 0.19 |
| χ₃₁ | 38 | +1.52 | −0.19 | 2.3×10⁻² | 1.71 |

Wide desert: Arch and the prime
sum agree to 6–8 digits on this
plane. That agreement *is*
λ_min(H). Narrow desert: they
differ at 10⁻², and λ_min(H)
stops shrinking.

## Formula

    H_{nm} = Arch_{nm}(L,q,s₀)
             − ∑_{p^k ≤ μ} χ(p^k) (log p)/p^{k/2}  θ_{nm}(log p^k)

θ_{00}(y)=2(L−y)/L,
θ_{0n}(y)=−2 sin(ω_n y)/(√2 π n),
ω_n = 2π n / L
(`scan_s.py` th_at).

ker ψ(0) is three numbers. The
pairing against every prime
power ≤ μ of that fixed test
function almost cancels the
archimedean integral. Lemma 2
at the 3-hat level is:

    |Arch(k) − Primes(k)|
    ≥ exp(−c τγ₁)    or not.

Numerically it is much smaller
than exp(−τγ₁) ≈ 10⁻⁴ on χ₅-16
(we have 10⁻⁶). The primes
know the desert more precisely
than a Slepian.

## Next

A 3-hat explicit formula is
finite (O(μ/log μ) terms).
Bounding |A−P| from below
without the zeros is a
truncated Weil estimate on
one test function. That is
unconditional and small-L
friendly. It does not give
the Schur factor 10⁶–10¹⁴.
