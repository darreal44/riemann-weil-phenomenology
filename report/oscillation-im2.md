# Oscillation on Im z = ±2

θ_v is sines and
cosines of ω_n z,
ω_n = 2π n / L real.
On z=x+2i:

    sin(ω(x+2i))
      = sin(ωx) cosh(2ω)
        + i cos(ωx) sinh(2ω)

There is an
oscillation in x,
amplitude
cosh(2ω n).

    n   ω     cosh(2ω)   e^{2ω}/ω
    1  2.27     46.8       20.7
    2  4.53   2190       2046

A Riemann-Lebesgue
bound |∫ e^{iωx} dx|
≤ 2/ω times that
amplitude *grows*
with n. The n=0
piece of θ_v is
2(L−z)/L, no
oscillation at all.
2e^{−3z/2} on x+2i
is 2e^{−3x/2} e^{−3i},
decay in x, no
ω-cancel.

So the sides of
the stadium do
oscillate for n≥1,
and the bound one
actually writes is
worse than |a|≤M
on a short real
segment. A primitive
of a is not
elementary (w is
csch, θ_v is
trig). The useful
primitive is Gauss
on [0,1], where
ω stays real and
cosh(0)=1.

Empty-contour +
oscillation does
not replace #52.
