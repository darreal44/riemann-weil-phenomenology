# Impact of N_eff

N_eff = 1 / Σ p_n², p_n = v₀(n)².
It is the participation ratio of
the ground state across hats, not
the number of small eigenvalues
(that is D_max) and not the depth
(that is ℓ).

## What moves with N_eff

| fenêtre | N | N_eff | |⟨e₁,v₀⟩| | mass 0–2 | ℓ | D_max |
|---|---|---|---|---|---|---|
| χ₁₃ µ=16 | 9 | 1.51 | 0.95 | 1.000 | 9.9 | 1.2 |
| χ₈ µ=16 | 9 | 1.90 | 1.00 | 1.000 | 18.4 | 2.0 |
| χ₅ µ=16 | 3 | 1.99 | 0.99 | 1.000 | 13.0 | 2.0 |
| χ₅ µ=16 | 17 | 2.14 | 0.97 | 1.000 | 33.1 | 3.1 |
| χ₅ µ=38 | 17 | 2.43 | 0.92 | 0.995 | 57.8 | 7.0 |
| χ₃ µ=16 | 17 | 2.32 | 0.94 | 0.998 | 47.9 | 5.0 |
| χ₃ µ=38 | 17 | 2.66 | 0.88 | 0.981 | 70.6 | 9.0 |
| χ₃ µ=80 | 25 | 3.00 | 0.83 | 0.947 | 111.1 | 14.0 |
| χ₂₉ µ=16 | 9 | 1.92 | **0.46** | 0.992 | 2.6 | 0.4 |

Three couplings, one decoupling.

**1. Lemma 2 / the 2-plane.**
N_eff ≤ 2.2 and |⟨e₁,v₀⟩| ≥ 0.95
together mean {v₀,v₁} live in
span{e₁,e₂}. The 2×2 of H is the
right object. That is χ₅ µ=16,
χ₈, χ₇, χ₄. Cost of freezing e₁:
a few percent.

**2. Leak versus cancellation.**
N_eff from 2.2 to 3.0 moves 5 %
of L² off hats 0–2 and drops
⟨e₁,v₀⟩ from 0.97 to 0.83. That
5 % is the tail that cancels H
down by 10⁴⁰ (`v0-tail.md`).
Impact on a truncated test
function: catastrophic. Impact
on the shape plot: almost
invisible. N_eff is the right
alarm for that, mass0–2 at three
decimals is not.

**3. Not depth.** ℓ / N_eff runs
from 6 to 37. Depth is D_max × 11
on a saturated Gram, ~8 D on an
unsaturated Q. N_eff stays in
[1.5, 3] while ℓ goes 3 → 111.
Using N_eff as a proxy for ℓ
is a category error.

**4. χ₂₉ is the other exception.**
N_eff=1.92 looks “two-hat”, but
⟨e₁,v₀⟩=0.46: the mass is on two
hats that are *not* e₁. H’s
ground state sits on e₂
(`H-spectrum.md`, angle 113°).
N_eff alone does not pick the
ansatz; the overlap with e₁ does.

## Practical cut

    N_eff ≤ 2.2  and  |⟨e₁,v₀⟩| ≥ 0.95
        →  Lemma 2 applies as written
    N_eff ∈ (2.2, 2.7)
        →  2-plane is the sketch;
           Rayleigh of e₁ is already
           missing tens of nats
    N_eff ≥ 2.9
        →  do not truncate; the
           identity H=T, C=−2H
           is the well

N_eff is a switch for the *ansatz*,
not a coordinate on the depth law.

Data: `report/N_eff-impact.json`.
