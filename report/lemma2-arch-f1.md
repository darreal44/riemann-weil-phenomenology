# Arch(f₁) is a Laplace series, closed

s₀ = 1/4 (even χ) or 3/4 (odd). F₀(f₁) = 2.
The archimedean kernel in the code is

    K(y) = 2 e^{-2 s₀ y} / (1 − e^{-2y})
         = 2 Σ_{m ≥ 0} e^{-α_m y},
           α_m = 2 s₀ + 2m.

    Arch(f₁)
    = CST
      + Σ_{m ≥ 0} ∫_0^L e^{-α_m y}
          ( 2 e^{-(2-2s₀)y} − θ_{f₁}(y) ) dy,

    CST = log(q/π) − γ − log(1 − e^{-2L}).

θ_{f₁} is elementary. Each integral
is a Laplace transform of
{1, y, cos ωy, y cos ωy, sin ωy}
on a finite interval, hence a
rational function of (α_m, ω, L):

    ∫_0^L e^{-α y} dy          = (1 − e^{-α L})/α
    ∫_0^L y e^{-α y} dy        = (1 − e^{-α L}(α L+1))/α²
    ∫_0^L e^{-α y} e^{iω y} dy = (1 − e^{(-α+iω)L})/(α − iω)

and the y-trig sibling
(1 − e^{(-α+iω)L} ((α−iω)L+1))/(α−iω)².

The series is geometric in e^{-2L}
(L = log 16 ⇒ e^{-2L} = 1/256).
Ten terms give more digits than
the 10^{-6} we are chasing.

## Check, μ = 16, unit e₁

| χ | q | s₀ | Arch(f₁) | Primes(f₁) | A−P |
|---|---|---|---|---|---|
| χ₅ | 5 | 1/4 | −0.978 | −0.987 | 9×10⁻³ |
| χ₃ | 3 | 3/4 | −0.622 | −0.625 | 3×10⁻³ |
| χ₈ | 8 | 1/4 | −0.508 | | |
| χ₁₃ | 13 | 1/4 | −0.022 | −0.243 | O(10⁻¹) |

χ₅, χ₃: one direction already
cancels to 10^{-3}. The second
direction of the 2-plane takes
that to 10^{-6}. χ₁₃: Arch(f₁)
is almost 0; the primes do not
match; H|ker stays 10^{-3}.

## What is now explicit

On the raised-cosine 2-plane,
every matrix element of Q is

    Arch_{ij} − Σ_{n ≤ μ} χ(n) Λ(n) n^{-1/2} θ_{ij}(log n)

with Arch_{ij} a 10-term Laplace
sum and θ_{ij} a combination of
(1−y/L), cos, sin as for θ_{f₁}.
No quadrature, no zeros.

Lemma 2 at 3 hats is a 2×2 of
these numbers. A lower bound is
an estimate of that determinant
(or of λ_min). Truncating the
prime sum is not enough; the
Laplace tail is negligible.
The object is finite and written.
