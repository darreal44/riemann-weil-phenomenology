# Q(v) ball for the rational witness

    python3 code/av_enclose.py

P(v) is the nine-term
sum χ(n) Λ(n) n^{-1/2} θ_v(log n),
n=2,3,4,7,8,9,11,13,16
(`rational-witness-chi5-mu16.md`).

    P(v) = −0.833404134
    A(v) ∈ [−0.829387, −0.826919]
    Q(v) ∈ [ 0.004017,  0.006485]

Lower edge 0.0040 > 0.
A ±0.003 error on P_rest
still leaves Q > 0.001.
Judge: `tests/test_av_enclose.py`.

Not RH. Same obligations
as `A-v-enclose.md`: |g''|
ceilings (now catalogued)
and the slab samples of θ_v.
