# Logic of tau2_pairing.py

61 lines. Consumes
`twisted_module` from
tau2_local. No Fmat.

## 1. The test function

g = 1_{[0,Λ]} on the
additive line. The
slice operator is
ϑ(λ)g(r)=λ^{-1/2}g(r/λ).
The matrix element
is elementary:

    ⟨g, ϑ(λ)g⟩
      = λ^{-1/2} |[0,Λ] ∩ [0,λΛ]|
      = Λ λ^{-1/2} min(1,λ)
      =: h_Λ(λ)

That is `h_Lam`.
It is not Connes’ h
on ℚ₂×; it is the
push of the additive
indicator to the
dilation coordinate.

## 2. The sum

    ⟨τ₂, h_Λ⟩ ≔ ∑_{n=−8}^{8} w(n) h_Λ(2^{-n})

λ = 2^{-n} = |u|_2
(module convention).
w(n) = twisted_module(n)
= raw(n) · √λ.
Units n=0 have w=0
(no Dirac at 1).

This *defines* a
pairing of the
shell masses against
that particular h_Λ.
It is not Thm 4
until one proves
h_Λ is the
restriction of the
idèle test function
in Connes. It is
the computation
the file can do.

## 3. Why the ratio is ~4

h_Λ is homogeneous
of degree 1 in Λ,
w is independent of
Λ, so the sum is
c Λ. The printed
ratio is
⟨τ₂,h_Λ⟩ / (Λ/2).
It sits at 3.984
with ±8 shells
(`tau2-pairing-run.md`).
The two dominant
terms n=±1 each
give Λ/2 at Λ=4
(w=1/√2, h=Λ√2).
Truncation eats
the 0.016.

## 4. What the file
quietly chooses

It imports
`twisted_module`,
not `twisted_inverse`.
The pairing is the
module reading.
Switching the import
would replace 1/√2
by √2 on n=+1 and
change c. That
switch is a one-line
convention, not a
new theorem.

## 5. What it is not

Not w₂ (windowed
∫ τ d*λ).
Not κ (block(2)×F_∞).
Not extensive vs
intensive: do not
compare 31.9 at
Λ=16 to w₂=1.08.
