# Paley–Wiener of type log 3, the whole class

The (log 2, log 3] step of Connes–Consani is positivity of the
truncated Weil form \(Q_L\) on the *whole* window space \(W_L\)
of length \(L=\log 3\), not on one Galerkin space \(V_N\). One
window is not covering and is not RH
(`notes/sampling-debranges-route.pdf`). This note records what
that distinction is, unconditionally, and a prime-side ladder
at \(\mu=3\). The step is not taken.

## 1. The class

\(W_L\): real even functions in \(L^2([-L/2,L/2])\). Cosine hats
\(\{V_N\}\) are nested, union dense (Fourier cosine basis).
\(c_L^*=\inf_{f\in W_L\setminus0}Q_L(f)/\|f\|^2\). The step is
\(c_L^*\ge0\).

**Lemma (Galerkin is the wrong direction).** For any real
symmetric form,
\(\lambda_{\min}(V_N)\ge\lambda_{\min}(V_{N+1})\ge c_L^*\).
A certificate \(Q>0\) on \(V_{31}\) is an *upper* bound on the
infimum, not a lower bound on the class.

*Proof.* Courant–Fischer on nested subspaces. \(\square\)

The Arb certificate `positivite_certifiee_mu3.py` (\(V_{31}\),
no zeros) does not take \(W_L\). Shipped:
`galerkin_takes_the_class() is False`.

**Lemma (\(Q_L\) is bounded on \(W_L\)).** Unconditional, any
finite \(L\). Pole and towers are finite translation pairings;
the archimedean term is an \(L^2\)-bounded convolution after
the \(F_0\) cancellation at \(y=0\). Hence
\(\lambda_{\min}(N)\downarrow c_L^*\in\mathbb R\) (possibly
negative). This is the RH-free half of Theorem 1 in
`notes/sampling-floor.pdf`. The RH half is \(c_L^*>0\) via
Beurling on the zeros; it is not used here.

**Corollary.** On \((\log2,\log3]\) the only interior prime is
\(2\) (`interior_primes(3)=[2]`, \(\theta(L)=0\)). So
\(Q_L=\mathrm{pole}+\mathrm{Arch}-T_2\) on this window
(\(\zeta\)); characters drop the pole.

## 2. Prime-side ladder at \(\mu=3\)

Shipped: `code/pw_log3.py`, `scan_s.assemble`,
`spectro_zeta.run`. Judge: `tests/test_pw_log3.py`.
Twelve character windows and three \(\zeta\) windows, 12 s
wall on 32 cores.

| object | \(N=9\) | \(17\) | \(25\) | \(33\) | nested | \(>0\) |
|---|---|---|---|---|---|---|
| \(\chi_5\) (has \(T_2\)) | \(4.416\times10^{-2}\) | \(4.369\times10^{-2}\) | \(4.358\times10^{-2}\) | \(4.354\times10^{-2}\) | yes | yes |
| \(\chi_4\) (no \(T_2\)) | \(7.041\times10^{-2}\) | \(6.986\times10^{-2}\) | \(6.972\times10^{-2}\) | \(6.966\times10^{-2}\) | yes | yes |
| \(\chi_3\) | \(9.929\times10^{-3}\) | \(9.744\times10^{-3}\) | \(9.706\times10^{-3}\) | \(9.691\times10^{-3}\) | yes | yes |
| \(\zeta\) | \(1.026\times10^{-7}\) | \(7.31\times10^{-8}\) | \(6.27\times10^{-8}\) | — | yes | yes |

\(\zeta\) at \(N=9\) reproduces the sampling-floor Gram entry
\(1.026\times10^{-7}\). The sequence is still descending toward
the published floor \(c_{\log3}\approx5.55\times10^{-8}\) (Gram,
under RH). Prime-side \(Q\) tracks it. Characters saturate at
once (\(N_{\mathrm{eff}}\approx1.1\)–\(1.4\)): almost no in-band
zeros at \(\mu=3\).

A nested positive ladder is compatible with \(c_L^*<0\) at
infinite \(N\). It is not the step.

## 3. Status

| Claim | Status |
|---|---|
| \(V_N\) nested, dense in \(W_L\) | theorem |
| \(\lambda_{\min}(V_N)\ge c_L^*\) (Courant) | theorem |
| Galerkin \(V_{31}\) takes the class | **false** |
| \(Q_L\) bounded on \(W_L\) | theorem (sampling-floor, RH-free half) |
| interior primes \(\{2\}\) | theorem (`log2-log3-step`) |
| prime-side ladder at \(\mu=3\), nested, \(>0\) | judged, this note |
| \(c_L^*\ge0\) on \(W_{\log3}\) | **open; not taken** |
| \((\forall L)\,Q_L\ge0\) | RH; not this note |

## 4. A alone, by character

On V₄, no primes (`report/A-by-chi-mu3.md`):
λ_min(A) is positive iff χ(2)=0 (χ₄ +0.073, χ₈ +0.247)
and negative iff χ(2)=−1 (χ₅ −0.223, χ₃ −0.215).
When χ(2)=−1 the ladder Q>0 is T₂ cancelling that
mode, not A dominating T₂ (`report/Cstar-dead.md`).
Still not c_L^*≥0.
