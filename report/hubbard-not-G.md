# Hubbard versus the hat Gram

The Hubbard model
H = −t ∑_<ij>σ c†c + U ∑ n↑n↓
has, for large U/t, two
Hubbard bands split by a
Mott gap ~U, plus a spin
scale J=4t²/U. Near the
Mott point the single-particle
spectrum rearranges
(pseudogap, weight transfer
upper/lower band).
That is a many-body PT
in (U/t, doping).

## What looks similar

    Hubbard              hat Gram G
    two bands + gap      deep wells + bulk
    upper band ~U        anti / plunge ℓ≲2
    lower band, spins    deep ℓ≫2
    doping closes gap    adding zeros shrinks D_max

A two-scale spectrum and
a gap between them. The
K*-plane split
deep / plunge / anti
is the closest picture:
three rungs, not two
bands.

## What does not match

- G is a Gram of samples,
  not a Hamiltonian. No t,
  no U, no filling.
- spec(G) is not in (0,1)
  and is not a DOS of
  electrons. λ>1 is
  sampling, not an upper
  Hubbard band.
- The Mott gap closes by
  doping or by U/t → 0.
  D_max shrinks when zeros
  enter the window — a
  density, not an
  interaction.
- No spin-charge separation,
  no holons/spinons, no
  J=4t²/U. ℓ₀ / D_max ≈ 11
  is π² + O(1), a Slepian
  number, not an exchange.

The repo already closed
Kondo, BCS, Anderson,
AZ as dictionaries for
v₀ / N_eff. Hubbard is
the same class: a two-scale
spectrum one can draw next
to the wells, and no
operator correspondence.
It does not give
#{ℓ>2}=D_max and it does
not move Q.
