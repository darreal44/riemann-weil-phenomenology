# Schur on v, not on the 3-plane

Tail T = H[{3,4,5}].
Correction for this v:

    vᵀ C T⁻¹ Cᵀ v  =  0.00403
    Q_head(v)       =  0.00551
    Q_Schur(v)      =  0.00148 > 0

    ‖Cᵀ v‖ = 0.091
    Cᵀ v   = (0.010, 0.083, 0.035)
             (mostly φ₄)

The crude majorant
‖C‖_F² / λ_min(T) = 0.52
is 129× the actual
correction. v is almost
orthogonal to the strong
mixing directions of C
(φ₂–φ₄ is 0.56; v₂ is
only 0.20).

So the tail subtracts
0.004 from Q and leaves
0.0015. Higher hats
nudge the witness, they
do not eat it. A proof
that writes
Q(v) ≥ Q_head − ‖Cᵀv‖²
/ λ_min(T) is 0.00551 −
0.091² / 1.56 = 0.0002,
still positive and only
a factor 7 from the
true Schur value.
