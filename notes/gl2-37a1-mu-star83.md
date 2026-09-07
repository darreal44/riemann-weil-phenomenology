<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# μ** of 37a1 drop-83 on (84, 100]

Preregistered (`report/prereg-37a1-mu-star83.md`):
2-unit grid 86…98, drop 83 only. Prime-side
Q, NB=80, dps=50. Not the Gram. Not RH.

Drop-83 is +3.3×10⁻⁹ at 84 and −0.080 at 100.
Drop-3 already flipped in (84, 86].

## Execution

`python code/gl2_drop83_star.py`, 7 jobs,
211 s wall. `report/gl2-37a1-mu-star83.json`.

| μ | drop 3 (known) | drop 83 |
|---|---|---|
| 84 | +0.048 | **+3.3×10⁻⁹** |
| **86** | −0.029 | **−4.0×10⁻¹⁰** |
| 88 | −0.099 | −3.6×10⁻⁵ |
| 90 | −0.162 | −2.9×10⁻⁴ |
| 92 | −0.220 | −6.9×10⁻⁴ |
| 94 | −0.274 | −1.5×10⁻³ |
| 96 | −0.325 | −4.5×10⁻³ |
| 98 | −0.372 | −2.9×10⁻² |
| 100 | −0.418 | −0.080 |

## Verdict: μ** ∈ (84, 86]

Same 2-unit bin as μ*. Prediction of a
later digit is dead. At 86, 83 is only
just a voter (λ₀ ~ −10⁻¹⁰, ℓ still 21.6);
3 is already −0.029. Unlike amplitudes,
same window (`vote-correlation.md`).
After 86, drop-83 deepens, steepens
after 96; 97 arrives at 97 and does not
vote at 100. Not a sixth slope. Not RH.

Judge: `tests/test_gl2_37a1_mu_star83.py`.

## Status

| Claim | Status |
|---|---|
| μ** ∈ (84, 100] | judged, refined to (84, 86] |
| μ** later than μ* | **false** (same bin) |
| drop-83 < 0 at 86 | judged (−4.0×10⁻¹⁰) |
| (∀ L) Q_L ≥ 0 | RH; not this note |
