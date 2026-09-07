# Gershgorin on A − P and on Q

Disk i: center Q_ii, radius
Σ_{j≠i} |Q_ij|. If every disk
sits in Re z > 0, then Q ≻ 0.
None of the natural matrices
satisfy that.

## 2-plane H₂ (the inequality)

μ=8
    φ₀ : 0.127 ± 0.195   left = −0.068
    φ₁ : 0.302 ± 0.195   left = +0.107

μ=16
    φ₀ : 0.092 ± 0.133   left = −0.041
    φ₁ : 0.194 ± 0.133   left = +0.060

μ=22
    φ₀ : 0.089 ± 0.132   left = −0.043
    φ₁ : 0.196 ± 0.132   left = +0.063

One disk is safe. The φ₀ disk
crosses zero by 0.04–0.07,
which is the whole well:
λ_min(H₂) is 10⁻⁴ to 10⁻³,
inside that overlap. Gershgorin
cannot see a number smaller
than the radius.

## 3-hat head and full Q

H₃: all three left edges
negative at μ=16 and 22
(−0.19 to −0.12).
Q: lowest left edge ≈ −1.4.
Four disks of Q do sit in
(0,∞) — the tail bulk.
They certify nothing about
λ₀.

## Diagonal scaling

D⁻¹ Q D⁻¹ (unit diagonal)
makes radii 1.4–3.6. Worse.
The off-diagonal mass is
larger than the diagonal
on the first rows; no
row-equilibration fixes
Gershgorin here.

## Reading

Gershgorin is a row-sum
test. The well is a
near-parallel cancellation
of two rows of size 0.1
(`AP-inequality.md`).
The row sums stay O(10⁻¹)
and the test stops at the
row sum. To certify
λ_min one needs the
*angle* between the rows
(det), which Gershgorin
throws away.
