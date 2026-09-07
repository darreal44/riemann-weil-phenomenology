# The operator K_I

Connes–Consani, *Spectral triples and
ζ-cycles* (Selecta 2021). Compact
archimedean piece of their scaling-site
trace. Rebuilt in `code/cc_arch.py`.
It is not ARCH of `scan_s` and it is
not Q.

## Construction

1. Prolates at bandwidth c = 2π, even
   angular functions PS_{2n,0}(2π, x)
   on [−1,1]. Finite Fourier eigenvalues
   λ_n (CC: 0.999971, −0.979485, 0.524,
   −0.059, …). The code reads λ_n from
   one interior point w=0.3; the test
   `test_cc_archimedean_calibration`
   locks the first three digits.

2. Analytic continuation ξ_n of the
   normalized restriction to [0,1],
   then

       t_n = λ_n²/(1−λ_n²) ξ_n(1)²,
       ε'(1+) = ∑ t_n  ≈ 22.9965.

   Five terms already give that number.
   This is the residue of their
   archimedean density at ρ=1+.

3. Kernel Qε(ρ), ρ>1, formula (99):
   a sum over n of
   λ_n²/(1−λ_n²) C_n(ρ), with C_n a
   pairing of ξ_n' on [1/ρ, 1] against
   the dilated ξ_n'(ρx), plus two
   endpoint terms. Qε(1)=0 by hand.

4. Interval I of length L (additive
   log-coordinate). Discretize with
   step ω, N = L/ω + 1. Toeplitz

       (K_I)_{jk} = ω/(2ε') Qε(e^{ω|j−k|}).

   That matrix *is* K_I in the code.
   Continuum limit ω→0, NMAX→∞.

## Spectrum, as published and as run

CC at L = log 2:

    λ_max = 1.05158,  λ₂ = 0.686,  λ₃ = 0.029.

One eigenvalue above 1. The README
records a second crossing at
L ≈ 1.01 (between log 2 and log 3).
That is the only spectral event of
K_I on the first semi-local window
(log 2, log 3].

Eigenvalues of a Toeplitz with
smooth symbol decay after the
Slepian count of the interval
versus the prolate band c=2π.
The “compact part” is this finite
list of λ ≳ 1; the rest of the
spectrum sits in (0,1) and is
discarded in the Sonin mechanism
they transport.

## What K_I is for

CC use the spectral subspace of
K_I for λ>1 as an archimedean
Sonin space: functions whose
Fourier mass is concentrated
where the scaling-site kernel is
larger than 1. On a window of
length log 2 that space is
one-dimensional. Adding place 2
is the first semi-local step.

`notes/semilocal-step` is the
measurement that this transport
fails: the prime-2 term does not
join that compact remainder, the
{∞,2} compression is not trace
class, and the conditioned
remainder is predominantly
*positive* on the twenty tests
where CC’s is negative. K_I
itself is not at fault; it
reproduces the published digits.
The failure is the joining.

## What K_I is not

| object | lives on | sees primes | sees zeros |
|---|---|---|---|
| K_I | log-interval I, kernel Qε | no | no |
| ARCH of Q_L | hats on [0,L], kernel K(y) | no | no |
| Q_L | same hats | yes, n≤e^L | via explicit formula |
| Connes Thm 4, v=∞ | τ_∞ on R_+^* | no | no |

ARCH and K_I are two compact
archimedean operators, different
kernels, different test classes.
Matching ε' and λ_n against CC
does not identify K_I with ARCH.
The 2×2 H = A−P never uses K_I.

K_I ≥ some projection is not
Weil positivity. Its λ_max > 1
at log 2 is a fact about prolates
at c=2π, not about ζ.

## Numerical caveats

- NMAX=8, t_n after n=4 is 10⁻⁴.
- λ_n from a single probe w=0.3,
  not an eigen-solve of the
  finite Fourier operator.
- Toeplitz step ω=2×10⁻³; the
  published λ_max is a continuum
  number. The code is a
  calibration, not an enclosure.
- Qε at ρ=1 is set to 0; the
  diagonal of K_I is therefore
  a discrete artefact of ω.

`tests/test_semilocal_fourier.py`
locks λ_0, λ_1, λ_2, ε'. It does
not lock the spectrum of K_I at
log 2. That comparison is a
print in `__main__`.
