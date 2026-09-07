# Numerical certificates in this repo

A certificate here
is an interval that
a script (or a
page) proves
contains the
object, plus a
kill/survive
against a
pre-registered
room.

## Machine + elementary M

    #52  [0,1] even   R₂=3.39×10⁻⁴ < 9.1×10⁻⁴
    #53  [0,1] odd    R₂=2.01×10⁻⁴, χ₃ Qlo>0
    #54  [0,1]∪[1,L]  Q χ₅ ∈[0.00516,0.00587]
    P    9-term sum   width 1 ulp

G₃ is evaluated.
R is bounded.
That is a
certificate of Q
for one v, one μ.

## Hand M, machine G₃

    M-by-hand  M<4010, R₂<3.53×10⁻⁴
    still under the #52 room.
    Qlo still uses machine G₃
    (`lower-bounds-M.md`).

## Not certificates

    #49 pencil Q>0        computed H, no R
    det H>0               eig of a float 3×3
    drop-3 / drop-83      λ₀ of large Q
    κ, w₂                 grids, killed
    Romberg table         check, no majorant

Float eig and
float λ₀ can be
turned into
certificates with
interval arithmetic
or a residual
bound. They have
not been.

## What a certificate
does not scale to

∀μ, ∀χ, Q_L on W_L.
Each new v or μ
rebuilds M (L
changes, ω
changes). The
method scales;
the page does not
write itself.
