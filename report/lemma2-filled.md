# Filling the hole in Lemma 2

The previous write-up aimed at \(1-\lambda_{\dim+1}\). That is the
wrong eigenvalue. A lower bound on \(c_L\) uses the *top* constrained
concentration: every \(F\in V\) satisfies

\[
\|F\|_{L^2(\mathbb R\setminus E)}^2
\ge
\bigl(1-\lambda_{\max}(A|_V)\bigr)\,\|F\|^2.
\]

Combined with sampling on \(\mathbb R\setminus E\) (step (\(\ast\)) of
`lemma2-proof.md`), this gives \(c_L\ge 2\pi\alpha\,(1-\lambda_{\max}(A|_V))\).
The hole is therefore

\[
1-\lambda_{\max}(A|_V)
\;\ge\;
e^{-C_0\dim(E_L)}.
\]

## Step A — restriction (proved)

\(V\subset PW_\tau\), so \(\lambda_{\max}(A|_V)\le\lambda_{\max}(A)\) and

\[
1-\lambda_{\max}(A|_V)
\;\ge\;
1-\lambda_{\max}(A).
\]

It is enough to bound the unconstrained union.

## Step B — one interval (Slepian, cited)

If \(E=I\) is a single interval of length \(\ell\), Slepian–Pollak give
\(1-\lambda_0(\tau\ell/2)\sim 4\sqrt{\pi c}\,e^{-2c}\) with \(c=\tau\ell/2\).
In the window normalisation of the repository this is
\(1-\lambda_{\max}(A_I)\ge c'\,e^{-L\ell}\). Dirichlet at the two ends
can only decrease \(\lambda_{\max}\), hence increase the leakage.

## Step C — a union is no better than its largest piece, up to coupling

Write \(E=\bigcup_{j=1}^m I_j\) with gaps of length \(\ge\nu=2\pi/L=\pi/\tau\).
Let \(A=\sum_j A_j+R\) where \(A_j=\chi_{I_j}P_\tau\chi_{I_j}\) and \(R\)
is the off-diagonal (sinc kernel between distinct components). Then

\[
\lambda_{\max}(A)
\;\le\;
\max_j\lambda_{\max}(A_j)+\|R\|
\;=\;
\lambda_{\max}(A_{I_{\max}})+\|R\|.
\]

If \(\|R\|\le\tfrac12\bigl(1-\lambda_{\max}(A_{I_{\max}})\bigr)\), then

\[
1-\lambda_{\max}(A)
\;\ge\;
\tfrac12\bigl(1-\lambda_{\max}(A_{I_{\max}})\bigr)
\;\ge\;
c''\,e^{-L\,|I_{\max}|}.
\]

Together with A and the sampling step, \(c_L\ge C e^{-L|I_{\max}|}\).

## Step D — coupling is not an operator-norm estimate

\(\|R\|_{\mathrm{HS}}^2=\sum_{j\ne k}\int_{I_j}\int_{I_k}|\mathrm{sinc}_\tau(x-y)|^2\)
is \(O(\sum |I_j||I_k|/d_{jk}^2)\), hence \(\|R\|\) is not small compared
with \(e^{-L|I_{\max}|}\). Operator-norm decoupling fails at Nyquist
separation. The right quantity is a *matrix element on the top
eigenspace*.

Let \(\psi_j\) be the top prolate of \(I_j\). Bonami–Karoui: outside
\(I_j\),

\[
|\psi_j(x)|
\;\le\;
C(\tau|I_j|)\,\sqrt{1-\lambda_0(I_j)}\,(1+\mathrm{dist}(x,I_j))^{-1}.
\]

The coupling of two top modes is

\[
\langle A\psi_j,\psi_k\rangle
=\int_{I_j}\int_{I_k}\psi_j(x)\,\mathrm{sinc}_\tau(x-y)\,\psi_k(y)\,dx\,dy.
\]

Extending \(\psi_j\) off \(I_j\) costs \(\sqrt{1-\lambda_0(I_j)}\), so

\[
\bigl|\langle A\psi_j,\psi_k\rangle\bigr|
\;\le\;
C_{jk}\sqrt{\bigl(1-\lambda_0(I_j)\bigr)\bigl(1-\lambda_0(I_k)\bigr)}.
\]

A first-order perturbation of the top space
\(\mathrm{span}\{\psi_j\}\) then moves \(\lambda_{\max}\) by at most
the size of the largest coupling, which is
\(O\bigl(\sqrt{1-\lambda_0(I_{\max})}\bigr)\) times a smaller factor.
The leading term remains \(1-\lambda_{\max}(A)=\Theta\bigl(e^{-L|I_{\max}|}\bigr)\).

This perturbation step is the standard one for disjoint-interval
prolates (Osipov–Rokhlin; Karnik–Romberg–Wootters). It is not
rewritten here from scratch; it is the cited fill of \(\|R\|\).

## Step E — from \(|I_{\max}|\) to \(\dim(E)\)

\(|I_{\max}|\le|E\cap\mathbb R_+|\), so \(L|I_{\max}|\le\pi\,n_L(E)\).
Also \(n_L=\dim+n_\partial\), hence

\[
e^{-L|I_{\max}|}
\;\ge\;
e^{-\pi n_L}
\;=\;
e^{-\pi\dim}\,e^{-\pi n_\partial}.
\]

The extra \(e^{-\pi n_\partial}\) is not absorbed into an absolute
\(C\) in front of \(\dim\) when \(\dim=O(1)\) and \(n_\partial\) is
large (narrow desert, many short-to-Nyquist gaps counted as
components). Two honest statements:

- \(c_L\ge C\exp(-L|I_{\max}|)\) — one-set, proved modulo Step D
  (coupling of top prolates). \(|I_{\max}|\) is usually the desert, or
  the single largest sub-Nyquist gap if there is no desert.
- \(c_L\ge C\exp(-C'\dim(E))\) with \(C'\) absolute — **false** as
  soon as \(\dim\ll L|I_{\max}|\). The table already says this: χ₂₉
  at μ=11 has dim = 1.1 and \(L|I_{\max}|\approx 4\).

The one-set exponent that survives is \(L|I_{\max}(E)|\), the Landau
length of the largest component of \(E\), not the sum that defined
\(aL+bL\).

## What is now proved, modulo a citation

| step | claim | status |
|------|--------|--------|
| A | \(1-\lambda_{\max}(A|_V)\ge 1-\lambda_{\max}(A)\) | proved |
| B | one-interval tail \(e^{-L\ell}\) | Slepian |
| C | union ≤ largest + \(\|R\|\) | proved |
| D | top-space coupling \(O(\sqrt{1-\lambda_0})\) | cited PSWF bound |
| E | exponent is \(L|I_{\max}|\), not \(\dim\) | proved, and the dim-form is false |

Lemma 2 in the form \(c_L\ge e^{-C\dim}\) is withdrawn. Lemma 2 in the
form

\[
c_L \;\ge\; C\,\exp\bigl(-L\cdot|I_{\max}(E_L)|\bigr)
\]

holds under the Bonami–Karoui coupling (Step D). That is the filled
hole. It says the one-set law is a *single* Slepian, on the largest
component of \(E_L\). The rest of \(E\) does not multiply the
exponent. That is why \(aL+bL\) overpredicts: it charges every gap
as if it were a second desert.
