# λ₂(K_I) crosses 1 at L = 1.008

Same Toeplitz as `cc_arch.py`, step
ω = 4×10⁻³, Qε from NMAX=8.

| L | λ₁ | λ₂ | λ₃ | #{λ>1} |
|---|---|---|---|---|
| log 2 = 0.693 | 1.0522 | 0.691 | 0.032 | 1 |
| 0.90 | 1.083 | 0.927 | 0.393 | 1 |
| 1.00 | 1.088 | 0.996 | 0.548 | 1 |
| 1.01 | 1.088 | 1.000 | 0.559 | 2 |
| log 3 = 1.099 | 1.090 | 1.039 | 0.685 | 2 |

Bisection: λ₂=1 at **L = 1.008**.
The README figure L≈1.01 is this
crossing, not a second independent
measurement.

λ_max at log 2 is 1.0522 against
CC’s 1.05158 (ω-error of order
10⁻³). λ₁ saturates near 1.09
already before log 3; the new
event on (log 2, log 3] is λ₂
only.

Still no primes and no zeros.
The crossing is a Slepian count:
the interval has grown enough
to admit a second prolate mode
above the compact threshold 1.
It does not move the first
semi-local step.

`code/KI_spectrum.py`,
`tests/test_KI_spectrum.py`
(ω=8×10⁻³, two lengths).
