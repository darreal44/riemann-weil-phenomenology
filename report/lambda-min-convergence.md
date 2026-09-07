# Convergence of λ_min

Courant on W_L:

    λ_min(S_N) ↓ c_L^*
    from above,
    S_N = P_N Q̂_L P_N.

The sequence is
monotone. It
proves c_L^*≤
every computed
value. It never
proves c_L^*≥0
by itself.

What has been
run at L=log 3:

    χ₅  N=9   λ_min=0.044
        cosine min=0.046
        λ_H(h=2)=0.053
        S_diag≈0.042

    χ₈  H00=0.311
        λ_H=0.257
        β=+0.055
        (lower bound,
        not a λ_min)

    χ₄  λ_H(h=2)=0.084
        λ_H(h=20)=0.070
        β(h=20)=+0.004

λ_H(h) for χ₄
drops from 0.084
to 0.070 and
flattens: the
well is already
in the first
modes. That is
consistent with
Courant (larger
head = smaller
λ_min of H,
closer to
c_L^* from
above, *if*
H were the
compression of
the whole
form — it is
not; tail T
is still
there).

β is a lower
bound that can
sit *below*
c_L^*. For χ₈
0.055 is far
below H00.
For χ₄ 0.004
is a thin
certificate,
not a
converged
λ_min.

No rate.
No N→∞
computation
on this L.
The monotone
diagram is
all there is.
