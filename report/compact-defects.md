# Compact defects in the zero set

A compact defect of Γ is a bounded piece that a Beurling–Malliavin
*exterior* density is allowed to ignore. The desert (0,γ₁) is the
model case. Long gaps of E_L cut at a finite T₀ are compact too.

## Sliding D⁻ after a cut (r=50)

| χ | cut at 0 | at γ₁ | at 20 | at 50 |
|---|----------|-------|-------|-------|
| χ₅ | 0.42 | 0.50 | 0.54 | 0.66 |
| χ₁₇ | 0.62 | 0.68 | 0.76 | 0.84 |
| χ₂₉ | 0.70 | 0.72 | 0.84 | 0.94 |

D⁺ barely moves (0.88 / 1.06 / 1.16): the richest windows already
sit high. D⁻ is the desert talking.

## What is compact

- (0,γ₁): one interval, finite. Exterior density must not see it.
  χ₅ jumps 0.42→0.50 when it is removed — enough to pass τ/π at
  μ=22 (0.49). The “NO” of `bm_density.py` at χ₅ μ=22 is the
  compact defect, not a sampling failure.
- A long gap (γ_k,γ_{k+1}) ⊂ E_L with both ends < T₀: compact.
  Removing all of them is *not* allowed to be dumped into
  “compact”: their number grows with T₀ (Weyl). Only finitely
  many, chosen independently of T, are compact defects.
- The tail T>T₀ is not compact. D⁻ at cut=50 is still a finite-T
  number, not D_BM.

## Rule

A defect is compact when it stays in a fixed compact as T→∞.
γ₁ is. The first N long gaps, N fixed, are. The whole E_L(T) is
not: |E| grows. Weighted BM can swallow the desert and a fixed
list of gaps; it cannot swallow |E|→∞. That is why C(χ) L|E|
still has an extensive piece after the compact part is removed.
