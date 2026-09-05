# GL2_NCUT and the positivity threshold

11a1, cap=μ, table a_n (n≤30). Same assembler.

| μ | λ0 (ncut=0) | ncut=1 | ncut=2 | Δ(ncut 0→2) |
|---|-------------|--------|--------|-------------|
| 8 | 1.364 | 1.380 | 1.395 | +0.031 |
| 11 | 1.201 | 1.209 | 1.218 | +0.017 |
| 16 | 1.059 | 1.063 | 1.067 | +0.008 |
| 22 | 0.818 | 0.820 | 0.822 | +0.004 |
| 30 | 0.586 | 0.587 | 0.588 | +0.002 |

λ0 falls smoothly toward 0. NCUT is a 1–2 % lift, smaller
as L grows (the cutoff log(1−e^{−2L}) → 0). It does not
set the sign.

A linear fit on μ=16–30 would cross zero around μ≈50, not
38. The λ0=−9.28 at μ=38 N=67 (gp) is therefore **not**
the continuation of this line. Two changes at once: gp
`ellan` for n>30, and N=67 instead of ~30.

μ=30 N=67 (table, same N as the failing run): λ0=+0.588.
The basis size is not the jump. The jump is gp `ellan`
for n=31…38, or a bug in that path. Next: μ=38 N=25 with
gp, and print a_n vs the table on n≤30.
