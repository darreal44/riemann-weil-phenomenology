# 2-plane H certified SPD at µ=16

`code/cert_2plane.py`: three-hat Q
projected on the exact frame

    e₁ = (√2, −1, 0)/√3
    e₂ = (−√2, −2, 3)/√15

Finite explicit formula, no zeros.
dps=36–40, NB=2.

| χ | H₁₁ | det H | λ_min(H) | λ_min(Q₃) | det/tr / eig |
|---|---|---|---|---|---|
| χ₅ | 9.31×10⁻⁵ | 1.27×10⁻⁸ | 3.21×10⁻⁶ | 2.26×10⁻⁶ | 1.000 |
| χ₃ | 2.18×10⁻⁴ | 5.67×10⁻¹⁰ | 6.31×10⁻⁸ | 3.70×10⁻⁸ | 1.000 |
| χ₄ | 1.18×10⁻³ | 1.21×10⁻⁶ | 1.11×10⁻⁵ | 5.65×10⁻⁶ | 1.000 |
| χ₈ | 1.71×10⁻³ | 1.99×10⁻⁴ | 1.73×10⁻⁴ | 8.11×10⁻⁵ | 1.000 |
| χ₁₃ | 0.212 | 4.89×10⁻³ | 2.08×10⁻³ | 8.59×10⁻⁴ | 1.000 |

det H > 0 and λ_min(H) > 0 on all
five. det/tr equals the computed
eigenvalue to 10⁻³ relative — the
bound of `H-lower-bound.md` is
saturated.

λ_min(Q₃) sits 1.4–2.5 below
λ_min(H): the third hat direction
outside the plane still moves the
floor, as in `lemma2-2x2.md`.

This is a high-dps evaluation of
the same quadrature as `scan_s`,
not an Arb enclosure. An interval
certificate would wrap the Gauss
panels and the nine prime terms;
the digits here are stable from
dps 36 to 40 and the sign is not
close except on χ₃ (det 5.7×10⁻¹⁰
against entries 10⁻³).

`tests/test_2plane_det.py` locks
the five signs.
