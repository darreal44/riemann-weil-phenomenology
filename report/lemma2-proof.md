# Lemma 2, written as a proof with one hole

## Objects

Fix \(L>0\), \(\tau=L/2\), \(E=E_L\), \(\partial E=\{\pm\gamma_k\}\) the
endpoints of the components of \(E\) (finite: \(n_\partial<\infty\)
once gaps beyond a cutoff \(T_0\) are ignored; take \(T_0=320\)).
Under RH, \(Q_L(f)=\sum_{\gamma\in\Gamma}F(\gamma)^2\) for
\(F=\hat f\in PW_\tau\).

Point evaluations on \(PW_\tau\) are continuous, so

\[
V=\bigl\{F\in PW_\tau:F\big|_{\partial E}=0\bigr\}
\]

is closed of codimension \(\le n_\partial\). Every \(F\in V\) factors
in the de Branges space of type \(\tau\) as

\[
F(z)=B(z)\,G(z),
\]

where \(B\) is the finite Blaschke product of \(PW_\tau\) (or the
structure-function factor) with simple zeros exactly at \(\partial E\),
and \(G\) belongs to the complementary de Branges space
\(\mathcal H(B)\subset PW_{\tau+\varepsilon}\). For a finite real zero
set this \(B\) may be taken as

\[
B(z)=\prod_{a\in\partial E}\frac{z-a}{z-a+2i\tau}\cdot e^{i\phi}
\]

up to a unimodular constant — type \(0\) as \(|z|\to\infty\) on the
real line, so \(G\) stays of type \(\tau\). (A product of sincs of type
\(\tau\) is the wrong model: it inflates the type. A polynomial is the
wrong model: it leaves \(L^2(\mathbb R)\).)

## Identity

Plancherel and the explicit formula give, for \(F=BG\in V\),

\[
\frac{Q_L(f)}{\|f\|^2}
=2\pi\frac{\sum_{\Gamma}|B(\gamma)G(\gamma)|^2}{\|BG\|_{L^2(\mathbb R)}^2}.
\]

The zeros in \(\partial E\) drop out of the sum (\(B(\partial E)=0\)).
The remaining set \(\Gamma\setminus\partial E\) sits in
\(\mathbb R\setminus\mathrm{int}(E)\).

## Split of the norm

Write \(\|BG\|^2=\|BG\|_{L^2(E)}^2+\|BG\|_{L^2(\mathbb R\setminus E)}^2\).

On \(E\), \(B\) vanishes at every endpoint and is analytic, so
\(|B(x)|\le C\,\mathrm{dist}(x,\partial E)^{1}\) near each end and
\(|B|\) is bounded on each component. Thus \(\|BG\|_{L^2(E)}\) is
controlled by the concentration of \(G\) on \(E\):

\[
\|BG\|_{L^2(E)}^2
\le
\|B\|_{\infty,E}^2\int_E|G|^2
\le
\|B\|_{\infty,E}^2\,\lambda_{\max}(A|_V)\,\|G\|^2_{\mathcal H(B)},
\]

where \(A=\chi_E P_\tau\chi_E\) and \(\lambda_{\max}(A|_V)\le 1\).
Lemma 1 says there are \(\dim(E)\) directions with
\(\lambda(A|_V)\ge 1-\delta\). Those directions make the numerator
small relative to \(\|BG\|_{L^2(E)}\) because \(B\big|_{\partial E}=0\)
and the next zeros lie outside \(E\). They produce the *upper* bound
on \(c_L\), already known.

The lower bound lives on the complement: one needs

\[
\sum_{\Gamma\setminus\partial E}|BG(\gamma)|^2
\;\ge\;
\alpha\,\|BG\|_{L^2(\mathbb R\setminus E)}^2
\]

with \(\alpha\) depending only on \(\tau\) and the separation of
\(\Gamma\setminus\partial E\) (Beurling sampling on the complement:
outside \(E\) the set \(\Gamma\) has density \(\to\infty\)). This
step is standard once \(\mathbb R\setminus E\) is a finite union of
unbounded intervals plus bounded gaps shorter than \(\nu\). Call it
(\(\ast\)).

## The hole

After (\(\ast\)),

\[
\frac{\sum_\Gamma|F(\gamma)|^2}{\|F\|^2}
\ge
\frac{\alpha\,\|F\|_{L^2(\mathbb R\setminus E)}^2}{\|F\|_{L^2(E)}^2+\|F\|_{L^2(\mathbb R\setminus E)}^2}
=
\frac{\alpha\,(1-\theta)}{\theta+(1-\theta)},
\]

where \(\theta=\|F\|_{L^2(E)}^2/\|F\|^2\) is the concentration of
\(F=BG\) on \(E\). For \(F\in V\),

\[
\theta
\le
\lambda_{\max}(A|_V)
\le 1-e^{-C_0\dim(E)}
\]

**if** the first eigenvalue of \(A|_V\) *below* the plunge satisfies
a Landau–Widom tail \(1-\lambda_{\dim+1}\ge e^{-C_0\dim}\). That tail
is known for *one* interval (Slepian: \(1-\lambda_0(c)\sim e^{-2c}\)).
It is **not** written for a finite union with Dirichlet conditions.
This is the hole.

If the tail holds, \(\theta\le 1-e^{-C_0\dim}\) for every \(F\in V\),
hence \(1-\theta\ge e^{-C_0\dim}\), hence

\[
\frac{\sum|F(\gamma)|^2}{\|F\|^2}
\ge
\alpha\,e^{-C_0\dim(E)}.
\]

Functions not in \(V\) have a nonzero value at some point of
\(\partial E\). That single term \(|F(a)|^2\) is \(\ge 0\) and does
not hurt a lower bound. More carefully: decompose
\(F=F_V+F_\perp\) with \(F_V\in V\). The perpendicular piece is a
combination of reproducing kernels at \(\partial E\), hence
\(\sum_{\partial E}|F|^2\gtrsim\|F_\perp\|^2\), which only increases
the Rayleigh quotient. So it is enough to bound \(V\).

## What is proved, what is not

Proved in this note:

1. Factorisation \(F=BG\) in \(PW_\tau\) for finite real \(\partial E\).
2. Reduction of the lower bound to functions in \(V\).
3. Sampling of \(BG\) on \(\Gamma\setminus\partial E\) over
   \(\mathbb R\setminus E\), up to the constant \(\alpha\) in (\(\ast\)),
   which is Beurling on a set of density \(\infty\).

Not proved:

4. Landau–Widom tail on a finite union, after Dirichlet:
   \(1-\lambda_{\dim+1}(A|_V)\ge\exp(-C_0\dim(E))\).

That single spectral gap is Lemma 2. For one interval it is Slepian.
For a union it is the same statement about the plunge of a
multi-interval prolate with zeros pinned at the ends. There is no
further algebraic reduction.

## Consequence

A proof of (4) with \(C_0\) absolute gives
\(c_L\ge 2\pi\alpha\,e^{-C_0\dim(E_L)}\) and closes the one-set law.
Until (4) exists, \(aL+bL\) remains a split of \(|E|\) and
\(\dim(E)\) remains a count, not an exponent.
