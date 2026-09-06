# Spectral tail of A = χ_E P_τ χ_E

τ = π. Nyström. Same unions.

## Counts and split of ∑ log(1−λ)

| E | \|E\| | #≥0.5 | #≥0.1 | log_hi (λ≥½) | log_mid (0.01–½) | log_all |
|---|---|---|---|---|---|---|
| [0,1] | 1.0 | 1 | 2 | −1.53 | −0.24 | −1.77 |
| [0,1]+0.3 close | 1.3 | 1 | 3 | −1.54 | **−0.62** | −2.17 |
| [0,1]+0.3 far | 1.3 | 1 | 3 | −1.53 | **−0.59** | −2.13 |
| [0,1]+two 0.3 | 1.6 | 1 | 3 | −1.57 | **−1.00** | −2.57 |
| [0,1]+[0,1] | 2.0 | 2 | 3 | −3.28 | −0.50 | −3.78 |
| [0,2] | 2.0 | 2 | 3 | −5.35 | −0.30 | −5.66 |

log_hi is the desert (I_max). log_lo
is empty at this discretisation. The
**mid-plunge** is where a 0.3-gap
lands: −0.24 → −0.62 → −1.00.

## First eigenvalues

| j | I=1 | +0.3 close | +0.3 far | +two 0.3 | I=2 |
|---|---|---|---|---|---|
| 0 | 0.783 | 0.786 | 0.784 | 0.792 | 0.981 |
| 1 | 0.205 | **0.387** | **0.315** | **0.427** | 0.750 |
| 2 | 0.011 | **0.122** | **0.184** | **0.310** | 0.244 |
| 3 | 0.000 | 0.005 | 0.012 | 0.069 | 0.025 |

λ₀ does not move. λ₁ and λ₂ do. Each
small extra interval lifts one
eigenvalue out of the floor into the
plunge. That is Widom's
"number of pieces" term, seen from
below.

## Plunge as −log(1−λ_j)

    I=1          0:1.53  1:0.23  2:0.01
    +0.3 close   0:1.54  1:0.49  2:0.13  3:0.01
    +two 0.3     0:1.57  1:0.56  2:0.37  3:0.07
    I=2          0:3.97  1:1.38  2:0.28

The desert writes a large −log(1−λ₀).
A gap writes a moderate −log(1−λ₁)
or −log(1−λ₂). Additive in the
log-det, not in λ₀.

## Lemma 2, restated on the tail

The object that sees E as a set is

\[
\log\det(I-A)_+
\;=\;
\sum_{j:\,\lambda_j(A)>\varepsilon}\log(1-\lambda_j).
\]

Split: the j=0 term is Slepian on
I_max; the rest of the plunge is the
gap tax. Lemma 2 is a lower bound on
−log det(I−A)_+, not on −log(1−λ₀).

Landau–Widom on a union already gives
the *count* of the plunge. The
*product* of (1−λ_j) on that block
is the missing estimate
(Widom 1964 has the count + a
log-perimeter; the product is a
stronger claim of the same paper's
determinant line, not written here
for Dirichlet-at-the-ends).
