# Gauss weights 5/18, 8/18, 5/18

They are the unique
positive weights
that make n=3
exact on
span{1,x,…,x^5}
with the three
Legendre nodes.
On [0,1]:

    ∑ w_i = 1
    ∑ w_i x_i^k = 1/(k+1)
      k=1,…,5

The nodes are the
roots of P₃ shifted
to [0,1]. P₃(t)=
(5t³−3t)/2 on
[−1,1]; roots
0, ±√(3/5).
Christoffel–Darboux
gives

    w_i = 1 / (P₃'(t_i) P₂(t_i))
    × (map Jacobian 1/2)

which evaluates to
5/18 at the ends
and 8/18 at the
centre. Symmetric
because the rule
is symmetric.

Check (floats):
moments 0..5 match
1/(k+1) to 1e-16.
Moment 6 is the
first miss, and
is exactly where
c₆ lives.

Not a free
parameter. Changing
a weight by 10⁻³
breaks exactness
on x^4 and the
remainder is no
longer pure a^{(6)}.
