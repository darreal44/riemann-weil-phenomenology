# θ_v on [0, L], v = (4,−3,1)/√26

L = log 16. Elementary
combination of the six
θ_{nm}, n,m ≤ 2.

## Values

    θ_v(0) = 2
    θ_v(L) = 0
    θ_v ≥ 0 on [0, L]
    strictly decreasing
    no zero inside (0, L)

    t=y/L    θ_v
    0        2
    1/4      1.1218     (n=2)
    1/2      0.3077     (n=4)
    3/4      0.0321     (n=8)
    1        0          (n=16)

## Derivatives

    θ_v'(0) ≈ θ_v'(L) ≈ −0.0381

Almost equal. The kernel
is not symmetric about
L/2 (θ(L/2)=0.31 ≠ 1),
but the slopes at the
ends match at 10⁻⁵.

## Matrix at y=0

    θ_{nm}(0) = 2 δ_{nm}

so θ_v(0) = 2 ‖v‖² = 2.
Off-diagonal hats vanish
at the origin; only the
diagonal F₀-like term
survives.

## Shape versus θ_{f₁}

θ_{f₁} (e₁ only, two hats)
is also ≥ 0 and decreasing
(`theta_f1.py`). Adding φ₂
with weight 1/√26 does not
break positivity. That is
why every prime term
w(n) θ_v(log n) has the
sign of χ(n) Λ(n), and
why P(v) is dominated by
n=2,3 (χ₅ both −1).

## Use

A decreasing positive
θ_v gives P_rest a sign
pattern identical to
χ(n), and a size ordered
by θ_v(log n) which we
already tabulated.
It does not by itself
bound A(v): A compares
θ_v to 2 e^{-3y/2},
which drops faster
(0.45 at y=1 versus
θ_v=0.67).
