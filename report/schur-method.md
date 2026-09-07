# Schur, as used

Block the ONB as head ⊕ tail:

    Q̂ ∼ [ H  C ] [ C* T ].

The Schur complement of T is H − C T^{-1} C*. If T>0 and that complement
is ≥0 then Q̂≥0 on the whole space. The lab never inverts T. It replaces
T^{-1} by D^{-1}/(1−ρ) when ρ<1 (Neumann) or by a diagonal (not a bound)
or by Frob/qmin (too fat on χ₅).

What Schur gives that Galerkin does not: a door to a lower bound on
λ_min, provided the replacement of T^{-1} is a true majorant of T^{-1}
in the PSD order. That is the whole method. If ρ≥1 the door closes and
one does not get to blame H.

Finite C (2×38) is a truncation of the coupling, completed by cfar. That
truncation is part of the proof only if the missing columns are
majorised (they are: Hilbert + θ).

Not a new complement.
