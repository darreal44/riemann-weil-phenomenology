# EM remainder bounds

The integral form is

    R_m = (−1)^{m+1} \frac{B_{2m+2}}{(2m+2)!} h^{2m+2} ∫_0^n \bar
    P_{2m+2}(t) f^{(2m+2)}(a+th) dt

with
|\bar P_{2k}| ≤ |B_{2k}|
(periodic Bernoulli). A crude bound is therefore

    |R_m| ≤ 2 |B_{2m+2}| / (2m+2)! h^{2m+2} (b−a) ‖f^{(2m+2)}‖_∞.

On [0,1] with m=0 (plain trapezoid) this is already |B₂|/2! × ‖g''‖_∞ ∼
(1/12)×9.6 ∼ 0.8 if one takes the whole interval as one panel — useless
against WINDOW. With N panels, h=1/N, |R|∼ ‖g''‖ / (12 N²) ∼ 0.8 / N²,
so N=20 would put the unsigned remainder near 0.002. That is comparable
to the mesh gap and still unsigned unless one knows the sign of g'' on
every panel (we do: well +, tail −). A signed trapezoid bound panel by
panel is just the chord or the tangent again.

The mesh is EM at order 0 with a local quadratic correction instead of
B₂. No new run.
