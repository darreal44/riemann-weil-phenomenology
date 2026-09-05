# Two lemmas for the one-set bound (5 September 2026)

Goal: \(c_L \ge \exp(-C\dim(E_L))\) under RH, with
\(\dim(E_L)=n_L(E)-n_\partial\). Lemma 1 is proved. Lemma 2 is the
missing analytic step, stated so it can be attacked alone.

## Lemma 1 (interlacing / Dirichlet count)

Let \(H=PW_\tau\), \(\tau=L/2\), and let
\(A=\chi_E P_\tau\chi_E\) acting on \(L^2(E)\) (or equivalently the
concentration operator on \(H\)). \(A\) is compact, \(0\le A\le 1\).
Let \(V=\{F\in H: F(\gamma)=0\text{ for all }\gamma\in\partial E\cap\mathbb R\}\),
a closed subspace of codimension at most \(n_\partial\) (point
evaluations on \(PW_\tau\) are continuous).

**Statement.** For every \(\delta\in(0,1)\),

\[
\#\{\lambda_j(A)\ge 1-\delta\}-n_\partial
\;\le\;
\#\{\lambda_j(A|_V)\ge 1-\delta\}
\;\le\;
\#\{\lambda_j(A)\ge 1-\delta\}.
\]

**Proof.** Cauchy interlacing for a compact self-adjoint operator
restricted to a codimension-\(k\) subspace: if
\(\lambda_1\ge\lambda_2\ge\cdots\) are the eigenvalues of \(A\) and
\(\mu_1\ge\mu_2\ge\cdots\) those of \(A|_V\), then
\(\lambda_{j+k}\le\mu_j\le\lambda_j\). Take \(k\le n_\partial\) and
count how many eigenvalues exceed \(1-\delta\).

**Landau–Widom input (cited, not re-proved).** For a finite union of
intervals \(E\), as \(\tau|E|\to\infty\),

\[
\#\{\lambda_j(A)\ge 1-\delta\}
=\frac{\tau}{\pi}|E|+\frac{n_\partial}{4\pi}\log(\tau\cdot\mathrm{sep})+O_\delta(1)
\]

(Widom 1964, Landau 1967, multi-interval prolates). The leading term
is \(n_L(E)=(L/\pi)|E\cap\mathbb R_+|\). Combined with interlacing,

\[
\dim_\delta(E)\;:=\;\#\{\lambda_j(A|_V)\ge 1-\delta\}
\;=\;n_L(E)-n_\partial+O(\log(\tau|E|)).
\]

This *is* the count written in `one-set-sampling.md`. It bounds the
number of modes that hide in \(E\) and vanish on \(\partial E\). It
does **not** bound \(c_L\) from below: those modes give an *upper*
bound on \(c_L\) (they make \(\sum_{\partial E}|F|^2=0\) and leak
only through \(1-\lambda\)).

## Lemma 2 (multiplier — missing)

Let \(B_E\) be any entire function of exponential type \(0\) or \(o(\tau)\)
that vanishes simply on \(\partial E\) (a polynomial
\(\prod_{\gamma\in\partial E}(z-\gamma)\) is allowed; a product of
normalized sincs of small type is allowed). Write functions vanishing
on \(\partial E\) as \(F=B_E G\). Then \(G\) lives in a Paley–Wiener
space of type \(\tau+O(n_\partial/T)\) for a large cutoff \(T\), or in
the de Branges space attached to \(B_E\).

**Statement needed.** There is an absolute \(C\) such that for every
\(G\) with \(F=B_E G\in PW_\tau\),

\[
\|F\|_{L^2(\mathbb R)}^2
\;\le\;
e^{C\dim(E_L)}\sum_{\gamma\in\Gamma}|F(\gamma)|^2
\qquad\text{or equivalently}\qquad
\sum_{\gamma\in\Gamma}|B_E(\gamma)G(\gamma)|^2
\;\ge\;
e^{-C\dim(E_L)}\|B_E G\|^2.
\]

If this holds, then under RH \(Q_L(f)=\sum F(\gamma)^2\) yields
\(c_L\ge e^{-C\dim(E_L)}\).

**Why the naive product fails.** A product of \(n_\partial\) sincs of
type \(\tau\) has type \(n_\partial\tau\), which is not \(PW_\tau\).
A polynomial \(P\) of degree \(n_\partial\) times \(G\in PW_\tau\) is
not square-integrable on \(\mathbb R\) unless \(G\) decays. The
correct object is the inner factor of the de Branges space
\(\mathcal H(E_{B})\) whose structure function vanishes on
\(\partial E\), or a Beurling–Malliavin multiplier of radius
proportional to \(\dim(E_L)/L\).

**Why Duffin–Schaeffer + Bernstein dies.** On a gap of length \(g\),

\[
\int_{\mathrm{gap}}|F|^2
\le
\frac{g}{2}\Bigl(\frac{g\tau}{\pi}\Bigr)^2\|F\|^2
+\text{endpoint terms}.
\]

The desert contributes \(1-\lambda_0(\tau\gamma_1)\sim e^{-L\gamma_1}\).
The bracket \(1-\lambda_0-C(g\tau)^2\) is negative of that same order
(*sampling-floor* §4). Gap-by-gap estimates cannot see \(E\) as a set.

**What a proof of Lemma 2 looks like.** One estimate, not a sum over
gaps:

\[
\log\frac{\|B_E G\|}{\|G\|_{H}}
=\frac{1}{2\pi}\int_{\mathbb R\setminus E} \log|B_E(x)|\,d\mu_G(x)
\]

for a spectral measure \(\mu_G\) of \(G\) (Jensen / Beurling–Malliavin
second theorem). If \(G\) is not concentrated on \(E\), the integral
sees \(\log|B_E|\) on the complement, which is \(\asymp n_\partial\log\)
and harmless. If \(G\) *is* concentrated on \(E\), \(F=B_E G\) is
small on \(\mathbb R\setminus E\) by construction of \(B_E\), and the
sum over \(\Gamma\subset\mathbb R\setminus\mathrm{int}(E)\) is a
sampling of \(G\) on a set of density \(\gg\tau/\pi\) outside \(E\).
The exponential cost is at most the number of hidden modes,
\(\dim(E_L)\). That last sentence is the lemma, not yet a proof.

## Status

| claim | status |
|-------|--------|
| \(c_L>0\) under RH | Theorem 1, *sampling-floor* |
| \(\dim_\delta(E)=n_L-n_\partial+O(\log)\) | Lemma 1 + cited LW |
| \(c_L\le\exp(-c\,n_L)\) | Slepian / Rayleigh, known upper bound |
| \(c_L\ge\exp(-C\dim(E_L))\) | **Lemma 2, open** |

Nothing here is a script. Lemma 2 is a statement in
Beurling–Malliavin / de Branges, not a scan of \(Q\).
