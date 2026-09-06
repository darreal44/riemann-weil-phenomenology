# Gauss sums U₂/U₄ and first sector split

Exact:

    τ(χ₃, e(u/16))  = 4 e^{iπ/8}
    τ(χ₁, e(3u/16)) = 4 e^{i3π/8}
    τ(χ₂, e(u/8))   = 4 e^{iπ/4}

Checked in `code/gauss_U2.py` to 1e-15.

A global τ is a phase: it does not change
∑λ² of the Hermitian compression.

Valuation filter on the lacunary n (stand-in for
conductor matching), N=120 R=4:

| sector | ∑λ² |
|--------|-----|
| triv (all n) | 3.033 |
| n even | 1.398 |
| n odd | 1.559 |
| triv N=240 | 3.599 |

even+odd ≈ triv. The log is split, not killed.
Each parity still grows if N grows. Π_k is not
a parity of n.
