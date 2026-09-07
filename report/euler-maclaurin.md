# Euler–Maclaurin

    ∫_a^b f = (h/2)(f(a)+f(b)) + h ∑_{k=1}^{n−1} f(a+kh) − ∑_{k=1}^m
    B_{2k}/(2k)! h^{2k} (f^{(2k−1)}(b)−f^{(2k−1)}(a)) + R_m.

R_m involves B_{2m+2} and f^{(2m+2)} on [a,b] (periodic Bernoulli or an
integral remainder).

A legal lower bound keeps the trapezoid plus the Bernoulli terms up to m
and subtracts |R_m|. Near y=0, f=a(y) or g, the odd derivatives at 0 are
large (g''(0)=9.6, g'''(0)=−7.2) and Bernoulli numbers grow fast. The
first correction already competes with the whole WINDOW. That is why the
local mesh (which never integrates a global B_{2k} h^{2k} f^{(2k−1)})
won on [0,1].

Romberg is EM without writing the derivatives: it cancels them
numerically. Same I_true.

Not a better g_lo.
