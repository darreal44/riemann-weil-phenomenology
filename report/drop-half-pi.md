# What if one drops ½π?

Monkeypatch of `HILBERT_HANKEL` in `row_of` on χ₃, everything else
fixed (θ-term, HS, 1/(4N)):

    Hankel used     ρ      ρ_far    S_lo
    π        0.590  0.503    −0.0086
    2        0.494  0.367    −0.0033
    1        0.430  0.248    −0.0008
    0        0.387  0.129    +0.0005

Removing ½π *does* flip S_lo, by half a thousandth. That is not a
certificate: the archimedean piece *is* the Hankel ½/(n+m) whose
essential norm is ½π (Hartman). Setting the constant to 0 is false.

The legal replacement of the whole Off_far (Hankel+Θ) *was* written
(`code/ql_off_s1.py`, remaining-before-rh 8h). It is the triangle

    π/2 − |w₂|  ≤  s₁^{ess}(Off)  ≤  π/2 + r_N + |w₂|.

χ₃: lower 1.081, upper 2.110 = Off_far. So s₁ ≤ 0.6 (PR #93), 0.8 and
1.0 lie *below* the essential lower bound and are false. Dropping ½π
stays false. The truncated Weyl trial on [32,M) (8i) does not exhibit
1.081: intercept 0.707 ≠ 0, and at M=2048 one is still 0.75 below π/2.
½π stays.

Not taken. Not RH.
