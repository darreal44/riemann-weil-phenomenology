# Product formula and Tamagawa measure on G = A*/Q*

## Product formula

For x ∈ Q*, ∏_v |x|_v = 1. Equivalent forms:

- no nontrivial element of Q* is an idèle of module ≠ 1;
- Q* ⊂ A^1 = {x ∈ A* : |x| = 1};
- a local condition |u|_2 = 2 on an idèle class forces
  |x|_∞ |x|_f\{2} = 1/2.

That last line is the only use we make of the product formula
on the {∞,2} slice: the slice coordinate λ is the surviving
archimedean module once place 2 has been fixed to a shell.

## Tamagawa measure on G = GL_1

G(A) = A*, G(Q) = Q*. A Tamagawa measure on G(A)/G(Q) is a Haar
measure whose local factors are the same local d*x_v as in
`haar-adeles.md`, with the global scalar fixed so that

    vol(A^1 / Q*) = 1.

For GL_1 over Q this volume is finite (compact idèle class group
of module 1) and the Tamagawa number τ(GL_1) = 1. No L-function
residue is required to *define* the measure; the residue of ζ at
s=1 appears as soon as one computes volumes of standard opens
with the Euler product ∏ vol(Z_p*) = ∏ (1 − p^{-1}) = 1/ζ(1),
which is divergent, and one regularizes by the same pole that
Tate subtracts.

On A*/Q* ≅ R+* × (A^1/Q*), Tamagawa Haar splits as

    dμ_Tam = d*λ  ×  dμ_{A^1/Q*},

with vol(A^1/Q*) = 1. The slice we compute with is exactly the
d*λ factor. The compact piece A^1/Q* is not discretized in Fmat.

## What this does not change

The 2-adic shell mass 1/√2 is local at p=2. Tamagawa only says
that this local Haar is the one that, together with d*λ and
vol(A^1/Q*)=1, is the global measure. It does not replace 1/√2
by a special value of ζ, and it does not put a log 2 into d*λ.

## Other groups

For a semisimple simply-connected G, Tamagawa's conjecture
(Weil) is τ(G)=1, proved over number fields. That G is not the
G of this repository. Transporting τ(E) or τ(SL_n) onto the
Weil quadratic form is a different paper. Here G = GL_1,
τ=1, and the only global measure in play is d*λ × (volume 1).
