# The matrix Q, χ₅ μ=16 N=8

9×9, hats φ₀…φ₈. Entries to
three decimals.

```
 0.092  0.133  0.147  0.081  0.335  0.155  0.012  0.133  0.014
 0.133  0.194  0.214  0.106  0.493  0.221  0.012  0.188  0.018
 0.147  0.214  0.239  0.041  0.563  0.222 -0.007  0.186  0.008
 0.081  0.106  0.041  3.013  0.935  0.278 -0.016  0.204  0.005
 0.335  0.493  0.563  0.935  2.302 -0.233 -0.349  0.049 -0.131
 0.155  0.221  0.222  0.278 -0.233  2.843 -0.444  0.155 -0.107
 0.012  0.012 -0.007 -0.016 -0.349 -0.444  0.563  0.662  0.025
 0.133  0.188  0.186  0.204  0.049  0.155  0.662  3.320 -0.527
 0.014  0.018  0.008  0.005 -0.131 -0.107  0.025 -0.527  3.054
```

## Two blocks

Head 3×3: every entry O(0.1).
Diagonal 0.09, 0.19, 0.24 —
smaller than several
off-diagonals (0.34, 0.49,
0.56 into φ₄). Not diagonally
dominant, which is why
Gershgorin died.

Tail T: diagonals 0.56–3.3,
off-diagonals smaller except
the (3,4)=0.94 and (6,7)=0.66
neighbours. Almost a bulky
SPD blob.

Coupling C = first three
rows, columns ≥3: the large
hits are into φ₄ (0.34, 0.49,
0.56). Rank-one-ish
(`C-spectrum.md`).

    ‖H₃‖_F = 0.52
    ‖C‖_F  = 1.12
    ‖T‖_F  = 6.3

cond(Q) ~ λ_max/λ₀ ~ 10¹².
cond(H₃) ~ 10⁵. cond(T) ~ 10.

## Pattern

Rows 0,1,2 are nearly
parallel (the 2-plane plus
φ₂). That is the
near-rank-1 head: three
rows, one direction, the
well sitting in the thin
residual.

No Toeplitz, no band.
φ₄ couples across the
whole head. A sparse
model of Q is wrong.
