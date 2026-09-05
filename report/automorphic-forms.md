# Automorphic forms, as they sit in this repository

## GL_1

An automorphic form on GL_1 / Q is a continuous function
φ : A*/Q* → C of moderate growth, or equivalently a Hecke
character of the idèle class group. Dirichlet characters χ
of conductor q are the finite-order ones: they are trivial
on R+* and on a congruence subgroup of Ẑ*.

Every L(s,χ) assembled in the repo is the standard L-function
of such a form. The zeros we harvest are the automorphic
spectrum of GL_1. The truncated Weil form Q_L is the explicit
formula for that L-function on a window of type L/2. No
cusp form on GL_2 has been used.

The Tamagawa measure d*λ × dμ_{A^1/Q*} of the previous note
is the Haar measure against which these φ are L^2. A unitary
character of A^1/Q* is an automorphic form of GL_1 on the
compact piece; ζ itself is the Eisenstein series of GL_1
(the trivial character, plus the pole).

## What the slice sees

The {∞,2} slice keeps the module R+* and one finite place.
An automorphic φ that is unramified at 2 is constant on
Z_2*-cosets; its matrix coefficient against ϑ(λ) is a function
of the module only. That is why τ_Λ(λ) can be written without
choosing a χ: it is the identity contribution (the trivial
form) of the compressed trace. The peaks at λ=2^{±1} are
that identity, evaluated at one place, not a cusp form.

A non-trivial χ ramified at 2 would twist the local factor
at 2 (ε-factor, conductor power of 2). None of the sixteen
harvested characters is totally ramified in a way that moves
the *location* of the peaks; a χ of even conductor changes
the local root number, not the module λ=2.

## GL_2, briefly

Cusp forms on GL_2 give L-functions of degree 2, Ramanujan
bounds, and a different explicit formula (two Γ-factors).
The Weil quadratic form and the floor c_L can be written
for those L-functions too. That is a new family of zeros,
not a new 2-adic mass: the local factor at 2 of a GL_2 form
is still a representation of GL_2(Q_2), whose Satake
parameters are not the shell weights p^{-1/2} of GL_1.

Nothing in the current Q, Gram, or τ_Λ is that representation.
Studying automorphic forms *here* means reading the existing
χ as GL_1 forms on A*/Q*, and leaving GL_2 as a different
explicit formula.

## Status

The objects already measured — ζ, χ_5, χ_17, χ_29, … — are
automorphic of GL_1. The 2-adic mass 1/√2 is the local
unramified computation for the trivial form at p=2. A cusp
form would be a new campaign of zeros, not a new Haar measure.
