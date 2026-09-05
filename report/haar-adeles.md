# Haar on the adèles, as used here

## Additive group A

A = R × ∏' Q_p (restricted product: almost all components in Z_p).
A Haar measure dx on A is the product of local Haars, unique up to
one scalar:

- R: Lebesgue dx_∞
- Q_p: dx_p with vol(Z_p) = 1

The finite adèles A_f = ∏' Q_p then have vol(Ẑ) = 1. There is no
preferred scalar mixing dx_∞ and dx_f; Connes' compressed trace
fixes it by matching the archimedean term to CC (39).

## Multiplicative group A*

Idèles: A* = R* × ∏' Q_p*. Restricted product: almost all components
in Z_p*. Local multiplicative Haars d*x_v = dx_v / |x_v|_v, with

- R+*: d*λ = dλ/λ   (the slice)
- Q_p*: d*u_p with vol(Z_p*) = 1 − 1/p
  (or the normalization vol(Z_p*) = 1 used in Connes 1999 Thm 4
  at p=2 — a constant 1/2 that is the origin of raw weight 1/2
  versus 1; we follow the paper we calibrate to).

The module |x| = ∏_v |x_v|_v. The kernel of the module is
A^1 = {|x|=1}. Tate: d*x = d*λ × d*x^1, and the volume of
A^1 / Q* is finite (the idèle class group of module 1).

## Product formula

For x ∈ Q*, ∏_v |x|_v = 1. So Q* sits in A^1. Haar on A* / Q*
descends. This is why a local shell at p=2 with |u|_2 = 2 must be
balanced by |x|_∞ = 1/2 (or the opposite) on the idèle class:
the slice coordinate λ is that archimedean module.

## What we use

- d*λ = dλ/λ on the slice = the R+* factor of d*x.
- d*u on Q_2* = the place-2 factor, vol(Z_2*) = 1 in Connes'
  normalization.
- Identification of the last two notes: on the shell |u|_2 = α,
  d*u pushes to δ_{λ=α} d*λ because the product formula has
  already spent the other places.

ζ does not define these measures. ζ appears as the Euler product
of the local volumes: vol(Z_p*) = 1 − p^{-1} and
ζ(s) = ∏ (1 − p^{-s})^{-1} is the generating function of those
volumes. The 2-adic mass 1/√2 is a local Haar computation at p=2,
not a special value of ζ.

## What we do not use

Haar on A itself (additive) enters the Fourier transform that
produces ϑ, already built into Fmat / the explicit formula.
We do not integrate over A or over A* / Q* numerically. The
semi-local slice {∞,2} keeps two factors of the product and
throws the rest into the implicit complement.
