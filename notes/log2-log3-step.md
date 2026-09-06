# The (log 2, log 3] step: a mechanism of another nature

Weil positivity for test functions supported in
\([2^{-1/2}, 2^{1/2}]\) (window length \(L=\log 2\)) is
Connes–Consani 2021. Crossing the prime 2 — positivity for
\(L\in(\log 2,\log 3]\) — is the first open step of their
semi-local program. This note names the two mechanisms, ships
the identities that distinguish them, and does not take the
step. No RH. No covering.

## 1. Mechanism A: the compact remainder at \(\Lambda=1\)

CC write the archimedean Weil functional as a positive Sonin
trace minus a remainder \(N_I=-2\varepsilon'(1^+)(\mathrm{Id}-K_I)\),
\(K_I\) compact Hilbert–Schmidt on \(L^2(I)\),
\(I=[-\tfrac12\log 2,\tfrac12\log 2]\). Positivity follows if
\(K_I\le 1\) except for finitely many eigenvalues, each cut by
a linear condition. They compute one eigenvalue above 1
(\(1.0516\)), \(\varepsilon'(1^+)=22.9965\),
\(\delta(1)=\sum\lambda(n)^2=2.2375\) finite. The kink of
\(\varepsilon\) at \(\rho=1\) is what produces \(-2\varepsilon'\mathrm{Id}\).

Shipped reconstruction: `code/cc_arch.py`, every published
digit. Judge: `tests/test_cc_2adic_status.py`,
`tests/test_KI_spectrum.py`.

**Where A stops.**

- \(K_I\) acquires a second eigenvalue above 1 at \(L\approx 1.01\)
  (`code/KI_spectrum.py`: one above 1 at \(\log 2\), two past
  \(L=1.02\)). The sufficient condition \(K_I\le 1\) already fails
  on \((\log 2,\log 3]\) while the archimedean form itself stays
  positive on the conditioned hyperplane at \(\log 3\).
- The prime-2 term cannot join the compact remainder
  (`notes/semilocal-step.pdf` §3): \(E+W_2\le 0\) is false.
- Transported to \(\{\infty,2\}\) at \(\Lambda=1\), the compression
  \(P_1\mathfrak F P_1\) is not trace class, \(\delta_S\) is
  log-divergent at \(\rho=1\) and spiked at \(\rho=2\), and
  \(D_S\circ Q\) is essentially *positive* where CC's remainder
  is essentially negative (`code/dq_sign.py`,
  `tests/test_semilocal_dq_sign.py`). The sign that made A work
  is reversed.
- Subtracting a log profile \(c(-\ln|\ln\rho|)\) from \(\delta_S\)
  does not make the excess finite (journal §107–108, 35th
  execution). That is not mechanism B.

Mechanism A, transported, is a measured negative. It is not the
step.

## 2. Two logarithms

The surplus of the semi-local remainder “has the form of”
\(2h(1)\log'\Lambda\) (`notes/semilocal-step.pdf` §5). That is a
reading, not an identification of operators. The two logarithms
depend on different arguments.

**Lemma (volume vanishes at the Sonin cutoff).**
`identity_orbit(h, 1) = 0`.

*Proof.* \(\log'1=\ln 1=0\). \(\square\)

At \(\Lambda=1\) there is nothing to subtract. CC's construction
lives exactly there, and uses that \(\delta(1)\) is finite at
one place. Semi-locally \(\delta_S(1)=\infty\); Theorem 4's
volume term does not cancel that infinity because it is zero.

**Lemma (two logarithms).** The identity orbit \(2h(1)\log'\Lambda\)
is a function of the cutoff \(\Lambda\). The HS divergence
\(\|P_1\mathfrak F P_1\|_{\mathrm{HS}}^2=0.65\log_2(1/h)+\mathrm{pf}\)
is a function of the cell width \(h\) at fixed cutoff. They are
not interchangeable.

*Proof of dependence.* Connes writes
\(2\log'\Lambda=\int_{|\lambda|\in[\Lambda^{-1},\Lambda]}d^*\lambda\).
On \(\mathbb R_{>0}\) with Haar \(d\lambda/\lambda\) this is
\(2\ln\Lambda\), so \(2h(1)\log'\Lambda=2h(1)\ln\Lambda\).
The HS coefficient is measured at fixed \(R\) as \(N\) grows, and
at fixed \(h=R/N\) is independent of \(R\)
(`report/finite-part-HS.md`: \(R=2,4,5\) at \(h=1/40\) give the
same \(\sum\lambda^2=3.257\)). Different variables. \(\square\)

The slice code fits slope 4 in \(\ln\Lambda\)
(`code/trace_formula.py`): \(R_\Lambda=\hat P_\Lambda P_\Lambda\)
counts both cutoffs. That is still a function of \(\Lambda\),
shipped as `identity_orbit_slice`. It is not \(0.65\log_2(1/h)\).

Shipped: `identity_orbit`, `identity_orbit_slice`,
`finite_part_hs`, `HS_LOG_COEFF`. Judge:
`tests/test_log2_log3_step.py`.

## 3. Mechanism B: the 1999 finite part

**Theorem (Connes 1999, Thm 4, finite \(S\), unconditional).**

\[
\operatorname{Tr}(R_\Lambda U(h))
= 2h(1)\log'\Lambda
+\sum_{v\in S}\int'_{k_v^*}h(u^{-1})/|1-u|_v\,d^*u
+o(1),\qquad \Lambda\to\infty.
\]

The left-hand side minus the identity orbit *is* the sum of the
local Weil integrals on \(S\). Zeros do not appear (\(S\) finite).
Positivity does not come for free: the finite part is the Weil
pairing on \(S\), not a compact operator sitting below 1.

This is the mechanism of another nature. It does not transport
the Sonin remainder across the place 2. It renormalises the
compressed trace by subtracting the volume *first*, at
\(\Lambda>1\) where that volume is not zero, and then reads a
pairing. The compact-remainder question is the wrong question
at \(\Lambda=1\) on \(\{\infty,2\}\).

Shipped: `finite_part_trace`. Citation:
`report/connes-theorem-4.md`. The \(o(1)\) is as \(\Lambda\to\infty\);
nothing here evaluates it at a finite \(\Lambda\).

## 4. What the window actually contains

**Lemma (interior primes).** For a window of length \(L=\log\mu\),
the primes that contribute to the explicit formula are those
with \(1<p<\mu\). A prime at the endpoint \(p=\mu\) has lag
\(y=L\), and \(\theta(L)=0\) for any test function supported in
\([0,L]\) (the autocorrelation at full lag has empty overlap).

**Corollary.** On \((\log 2,\log 3]\), the only interior prime
is \(2\). At \(L=\log 2\) the interior is empty (the prime 2
sits at the endpoint and vanishes). That is why mechanism A
can ignore primes, and why the first open step is exactly the
entry of \(W_2\).

Shipped: `interior_primes`. `interior_primes(2)=[]`,
`interior_primes(3)=[2]`.

The Weil form on this interval is therefore \(\mathrm{Arch}-T_2\)
(plus a pole for \(\zeta\)). The Galerkin certificate
`code/positivite_certifiee_mu3.py` (Q defined positive on \(V_{31}\)
at \(\mu=3\), Arb, no zeros) is this pairing on a
31-dimensional cosine space, interior primes \(\{2\}\). It is
mechanism B as a finite-N Weil pairing, not mechanism A as a
remainder bound. It is not positivity for the whole
Paley–Wiener class of type \(\log 3\).

## 5. Status

| Claim | Status |
|---|---|
| CC digits of \(K_I\), \(\varepsilon'(1^+)\), \(\delta(1)\) | reconstructed |
| \(\#\{\lambda(K_I)>1\}=1\) at \(\log 2\) | judged (`KI_spectrum`) |
| \(\#\{\lambda(K_I)>1\}\ge 2\) past \(L=1.02\) | judged |
| arch \(D\circ Q\) essentially negative at \(\log 2\) | judged (`dq_sign`) |
| semi-local \(D_S\circ Q\) essentially positive at \(\log 3\) | judged |
| identity orbit vanishes at \(\Lambda=1\) | theorem, this note |
| two logarithms (\(\Lambda\) vs \(1/h\)) | theorem, this note |
| interior primes on \((\log 2,\log 3]\) = \(\{2\}\) | theorem, this note |
| Thm 4 finite part = \(S\)-local Weil | Connes 1999, cited |
| (log 2, log 3] by transporting CC remainder | negative, measured |
| profile subtraction \(c\log\) makes \(D^{\mathrm{ren}}\circ Q\) compact | false (journal §107) |
| Q\((\mu=3)>0\) on \(V_{31}\) | Galerkin certificate, not the class (`notes/pw-log3.md`) |
| (log 2, log 3] for the whole PW class | **open; not taken** (`notes/pw-log3.md`) |
| \((\forall L)\,Q_L\ge 0\) | RH; not this note |
