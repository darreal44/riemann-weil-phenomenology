# d*λ of the slice = d*u of Connes

## The two Haars

Slice coordinate: λ ∈ R_+^*, the module of ϑ(λ)g(r) = λ^{-1/2} g(r/λ).
Haar on the slice:

    d*λ = dλ / λ.

Connes (1999), place 2: u ∈ Q_2^*, Haar d*u normalized by
∫_{Z_2^*} d*u = 1. Each shell 2^n Z_2^* has d*u-measure 1.

## Push-forward

Identify the module of the slice with the 2-adic module,

    λ = |u|_2 = 2^{-n}  on the shell of order n.

A shell of d*u-measure 1 is a point of R_+^*. The only measure on
R_+^* that records a shell as mass 1 is a Dirac in d*λ:

    (d*u) |_{|u|_2 = α}  ≅  δ_{λ=α}\, d*λ.

No log 2 appears here: log 2 is the additive spacing of the shells
in the coordinate t = log λ, but d*λ = dt already assigns mass 1
per shell. Using dt / log 2 = dλ / (λ log 2) would put mass
1/log 2 on each shell and manufacture the Bombieri factor.

## Pairing

Theorem 4 reads against test functions h on R_+^* by

    ⟨τ_2, h⟩ = Σ_n w_n h(2^{-n}),

w_n = (raw shell weight) × (twist). The raw weights are
w_{-1}^{raw} = 1/2 at λ=2 and w_{+1}^{raw} = 1 at λ=1/2
(`code/tau2_local.py`). The operator ϑ already contains λ^{-1/2},
and the archimedean calibration of τ_Λ is CC (39), which contains
√λ. The 2-adic partner in *that* calibration is the twisted weight

    w_{±1} = 1/√2 = 0.7071.

Therefore

    ∫_{window containing only λ=2} (τ_S − τ_∞) d*λ  →  1/√2

as a pairing of measures, once the peak is a Dirac in d*λ.

## Where log 2 comes from

(log 2)/√2 = 0.4901 is the same mass read against
dλ/(λ log 2) = d log_2 λ, or written as a coefficient in front of
δ(λ−2) dλ instead of δ_{log λ} d*λ:

    δ(λ−2) dλ = 2 δ_{λ=2} d*λ.

Conventions that treat τ as a density in λ (Lebesgue) and then
multiply or divide by λ or by log 2 at the point λ=2 produce 0.49
or 1.41. They are not a second local integral.

## What the grid was doing

`weights_2adic.py` computes ∫ (τ_S−τ_A) dλ/λ, which *is* d*λ. The
integrand is not a Dirac: width ~ Λ^{-2}, height growing, lobes
of opposite sign. The integral is the pairing against a fat
window, not against the shell. That is why it walks through 0.49
toward 1.4. The identification above does not use that number.

## Status

d*λ ≡ d*u under λ = |u|_2, one shell ↔ mass 1. The locked mass
in this convention is 1/√2 at λ=2 and at λ=1/2. The remaining
task is not a measure: it is to accept that the Fmat peak is not
yet that Dirac, and to stop reading a running integral as the
shell weight.
