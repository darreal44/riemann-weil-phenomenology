# A(v) for the rational witness: enclosure of [0, 1]

Origin (`report/rational-witness-chi5-mu16.md`, `A-v-expansion.md`,
`A-v-tail.md`) reduced positivity of truncated Weil on χ₅ at μ=16
to one vector

    v = (4, −3, 1)/√26

(overlap 0.993 with measured v₀, no eigensolver) and split

    Q(v) = A(v) − P(v),     A(v) = CST + ½ I_{[0,1]} + ½ I_{[1,L]}.

CST is elementary. P is a nine-term sum of elementary lag kernels
at log n. The remaining analytic object was I_{[0,1]}. This note
encloses it.

## What is already a theorem (origin)

- CST = log(5/π) − γ − log(1−1/256), exact.
- θ_{nm} elementary (`H_2plane_independent.th`, `notes/demonstrations.md` §3).
- P_head(n=2,3,4) and P_rest(n=7…16) are finite explicit sums.
- A 10⁻³ error on each rest θ_v moves P_rest by ≲ 0.003, less than
  the room Q(v)≈0.0055, *provided* A(v) ∈ [−0.8303, −0.8244].
- Almost all of the integral lives on [0,1] (tail [1,L] is 2.6%).

## Lemma (enclosure)

Let v be as above, χ₅, μ=16, L=log 16. The pairing is the
truncated Weil form of `scan_s` / `H_2plane_independent` (no zeros).
Arb integration of the regularised integrand

    K(y)(2 e^{−3y/2} − θ_v(y)),
    K(y) = 2 e^{−y/2}/(1−e^{−2y}),

from 10^{-20} to 1 and from 1 to L, plus the exact CST and the
nine-term P, produces balls (`code/av_witness.py`)

    A(v) ∈ (−0.8303, −0.8244),
    Q(v) > 0.

Judge: `tests/test_av_witness.py`. The ball for Q excludes 0 from
below; the ball for A sits in the window that keeps Q>0 after a
±0.003 error on P_rest.

This is a verification in the style of the μ=3 5×5 certificate
and of `H2_arb`: an explicit finite formula, enclosed. It is not
a comparison-function estimate of I_{[0,1]} by hand.

## What a hand bound on [0,1] still needs

The integrand is regular at 0 (θ_v(0)=2 cancels 2 e^0; K∼1/y times
O(y)). A crude majorant θ_v ≤ 2 makes ∫ K(2e^{−3y/2}−2) diverge
and is useless. A linear majorant must match θ_v'(0). The closed
combination ∑ v_n v_m th_{nm} is elementary in (y/L, 2π y/L); its
second derivative on [0,1] is a bounded trigonometric polynomial
and would feed a trapezoid or Gauss remainder. That remainder is
not written here.

On [1,L] origin already recorded a sign change at y≈1.59. The
Arb tail ball is O(10^{-2}) and four times Q(v); a hand bound
there is secondary once [0,1] is enclosed.

## Status

| piece | status |
|---|---|
| CST | elementary (origin) |
| θ_v, P | elementary finite sum (origin + `theta_vec`) |
| I_{[0,1]}, I_{[1,L]}, A, Q | Arb balls, Q>0 (this note) |
| Cauchy |a^{(6)}| on [0,1], two panels | judged (`notes/av-cauchy-a6.md`) |
| comparison estimate of I_{[0,1]} | open (chord misses 0.22) |
| det(A−P) by max-norm rest | fails (`det-hand-chi5-mu16.md`) |
| (∀ L) Q_L ≥ 0 | RH; not this note |
