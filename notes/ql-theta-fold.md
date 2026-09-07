<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# The fold, one page

Even real \(f\) on \([-L/2,L/2]\),
\(\|f\|_2=1\). \(T_y f(x)=f(x-y)\)
on the window. \(\theta(y)=2\langle f,T_y f\rangle\).
Fix \(L/3\le y<L/2\). Write
\(I=[y-L/2,L/2]\) for the
\(x\)-support of the product
\(f(x)f(x-y)\).

Five intervals, disjoint, union \(I\):

    I₋C  [y−L/2, 0]           copy of C by evenness
    I_A  [0, L/2−y]           A
    I_M1 [L/2−y, 2y−L/2]      M₁
    I_M2 [2y−L/2, y]          M₂
    I_C  [y, L/2]             C

Lengths: \(|A|=|C|=L/2-y\),
\(|M_2|=L-2y\), \(|M_1|=3y-L\),
sum \(L-y=|I|\). On \([0,L/2]\)
the four pieces \(A,M_1,M_2,C\)
partition the half-window
(\(I_{-C}\) is the even image of \(C\)
and does not sit in \([0,L/2]\)).

Masses of \(h=\sqrt2\,f|_{[0,L/2]}\):

    α = ∫_A h²,  β = ∫_C h²,
    μ₁ = ∫_{M₁} h²,  μ₂ = ∫_{M₂} h²,
    α+β+μ₁+μ₂ = 1.

Pairing. The shift \(x\mapsto x+y\)
sends \(A\) onto \(C\). Evenness
\(f(-x)=f(x)\) sends \(A\) onto \(M_2\)
(the fold: \(x\mapsto y-x\) maps
\(A\) to \(M_2\)). \(M_1\) is stable
under \(x\mapsto y-x\). Hence

    ⟨f, T_y f⟩
      = ∫_{I_A} f f(·−y) + ∫_{I_C} …
      + ∫_{I_M2} … + ∫_{I_{-C}} …
      + ∫_{I_M1} …

The two AC copies are equal;
the two AM₂ copies are equal.
Cauchy–Schwarz on each type:

    |2 ∫_A f(x) f(x−y) dx|
      ≤ 2 ‖f‖_A ‖f‖_C
      = √(αβ)     (because ‖f‖_A² = α/2)

Wait: \(h=\sqrt2 f\) so
\(\|f\|_A^2=\alpha/2\), and
\(2\|f\|_A\|f\|_C=\sqrt{\alpha\beta}\).
Two AC copies: \(2\sqrt{\alpha\beta}\).
Two AM₂ copies: \(2\sqrt{\alpha\mu_2}\).
M₁ against itself:
\(2\|f\|_{M_1}^2=\mu_1\).

Therefore
\(|\theta|\le 2\sqrt{\alpha\beta}+2\sqrt{\alpha\mu_2}+\mu_1\).
The simplex bound of #72 is
\(\le\sqrt2\). Equality: constant
mode, \(\alpha=1/2\), \(\beta=\mu_2=1/4\),
\(\mu_1=0\), and
\(\theta=2(L-y)/L=\theta_{00}\).

Band \(L/4\le y<L/3\): \(M_1=\emptyset\),
the fold of \(A\) meets \(A\). The
χ₃ μ=5 take uses \(y/L=0.4307\in(1/3,1/2)\)
and does not need that degeneration.

One \(L\). Not \((\forall L)\). Not RH.
LICENSE.md
