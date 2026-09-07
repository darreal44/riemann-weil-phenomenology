# Maass arch from the digamma

`python code/arch_maass_digamma.py`

W(t) = Re ½ ψ(¼ + i(t±R)/2) − log π.

On maass1, μ=6, N=9:

    G00 = 0.066
    A00 = 0.800     (digamma integral)
    P00 = −0.886    (Λ_f / √n)
    Q00 = 1.686
    λ₀  = −0.871

Same λ₀ as the recycled Dirichlet panel
in `scan_q_maass.py`. The panel *was*
this integral. Replacing it by an
explicit digamma does not move Q.

A itself is already indefinite
(λ_min(A) ≈ −1.31). The gap Q00−G00
≈ 1.62 is an additive O(1) on the
constant mode, not a global scale.
ĥ and θ *are* a Fourier pair
(checked: ˆθ = 2 φ₀²).

A constant ĥ(0)·c with ĥ(0)=2L≈3.58
would need c≈−0.45 to hit G00; none
of {−γ, −log π, −(γ+log π)/2π}
equals that and stays consistent
with the bulk.

The missing piece is the Weil
*measure* for Γ_R(s±iR) (including
the Fricke sign / completed
conductor), not another s0.
