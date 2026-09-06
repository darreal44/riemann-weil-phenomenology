# Demonstrations (unconditional lemmas)

Origin already has the evaluation-kernel Landau bound
(`notes/discrete-landau.tex`) and the Schur *complement* as
block elimination (`report/schur-lemma.md`). This note records
three lemmas that close pieces of the remaining list, with
shipped judges. None of them is RH.

---

## 1. Courant: the 2-plane is necessary, not sufficient

Let \(Q\) be any real symmetric form on the hat space, \(H\) its
restriction to a subspace \(V\) (here \(\mathrm{span}\{e_1,e_2\}\)).

**Lemma (Courant–Fischer).** \(\lambda_{\min}(H)\ge\lambda_{\min}(Q)\).

*Proof.* The min of a Rayleigh quotient over a subspace is at least
the min over the whole space. \(\square\)

**Corollary.** If \(\lambda_0(Q)>0\) then \(\det H>0\). The converse
is false in general: positivity of truncated Weil on two test
functions does not force positivity on the whole hat space.

Judge: `tests/test_schur_spd.py`. On \(\chi_{13}\), \(\mu=16\),
\(\lambda_{\min}(H)/\lambda_0(Q)>10\). The 2-plane can be SPD while
the well of \(Q\) is ten times deeper. This is the transfer
obstruction of `remaining-before-rh` §4, as a theorem.

---

## 2. Schur: sign is an identity; the value is not

Split \(Q=\begin{pmatrix}H&C\\C^T&T\end{pmatrix}\),
\(\Delta=H-CT^{-1}C^T\).

**Lemma (completing the square).** If \(T>0\),

\[
\langle Qx,x\rangle
=\langle\Delta u,u\rangle
+\bigl\|T^{1/2}(v+T^{-1}C^T u)\bigr\|^2,
\qquad x=(u,v).
\]

Hence \(Q>0\) if and only if \(\Delta>0\).

*Proof.* Expand the square; \(T>0\) makes the second term a norm.
Both summands nonnegative iff \(\Delta\ge 0\). Definite: same with
strict inequality. \(\square\)

This is the exact reduction: positivity of the whole hat matrix
is positivity of a \(3\times 3\), *once* the tail \(T\) is known
positive (bulk eigenvalues of \(Q\), \(O(1)\), not the well).

**Lemma (graph Rayleigh).** \(\lambda_0(Q)\le\lambda_{\min}(\Delta)\).
If the ground state lies on the graph \(v=-T^{-1}C^T u\), equality
holds. Numerically the ratio is \(1.000\)–\(1.004\)
(`lemma2-schur-3.md`, `test_chi13_Q_positive_iff_T_and_delta`).

The nonlinear eigenproblem is \(\Delta_\lambda u=\lambda u\) with
\(\Delta_\lambda=H-C(T-\lambda I)^{-1}C^T\). Replacing \(T-\lambda I\)
by \(T\) is legitimate once \(\lambda_0\ll\lambda_{\min}(T)\), which
is the measured regime.

**Not proved.** \(\|CT^{-1}C^T\|\le\lambda_{\min}(H)-\varepsilon\).
That is still the missing bound of `report/schur-lemma.md`. The
present lemma does not produce it: \(\Delta=H-(\text{PSD})\), so a
lower bound on \(H\) is an *upper* bound on nothing useful for
\(\lambda_0\).

---

## 3. The lag kernel of the raised cosine is elementary

Hats: \(\varphi_0=L^{-1/2}\), \(\varphi_n=\sqrt{2/L}\cos(\omega_n y)\),
\(\omega_n=2\pi n/L\). Unit \(e_1=(\sqrt2,-1,0)/\sqrt3\).

**Lemma.** For \(y\in[0,L]\), \(\omega=2\pi/L\),

\[
\theta_{f_1}(y)
=\frac23\Bigl(1-\frac yL\Bigr)\bigl(2+\cos(\omega y)\bigr)
+\frac1\pi\sin(\omega y).
\]

*Proof.* \(\theta=\sum_{n,m=0,1}(e_1)_n(e_1)_m\,\mathrm{th}_{nm}(y)\)
with the elementary table

\[
\begin{aligned}
\mathrm{th}_{00}&=2(L-y)/L,\\
\mathrm{th}_{01}&=-\sqrt2\,\sin(\omega y)/\pi,\\
\mathrm{th}_{11}&=2\bigl((L-y)/L\cos(\omega y)-\sin(\omega y)/(2\pi)\bigr).
\end{aligned}
\]

Let \(a=\sqrt{2/3}\), \(b=-1/\sqrt3\). Then
\(a^2\mathrm{th}_{00}+2ab\,\mathrm{th}_{01}+b^2\mathrm{th}_{11}\)
collapses to the displayed formula. \(\square\)

The right-hand side depends on \(t=y/L\) only. Write
\(g(t)=\theta_{f_1}(tL)\).

**Lemma (positivity).** \(g(t)\ge 0\) on \([0,1]\), \(g(1)=0\), \(g(0)=2\).

*Proof.* On \([0,1/2]\), \(\sin(2\pi t)\ge 0\) and \(2+\cos\ge 1\), so
\(g>0\). On \([0,t_\star]\) with \(t_\star=1-\sqrt3/(2\pi)\approx0.724\),
the phase bound
\(g(t)\ge\frac43(1-t)-\sqrt{\frac49(1-t)^2+1/\pi^2}\)
is nonnegative (square both sides). On the compact remainder
\([t_\star,1]\) a grid of \(2000\) points has \(\min g\ge 0\)
(`test_g_nonnegative_on_unit_interval`); \(g(1)=0\). \(\square\)

The last interval is a finite check, not an asymptotic. Together
with the closed form this is the object a hand bound on
\(P(f_1)=\sum_{n\le\mu}\chi(n)\Lambda(n)n^{-1/2}\theta_{f_1}(\log n)\)
can use: every term is explicit, \(\theta_{f_1}(\log n)>0\) at every
prime power \(n\le\mu\) (`test_theta_f1_positive_at_prime_lags_mu16`).
Signs of \(\chi\) still decide whether the terms add or cancel; that
is why dropping \(n>8\) flips \(\det(A-P)\).

---

## 4. Edge expansion, exact remainder

Even cosine hats on \([0,L]\):

\[
\hat\eta_0(\gamma)=\frac{2\sin(\gamma L/2)}{\gamma\sqrt L},\qquad
\hat\eta_n(\gamma)=\sqrt{\frac2L}\,\frac{2\gamma\sin(\gamma L/2)}{\gamma^2-\omega_n^2}.
\]

**Lemma (split).** For any coefficient vector \(v\) and any
\(\gamma\notin\{\omega_n\}\),

\[
\hat\psi(\gamma)
=2\psi(0)\,\frac{\sin(\gamma L/2)}{\gamma}+r(\gamma),
\]

\[
\psi(0)=L^{-1/2}\Bigl(v_0+\sqrt2\sum_{n\ge1}v_n\Bigr),
\]

\[
r(\gamma)
=\frac{2\sqrt2\sin(\gamma L/2)}{\sqrt L}
\sum_{n\ge1}v_n\frac{\omega_n^2}{\gamma(\gamma^2-\omega_n^2)}.
\]

*Proof.* Write \(\hat\psi=\sum v_n\hat\eta_n\) and
\(2\psi(0)\sin(\gamma L/2)/\gamma\), subtract, use
\(\gamma/(\gamma^2-\omega_n^2)-1/\gamma=\omega_n^2/(\gamma(\gamma^2-\omega_n^2))\).
\(\square\)

Judge: `tests/test_edge_expansion.py`. Special cases: constant mode
has \(r\equiv0\); \(e_1\in\ker\psi(0)\) has vanishing jump, so
\(\hat\psi=r\).

**What this does for the edge lemma.** Under RH (or on the zero Gram),
\(\lambda_0=\sum_\gamma|\hat\psi(\gamma)|^2\). Splitting in-band /
out-of-band and dropping \(r\) produces the jump heuristic
\(\lambda_0\approx 8\psi(0)^2\sum_{\gamma>\omega_{\max}}\sin^2(\gamma L/2)/\gamma^2\).
The identity above makes the error explicit:
\(|r(\gamma)|\le C\|v\|_1\omega_{\max}^2/(\gamma(\gamma^2-\omega_{\max}^2))\)
for \(\gamma>\omega_{\max}\). Bounding the sum of \(r\) against the
jump, uniformly in the ground state \(v\), is the remaining analysis.
It is harmonic analysis on a window; it contains no prime. It is
not done here.

On the measured windows \(R=-\ln\lambda_0+2\ln|\psi(0)|\) tracks
\(-\ln S(\omega_{\max})\) with
\(S\sim(4/\pi)\log(\omega_{\max})/\omega_{\max}\), hence \(O(1)\) at
the \(N\) we ran and slowly growing in \(N\). The statement
“\(R=O(1)\) absolutely” is therefore the wrong limit.

---

## 5. What is now a theorem, what is not

| Claim | Status |
|---|---|
| \(\dim\ker\mathrm{Eval}_\omega\ge n(\omega)-N_\Gamma(\omega)\) | proved (`discrete-landau`) |
| \(\lambda_{\min}(H)\ge\lambda_0(Q)\) | proved (Courant, this note) |
| \(T>0\Rightarrow(Q>0\Leftrightarrow\Delta>0)\) | proved (Schur square, this note) |
| \(\lambda_0=\lambda_{\min}(\Delta)\) as matrices | false in general; true on the graph, measured |
| \(\theta_{f_1}\) closed and \(\ge0\) | proved (this note; compact interval by grid) |
| \(\hat\psi=\) jump \(+\,r\) | proved (this note) |
| \(\#\{\ell_k>2\}=D_{\max}\) without threshold | not proved |
| \(\log(1/A)\) closed | not proved |
| \(\|CT^{-1}C^T\|<\lambda_{\min}(H)\) | not proved |
| \(\det(A-P)>0\) by estimates keeping every \(n\le\mu\) | not proved |
| edge remainder sum dominated by the jump, uniformly in \(v_0\) | not proved |
| 3-point Gauss of A(v) on [0,1] | arithmetic check (`notes/av-gauss.md`); remainder majorant not written |
| flint-free A(v), Q(v)>0 ball | judged (`code/av_enclose.py`, `report/Q-v-ball.md`); comparison still open |
| \((\forall L)\,Q_L\ge0\) | RH; not this note |
