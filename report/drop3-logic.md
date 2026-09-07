# Logic of drop-3

Full prime-side form
on the window:

    Q = A − P
    P = ∑_{n≤μ} a_n (log p)/√n  θ(log n)

drop-3 is the same
assemble with the
n=3 term omitted
(not 9, not 27):

    Q_{−3} = A − (P − P₃) = Q + P₃

Judged: Q ≽ 0
(λ₀ full ~ 10^{-9})
and Q_{−3} crosses
0 in (84, 86].

That crossing is
possible only if
P₃ < 0, so that
removing 3 *lowers*
the form. For 37a1,
a₃=−3, log 3 / √3
>0, θ>0, hence
P₃<0. Including 3
adds |P₃| to Q.
3 is necessary
when |P₃| is the
margin that kept
λ₀ above 0.

μ* ∈ (84, 86] is
the first cutoff
where that margin
is required. At 84
the bonus is not
yet enough to be
the difference
between PSD and
not (drop-3 still
+0.048). At 86 it
is (drop-3 −0.029).
83’s arrival at 84
changed the
*background* A−P'
by 0.04; the sign
of Q_{−3} flipped
on the next step
when P₃ and the
new background
met.

drop-3 is not a
derivative in μ
and not Granger.
It is one matrix
with one term
left out.
