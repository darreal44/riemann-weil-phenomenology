# Widom and "phase transitions": three different theorems

Harold Widom (1932-2021) is
cited for three spectral
transitions. Only one is
the plunge we use.

## 1. Landau-Widom 1980 -- the plunge

H. J. Landau & H. Widom,
Eigenvalue distribution of
time and frequency limiting,
J. Math. Anal. Appl. 77
(1980), 469-481.

The operator chi_T F^{-1} chi_Omega F
(time T, band Omega) has
eigenvalues in (0,1). As
the time-bandwidth product
c = |T||Omega|/2pi -> infinity:

    ~ 2c eigenvalues near 1
    ~ rest near 0
    a transition band of
    width O(log c) in the
    index, where lambda drops
    from 1-delta to delta.

That drop is the
"phase transition" of the
concentration operator:
two bulk phases (concentrated
/ not) separated by
O(log c) transitional
prolates. Daubechies later
made the width explicit.
It is not a thermodynamic
PT (no free energy, no
order parameter in T).

On the Gram of hats we
measured one extra well in
(1/2, 2] at mu=16, N=30
(`landau-plunge-count.md`).
O(log c)~3.4 could hold a
few modes; we see one.
Transferring Landau-Widom
from chi_E P chi_E to the hat
Gram is the open step in
`remaining-before-rh` section 1.

## 2. Szego-Widom -- Toeplitz determinants

Widom's proof of the
strong Szego theorem
(smooth symbol a>0):

    log det T_n(a) = n log G(a) + E(a) + o(1)

When a has jumps
(Fisher-Hartwig), the
second term changes
character: a different
asymptotic "phase",
used for Ising
magnetization (Onsager)
and later for ASEP
(Tracy-Widom). That is a
transition in the symbol,
not in an eigenvalue
plunge of a limiter.

## 3. What this is not

First-order PT of transfer
matrices, Widom factors of
Chebyshev polynomials on
compact sets, Tracy-Widom
edge laws for random
matrices: same name, other
papers. None of them
supplies #{ell_k > 2}=D_max
for the hat Gram.

The only Widom statement
that could close the
threshold-free count is
section 1, and only after
the limiter is identified
with G.
