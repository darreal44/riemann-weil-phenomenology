# Derivation of S_diag

Block Q̂ as

    [ H   C ] [ C*  T ].

If T were diagonal D = diag(T), the Schur complement would be exactly

    S_diag = H − C D^{-1} C*.

Reason: the quadratic form on a head vector h plus tail t is h* H h + 2
h* C t + t* T t. Minimising in t for fixed h, when T=D, gives t = −
D^{-1} C* h and the value h* (H − C D^{-1} C*) h.

T is not diagonal. S_diag is therefore not S. It is the Schur complement
of the diagonal part of the *computed* near block only (hats
HEAD…N_NEAR). Off-diagonals of that block are moved into ρ_N and paid
for by 1/(1−ρ).

On χ₃, C D^{-1} C* eats 0.011 of λ_H (0.0185 → 0.0076). That step is
exact for the matrix written in the script, not an approximation of the
infinite C.

Not RH.
