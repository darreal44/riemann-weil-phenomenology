# Weyl ratio in the harvest

For zeros on the critical line, counted on (0,T],

    N_+(T) ∼
    (T/2π) log(q T / 2π) + A(χ) + o(1)

(one side; the constant A depends on the Γ-shift s₀ and the root
number). The two-sided count N(T)+N(−T) is about twice that for even
functional equations without a zero at 1/2.

The harvest ratio is

    r =
    (number of stored γ in (0,T]) / N_+(T).

A complete one-sided list has r≈1. An early bug divided by the two-sided
formula and demanded r>0.9: a complete file looked like r≈0.5 and would
have been read as a failed moisson (`weyl-density-check.md`, Claude’s
correction). The judge is now 0.9 < r < 1.1 one-sided
(`test_chi5_150_is_complete_one_sided_weyl`).

This ratio checks the pkl against the Weyl law for zeros. It is not
λ_min and not the operator Weyl law (`weyl-law-two.md`).
