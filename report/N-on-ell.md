# Impact of N on ell

Two different N.

## 1. Basis size N = NB+1 (Fourier)

Gram, μ=22 fixed, vary NB.

| | N=17 | N=25 | N=37 | N=67 |
|---|------|------|------|------|
| 11a1 ell | 23.05 | 22.46 | 22.01 | 21.77 |
| χ₂₉ ell | 5.09 | 4.98 | 4.91 | 4.86 |

ell *drops* a little when the basis grows (λ0 rises: more
directions, the min is less constrained). From N=37 to 67
the change is 1 % (χ₂₉) and 1 % (11a1). The protocol
N=37 at μ=22 and N=67 at μ=38 is past the plateau.
χ₅ Gram is indefinite below N=67 at this μ — not a
physical N-effect, a cutoff artifact.

## 2. Conductor N (or q)

GL₂ Gram s_hat vs conductor (`gl2-gram-slopes.md`):
0.65 (N=11) → 0.15 (N=67). Dirichlet: χ₃₁ q=31 s_hat=0.32
sits next to 32a1/37a1. Larger conductor → shorter desert
→ smaller ell and s_hat. That is |E|, not the matrix size.

## Rule

Quote ell only after N_basis ≳ 30 at μ=22. Do not compare
ell across conductors without dividing by |E| or L|E|.
