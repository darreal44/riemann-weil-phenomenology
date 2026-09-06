# Lemma (analytic half of conjecture B) — status

**Claim.** The ground-state test function Θ_v of the prime-side
truncated Weil form is the autocorrelation of the extremal
function of the desert. Hence

    Θ_v(y) > 0 on (0, L),     Θ_v(L) = 0,

    −ln Θ_v(y) = C (s/L) φ(y),     y² ≲ φ(y) ≲ y e^y,

with C of order 1 (0.6 for one Γ_ℝ, 1.0 for several — Claude §123;
C_emp ≈ 1.53 at ζ, µ=11, dim 9).

**What is proved or measured.**

1. Θ_v of *prime-side* Q is positive and smooth on (0,L)
   (`code/theta_v_qpr.py`). The zero-Gram vector is the
   desert artefact and must not be used.
2. (−ln Θ_v)/(y e^y) locks at 1.53 for y ≳ 1.4 at this window.
   A Gaussian (lock on y²) is excluded.
3. Mass of v̂ sits in the desert (|v̂(1)|² ≈ 0.8 in §122), so
   the identification with a desert extremal is the right
   *class* of functions.

**What fails as an equality.**

The raw Slepian of the single interval [0, γ₁] on time [0,L]
has concentration 1 − 10⁻¹⁴ at µ=11, and its autocorrelation
Θ_Sl has the same *envelope*, but

    r_S = (−ln Θ_Sl)/(y e^y)  falls  19 → 1.26
    r_Q                       locks           1.53

and Θ_Q decays faster in the last third of the window
(`code/theta_vs_slepian.py`). A flat band [0,γ₁] oscillates;
Q does not. The weight |v̂(ω)|² is peaked at 0, and the
set is desert + sub-Nyquist, not one interval.

**Gap to a proof.**

Need the autocorrelation of the *weighted* one-set
extremal (Beurling of E_L with the measured density
e^{−αω} in the desert), or a Laplace-method derivation
of y e^y from that density. The raw Slepian is not the
kernel. This does not prove RH; it locates Θ_v in
harmonic analysis of a hole.
