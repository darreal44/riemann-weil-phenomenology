# P is exact; Q is A minus a point

χ₅, μ=16, n=p^k≤16,
v=(4,−3,1)/√26.

    P(v) = ∑ χ(n) (log p)/√n  θ_v(log n)

Nine terms, θ_v
elementary (sines).
n=16: log n=L,
θ_v(L)=0, term=0.

    n   χ    term
    2  −1   −0.549807324622
    3  −1   −0.353208188406
    4  +1   +0.106638027778
    7  −1   −0.040232890707
    8  −1   −0.007863109843
    9  +1   +0.007609815597
   11  +1   +0.008656716342
   13  −1   −0.005197180542
   16  +1    0
         P= −0.833404134402

mpmath dps=50 agrees
with float to 1 ulp
(~2×10⁻¹⁶). CST =
log(5/π)−γ−log(1−1/256)
same. No Cauchy on P:
the sum is finite.

#54 A-ball
    A ∈ [−0.828243, −0.827540]
width 7.0×10⁻⁴
(the two R’s).

    Q = A − P
      ∈ [0.005162, 0.005865]

P contributes 0 to
the width. Qlo>0
is Alo>P, i.e.
Alo + 0.833404 > 0.
That is the natural
rung: an arithmetic
interval minus an
elementary sum.
One v, one μ.
Not (∀μ). Not RH.

    python3 -c "from av_enclose import p_of_v; print(p_of_v())"
