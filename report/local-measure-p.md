# Local measure at p

## Additive

dx_p on Q_p, vol(Z_p) = 1. Then vol(p^n Z_p) = p^{-n}.
Fourier transform on Q_p is unitary for this choice (self-dual
against the standard additive character ψ(x) = exp(2πi {x}_p)).

## Multiplicative

d*x_p = dx_p / |x|_p. Two current normalizations of the unit group:

- Tamagawa / Tate: vol(Z_p*) = 1 − p^{-1} = φ(p)/p.
- Connes 1999 Thm 4, as used at p=2: vol(Z_p*) = 1.

The ratio is 1 − p^{-1}. Every local mass below scales by that
constant if one switches. We keep Connes' 1 on Z_p* when quoting
shell masses of τ_p, and we record the Tate factor separately.

## Shells

Q_p* = ⨆_{n∈Z} p^n Z_p*. Under vol(Z_p*) = 1 each shell has
d*x_p-measure 1. The module |x|_p = p^{-n} on the n-th shell.
Pushed to the slice as in `dstar-identification.md`,

    (d*x_p) |_{|x|_p = p^{-n}}  ≅  δ_{λ = p^{-n}} d*λ.

## Local Weil weight |1 − u|_p^{-1}

On the shell n:

- n > 0 (|u|_p < 1): |1−u|_p = 1, raw weight 1.
- n < 0 (|u|_p > 1): |1−u|_p = |u|_p = p^{-n}, raw weight p^{n}.
- n = 0 (units): |1−u|_p depends on u mod p. For p odd,
  |1−u|_p = 1 on a set of measure 1 − 1/(p−1) inside Z_p* in the
  Tate normalization; this shell is *not* a point mass of τ_p
  on the slice. The point masses are n = ±1, λ = p^{±1}.

Twisted by λ^{1/2} as ϑ does:

    n = −1 (λ = p):  raw = 1/p,  twisted = p^{-1} · √p = p^{-1/2}
    n = +1 (λ = 1/p): raw = 1,   twisted = p^{-1/2}

At p=2 this is 1/√2 and 1/√2. At p=3: 1/√3 ≈ 0.577. At a general
p the two shells that the slice can see as peaks of τ_S − τ_∞
are λ = p and λ = 1/p, each of twisted mass p^{-1/2}.

## Tate factor

vol(Z_p*) = 1 − p^{-1} = 1/ζ_p(1). The Euler product of these
volumes is the pole of ζ. It does not move the *ratio* of the
two shells n=±1. It multiplies every shell by 1−p^{-1} if one
insists on Tate instead of Connes. Then the twisted masses
become (1−p^{-1}) p^{-1/2}. At p=2: (1/2)/√2 = 0.353, which
is neither 0.49 nor 0.707 — a third convention, not used here.

## What the slice can test

Peaks of τ_S − τ_∞ at λ = p^{±1} with masses p^{-1/2} (Connes
twist, vol units = 1). For p=2 that is the locked 0.7071.
A peak at λ=3 of mass 1/√3 would be the same theorem at the
next place, still without ζ beyond naming p.
