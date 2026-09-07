# Weight functions

    w_even(y) = 2 e^{−y/2} / (1−e^{−2y})
    w_odd(y)  = 2 e^{−3y/2} / (1−e^{−2y})

Near 0, 1−e^{−2y} ∼ 2y, so w_even ∼ 1/y and w_odd ∼ 1/y as well (the
exponential tends to 1). g(0)=0 and g(y)∼c y cancel the pole: a=½ w g
has a finite limit (`kernel_limit_0`).

At y=1 both weights are ordinary O(1). They never change sign on (0,∞).
A lower bound g_lo≤g therefore gives a_lo≤a without a sign flip.

w is not the Weil test function and not the Slepian weight. It is the
density that turns g into the archimedean integrand of A.

Not a new mesh.
