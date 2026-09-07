# Schur complements, here

Block a self-adjoint
operator (or matrix)

    [ H   C ]
    [ C*  T ]

with T invertible
and T ≥ δ I, δ>0.
The Schur
complement of T is

    S = H − C T^{-1} C*

and

    [H C; C* T] ≥ 0
      ⇔  T≥0 and S≥0.

If one only has
‖T^{-1}‖ ≤ 1/δ
then

    S ≥ H − ‖C‖²/δ

in the quadratic-
form sense
(operator norm of
C, or Frobenius
as a crude majorant).
#58 uses that
majorant:

    β = λ_min(H) − ‖C‖_F² / δ
    δ = qmin − ‖Off_T‖

H is the finite
head (2×2 cosine).
T is the infinite
tail. C is the
coupling. β>0
⇒ S>0 ⇒ the
block ≥0 on the
whole ONB ⇒
Q̂_L≥0 on W_L
*if* the cosine
ONB is complete
for the form,
which it is for
even functions
on the interval.

What β is not:
a Schur
complement of
the *true* T.
It replaces
T^{-1} by 1/δ
and C by its
Frobenius size.
That is why χ₈
can be taken
(δ large, λ_H
decent) and χ₅
cannot even
when Off_T=0
(‖C‖²/λ_H > qmin:
the majorant of
C T^{-1} C* is
already larger
than H).

A sharper Schur
would keep the
actual C T^{+} C*
(or a better
‖C‖_{H→T})
instead of
‖C‖_F²/δ.
That is the
only remaining
Schur move on
χ₅. It is not
SOS. It is not
Krein’s μ.
